import json
from pathlib import Path

src=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-rational-quotients.json').read_text())
assert src['active_local_pair_count']==22
packet={'schema':'marici.five_site_g5_transverse_pair_residue_orientation.v1',
 'wall_swap':'(h1,row1) <-> (h2,row2)',
 'quadratic_pole_under_swap':'invariant',
 'normal_determinant_under_swap':'D -> -D',
 'ordered_double_residue_under_swap':'Res_B Res_A = - Res_A Res_B',
 'orientation_line':'det(N^*_{A,B})',
 's2_character':'sign',
 'scalar_denominator_product_character':'trivial',
 'coefficient_orientation_is_distinct_from_scalar_occurrence_symmetry':True,
 'active_local_pair_count':22,'global_labelled_occurrence_count':110,
 'new_carrier_generator':False}
Path('research/benincasa/results/five-site-g5-transverse-pair-residue-orientation.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
