#!/usr/bin/env python3
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
x=json.loads((R/'research/aspect/results/u_g4_owner_side_field_extraction.v1.json').read_text())
s=(R/x['primary_record']).read_text()
e=x['independently_extracted'];t=x['typing_comparison']
checks={
 'source_exists':(R/x['primary_record']).exists(),
 'radial_carrier_literal':e['radial_target_carrier'] in s,
 'loading_literal':e['completed_loading'] in s,
 'cutoff_map_literal':e['finite_cutoff_map'] in s,
 'coefficient_literal':e['arithmetic_coefficient'].replace('sum_(k>=1)','sum_{k>=1}') in s,
 'graph_metric_literal':e['graph_metric'] in s,
 'owner_readback_false':x['authority_readback']['g4_owner_readback'] is False,
 'not_authoritative_without_adoption':x['authority_readback']['usable_as_authoritative_U_G4_without_adoption'] is False,
 'independent_candidate':e['independent_of_T_pair_to_border'] is True,
 'domain_gap':t['domain_identification']=='missing',
 'codomain_gap':t['codomain_identification']=='missing',
 'first_incompatibility':t['first_incompatible_field']=='source_carrier',
 'generator_images_missing':x['worksheet_population']['U_G4_generator_images']=='missing',
 'rh_not_promoted':x['rh_implication'] is False}
o={'schema':'marici.aspect.u-g4-owner-side-field-extraction-check.v1','passed':all(checks.values()),'checks':checks,'verdict':x['verdict']}
(R/'research/aspect/results/u_g4_owner_side_field_extraction.check.v1.json').write_text(json.dumps(o,indent=2)+'\n');print(json.dumps(o,indent=2));raise SystemExit(0 if o['passed'] else 1)
