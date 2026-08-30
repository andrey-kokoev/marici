#!/usr/bin/env python3
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from categorical_compiler import compile_diagram
d=json.loads((ROOT/"research/aspect/contracts/flavor-wp996-categorical-audit.v1.json").read_text(encoding="utf-8"))
source=json.loads((ROOT/"research/flavor/results/wp996_bounded_control_chebyshev_optimum.json").read_text(encoding="utf-8"))
r=compile_diagram(d);physical=r["inverse_design"]["physical_selected_controller"];formal=r["inverse_design"]["conditional_chebyshev_optimum"]
samples=source["sample_rows"]
homogeneous=all(Fraction(row["full_rank"]["radius"])==Fraction(int(B),5489) for B,row in samples.items())
checks={
 "source_wp996_passes":source["status"]=="PASS" and all(source["checks"].values()),
 "exact_joint_radius":source["joint_optimal_radius"]=="B/5489",
 "exact_improvement":Fraction(source["improvement_factor_over_wp994_ray"])==Fraction(24697,5489),
 "sample_scale_homogeneity":homogeneous,
 "categorical_cell_passes":r["passed"] and r["cells"][0]["passed"],
 "scale_fiber_not_collapsed":not r["fibers"][0]["comparisons"][0]["verified_equivalent"],
 "formal_claim_admitted":formal["status"]=="admitted",
 "physical_claim_blocked":physical["status"]=="missing_witnesses" and set(physical["missing"])=={"source_control_norm","source_bound_B","closed_loop_dual_error"},
 "promotion_blocked":not r["promotions"][0]["admitted"],
 "joint_horns_unsupported":all(x["state"]=="unsupported" and not x["admitted"] for x in r["higher_coherence"]),
 "optical_transfer_refused":not r["functors"][0]["transfer_admitted"],
 "highest_gain_falsifier":physical["ranked_experiments"][0]["id"]=="source_derived_actuator_cost_ball" and physical["ranked_experiments"][0]["gain"]==2
}
out={"schema":"marici.aspect.flavor-wp996-categorical-audit.v1","source_model":"wp996-bounded-control-chebyshev-optimum","checks":checks,"categorical_compilation":r,"passed":all(checks.values()),"disposition":"conditional formal optimum survives; physical promotion fails at source norm/bound and closed-loop dual-error witnesses"}
(ROOT/"research/aspect/results/flavor_wp996_categorical_audit.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"schema":out["schema"],"checks":checks,"disposition":out["disposition"],"passed":out["passed"]},indent=2));raise SystemExit(0 if out["passed"] else 1)
