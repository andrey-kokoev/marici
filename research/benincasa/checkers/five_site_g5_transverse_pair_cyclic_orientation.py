import json
from pathlib import Path

orb=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-cyclic-assembly.json').read_text())
ori=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-residue-orientation.json').read_text())
assert orb['free_orbit_count']==22 and ori['s2_character']=='sign'
packet={'schema':'marici.five_site_g5_transverse_pair_cyclic_orientation.v1',
 'cyclic_derivative':'orientation-preserving 2*pi/5 rotation on the loop tangent plane',
 'tangent_determinant_per_step':1,
 'wall_order_rule':'(A,B) maps to (sigma(A),sigma(B)) without exchange',
 'normal_orientation_transition_per_step':1,
 'five_step_composition':1,
 's2_wall_exchange_sign_retained':True,
 'c5_character':[110,0,0,0,0],
 'cyclic_orientation_twist':False,
 'free_orbit_count':22,'global_labelled_occurrence_count':110}
Path('research/benincasa/results/five-site-g5-transverse-pair-cyclic-orientation.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
