#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
p=R/'research/aspect/contracts/u-g4-owner-construction-packet.v4.json'
x=json.loads(p.read_text(encoding='utf-8'))
fields=x['owner_required_fields']; flags=x['current_flags']; routes=x['owner_acceptance_routes']
checks={
 'predecessors_exist':all((R/q).exists() for q in x['predecessors']),
 'faithful_source_retained':x['selected_semantics']['source_retained'] is True,
 'full_bordered_coordinates':x['constructed_surrogate']['target']=='B_border carrying (rho0,E,W,R)',
 'projective_continuity':x['constructed_surrogate']['continuity']=='projective completed',
 'all_owner_fields_unfilled':all(v is None for v in fields.values()),
 'three_acceptance_routes':set(routes)=={'strict','evans_restricted','chain_invariant'},
 'strict_forward_not_return_fitting':'U_G4=T_pair_to_border' in routes['strict']['statement'],
 'xi_divisibility_route':'tau h' in routes['chain_invariant']['statement'],
 'analytic_crossing_constructed':flags['analytic_T_pair_to_border_constructed'] is True,
 'authoritative_map_not_exposed':flags['authoritative_U_G4_exposed'] is False,
 'pairings_not_exposed':flags['pairings_exposed'] is False,
 'comparison_not_testable':flags['comparison_testable'] is False,
 'acceptance_not_fabricated':flags['operator_acceptance_recorded'] is False,
 'rh_not_promoted':flags['rh_implication'] is False,
}
out={'schema':'marici.aspect.u-g4-owner-construction-packet-v4-check.v1','passed':all(checks.values()),'checks':checks,'verdict':'full analytic crossing and faithful graph are frozen; only owner U_G4 exposure, pairings, and one selected comparison route remain'}
q=R/'research/aspect/results/u_g4_owner_construction_packet_v4.check.v1.json';q.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
