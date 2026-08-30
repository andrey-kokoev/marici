import json
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-residue-orientation.json').read_text())
assert src['s2_character']=='sign'
packet={'schema':'marici.five_site_g5_transverse_pair_gysin_covariance.v1',
 'morse_coordinate_change':{
  'rule':'x_prime=S*x; dx=det(S)^(-1)*dx_prime; L_prime=L*S^(-1)',
  'determinant_rule':'det(L_prime)=det(L)/det(S)',
  'residue_ratio_rule':'det(S)^(-1)/det(L_prime)=1/det(L)',
  'conclusion':'invariant'},
 'wall_basis_change':{
  'rule':'h_prime=R*h; L_prime=R*L',
  'quadratic_rule':'h_prime^T*L_prime^(-T)*L_prime^(-1)*h_prime=h^T*L^(-T)*L^(-1)*h',
  'determinant_rule':'det(L_prime)=det(R)*det(L)',
  'residue_rule':'Res_prime=det(R)^(-1)*Res',
  'compensating_line':'det(N^*)'},
 'strict_local_gysin_map_exists':True,
 'map_level':'source-normalized local de Rham coefficient germ',
 'physical_relative_chain_map_constructed':False,
 'active_local_pair_count':22,'global_labelled_occurrence_count':110,
 'new_carrier_generator':False}
Path('research/benincasa/results/five-site-g5-transverse-pair-gysin-covariance.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
