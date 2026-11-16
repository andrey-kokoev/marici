import ts from "typescript";
import { parse, NodeTypes, type TemplateChildNode } from "@vue/compiler-dom";
import { FindingSchema, type Finding } from "./audit.ts";
import { canonicalPath as canonical, isVueOwned } from "./ownership.ts";

const executable = /\.(?:[cm]?tsx?|vue|[cm]?jsx?|html|sh|bash|ps1|py|pyw|cmd|bat)$/i;
const excluded = ["**/node_modules/**", ".verification/**", "dist/**"];

/** Enumerate source independently of tsconfig, so exclusions cannot hide owned files. */
export function checkCoverage(
  nativeConfig = "tsconfig.json",
  vueConfig = "tsconfig.vue.json",
): Finding[] {
  const findings: Finding[] = [];
  function report(file: string, message: string): void {
    findings.push(FindingSchema.parse({ file, offset: 0, message }));
  }
  const host = {
    ...ts.sys,
    onUnRecoverableConfigFileDiagnostic(diagnostic: ts.Diagnostic) {
      throw new Error(ts.flattenDiagnosticMessageText(diagnostic.messageText, "\n"));
    },
  };
  const typescript = ts.getParsedCommandLineOfConfigFile(nativeConfig, undefined, host);
  const vue = ts.getParsedCommandLineOfConfigFile(
    vueConfig,
    undefined,
    host,
    undefined,
    undefined,
    [{ extension: ".vue", isMixedContent: true, scriptKind: ts.ScriptKind.Deferred }],
  );
  if (typescript === undefined || vue === undefined)
    throw new Error("Coverage project unavailable");
  const tsFiles = new Set(typescript.fileNames.map(canonical));
  const vueFiles = new Set(vue.fileNames.map(canonical));
  for (const file of ts.sys.readDirectory(".", undefined, excluded, ["**/*"])) {
    if (!executable.test(file)) continue;
    const lower = file.toLowerCase();
    const name = canonical(file);
    if (/\.(?:[cm]?jsx?|sh|bash|ps1|py|pyw|cmd|bat)$/.test(lower)) {
      report(file, "Unchecked JavaScript or alternate-language executable source is prohibited");
      continue;
    }
    if (/\.d\.[cm]?ts$/.test(lower)) {
      report(file, "Handwritten ambient source is not admitted");
      continue;
    }
    if (lower.endsWith(".html")) {
      if (name !== canonical("index.html")) {
        report(file, "Only the checked application bootstrap HTML is admitted");
        continue;
      }
      const source = ts.sys.readFile(file);
      if (source === undefined) throw new Error(`Cannot read ${file}`);
      const root = parse(source, {
        onError(error) {
          report(file, error.message);
        },
      });
      function visit(node: TemplateChildNode): void {
        if (node.type !== NodeTypes.ELEMENT) return;
        if (!["html", "head", "meta", "title", "body", "div", "script", "link"].includes(node.tag))
          report(file, `Unsupported bootstrap element: ${node.tag}`);
        if (node.props.some((prop) => prop.type !== NodeTypes.ATTRIBUTE || /^on/i.test(prop.name)))
          report(file, "Executable HTML attributes/directives are prohibited");
        if (node.tag === "script") {
          const sourceAttribute = node.props.find(
            (prop) => prop.type === NodeTypes.ATTRIBUTE && prop.name === "src",
          );
          const typeAttribute = node.props.find(
            (prop) => prop.type === NodeTypes.ATTRIBUTE && prop.name === "type",
          );
          const src =
            sourceAttribute?.type === NodeTypes.ATTRIBUTE
              ? sourceAttribute.value?.content
              : undefined;
          const type =
            typeAttribute?.type === NodeTypes.ATTRIBUTE ? typeAttribute.value?.content : undefined;
          if (
            type !== "module" ||
            src === undefined ||
            !/^\/?[A-Za-z0-9_-]+(?:\/[A-Za-z0-9_-]+)*\.ts$/.test(src) ||
            !(
              tsFiles.has(canonical(src.replace(/^\//, ""))) ||
              (isVueOwned(src.replace(/^\//, "")) &&
                vueFiles.has(canonical(src.replace(/^\//, ""))))
            ) ||
            node.children.some(
              (child) => child.type !== NodeTypes.TEXT || child.content.trim() !== "",
            )
          )
            report(
              file,
              "Bootstrap scripts must reference a checked local TypeScript entrypoint; inline scripts are prohibited",
            );
        }
        node.children.forEach(visit);
      }
      root.children.forEach(visit);
      continue;
    }
    if (!vueFiles.has(name) || (!lower.endsWith(".vue") && !isVueOwned(name) && !tsFiles.has(name)))
      report(file, "Source escaped the checking projects");
  }
  return findings;
}
