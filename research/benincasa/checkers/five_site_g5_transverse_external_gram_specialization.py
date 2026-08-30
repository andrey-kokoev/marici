import json
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-g5-transverse-supported-physical-object.json').read_text())
assert src['labelled_summand_count']==110 and src['external_gram_monodromy']==-1
packet={'schema':'marici.five_site_g5_transverse_external_gram_specialization.v1',
 'rank_drop_chart':'Q=diag(1,1,s), H=diag(1,1,s^2), det(H)=s^2',
 'physical_coordinate_map':'u=(ell1,ell2,s*ell3)',
 'jacobian':'du1 wedge du2 wedge du3=s*dell1 wedge dell2 wedge dell3',
 'kummer_branch':'sqrt(det(H))=s on the oriented cover',
 'strict_transform_current':'du1 wedge du2 wedge du3/s=dell1 wedge dell2 wedge dell3',
 'deck_action':'s -> -s flips both the coordinate Jacobian and Kummer branch',
 'combined_current_deck_character':1,
 'generic_gram_nearby_excess_rank':0,
 'transverse_supported_summands_extend_conditionally':'yes, away from additional wall tangency and soft loci',
 'new_carrier_generator':False,
 'scope':'generic corank-one external-Gram specialization, not deeper tangency strata'}
Path('research/benincasa/results/five-site-g5-transverse-external-gram-specialization.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
