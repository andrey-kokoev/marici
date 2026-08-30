import json
from pathlib import Path

coef=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-exact-coefficients.json').read_text())
cyc=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-cyclic-assembly.json').read_text())
rat=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-rational-quotients.json').read_text())
ori=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-residue-orientation.json').read_text())
phys=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-physical-intersections.json').read_text())
gram=json.loads(Path('research/benincasa/results/five-site-d3-physical-current.json').read_text())
node=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-threshold-node.json').read_text())
assert coef['all_active_coefficients_certified_nonzero'] and cyc['global_labelled_occurrence_count']==110
assert rat['coefficient_rank_per_labelled_occurrence']==1 and ori['orientation_line']=='det(N^*_{A,B})'
assert phys['physical_pairing_constructed'] and gram['coefficient_character'].endswith('det(H)^(-1/2)')
assert node['kinematic_discriminant_square_class']=='-1'
packet={'schema':'marici.five_site_g5_transverse_supported_physical_object.v1',
 'object':'K_det(H)^(-1/2) tensor direct_sum_[labelled (A,B)] i_(A,B),*(L_(A,B) tensor det(N^*_(A,B)))',
 'labelled_summand_count':110,'rank_per_summand':1,'cyclic_character':[110,0,0,0,0],
 'local_pairing_normalization':'physical intersection index cancels determinant-line orientation; remaining scalar is the exact source double residue',
 'source_coefficients_certified_nonzero':True,
 'quadratic_pole_monodromy':1,'external_gram_monodromy':-1,
 'monodromies_commute_on_generic_normal_crossing_locus':True,
 'threshold_node_splitting_field':'Q(i)','new_kinematic_character_at_node':False,
 'new_carrier_generator':False,
 'scope':'supported local physical coefficient object on the nonsingular external-Gram chart'}
Path('research/benincasa/results/five-site-g5-transverse-supported-physical-object.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
