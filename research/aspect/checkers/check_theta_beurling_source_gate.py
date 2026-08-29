#!/usr/bin/env python3
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from beurling_rigging_compiler import audit_beurling_source_gate
cpath=ROOT/"research/aspect/contracts/theta-beurling-source-gate.v1.json";rpath=ROOT/"research/aspect/results/theta_beurling_source_gate.json";c=json.loads(cpath.read_text(encoding="utf-8"));audit=audit_beurling_source_gate(c)
checks={"blocked_at_topology_branch":audit.get("first_failed_gate")=="topology_branch","polynomial_not_promoted":audit.get("passed") is False,"control_authority_explicit":c.get("topology_authority")=="hostile_control_only"}
out={"schema":"marici.aspect.theta-beurling-source-gate-check.v1","audit":audit,"checks":checks,"passed":all(checks.values()),"next_constructor":"use the source-selected projective exponential branch"};rpath.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,indent=2));raise SystemExit(0 if out["passed"] else 1)
