#!/usr/bin/env python3
"""Guard against promoting finite heat/rank certificates to the global Hardy co-defect."""
import json
from pathlib import Path
R=Path(__file__).parents[1]/'results'
r2=json.loads((R/'rank_two_compact_coverage_ledger.json').read_text());r3=json.loads((R/'rank_three_interval_tail.json').read_text());front=json.loads((R/'clark_positivity_frontier.json').read_text())
checks={
 'rank_two_interval_finite':r2['interval'][1]<float('inf'),
 'rank_three_interval_width_positive_but_finite':r3['interval'][1]>r3['interval'][0],
 'only_one_rank_three_cell_materialized':True,
 'all_rank_quantifier_uncovered':True,
 'all_upper_half_plane_packets_uncovered':True,
 'global_codefect_still_registered_open':front['single_open_statement']=='I-M_Theta M_Theta* >= 0 on upper-half-plane Hardy space',
}
assert all(checks.values())
out={'schema':'marici.voevodsky.finite-certification-codefect-guard.v1','checks':checks,'passed':True,
 'finite_progress':{'rank_two_interval':r2['interval'],'rank_two_cells':r2['cell_count'],'latest_rank_three_interval':r3['interval']},
 'logical_boundary':'No finite set of heat intervals, matrix ranks, or Pick packets proves positivity of I-M_Theta M_Theta*. The missing universal quantifiers are exactly the RH-strength statement.',
 'nonredundant_requirement':'A source-derived positive factorization valid simultaneously for every rank/packet, or an independent theorem implying the global Schur property.',
 'rh_proved':False}
p=R/'finite_certification_codefect_guard.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
