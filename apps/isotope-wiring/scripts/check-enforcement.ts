import { z } from "zod";
import { API, documentURIToFileName, fileNameToDocumentURI } from "typescript/unstable/sync";
import { auditProject, TypeFindingSchema } from "./type-audit.js";

const CompilerOverridesSchema = z.strictObject({
  strict: z.boolean().optional(),
  noUncheckedIndexedAccess: z.boolean().optional(),
});
const ProbeSchema = z.strictObject({
  name: z.string().regex(/^[a-z-]+$/),
  source: z.string(),
  expected: TypeFindingSchema.shape.code.nullable(),
  overrides: CompilerOverridesSchema.optional(),
});
// Negative examples are strings compiled in a virtual filesystem, never unchecked
// application files or retained source excluded from lint/type checking.
const probes = z.array(ProbeSchema).parse([
  { name: "explicit-any", source: "export const value: any = 1;", expected: "forbidden-type" },
  {
    name: "explicit-unknown",
    source: "export const value: unknown = 1;",
    expected: "forbidden-type",
  },
  {
    name: "catch-return",
    source:
      'export function caught() { try { throw new Error("probe"); } catch (error) { return error; } }',
    expected: "forbidden-type",
  },
  {
    name: "local-helper",
    source:
      'function caught() { try { throw new Error("probe"); } catch (error) { return error; } } export const result = caught();',
    expected: "forbidden-type",
  },
  {
    name: "json-result",
    source: 'export const result = JSON.parse("{}");',
    expected: "forbidden-type",
  },
  {
    name: "json-validator-intermediate",
    source:
      'import { z } from "zod"; export const result = z.strictObject({ id: z.string() }).parse(JSON.parse("{}"));',
    expected: "forbidden-type",
  },
  {
    name: "bindingless-catch",
    source:
      'export function failure() { try { throw new Error("probe"); } catch { return "syntax-error"; } }',
    expected: null,
  },
  {
    name: "promise-result",
    source: 'export const result = new Promise(resolve => { resolve("x"); });',
    expected: "forbidden-type",
  },
  {
    name: "nested-schema",
    source: 'import { z } from "zod"; export const S = z.object({ nested: z.array(z.unknown()) });',
    expected: "unchecked-escape",
  },
  {
    name: "unregistered-schema",
    source: 'import { z } from "zod"; const S = z.custom(); export const result = S.parse(1);',
    expected: "unchecked-escape",
  },
  {
    name: "concrete-custom",
    source: 'import { z } from "zod"; export const S = z.custom<string>();',
    expected: "unchecked-escape",
  },
  {
    name: "aliased-custom",
    source: 'import { custom as unchecked } from "zod"; export const S = unchecked<string>();',
    expected: "unchecked-escape",
  },
  {
    name: "computed-custom",
    source: 'import { z } from "zod"; export const S = z["custom"]<string>();',
    expected: "unchecked-escape",
  },
  {
    name: "computed-key-custom",
    source: 'import { z } from "zod"; const key = "custom"; export const S = z[key]<string>();',
    expected: "unchecked-escape",
  },
  {
    name: "suppression",
    source: '// @ts-ignore\nexport const value = "x";',
    expected: "unchecked-escape",
  },
  {
    name: "lint-suppression",
    source: '// oxlint-disable\nexport const value = "x";',
    expected: "unchecked-escape",
  },
  {
    name: "assertion",
    source: 'export const value = "x" as string;',
    expected: "unchecked-escape",
  },
  {
    name: "nonnull",
    source: "export function value(x?: string) { return x!; }",
    expected: "unchecked-escape",
  },
  {
    name: "ambient-escape",
    source:
      'declare function pretendValid(text: string): { id: string }; export const value = pretendValid("{}");',
    expected: "unchecked-escape",
  },
  {
    name: "literal-const",
    source: 'export const options = ["red", "blue"] as const;',
    expected: null,
  },
  {
    name: "weakened-strict",
    source: 'export const value = "x";',
    overrides: { strict: false },
    expected: "weak-configuration",
  },
  {
    name: "unchecked-index",
    source: 'export const value = "x";',
    overrides: { noUncheckedIndexedAccess: false },
    expected: "weak-configuration",
  },
  {
    name: "typed-schema",
    source:
      'import { z } from "zod"; export const S = z.object({ text: z.string() }); export const result = S.parse({ text: "x" });',
    expected: null,
  },
  { name: "comment-in-string", source: 'export const data = "// @ts-ignore";', expected: null },
]);
const configSchema = z.strictObject({
  extends: z.string(),
  files: z.array(z.string()),
  include: z.array(z.string()),
  compilerOptions: CompilerOverridesSchema.optional(),
});
const rootApi = new API();
let configName: string;
try {
  const snapshot = rootApi.updateSnapshot({ openProjects: ["tsconfig.json"] });
  try {
    const project = snapshot.getProject("tsconfig.json");
    if (project === undefined) throw new Error("Root project missing");
    configName = project.configFileName;
  } finally {
    snapshot.dispose();
  }
} finally {
  rootApi.close();
}
const base = fileNameToDocumentURI(configName);
const virtual = new Map<string, string>();
const normalize = (path: string): string => path.replaceAll("\\", "/").toLowerCase();
const paths = probes.map((probe) => {
  const config = documentURIToFileName(
    new URL(`./.type-probes/${probe.name}/tsconfig.json`, base).href,
  );
  const source = documentURIToFileName(new URL(`./.type-probes/${probe.name}/input.ts`, base).href);
  virtual.set(normalize(source), probe.source);
  virtual.set(
    normalize(config),
    JSON.stringify(
      configSchema.parse({
        extends: configName,
        files: [source],
        include: [],
        compilerOptions: probe.overrides,
      }),
    ),
  );
  return config;
});
const api = new API({
  fs: {
    readFile: (path) => virtual.get(normalize(path)),
    fileExists: (path) => (virtual.has(normalize(path)) ? true : undefined),
    directoryExists: (path) =>
      [...virtual.keys()].some((file) => file.startsWith(normalize(path).replace(/\/$/, "") + "/"))
        ? true
        : undefined,
  },
});
try {
  const snapshot = api.updateSnapshot({ openProjects: paths });
  try {
    for (const [index, probe] of probes.entries()) {
      const path = paths[index];
      if (path === undefined) throw new Error("Probe path missing");
      const project = snapshot.getProject(path);
      if (project === undefined) throw new Error(`Probe project missing: ${probe.name}`);
      const findings = auditProject(project);
      if (
        probe.expected === null
          ? findings.length !== 0
          : !findings.some((finding) => finding.code === probe.expected)
      )
        throw new Error(`Enforcement regression: ${probe.name}: ${JSON.stringify(findings)}`);
    }
  } finally {
    snapshot.dispose();
  }
} finally {
  api.close();
}
console.log(`PASS: ${probes.length} repeatable compiler-backed enforcement probes`);
