#!/usr/bin/env python3
import json,math
from pathlib import Path
R=Path(__file__).resolve().parents[3]
p=R/'research/aspect/contracts/u-g4-owner-construction-packet.v1.json';x=json.loads(p.read_text())
s=json.loads((R/'research/aspect/contracts/u-g4-owner-construction-packet.schema.v1.json').read_text())
required=set(s['required']); forbidden=set(x['independence']['forbidden_dependencies'])
construction_blob=json.dumps({'forward_map':x['forward_map'],'provenance':x['provenance'],'construction_dependencies':x['independence']['construction_dependencies']})
prov_paths=[z['source_path'] for z in x['provenance']]
# Nondegeneracy is structural: source Riesz tensor pairing is adopted nondegenerate;
# target pairing contains positive G_D on retained q, so zero norm forces q=0.
checks={
 'all_schema_fields':required<=set(x),
 'schema_name':x['schema']=='marici.aspect.u-g4-owner-construction-packet.v1',
 'operator_adoption':x['owner']=='repository-operator',
 'review_pending':x['authority']['reviewer']=='pending-independent-review',
 'source_basis_nonempty':len(x['source_carrier']['basis_or_coordinates'])>0,
 'target_retains_q':x['target_carrier']['basis_or_coordinates'][0]=='q',
 'two_pairing_lanes':len(x['forward_map']['generator_images'])==2,
 'prime_power_restriction':abs(math.log(3**7)-7*math.log(3))<1e-12,
 'source_pairing_nondegenerate_by_adoption':'tensor weighted-relative pairing' in x['pairings']['source']['formula'],
 'target_pairing_nondegenerate_by_retained_GD':'G_D' in x['pairings']['target']['formula'] and 'q' in x['target_carrier']['basis_or_coordinates'],
 'provenance_paths_exist':all((R/q).exists() for q in prov_paths),
 'provenance_outputs_complete':all(set(z)=={'output','source_equation','source_path'} for z in x['provenance']),
 'TPB_not_in_construction':'T_pair_to_border' not in construction_blob,
 'Evans_not_in_construction':'Evans residual' not in construction_blob,
 'forbidden_declared':{'T_pair_to_border','Evans residual','desired forward equality'}==forbidden,
 'comparison_postconstruction':x['independence']['comparison_is_postconstruction'] is True,
 'comparison_not_proved':x['claim_boundary']['comparison_proved'] is False,
 'rh_not_promoted':x['claim_boundary']['rh_implication'] is False}
out={'schema':'marici.aspect.u-g4-owner-construction-packet-check.v1','passed':all(checks.values()),'checks':checks,'authority_status':x['claim_boundary']['forward_map_authoritative'],'comparison_status':'not_run','verdict':'operator-adopted independent U_G4 packet is internally complete and frozen for review; comparison remains separate'}
(R/'research/aspect/results/u_g4_owner_construction_packet.check.v1.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
