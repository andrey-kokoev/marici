import json
from pathlib import Path

packet={
 'schema':'marici.five_site_region_pair_polar_feynman_elliptic.v1',
 'corrected_entry':1840,
 'local_integral':'I(delta_1,delta_2)=integral_R3 d3x/((x^T H_1 x+delta_1)*(x^T H_2 x+delta_2))',
 'feynman_identity':'1/(p*q)=integral_0^1 ds/(s*p+(1-s)*q)^2',
 'gaussian_identity':'integral_R3 d3x/(x^T C x+M)^2=pi^2/(sqrt(det C)*sqrt(M))',
 'reduced_period':'pi^2*integral_0^1 ds/[sqrt(det(sH_1+(1-s)H_2))*sqrt(s*delta_1+(1-s)*delta_2)]',
 'rank_two_hessian_data':['rank(H_1)=rank(H_2)=2','kernels are distinct focal-segment directions'],
 'determinant_factorization':'det(sH_1+(1-s)H_2)=s*(1-s)*L(s), with L(s) generically linear and nonzero on (0,1)',
 'period_curve':'w^2=s*(1-s)*L(s)*(s*delta_1+(1-s)*delta_2)',
 'generic_curve_genus':1,
 'coefficient_system':'rank-two elliptic Gauss-Manin variation with an overall square-root Kummer scaling character',
 'diagonal_scaling':'delta_1=delta_2=delta gives I~delta^(-1/2) times an elliptic period of s(1-s)L(s)',
 'entry_1840_surviving_statement':'the semisimple normal scaling/monodromy is square-root Kummer; rank-one does not describe the full coefficient variation',
 'carrier_support':'existing Gram/segment-intersection carrier from Entry 1839',
 'new_carrier_datum':False,
 'new_coefficient_complexity':'elliptic rank two, compiled canonically from the two physical Hessians',
}
Path('research/benincasa/results/five-site-region-pair-polar-feynman-elliptic.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('determinant_factorization','period_curve','generic_curve_genus','coefficient_system','new_carrier_datum')},sort_keys=True))
