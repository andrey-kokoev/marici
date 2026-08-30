import json
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-rational-quotients.json').read_text())
assert src['active_local_pair_count']==22 and src['normal_determinant']=='D=a*d-b*c != 0'

# For L=[[a,b],[c,d]], x=L^{-1}h has
# x1=(d*h1-b*h2)/D and x2=(-c*h1+a*h2)/D.
# At tau=0 the quadratic is x1^2+x2^2 and factors over Q(i).
packet={'schema':'marici.five_site_g5_transverse_pair_threshold_node.v1',
 'active_local_pair_count':22,
 'tau_zero_quadratic':'((d*h1-b*h2)^2+(-c*h1+a*h2)^2)/D^2',
 'factor_1':'((d-i*c)*h1+(-b+i*a)*h2)/D',
 'factor_2':'((d+i*c)*h1+(-b-i*a)*h2)/D',
 'binary_quadratic_discriminant':'-4/D^2',
 'kinematic_discriminant_square_class':'-1',
 'splitting_field':'Q(i)',
 'node_type':'uv=0 after constant etale extension and linear normal change',
 'vanishing_cycle_rank':1,'node_monodromy':1,
 'new_kinematic_kummer_character':False,
 'new_carrier_generator':False,
 'classification':'constant-field nodal specialization of the existing quadratic coefficient pole'}
Path('research/benincasa/results/five-site-g5-transverse-pair-threshold-node.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
