#!/usr/bin/env python3
"""Authority inventory for a theta/Tate operator on principal parts."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/strominger/results/rh_source_filtered_operator_authority_audit.json"
TATE=ROOT/"src/ledger/20260825-2550 The Global Tate Integral Is the Legal Joint Completion.md"
COFACTOR=ROOT/"src/ledger/20260825-2601 Determinant Control Needs a Cofactor Bound.md"
CUTOFF=ROOT/"research/grothendieck/adelic-height-supplies-the-canonical-reciprocal-cutoff.md"
ADJOINT=ROOT/"research/grothendieck/adjoint-completion-makes-the-constant-source-channel-dynamical-and-forces-a-separate-response-port.md"
tate=TATE.read_text(encoding="utf-8"); cof=COFACTOR.read_text(encoding="utf-8"); cut=CUTOFF.read_text(encoding="utf-8"); adj=ADJOINT.read_text(encoding="utf-8")
checks={
 "global_tate_integral_supplies_scalar_joint_completion":"noncircular joint completion" in tate,
 "global_tate_integral_explicitly_lacks_operator_incidence":"does not by itself construct the operator-valued" in tate,
 "fixed_rank_theta_operator_explicitly_unsupplied":"No source-authorized theta/Tate higher-rank complex" in cof,
 "adelic_height_proves_cutoff_but_not_boundary_action":"The cutoff premise is now proved" in cut and "remaining premise is uniform" in cut,
 "adjoint_completion_requires_separate_response_port":"must be different ports" in adj and "derive the response row" in adj,
}
payload={"schema":"marici.strominger.rh_source_filtered_operator_authority_audit.v1","status":"passed" if all(checks.values()) else "failed","sources":[str(x.relative_to(ROOT)) for x in [TATE,COFACTOR,CUTOFF,ADJOINT]],"verdict":"Prior research supplies the scalar Tate completion, reciprocal-invariant adelic cutoff, and the typed input-state-output architecture. It explicitly does not supply an operator-valued seam incidence map, fixed-rank theta/Tate complex, response row, or invertible action on the associated-graded boundary class. Therefore no source operator F acts on the principal-parts tower yet. The abstract filtered Schur constructor cannot be instantiated without manufacturing precisely the missing datum.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8"); print(json.dumps(payload,indent=2)); raise SystemExit(0 if all(checks.values()) else 1)
