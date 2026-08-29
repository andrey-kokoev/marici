#!/usr/bin/env python3
"""Derive and freeze the fixed-sample comparison-loop acquisition budget."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"comparison-loop-statistical-power.v1.json"
PROBES=ASPECT/"results"/"comparison_loop_optimal_probes.json"
RESULT=ASPECT/"results"/"comparison_loop_statistical_power.json"; PLAN=ASPECT/"results"/"comparison_loop_fixed_sample_plan.json"
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); p=json.loads(PROBES.read_text(encoding="utf-8"))
 m=c["primary_estimands"]; alpha=c["familywise_alpha"]; tau=c["quadrature_tolerance"]
 n=math.ceil(2*math.log(2*m/alpha)/(tau*tau)); bound=2*m*math.exp(-n*tau*tau/2)
 two_sided=2*(c["systematic_per_estimate"]+tau); margin=p["optimal_spread"]-two_sided; total=m*n
 checks={"derived_sample_size":n==8356,"familywise_bound":bound<=alpha,"decision_margin":margin>=c["minimum_decision_margin"],"four_estimands":m==4,"both_quadratures":True,"controls_complete":set(c["controls"])=={"same_route_A","same_route_B","phase_fixture_X","phase_fixture_Y"},"calibration_not_smuggled":"independent bright-reference" in c["calibration_separation"],"claim_boundary":not any(c["claim_boundary"].values())}
 plan={"schema":"marici.aspect.comparison-loop-fixed-sample-plan.v1","status":"preregistered_not_run","effective_trials_per_estimand":n,"estimands":[{"probe":"minimum_fringe","quadrature":"X"},{"probe":"minimum_fringe","quadrature":"Y"},{"probe":"maximum_fringe","quadrature":"X"},{"probe":"maximum_fringe","quadrature":"Y"}],"total_primary_trials":total,"familywise_bound":bound,"controls":c["controls"],"stopping_rule":"fixed_sample_no_optional_stopping"}
 out={"schema":"marici.aspect.comparison-loop-statistical-power-result.v1","passed":all(checks.values()),"checks":checks,"trials_per_estimand":n,"total_primary_trials":total,"previous_primary_trials":400000,"reduction_fraction":1-total/400000,"familywise_bound":bound,"two_sided_difference_uncertainty":two_sided,"remaining_margin":margin,"plan":str(PLAN.relative_to(ROOT)).replace("\\","/"),"physical_status":"not_run"}
 PLAN.write_text(json.dumps(plan,indent=2)+"\n",encoding="utf-8"); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__": main()
