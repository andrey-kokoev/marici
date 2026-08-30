#!/usr/bin/env python3
import copy,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from formula_synthesizer import synthesize_bridges
p=ROOT/"research/aspect/contracts/flavor-wp996-formula-synthesis.v1.json";c=json.loads(p.read_text(encoding="utf-8"));r=synthesize_bridges(c)
conditional=r["stages"][0];scale=r["stages"][1];closed=r["stages"][2]
hostile=copy.deepcopy(c);hostile["stages"][0]["equations"]=[e for e in hostile["stages"][0]["equations"] if "radius" not in e["coefficients"]];rh=synthesize_bridges(hostile)
fitted=copy.deepcopy(c);fitted["stages"][1]["observer_fitted"]=True;rf=synthesize_bridges(fitted)
checks={
 "conditional_formulas_derived":conditional["status"]=="derived" and len(conditional["formulas"])==7,
 "radius_formula_exact":conditional["formulas"]["radius"]["parameter_coefficients"]=={"B":"1/5489"},
 "full_rank_target_exact":conditional["formulas"]["Q_full"]["parameter_coefficients"]=={"B":"-7/49401"},
 "assumption_not_source_derivation":not any(x["source_derived"] for x in conditional["formulas"].values()),
 "physical_scale_underdetermined":scale["status"]=="underdetermined" and scale["underdetermined"]==["B"],
 "closed_loop_underdetermined":closed["status"]=="underdetermined",
 "physical_bridge_not_certified":r["bridge_status"]=="underdetermined" and set(r["missing_source_formulas"])=={"physical_scale.B","closed_loop.dual_error_bound"},
 "equation_deletion_first_failure":rh["stages"][0]["status"]=="partially_derived" and "radius" in rh["stages"][0]["underdetermined"],
 "observer_fitting_rejected":rf["stages"][1]["first_failed_gate"]=="observer_fitting"
}
out={"schema":"marici.aspect.flavor-wp996-formula-synthesis-check.v1","checks":checks,"synthesis":r,"passed":all(checks.values()),"disposition":"conditional formulas derived exactly; physical bridge formulas underdetermined"}
(ROOT/"research/aspect/results/flavor_wp996_formula_synthesis.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps({"schema":out["schema"],"checks":checks,"disposition":out["disposition"],"passed":out["passed"]},indent=2));raise SystemExit(0 if out["passed"] else 1)
