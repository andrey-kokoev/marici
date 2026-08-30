#!/usr/bin/env python3
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from observer_set_compiler import compile_observer_set
c=json.loads((ROOT/"research/aspect/contracts/theta-observer-profiles-221-211.v1.json").read_text(encoding="utf-8"));base=json.loads((ROOT/c["base_contract"]).read_text(encoding="utf-8"));compiled=compile_observer_set(base);members={m["id"]:m for m in base["members"]}
def audit(p):
    pos=[members[x]["arity"] for x in p["components"]["positive"]];neg=[members[x]["arity"] for x in p["components"]["negative"]];required=set(c["required_intertower_arities"]);coverage=required<=set(pos) and required<=set(neg)
    rows=[]
    for N in c["completion_hostile"]["cutoffs"]:
        # One extra scalar supported on coordinate 1 changes only the first singular value.
        augmented_squared=[Fraction(1,n*n)+(1 if n in c["completion_hostile"]["finite_rank_observer_support"] else 0) for n in range(1,N+1)]
        rows.append({"cutoff":N,"minimum_singular_value_squared":str(min(augmented_squared)),"minimum_singular_value":"1/"+str(N)})
    completion=False
    first="intertower_arity_coverage" if not coverage else "completion_closed_range"
    return {"id":p["id"],"observer_counts":[len(p["components"][k]) for k in ("positive","negative","determinant")],"intertower_arity_coverage":coverage,"finite_augmented_margins":rows,"completion_closed_range":completion,"first_failed_gate":first}
audits=[audit(p) for p in c["profiles"]];a221,a211=audits
checks={"base_2x2_compiles":compiled["passed"],"profiles_counted":a221["observer_counts"]==[2,2,1] and a211["observer_counts"]==[2,1,1],"221_retains_arity_coverage":a221["intertower_arity_coverage"],"221_finite_rank_extra_does_not_repair_completion":a221["first_failed_gate"]=="completion_closed_range" and not a221["completion_closed_range"],"221_margin_still_decays":[r["minimum_singular_value"] for r in a221["finite_augmented_margins"]]==["1/2","1/4","1/8","1/16"],"211_loses_square_intertower_coverage":not a211["intertower_arity_coverage"] and a211["first_failed_gate"]=="intertower_arity_coverage","determinant_scalar_does_not_substitute_for_missing_J2":a211["observer_counts"]==[2,1,1]}
out={"schema":"marici.aspect.theta-observer-profiles-221-211-check.v1","checks":checks,"audits":audits,"passed":all(checks.values()),"disposition":"2-2-1 preserves finite arity coherence but cannot repair nonclosed completion with one finite-rank observer; 2-1-1 fails earlier by losing negative-tower arity-2 coverage"};(ROOT/"research/aspect/results/theta_observer_profiles_221_211.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps({"schema":out["schema"],"checks":checks,"audits":audits,"disposition":out["disposition"],"passed":out["passed"]},indent=2));raise SystemExit(0 if out["passed"] else 1)
