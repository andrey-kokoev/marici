import json
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-rational-quotients.json').read_text())
assert src['active_local_pair_count']==22
packet={'schema':'marici.five_site_g5_transverse_pair_tangency_rees.v1',
 'rank_one_normal_form':['g1=h1+u','g2=h2+alpha*u+epsilon*v'],
 'tangency_normal':'epsilon=det(L) up to a unit',
 'compatibility_normal':'k=h2-alpha*h1',
 'double_residue':'epsilon/(k^2+epsilon^2*(tau+h1^2)) up to an analytic unit',
 'weighted_center':'(epsilon,k) with equal Rees weight one',
 'exceptional_chart':'k=epsilon*kappa',
 'pulled_back_residue':'1/(epsilon*(kappa^2+tau+h1^2))',
 'normalized_exceptional_grade':'epsilon*Res=1/(kappa^2+tau+h1^2)',
 'exceptional_rank':1,'exceptional_nilpotent_rank':0,
 'generic_k_nonzero_specialization':'zero',
 'support_condition':'epsilon=0 and k=0',
 'classification':'derived polar/compatibility support of two existing wall sections',
 'new_primary_carrier_generator':False,
 'physical_activation_computed':False}
Path('research/benincasa/results/five-site-g5-transverse-pair-tangency-rees.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
