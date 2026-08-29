#!/usr/bin/env python3
import copy,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from projective_rigging_compiler import compile_projective_rigging
cpath=ROOT/"research/aspect/contracts/theta-projective-exponential-rigging.v1.json";rpath=ROOT/"research/aspect/results/theta_projective_exponential_rigging.json";base=json.loads(cpath.read_text(encoding="utf-8"));audit=compile_projective_rigging(base)
def hostile(name,mutate,expected):
    c=copy.deepcopy(base);mutate(c);r=compile_projective_rigging(c);return {"id":name,"expected":expected,"actual":r.get("first_failed_gate"),"passed":r.get("first_failed_gate")==expected}
hostiles=[hostile("finite_scales_only",lambda c:c.update(all_positive_scales=False),"projective_scale"),hostile("fixed_rung_adams",lambda c:c["adams_transport"][0].update(fixed_rung_bounded_claim=True),"seminorm_transport"),hostile("collapse_grades",lambda c:c["grade_roles"].update(primitive="hilbert_state"),"grade_asymmetry"),hostile("riesz_promote_primitive",lambda c:c["dual_rows"][2].update(promoted_to_hilbert_state=True),"strong_dual"),hostile("direct_archimedean_current",lambda c:c["grade_roles"].update(archimedean="attached_boundary_current"),"grade_asymmetry")]
checks={"source_topology_selected":base["topology_authority"]=="source_selected","archimedean_kept_on_determinant_line":base["grade_roles"]["archimedean"]=="determinant_line_tensor_extension","blocked_at_archimedean_operator_lift":audit.get("first_failed_gate")=="archimedean_operator_lift","common_graph_domain_not_reached":base["common_graph_domain"]["status"]=="open","hostiles":all(x["passed"] for x in hostiles)}
out={"schema":"marici.aspect.theta-projective-rigging-check.v1","audit":audit,"hostiles":hostiles,"checks":checks,"passed":all(checks.values()),"next_constructors":["derive the explicit determinant-line-to-operator lift","then construct one source-authorized common graph domain for the nine mixed operators"]};rpath.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,indent=2));raise SystemExit(0 if out["passed"] else 1)
