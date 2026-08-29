#!/usr/bin/env python3
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from formula_synthesizer import synthesize_bridges
c=json.loads((ROOT/"research/aspect/contracts/flavor-wp1037-formula-synthesis.v1.json").read_text(encoding="utf-8"));source=json.loads((ROOT/"research/flavor/results/wp1037_discrete_source_actuator_type_no_go.json").read_text(encoding="utf-8"));r=synthesize_bridges(c)
local,substrate,closed=r["stages"]
zero=lambda name:local["formulas"][name]=={"constant":"0","parameter_coefficients":{},"source_derived":True}
checks={
 "wp1037_source_passes":source["status"]=="PASS",
 "authorized_rank_zero":source["authorized_local_actuator"]["rank"]==0,
 "unit_neighborhood_singleton":source["authorized_local_actuator"]["unit_ball_points"]==[[2,23]],
 "zero_command_formula_derived":local["status"]=="derived" and zero("delta_k") and zero("delta_C"),
 "local_radius_formula_is_zero":zero("B_local"),
 "wp996_positive_budget_impossible_locally":local["formulas"]["B_local"]["constant"]=="0",
 "continuous_relaxation_rejected_by_source":source["false_continuous_repair"]["hostile_command"]=="(1/2,0) leaves the integer source domain",
 "common_substrate_formula_underdetermined":substrate["status"]=="underdetermined" and set(substrate["free_unknowns"])=={"preparation_arrow","support_bound","cost_bound"},
 "closed_loop_formula_underdetermined":closed["status"]=="underdetermined",
 "overall_bridge_not_derived":r["bridge_status"]=="underdetermined"
}
out={"schema":"marici.aspect.flavor-wp1037-formula-synthesis-check.v1","checks":checks,"synthesis":r,"derived_local_support":{"reachable_displacements":[[0,0]],"cost_law":"cost(0,0)=0; cost(delta)=infinity for every other local displacement","scalar_radius":"B_local=0"},"missing_formula_type":"common-substrate discrete preparation arrows plus source-derived support/cost, followed by closed-loop error","passed":all(checks.values())}
(ROOT/"research/aspect/results/flavor_wp1037_formula_synthesis.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps({"schema":out["schema"],"checks":checks,"derived_local_support":out["derived_local_support"],"missing_formula_type":out["missing_formula_type"],"passed":out["passed"]},indent=2));raise SystemExit(0 if out["passed"] else 1)
