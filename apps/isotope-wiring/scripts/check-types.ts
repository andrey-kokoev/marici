import { auditCurrentTypes } from "./audit-current-types.ts";

const findings = auditCurrentTypes();
for (const finding of findings)
  console.error(
    `${finding.file}:${finding.line}:${finding.column} ${finding.code}: ${finding.message}`,
  );
if (findings.length > 0)
  throw new Error(`${findings.length} forbidden or unchecked application types`);
console.log("PASS: TypeScript 7 project source audit (Vue-owned code is checked by the sidecar)");
