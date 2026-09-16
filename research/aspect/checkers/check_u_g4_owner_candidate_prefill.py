#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
x=json.loads((R/'research/aspect/results/u_g4_owner_candidate_prefill.v1.json').read_text())
texts=[(R/p).read_text() for p in x['sources']]
t='\n'.join(texts);c=x['candidate_fields']
checks={
 'sources_exist':all((R/p).exists() for p in x['sources']),
 'basis_source_derived':c['source_carrier']['basis_or_coordinates'] in t,
 'riesz_source_derived':c['pairing_formula']['relative_Riesz'] in t,
 'trace_coordinates_source_derived':all(q in t for q in c['target_carrier']['trace_coordinates']),
 'loading_source_derived':c['global_map']['formula'] in t,
 'cutoff_source_derived':c['global_map']['finite_cutoff'] in t,
 'coefficient_source_derived':c['local_generator_map']['loading_coefficient'] in t,
 'existing_checker_passed':x['existing_checker']['latest_result']['passed'] is True,
 'all_grades':x['existing_checker']['latest_result']['all_grades'] is True,
 'independent_of_comparison':not x['independence']['reads_T_pair_to_border'] and not x['independence']['reads_Evans_residual'],
 'pairing_matrix_still_missing':c['pairing_formula']['coordinate_matrices'] is None,
 'owner_gate_open':not x['promotion']['authoritative_U_G4'],
 'comparison_blocked':not x['promotion']['comparison_permitted'],
 'rh_not_promoted':not x['promotion']['rh_implication']}
o={'schema':'marici.aspect.u-g4-owner-candidate-prefill-check.v1','passed':all(checks.values()),'checks':checks,'remaining_count':len(x['remaining_for_owner_packet']),'verdict':'local independent candidate now supplies basis-level map and completion laws; owner adoption and carrier/pairing identifications remain'}
(R/'research/aspect/results/u_g4_owner_candidate_prefill.check.v1.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));raise SystemExit(0 if o['passed'] else 1)
