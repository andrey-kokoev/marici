import ts from "typescript";
import { auditVue } from "./audit.ts";
import { checkCoverage } from "./coverage.ts";

const findings = [...checkCoverage(), ...auditVue()];
for (const finding of findings)
  ts.sys.write(`${finding.file}:${finding.offset}: ${finding.message}\n`);
if (findings.length > 0) throw new Error(`${findings.length} Vue checking failures`);
ts.sys.write("PASS: Vue type checking and authored-value audit (TypeScript 6 sidecar)\n");
