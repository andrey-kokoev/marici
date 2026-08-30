import json
from pathlib import Path

packet={
 'schema':'marici.five_site_region_pair_polar_elliptic_discriminant.v1',
 'segment_hessians':'H_i=h_i*(I-e_i*e_i^T), h_i=R_i/[s_i*(R_i-s_i)]>0',
 'angle':'cos(theta)=e_1.e_2',
 'mixed_hessian_determinant':'det(xH_1+(1-x)H_2)=x*(1-x)*h_1*h_2*sin(theta)^2*(x*h_1+(1-x)*h_2)',
 'elliptic_curve':'w^2=x*(1-x)*(x*h_1+(1-x)*h_2)*(x*delta_1+(1-x)*delta_2), up to a nonzero square/unit',
 'branch_points':['0','1','-h_2/(h_1-h_2)','-delta_2/(delta_1-delta_2)'],
 'discriminant_support':[
   {'factor':'sin(theta)','classification':'parallel/coincident focal directions; deeper existing Gram degeneracy'},
   {'factor':'h_1*h_2','classification':'focal-segment endpoint/soft degeneration'},
   {'factor':'delta_1*delta_2','classification':'existing two labelled wall normals'},
   {'factor':'h_1*delta_2-h_2*delta_1','classification':'elliptic coefficient collision compiled from Hessian and normal ratios'},
 ],
 'generic_coefficient_collision':'h_1*delta_2-h_2*delta_1=0',
 'generic_collision_is_carrier':False,
 'new_carrier_datum':False,
 'classification':'all geometric degenerations lie on existing Gram/soft/wall support; the residual divisor is internal elliptic coefficient support',
}
Path('research/benincasa/results/five-site-region-pair-polar-elliptic-discriminant.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('mixed_hessian_determinant','generic_coefficient_collision','generic_collision_is_carrier','new_carrier_datum')},sort_keys=True))
