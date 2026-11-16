import ts from "typescript";
import { parse } from "@vue/compiler-sfc";
import { NodeTypes, type TemplateChildNode, type ExpressionNode } from "@vue/compiler-dom";
import { createParsedCommandLine, createVueLanguagePlugin } from "@vue/language-core";
import { proxyCreateProgram } from "@volar/typescript/lib/node/proxyCreateProgram.js";
import { getServiceScript } from "@volar/typescript/lib/node/utils.js";
import { translateOffset } from "@volar/source-map";
import type { Language } from "@volar/language-core";
import { z } from "zod";
import { isVueOwned } from "./ownership.ts";

export const FindingSchema = z.strictObject({
  file: z.string(),
  offset: z.number().int().nonnegative(),
  message: z.string(),
});
export type Finding = z.infer<typeof FindingSchema>;
const forbiddenDirective =
  /@(?:ts-(?:ignore|expect-error|nocheck)|vue-(?:ignore|expect-error|skip))\b|\b(?:oxlint|eslint)-disable\b/;

function objectType(type: ts.Type): type is ts.ObjectType {
  return (type.flags & ts.TypeFlags.Object) !== 0;
}
function referenceType(type: ts.Type): type is ts.TypeReference {
  return objectType(type) && (type.objectFlags & ts.ObjectFlags.Reference) !== 0;
}

/** Real Vue service scripts, not regex-extracted approximations of template expressions. */
export function auditVue(rootNames?: string[], configName = "tsconfig.vue.json"): Finding[] {
  const config = createParsedCommandLine(ts, ts.sys, ts.sys.resolvePath(configName));
  const parsedFiles = ts.getParsedCommandLineOfConfigFile(
    ts.sys.resolvePath(configName),
    undefined,
    {
      ...ts.sys,
      onUnRecoverableConfigFileDiagnostic(diagnostic) {
        throw new Error(ts.flattenDiagnosticMessageText(diagnostic.messageText, "\n"));
      },
    },
    undefined,
    undefined,
    [{ extension: ".vue", isMixedContent: true, scriptKind: ts.ScriptKind.Deferred }],
  );
  if (parsedFiles === undefined) throw new Error("Cannot load Vue checking project");
  const files = rootNames ?? parsedFiles.fileNames;
  const findings: Finding[] = [];
  function report(file: string, offset: number, message: string): void {
    findings.push(FindingSchema.parse({ file, offset, message }));
  }
  const required = [
    config.options.strict,
    config.options.noUncheckedIndexedAccess,
    config.options.exactOptionalPropertyTypes,
    config.options.noImplicitOverride,
    config.options.noFallthroughCasesInSwitch,
    config.options.noImplicitReturns,
    config.options.noPropertyAccessFromIndexSignature,
    config.vueOptions.checkUnknownProps,
    config.vueOptions.checkUnknownEvents,
    config.vueOptions.checkUnknownDirectives,
    config.vueOptions.checkUnknownComponents,
    config.vueOptions.strictVModel,
  ];
  const overrides = [
    config.options.noImplicitAny,
    config.options.strictNullChecks,
    config.options.strictFunctionTypes,
    config.options.strictBindCallApply,
    config.options.strictPropertyInitialization,
    config.options.noImplicitThis,
    config.options.useUnknownInCatchVariables,
    config.options.strictBuiltinIteratorReturn,
  ];
  if (
    required.some((value) => value !== true) ||
    overrides.some((value) => value === false) ||
    config.options.allowJs !== false ||
    config.options.skipLibCheck !== false
  )
    report(configName, 0, "Strict Vue compiler baseline was weakened");
  if (
    config.vueOptions.skipTemplateCodegen ||
    config.vueOptions.plugins.length > 0 ||
    config.vueOptions.lib !== "vue" ||
    config.vueOptions.extensions.length !== 1 ||
    config.vueOptions.extensions[0] !== ".vue" ||
    config.vueOptions.vitePressExtensions.length > 0 ||
    config.vueOptions.petiteVueExtensions.length > 0
  )
    report(configName, 0, "Unchecked template generation configuration is prohibited");
  let language: Language<string> | undefined;
  const create = proxyCreateProgram(ts, ts.createProgram, () => ({
    languagePlugins: [
      createVueLanguagePlugin(ts, config.options, config.vueOptions, (id: string) => id),
    ],
    setup(value) {
      language = value;
    },
  }));
  const program = create({
    rootNames: files,
    options: { ...config.options, allowNonTsExtensions: true },
    host: ts.createCompilerHost(config.options),
  });
  if (language === undefined) throw new Error("Vue language service did not initialize");
  const activeLanguage = language;
  const checker = program.getTypeChecker();
  // Vue's options-only reader deliberately returns no file names; use the real file reader's diagnostics.
  for (const diagnostic of [...parsedFiles.errors, ...ts.getPreEmitDiagnostics(program)]) {
    if (diagnostic.category === ts.DiagnosticCategory.Error)
      report(
        diagnostic.file?.fileName ?? "tsconfig.vue.json",
        diagnostic.start ?? 0,
        `TS${diagnostic.code}: ${ts.flattenDiagnosticMessageText(diagnostic.messageText, "\n")}`,
      );
  }
  const vueFiles = program
    .getSourceFiles()
    .filter(
      (file) =>
        (file.fileName.endsWith(".vue") || isVueOwned(file.fileName)) &&
        !program.isSourceFileFromExternalLibrary(file),
    );
  function sourceOffset(node: ts.Node): number | undefined {
    if (
      !node.getSourceFile().fileName.endsWith(".vue") &&
      isVueOwned(node.getSourceFile().fileName)
    )
      return node.getStart(node.getSourceFile());
    const anchor = ts.isCallExpression(node) || ts.isNewExpression(node) ? node.expression : node;
    if (ts.isCallExpression(anchor)) {
      const declaration = checker.getResolvedSignature(anchor)?.declaration;
      const input = anchor.arguments[0];
      if (
        input !== undefined &&
        declaration !== undefined &&
        ts.isFunctionDeclaration(declaration) &&
        declaration.name?.text === "__VLS_unwrap" &&
        declaration
          .getSourceFile()
          .fileName.replaceAll("\\", "/")
          .includes("/@vue/language-core/types/template-helpers.d.ts")
      )
        return sourceOffset(input);
    }
    const token = ts.isPropertyAccessExpression(anchor) ? anchor.name : anchor;
    const file = node.getSourceFile();
    const [service, , source] = getServiceScript(activeLanguage, file.fileName);
    if (service === undefined || source === undefined) return undefined;
    const prefix = service.preventLeadingOffset ? 0 : source.snapshot.getLength();
    const map = activeLanguage.maps.get(service.code, source);
    // Omit completion-only synthetic code. Explicitly disabled verification still
    // counts as authored: suppressions must not hide an unsafe value.
    for (const mapping of map.mappings) {
      if (mapping.data.verification === undefined) continue;
      const offset = translateOffset(
        token.getStart(file) - prefix,
        mapping.generatedOffsets,
        mapping.sourceOffsets,
        mapping.generatedLengths ?? mapping.lengths,
        mapping.lengths,
      );
      if (
        offset !== undefined &&
        source.snapshot.getText(offset, offset + token.getWidth(file)) === token.getText(file)
      )
        return offset;
    }
    // Calls on auto-unwrapped refs are spelled read.value() in the service
    // script but read() in the SFC. Keep the call result in the audit.
    if (ts.isPropertyAccessExpression(anchor) && anchor.name.text === "value")
      return sourceOffset(anchor.expression);
    return undefined;
  }
  function owned(declaration: ts.Declaration): boolean {
    const file = declaration.getSourceFile();
    return file.fileName.endsWith(".vue")
      ? sourceOffset(declaration) !== undefined
      : !program.isSourceFileFromExternalLibrary(file) && !program.isSourceFileDefaultLibrary(file);
  }
  function unsafe(type: ts.Type, callable: boolean, seen = new Set<ts.Type>()): boolean {
    if ((type.flags & (ts.TypeFlags.Any | ts.TypeFlags.Unknown)) !== 0) return true;
    if (seen.has(type)) return false;
    const next = new Set(seen).add(type);
    // Component constructors are framework handles. Vue's DefineComponent has
    // internal top-type defaults even for fully typed props; those defaults are
    // not application data. Authored props/expressions remain checked below and
    // by Vue's semantic checker (including cross-component prop probes).
    function vueInstance(candidate: ts.Type): boolean {
      const props = candidate.getProperty("$props");
      return (
        props?.declarations?.some((declaration) =>
          declaration
            .getSourceFile()
            .fileName.replaceAll("\\", "/")
            .includes("/@vue/runtime-core/"),
        ) === true
      );
    }
    const component =
      vueInstance(type) ||
      type
        .getConstructSignatures()
        .some((signature) => vueInstance(checker.getReturnTypeOfSignature(signature)));
    if (
      !component &&
      type.isUnionOrIntersection() &&
      type.types.some((member) => unsafe(member, callable, next))
    )
      return true;
    if (
      !component &&
      referenceType(type) &&
      checker.getTypeArguments(type).some((argument) => unsafe(argument, false, next))
    )
      return true;
    if (!component && type.aliasTypeArguments?.some((argument) => unsafe(argument, false, next)))
      return true;
    if (
      callable &&
      type
        .getCallSignatures()
        .some((signature) => unsafe(checker.getReturnTypeOfSignature(signature), false, next))
    )
      return true;
    if (
      checker
        .getIndexInfosOfType(type)
        .some(
          (index) =>
            index.declaration !== undefined &&
            owned(index.declaration) &&
            unsafe(index.type, false, next),
        )
    )
      return true;
    return type
      .getProperties()
      .some(
        (property) =>
          property.declarations?.some(owned) &&
          unsafe(checker.getTypeOfSymbol(property), true, next),
      );
  }
  for (const file of vueFiles) {
    const text = ts.sys.readFile(file.fileName);
    if (text === undefined) throw new Error(`Cannot read ${file.fileName}`);
    if (file.fileName.endsWith(".vue")) {
      const parsed = parse(text, { filename: file.fileName });
      for (const error of parsed.errors)
        report(file.fileName, 0, typeof error === "string" ? error : error.message);
      const descriptor = parsed.descriptor;
      if (
        descriptor.script !== null ||
        descriptor.scriptSetup?.lang !== "ts" ||
        descriptor.scriptSetup.src !== undefined ||
        descriptor.template?.src !== undefined ||
        (descriptor.template?.lang !== undefined && descriptor.template.lang !== "html") ||
        descriptor.customBlocks.length > 0
      )
        report(
          file.fileName,
          0,
          "Only local script-setup TypeScript and HTML templates are admitted; no external/custom blocks",
        );
      if (descriptor.styles.some((style) => /\bv-bind\s*\(/.test(style.content)))
        report(
          file.fileName,
          0,
          "CSS expression checking is not yet admitted; bind styles in the checked template",
        );
      // Vue exposes actual HTML comments; quoted markup strings are not directives.
      for (const comment of descriptor.comments ?? []) {
        if (forbiddenDirective.test(comment))
          report(file.fileName, 0, "Vue/type/lint suppression is prohibited");
      }
      function inspectExpression(node: ExpressionNode): void {
        if (node.type === NodeTypes.SIMPLE_EXPRESSION && !node.isStatic)
          inspectSnippet(node.content, node.loc.start.offset);
      }
      function inspectTemplate(node: TemplateChildNode): void {
        if (node.type === NodeTypes.INTERPOLATION) inspectExpression(node.content);
        if (node.type === NodeTypes.ELEMENT) {
          for (const prop of node.props)
            if (prop.type === NodeTypes.DIRECTIVE) {
              if (prop.exp !== undefined) inspectExpression(prop.exp);
              if (prop.arg !== undefined) inspectExpression(prop.arg);
            }
        }
        if (node.type === NodeTypes.COMMENT && forbiddenDirective.test(node.content))
          report(file.fileName, node.loc.start.offset, "Vue/type/lint suppression is prohibited");
        if (
          node.type === NodeTypes.ELEMENT ||
          node.type === NodeTypes.FOR ||
          node.type === NodeTypes.IF_BRANCH
        )
          node.children.forEach(inspectTemplate);
        if (node.type === NodeTypes.IF) node.branches.forEach(inspectTemplate);
      }
      if (descriptor.template !== null) {
        if (descriptor.template.ast === undefined)
          report(file.fileName, 0, "Template AST unavailable; cannot audit source");
        else descriptor.template.ast.children.forEach(inspectTemplate);
      }
      if (descriptor.scriptSetup !== null)
        inspectSnippet(descriptor.scriptSetup.content, descriptor.scriptSetup.loc.start.offset);
    }
    function inspectSnippet(content: string, base: number): void {
      const script = ts.createSourceFile("authored.ts", content, ts.ScriptTarget.Latest, true);
      function inspectSyntax(node: ts.Node): void {
        for (const range of [
          ...(ts.getLeadingCommentRanges(script.text, node.pos) ?? []),
          ...(ts.getTrailingCommentRanges(script.text, node.end) ?? []),
        ]) {
          if (forbiddenDirective.test(script.text.slice(range.pos, range.end)))
            report(file.fileName, base, "Type/lint suppression is prohibited");
        }
        if (
          node.kind === ts.SyntaxKind.AnyKeyword ||
          node.kind === ts.SyntaxKind.UnknownKeyword ||
          node.kind === ts.SyntaxKind.DeclareKeyword ||
          ts.isNonNullExpression(node) ||
          ts.isTypeAssertionExpression(node) ||
          (ts.isAsExpression(node) && node.type.getText(script) !== "const")
        )
          report(
            file.fileName,
            base + node.getStart(script),
            "Forbidden type or unchecked assertion/declaration",
          );
        ts.forEachChild(node, inspectSyntax);
      }
      inspectSyntax(script);
    }
    if (!file.fileName.endsWith(".vue")) inspectSnippet(text, 0);
    const reported = new Set<number>();
    function inType(node: ts.Node): boolean {
      let parent: ts.Node | undefined = node.parent;
      while (parent !== undefined) {
        if (
          ts.isTypeNode(parent) ||
          ((ts.isImportSpecifier(parent) ||
            ts.isImportClause(parent) ||
            ts.isExportSpecifier(parent) ||
            ts.isExportDeclaration(parent)) &&
            parent.isTypeOnly)
        )
          return true;
        if (ts.isStatement(parent) || ts.isExpressionStatement(parent)) return false;
        parent = parent.parent;
      }
      return false;
    }
    function visit(node: ts.Node): void {
      const offset = sourceOffset(node);
      if (offset !== undefined) {
        const isValue =
          (ts.isIdentifier(node) &&
            !inType(node) &&
            !(ts.isBindingElement(node.parent) && node.parent.propertyName === node)) ||
          ts.isCallExpression(node) ||
          ts.isNewExpression(node) ||
          ts.isPropertyAccessExpression(node) ||
          ts.isElementAccessExpression(node) ||
          ts.isArrowFunction(node) ||
          ts.isFunctionExpression(node);
        // Vue inserts .value unwrapping with Ref<unknown> bookkeeping. Check its
        // effective result, not that synthetic receiver; an authored .value is never skipped.
        const inspected =
          ts.isIdentifier(node) &&
          ts.isPropertyAccessExpression(node.parent) &&
          node.parent.name.text === "value" &&
          sourceOffset(node.parent.expression) === offset &&
          (sourceOffset(node.parent.name) === undefined ||
            sourceOffset(node.parent.name) === offset)
            ? node.parent
            : node;
        if (
          isValue &&
          unsafe(
            checker.getTypeAtLocation(inspected),
            ts.isIdentifier(node) || ts.isArrowFunction(node) || ts.isFunctionExpression(node),
          ) &&
          !reported.has(offset)
        ) {
          reported.add(offset);
          report(
            file.fileName,
            offset,
            `Forbidden inferred any/unknown in authored Vue value: ${node.getText(file).slice(0, 80)}: ${checker.typeToString(checker.getTypeAtLocation(inspected))}`,
          );
        }
        if (ts.isCallExpression(node) || ts.isNewExpression(node)) {
          const declaration = checker.getResolvedSignature(node)?.declaration;
          if (
            declaration !== undefined &&
            /\/zod\//.test(declaration.getSourceFile().fileName.replaceAll("\\", "/")) &&
            ts.isFunctionDeclaration(declaration) &&
            declaration.name !== undefined &&
            ["custom", "any", "unknown"].includes(declaration.name.text)
          )
            report(file.fileName, offset, "Unchecked Zod constructor is prohibited");
        }
      }
      ts.forEachChild(node, visit);
    }
    visit(file);
  }
  for (const name of files) {
    if (
      name.endsWith(".vue") &&
      !vueFiles.some(
        (file) =>
          file.fileName.replaceAll("\\", "/").toLowerCase() ===
          name.replaceAll("\\", "/").toLowerCase(),
      )
    )
      report(name, 0, "Vue source was not checked");
  }
  return findings;
}
