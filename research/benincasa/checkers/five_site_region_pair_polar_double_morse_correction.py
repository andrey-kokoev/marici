import json
from pathlib import Path

packet={
 'schema':'marici.five_site_region_pair_polar_double_morse_correction.v1',
 'corrected_entry':1837,
 'polar_owner_gradient':'grad(q_1)=0 on the open owner focal segment',
 'positive_landau_equation':'alpha*grad(q_1)+beta*grad(q_2)=0 with alpha,beta>0',
 'forced_consequence':'grad(q_2)=0; the point lies on the second focal segment as well',
 'transverse_second_wall_case':'not a Landau point and withdrawn as a coefficient model',
 'generic_true_polar_geometry':'two nonparallel focal segments intersect at one point',
 'hessian_kernels':['ker(H_1)=tangent line to segment 1','ker(H_2)=tangent line to segment 2'],
 'positive_combination':'alpha*H_1+beta*H_2 positive definite when segment directions are nonparallel',
 'local_integral':'integral d3x/((delta_1+Q_1(x))*(delta_2+Q_2(x)))',
 'diagonal_scaling':'delta_1~delta_2~delta gives delta^(3/2-2)=delta^(-1/2)',
 'local_period_type':'rank-one square-root Kummer/Morse coefficient with monodromy -1 on a generic diagonal normal',
 'carrier_support':'existing Gram segment-intersection divisor plus labelled focal-length equality',
 'new_carrier_datum':False,
 'deeper_gate':'parallel or coincident focal segments make the Hessian degenerate and require a separate excess calculation',
}
Path('research/benincasa/results/five-site-region-pair-polar-double-morse-correction.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('forced_consequence','transverse_second_wall_case','diagonal_scaling','local_period_type','new_carrier_datum')},sort_keys=True))
