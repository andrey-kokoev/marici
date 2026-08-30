import json
from pathlib import Path

exact=json.loads(Path('research/benincasa/results/five-site-disjoint-region-pair-exact-survivor.json').read_text())
residue=json.loads(Path('research/benincasa/results/five-site-disjoint-region-pair-source-residue.json').read_text())
assert exact['both_physical_gradients_nonzero']
assert exact['positive_multiplier_ratio']==1
assert residue['transverse_morse_nondegenerate']

packet={
 'schema':'marici.five_site_region_pair_deformation_jacobian.v1',
 'representative':['g_123','g_125'],
 'unknowns':['ell_1','ell_2','ell_3','t','lambda'],
 'equations':['q_1=0','q_2=0','grad(q_1)+lambda*grad(q_2)=0'],
 'symmetric_point_relations':['lambda=1','v_2=-v_1=-v','H=H_1+H_2 positive definite','v nonzero'],
 'jacobian_after_sum_difference_rows':[
   ['0','0','0','6','0'],
   ['2*v^T','0','0'],
   ['H','0','-v'],
 ],
 'reduced_determinant_factor':'det(H)*(v^T*H^{-1}*v)',
 'reduced_determinant_positive':True,
 'full_landau_jacobian_invertible':True,
 'implicit_function_consequence':'unique smooth real solution (ell,t,lambda) for every sufficiently small labelled real external deformation',
 'open_conditions_preserved':['lambda>0','all internal distances>0','remaining source walls nonzero','source residue nonzero'],
 'classification':'the homogeneous threshold is a slice of a persistent multivariate coefficient discriminant over the same pair incidence',
 'new_carrier_datum':False,
}
Path('research/benincasa/results/five-site-region-pair-deformation-jacobian.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('reduced_determinant_factor','reduced_determinant_positive','full_landau_jacobian_invertible','new_carrier_datum')},sort_keys=True))
