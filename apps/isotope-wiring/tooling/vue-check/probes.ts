import ts from "typescript";
import { z } from "zod";
import { auditVue } from "./audit.ts";
import { checkCoverage } from "./coverage.ts";
import { auditCurrentTypes } from "../../scripts/audit-current-types.ts";

const ProbeSchema = z.strictObject({
  name: z.string(),
  script: z.string(),
  template: z.string(),
  expected: z.string().nullable(),
  child: z.string().optional(),
  lang: z.enum(["ts", "js"]).default("ts"),
});
const probes = z.array(ProbeSchema).parse([
  {
    name: "valid-ref",
    script: 'import { ref } from "vue"; const value = ref(123);',
    template: "{{ value.toFixed(2) }}",
    expected: null,
  },
  {
    name: "valid-zod",
    script:
      'import { z } from "zod"; const S=z.strictObject({label:z.string()}); const value=S.parse({label:"x"});',
    template: "{{ value.label.toUpperCase() }}",
    expected: null,
  },
  {
    name: "script-error",
    script: 'const value: number = "wrong";',
    template: "{{ value }}",
    expected: "TS2322",
  },
  {
    name: "template-error",
    script: "const value=123;",
    template: "{{ value.toUpperCase() }}",
    expected: "TS2339",
  },
  {
    name: "explicit-any",
    script: "const value: any=123;",
    template: "{{ value }}",
    expected: "Forbidden",
  },
  {
    name: "explicit-unknown",
    script: "const value: unknown=123;",
    template: "{{ value }}",
    expected: "Forbidden",
  },
  {
    name: "json-result",
    script: 'const value=JSON.parse("{}");',
    template: "{{ value }}",
    expected: "Forbidden inferred",
  },
  {
    name: "catch-return",
    script:
      'function caught(){try{throw new Error("x");}catch(error){return error;}} const value=caught();',
    template: "{{ value }}",
    expected: "Forbidden inferred",
  },
  {
    name: "template-json",
    script: "const value=123;",
    template: '{{ value }} {{ JSON.parse("{}") }}',
    expected: "Forbidden inferred",
  },
  {
    name: "script-suppression",
    script: '// @ts-ignore\nconst value: number="wrong";',
    template: "{{ value }}",
    expected: "suppression",
  },
  {
    name: "vue-suppression",
    script: "const value=123;",
    template: "<!-- @vue-ignore -->\n{{ value.toUpperCase() }}",
    expected: "suppression",
  },
  {
    name: "assertion",
    script: 'const value="x" as string;',
    template: "{{ value }}",
    expected: "Forbidden",
  },
  {
    name: "custom-schema",
    script: 'import { z } from "zod"; const value=z.custom<string>().parse("x");',
    template: "{{ value }}",
    expected: "Unchecked Zod",
  },
  {
    name: "bindingless-catch",
    script:
      'function safe(){try{throw new Error("x");}catch{return "failed";}} const value=safe();',
    template: "{{ value }}",
    expected: null,
  },
  {
    name: "template-generic-default",
    script: "function read<T>() { return new Promise<T>(() => {}); }",
    template: "{{ read() }}",
    expected: "Forbidden inferred",
  },
  {
    name: "template-ref-generic-default",
    script: 'import {ref} from "vue"; const read=ref(<T>() => new Promise<T>(()=>{}));',
    template: "{{ read() }}",
    expected: "Forbidden inferred",
  },
  {
    name: "template-ref-generic-concrete",
    script: 'import {ref} from "vue"; const read=ref(<T>() => new Promise<T>(()=>{}));',
    template: "{{ read<string>() }}",
    expected: null,
  },
  {
    name: "template-generic-concrete",
    script: "function read<T>() { return new Promise<T>(() => {}); }",
    template: "{{ read<string>() }}",
    expected: null,
  },
  {
    name: "template-assertion",
    script: 'const value="x";',
    template: "{{ value as any }}",
    expected: "Forbidden",
  },
  {
    name: "template-nonnull",
    script: 'const value="x";',
    template: "{{ value! }}",
    expected: "Forbidden",
  },
  {
    name: "nested-unknown",
    script: "const value=new Promise(resolve=>{resolve(1);});",
    template: "{{ value }}",
    expected: "Forbidden inferred",
  },
  {
    name: "unknown-ref",
    script:
      'import {ref} from "vue"; function caught(){try{throw new Error("x");}catch(error){return error;}} const value=ref(caught());',
    template: "{{ value }}",
    expected: "Forbidden inferred",
  },
  {
    name: "destructured-value",
    script:
      'import {z} from "zod"; const {label:value}=z.strictObject({label:z.string()}).parse({label:"x"});',
    template: "{{ value.toUpperCase() }}",
    expected: null,
  },
  {
    name: "schema-props",
    script:
      'import {z} from "zod"; const S=z.strictObject({label:z.string()}); type Props=z.infer<typeof S>; const props=defineProps<Props>();',
    template: "{{ props.label.toUpperCase() }}",
    expected: null,
  },
  {
    name: "typed-loop",
    script:
      'import {z} from "zod"; const values=z.array(z.strictObject({label:z.string()})).parse([{label:"x"}]);',
    template:
      '<span v-for="value in values" :key="value.label">{{ value.label.toUpperCase() }}</span>',
    expected: null,
  },
  {
    name: "computed-custom",
    script: 'import {z} from "zod"; const key="custom"; const value=z[key]<string>().parse("x");',
    template: "{{ value }}",
    expected: "Unchecked Zod",
  },
  {
    name: "typed-component",
    script: 'import Child from "./Child.vue"; const value="x";',
    template: '<Child :label="value" />',
    child:
      '<script setup lang="ts">import {z} from "zod"; const S=z.strictObject({label:z.string()}); type Props=z.infer<typeof S>; const props=defineProps<Props>();</script><template>{{props.label}}</template>',
    expected: null,
  },
  {
    name: "wrong-component-prop",
    script: 'import Child from "./Child.vue"; const value=123;',
    template: '<Child :label="value" />',
    child:
      '<script setup lang="ts">import {z} from "zod"; const S=z.strictObject({label:z.string()}); type Props=z.infer<typeof S>; const props=defineProps<Props>();</script><template>{{props.label}}</template>',
    expected: "TS2322",
  },
  {
    name: "javascript-sfc",
    lang: "js",
    script: "const value=123;",
    template: "{{ value }}",
    expected: "Only local",
  },
  {
    name: "directive-string",
    script: 'const value="// @ts-ignore";',
    template: "{{ value }}",
    expected: null,
  },
]);
// Generated negative input only; remove it even when a probe fails.
const directory = ts.sys.resolvePath(".verification/vue-probes");
ts.sys.createDirectory(directory);
const file = `${directory}/Probe.vue`;
const child = `${directory}/Child.vue`;
const deleteFile = ts.sys.deleteFile?.bind(ts.sys);
if (deleteFile === undefined) throw new Error("Probe cleanup is unavailable");
try {
  for (const probe of probes) {
    deleteFile(child);
    if (probe.child !== undefined) ts.sys.writeFile(child, probe.child);
    ts.sys.writeFile(
      file,
      `<script setup lang="${probe.lang}">\n${probe.script}\n</script>\n<template><p>${probe.template}</p></template>\n`,
    );
    const findings = auditVue([file]);
    if (
      probe.expected === null
        ? findings.length !== 0
        : !findings.some((finding) => finding.message.includes(probe.expected ?? ""))
    )
      throw new Error(`Vue enforcement regression: ${probe.name}: ${JSON.stringify(findings)}`);
  }
} finally {
  deleteFile(file);
  deleteFile(child);
}
const disabledConfig = `${directory}/tsconfig.json`;
const configProbe = (text: string, expected: string): void => {
  try {
    ts.sys.writeFile(
      file,
      '<script setup lang="ts">const value=1;</script><template>{{value}} {{JSON.parse("{}")}}</template>',
    );
    ts.sys.writeFile(disabledConfig, text);
    if (!auditVue([file], disabledConfig).some((finding) => finding.message.includes(expected)))
      throw new Error(`Vue configuration escape: ${expected}`);
  } finally {
    deleteFile(file);
    deleteFile(disabledConfig);
  }
};
configProbe(
  '{"extends":"../../tsconfig.vue.json","vueCompilerOptions":{"skipTemplateCodegen":true}}',
  "Unchecked template generation",
);
configProbe(
  '{"extends":"../../tsconfig.vue.json","vueCompilerOptions":{"checkUnknownProps":false}}',
  "Strict Vue compiler baseline",
);
for (const suffix of ["worker.ts", "config.ts", "verification-helper.ts", "worker.js"]) {
  const name = `enforcement-probe.${suffix}`;
  if (ts.sys.fileExists(name)) throw new Error(`Refusing to overwrite ${name}`);
  try {
    ts.sys.writeFile(
      name,
      suffix.endsWith(".js")
        ? "export const value=1;"
        : 'export function caught(){try{throw new Error("probe");}catch(error){return error;}}',
    );
    const rejected = suffix.endsWith(".js")
      ? checkCoverage().some(
          (finding) => finding.file.endsWith(name) && finding.message.includes("JavaScript"),
        )
      : auditCurrentTypes().some(
          (finding) => finding.file.endsWith(name) && finding.code === "forbidden-type",
        );
    if (!rejected) throw new Error(`Coverage regression: ${name}`);
  } finally {
    deleteFile(name);
  }
}
const ownedProbe = "src/vue/enforcement-probe.ts";
if (ts.sys.fileExists(ownedProbe)) throw new Error("Refusing to overwrite Vue-owned probe");
const ownedCases = z
  .array(z.string())
  .parse([
    'export function caught(){try{throw new Error("probe");}catch(error){return error;}}',
    'export const value=JSON.parse("{}");',
    'import {createApp} from "vue"; import App from "./App.vue"; export const value=createApp(App).mount("#app").$el;',
  ]);
try {
  for (const source of ownedCases) {
    ts.sys.writeFile(ownedProbe, source);
    if (
      !auditVue([ts.sys.resolvePath(ownedProbe)]).some(
        (finding) =>
          finding.file.replaceAll("\\", "/").endsWith(ownedProbe) &&
          finding.message.includes("Forbidden"),
      )
    )
      throw new Error("Unsafe Vue-owned TypeScript escaped auditing");
  }
} finally {
  deleteFile(ownedProbe);
}
const partialConfig = "tsconfig.enforcement-probe.json";
const omittedVue = "enforcement-probe.vue";
if (ts.sys.fileExists(partialConfig) || ts.sys.fileExists(omittedVue))
  throw new Error("Refusing to overwrite coverage probes");
try {
  ts.sys.writeFile(partialConfig, '{"extends":"./tsconfig.json","include":["src/**/*.ts"]}');
  ts.sys.writeFile(
    omittedVue,
    '<script setup lang="ts">const value=1;</script><template>{{value}}</template>',
  );
  const findings = checkCoverage(partialConfig, partialConfig);
  if (
    !findings.some(
      (finding) =>
        finding.file.replaceAll("\\", "/").endsWith("tooling/vue-check/check.ts") &&
        finding.message.includes("escaped"),
    )
  )
    throw new Error("Excluded helper escaped coverage");
  if (
    !findings.some(
      (finding) => finding.file.endsWith(omittedVue) && finding.message.includes("escaped"),
    )
  )
    throw new Error("Excluded SFC escaped coverage");
} finally {
  deleteFile(partialConfig);
  deleteFile(omittedVue);
}
ts.sys.write(
  `PASS: ${probes.length} Vue controls/rejection probes, 2 configuration probes and 9 source-coverage/ownership probes\n`,
);
