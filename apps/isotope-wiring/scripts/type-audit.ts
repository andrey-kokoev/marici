import { z } from "zod";
import {
  SignatureKind,
  SymbolFlags,
  TypeFlags,
  type Project,
  type Type,
} from "typescript/unstable/sync";
import { SyntaxKind, type Node } from "typescript/unstable/ast";
import * as is from "typescript/unstable/ast/is";
import { getLeadingCommentRanges, getTrailingCommentRanges } from "typescript/unstable/ast/scanner";

export const TypeFindingSchema = z.strictObject({
  file: z.string(),
  line: z.number().int().positive(),
  column: z.number().int().positive(),
  code: z.enum(["forbidden-type", "unchecked-escape", "missing-type", "weak-configuration"]),
  message: z.string(),
});
export type TypeFinding = z.infer<typeof TypeFindingSchema>;

/** Audit every owned source in the compiler program, not just schema exports. */
export function auditProject(project: Project): TypeFinding[] {
  const findings: TypeFinding[] = [];
  const options = project.compilerOptions;
  const required = [
    options.strict,
    options.noUncheckedIndexedAccess,
    options.exactOptionalPropertyTypes,
    options.noImplicitOverride,
    options.noFallthroughCasesInSwitch,
    options.noImplicitReturns,
    options.noPropertyAccessFromIndexSignature,
  ];
  const strictOverrides = [
    options.noImplicitAny,
    options.strictNullChecks,
    options.strictFunctionTypes,
    options.strictBindCallApply,
    options.strictPropertyInitialization,
    options.noImplicitThis,
    options.useUnknownInCatchVariables,
    options.strictBuiltinIteratorReturn,
  ];
  if (
    required.some((value) => value !== true) ||
    strictOverrides.some((value) => value === false) ||
    options.allowJs !== false ||
    options.skipLibCheck !== false
  )
    findings.push(
      TypeFindingSchema.parse({
        file: project.configFileName,
        line: 1,
        column: 1,
        code: "weak-configuration",
        message: "Strict compiler baseline was weakened",
      }),
    );
  const files = project.program
    .getSourceFileNames()
    .map((name) => {
      const file = project.program.getSourceFile(name);
      if (file === undefined) throw new Error(`Compiler source unavailable: ${name}`);
      return file;
    })
    .filter(
      (file) =>
        !project.program.isSourceFileFromExternalLibrary(file) &&
        !project.program.isSourceFileDefaultLibrary(file),
    );
  const owned = new Set(files.map((file) => file.fileName.replaceAll("\\", "/").toLowerCase()));
  const checker = project.checker;
  const typeCache = new Map<string, boolean>();
  const owns = (path: string): boolean => owned.has(path.replaceAll("\\", "/").toLowerCase());
  const pendingTypes = new Set<string>();
  function unsafeType(type: Type, inspectCallable: boolean): boolean {
    const key = `${type.id}/${inspectCallable}`;
    const cached = typeCache.get(key);
    if (cached !== undefined) return cached;
    if (pendingTypes.has(key)) return false;
    pendingTypes.add(key);
    let unsafe = (type.flags & (TypeFlags.Any | TypeFlags.Unknown)) !== 0;
    if (!unsafe && (type.isUnionType() || type.isIntersectionType()))
      unsafe = type.getTypes().some((member) => unsafeType(member, inspectCallable));
    if (!unsafe && type.isTypeReference())
      unsafe = checker.getTypeArguments(type).some((argument) => unsafeType(argument, false));
    if (!unsafe)
      unsafe = type.getAliasTypeArguments().some((argument) => unsafeType(argument, false));
    if (!unsafe && inspectCallable) {
      unsafe = checker.getSignaturesOfType(type, SignatureKind.Call).some((signature) => {
        const result = checker.getReturnTypeOfSignature(signature);
        return result !== undefined && unsafeType(result, false);
      });
    }
    // Library declarations are not recursively policed. Actual application reads
    // of their unsafe fields/results are checked as expressions below.
    if (!unsafe && type.isObjectType()) {
      unsafe = checker.getPropertiesOfType(type).some((property) => {
        if (!property.declarations.some((declaration) => owns(declaration.path))) return false;
        const value = checker.getTypeOfSymbol(property);
        return value !== undefined && unsafeType(value, true);
      });
    }
    pendingTypes.delete(key);
    typeCache.set(key, unsafe);
    return unsafe;
  }
  for (const file of files) {
    const reported = new Set<string>();
    function report(node: Node, code: TypeFinding["code"], message: string): void {
      const key = `${node.pos}/${code}`;
      if (reported.has(key)) return;
      reported.add(key);
      const location = file.getLineAndCharacterOfPosition(node.getStart(file));
      findings.push(
        TypeFindingSchema.parse({
          file: file.fileName,
          line: location.line + 1,
          column: location.character + 1,
          code,
          message,
        }),
      );
    }
    const values: Node[] = [];
    const callables = new Set<Node>();
    function add(node: Node, inspectCallable = false): void {
      values.push(node);
      if (inspectCallable) callables.add(node);
    }
    function visit(node: Node): void {
      for (const range of [
        ...(getLeadingCommentRanges(file.text, node.pos) ?? []),
        ...(getTrailingCommentRanges(file.text, node.end) ?? []),
      ]) {
        if (
          /@ts-(?:ignore|expect-error|nocheck)\b|\b(?:oxlint|eslint)-disable\b/.test(
            file.text.slice(range.pos, range.end),
          )
        )
          report(node, "unchecked-escape", "Type/lint suppression directives are prohibited");
      }
      if (node.kind === SyntaxKind.AnyKeyword || node.kind === SyntaxKind.UnknownKeyword)
        report(node, "forbidden-type", "Forbidden explicit top type");
      if (node.kind === SyntaxKind.DeclareKeyword)
        report(
          node,
          "unchecked-escape",
          "Handwritten ambient declarations cannot assert runtime safety",
        );
      if (
        is.isNonNullExpression(node) ||
        is.isTypeAssertion(node) ||
        (is.isAsExpression(node) && node.type.getText(file) !== "const")
      )
        report(node, "unchecked-escape", "Assertions cannot establish validated application data");
      if (
        (is.isVariableDeclaration(node) ||
          is.isParameterDeclaration(node) ||
          is.isBindingElement(node)) &&
        node.name !== undefined
      )
        add(node.name, true);
      if (is.isFunctionLikeDeclaration(node)) add(node, true);
      if (is.isTypeAliasDeclaration(node)) add(node.name, true);
      if (
        is.isCallExpression(node) ||
        is.isNewExpression(node) ||
        is.isPropertyAccessExpression(node) ||
        is.isElementAccessExpression(node)
      )
        add(node);
      if (is.isReturnStatement(node) && node.expression !== undefined) add(node.expression, true);
      if (is.isPropertyAssignment(node)) add(node.initializer, true);
      // Ban the unchecked custom-schema escape even when it is given a concrete
      // generic type. Resolve aliases rather than matching the spelling `z`.
      if (
        is.isPropertyAccessExpression(node) ||
        is.isElementAccessExpression(node) ||
        is.isIdentifier(node)
      ) {
        const location = is.isPropertyAccessExpression(node)
          ? node.name
          : is.isElementAccessExpression(node)
            ? node.argumentExpression
            : node;
        const symbol = checker.getSymbolAtLocation(location);
        if (symbol !== undefined) {
          const target =
            (symbol.flags & SymbolFlags.Alias) !== 0 ? checker.getAliasedSymbol(symbol) : symbol;
          if (
            ["custom", "ZodCustom", "any", "unknown"].includes(target.name) &&
            target.declarations.some((declaration) =>
              /\/zod\//.test(declaration.path.replaceAll("\\", "/")),
            )
          )
            report(node, "unchecked-escape", "Unchecked/top-type Zod constructors are prohibited");
        }
      }
      if (is.isCallExpression(node) || is.isNewExpression(node)) {
        const declaration = checker.getResolvedSignature(node)?.declaration;
        if (declaration !== undefined && /\/zod\//.test(declaration.path.replaceAll("\\", "/"))) {
          const origin = declaration.resolve(project);
          if (
            origin !== undefined &&
            is.isFunctionDeclaration(origin) &&
            origin.name !== undefined &&
            ["custom", "any", "unknown"].includes(origin.name.text)
          )
            report(
              node,
              "unchecked-escape",
              "Unchecked/top-type Zod call is prohibited regardless of access syntax",
            );
        }
      }
      node.forEachChild(visit);
    }
    visit(file);
    const types = checker.getTypeAtLocation(values);
    for (const [index, node] of values.entries()) {
      const type = types[index];
      if (type === undefined)
        report(
          node,
          "missing-type",
          "Compiler could not establish a type for this application value",
        );
      else if (unsafeType(type, callables.has(node)))
        report(node, "forbidden-type", "Application value or result contains a forbidden top type");
    }
  }
  return findings;
}
