import json
from pathlib import Path

coef=json.loads(Path('research/benincasa/results/five-site-g5-transverse-pair-exact-coefficients.json').read_text())
grad=json.loads(Path('research/benincasa/results/five-site-g5-region-pair-gradient-census.json').read_text())
active=sorted({tuple(q['walls']) for q in coef['certificates'] if q['sheet']==-1})
assert len(active)==22 and coef['all_active_coefficients_certified_nonzero']
for pair in active:
 for sh in grad['exact_interval_certificates']:
  q=next(x for x in sh['pairs'] if tuple(x['walls'])==pair)
  assert not q['same_boundary_occurrences'] and not q['certified_collinear']

# Universal normalized model.  L=[[a,b],[c,d]], det D != 0.
# Solving L x=-h gives x=L^{-1}(-h), and x^T x has numerator below / D^2.
quadratic_numerator={
 'h1_squared':'c^2+d^2',
 'h1_h2':'-2*(a*c+b*d)',
 'h2_squared':'a^2+b^2',
}
packet={'schema':'marici.five_site_g5_transverse_pair_rational_quotients.v1',
 'active_local_pair_count':22,'sheetwise_gradient_certificate_count':44,
 'normal_matrix':'L=[[a,b],[c,d]]','normal_determinant':'D=a*d-b*c != 0',
 'double_residue':'(2*pi*i)^2/(D*(tau+h^T*L^(-T)*L^(-1)*h))',
 'quadratic_numerator_over_D_squared':quadratic_numerator,
 'coefficient_rank_per_labelled_occurrence':1,'semisimple_monodromy':1,'nilpotent_rank':0,
 'kummer_tensor_product':False,
 'reason':'two independent wall residues fix both Morse variables and leave a meromorphic quadratic pole',
 'global_labelled_rank':110,'cyclic_character':[110,0,0,0,0],
 'new_carrier_generator':False}
Path('research/benincasa/results/five-site-g5-transverse-pair-rational-quotients.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps(packet,sort_keys=True))
