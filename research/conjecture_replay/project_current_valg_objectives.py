#!/usr/bin/env python3
import json,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];sys.path.insert(0,str(R/'research/conjecture_net'))
from objective_projection import *
actions=[
 ActionAssessment('VC2f_exact_weighted_overlap_reconstruction',frozenset({'exact_overlap_comparison','advance_valg_frontier'}),8,12,.25,.65,.55,.8,3,.1),
 ActionAssessment('VC2g_support_boundary_pre_audit',frozenset({'physical_admissibility','advance_valg_frontier'}),3,4,.25,.9,.75,.85,2,.25),
 ActionAssessment('VC2h_coefficient_height_feasibility_scout',frozenset({'reconstruction_feasibility','advance_valg_frontier'}),1,1.5,.25,.5,.95,.6,1,.4),
 ActionAssessment('NET1_calibrate_branch_probabilities',frozenset({'planner_calibration'}),2,3,.7,.2,.8,.9,2,1.0)]
objectives=[
 Objective('exact_algebraic_progress',ObjectiveKind.PROOF_QUALITY,'exact_overlap_comparison','maximum_certificate_strength',required_certificate=3),
 Objective('physical_authority_first',ObjectiveKind.FALSIFICATION,'physical_admissibility','maximum_falsification_value'),
 Objective('minimum_runtime_frontier_move',ObjectiveKind.COST,'advance_valg_frontier','minimum_expected_cost'),
 Objective('maximum_information_frontier_move',ObjectiveKind.INFORMATION,'advance_valg_frontier','maximum_information_gain'),
 Objective('planner_reliability',ObjectiveKind.GRAPH_MAINTENANCE,'planner_calibration','maximum_graph_repair')]
recs=[recommend(o,actions) for o in objectives]
out={'schema':'marici.conjecture-replay.current-v-alg-objective-projections.v1','assessment_warning':'Success probabilities and non-cost scores are declared engineering priors, not observed frequencies. The immutable evidence log is objective-neutral.','actions':[{'action':a.action,'reaches':sorted(a.reaches),'expected_cost':a.expected_cost,'worst_cost':a.worst_cost,'success_probability':a.success_probability,'falsification_value':a.falsification_value,'information_gain':a.information_gain,'robustness':a.robustness,'certificate_strength':a.certificate_strength,'graph_repair_value':a.graph_repair_value} for a in actions],'objectives':[{'name':o.name,'kind':o.kind.value,'target':o.target,'functional':o.functional,'risk':o.risk_attitude,'budget':o.budget,'required_certificate':o.required_certificate} for o in objectives],'recommendations':[r.__dict__ for r in recs],'passed':len({r.action for r in recs})>=3};assert out['passed'];(R/'research/conjecture_replay/results/current_valg_objective_projections.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'recommendations':{r.objective:r.action for r in recs}}))
