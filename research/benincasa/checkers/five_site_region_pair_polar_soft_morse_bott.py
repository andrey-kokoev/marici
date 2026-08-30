import json
from pathlib import Path

packet={
 'schema':'marici.five_site_region_pair_polar_soft_morse_bott.v1',
 'representative':['g_123','g_125'],
 'polar_direction':'n=-u_partner, equivalently motion from one focus toward the other',
 'exact_segment_identity':'|ell-C_e|+|ell-C_b|=|C_b-C_e| for ell on the open focal segment',
 'local_coordinates':['s along the focal segment','rho in the two transverse directions'],
 'distance_sum_expansion':'R + R*|rho|^2/(2*s*(R-s)) + O(|rho|^4), 0<s<R',
 'owner_wall_normal_form':'q_owner=delta+kappa(s)*|rho|^2+O(|rho|^4), kappa(s)=R/(2*s*(R-s))>0',
 'transverse_other_wall_gate':'partial_s(q_other) nonzero at the collision point',
 'double_localization':'Res_{q_other} d3ell/(q_owner*q_other) = nonzero_unit*d2rho/(delta+kappa*|rho|^2+...)',
 'generic_polar_period_type':'ordinary grade-zero logarithmic line',
 'carrier_classification':'existing edge-soft endpoint plus existing second region wall, with a Morse-Bott focal segment',
 'new_carrier_datum':False,
 'deeper_gate':'if partial_s(q_other)=0, retain the higher tangency and compute a separate excess complex',
 'scope':'conditional local normal form; existence of a polar collision in the dehomogenized physical family is not asserted',
}
Path('research/benincasa/results/five-site-region-pair-polar-soft-morse-bott.json').write_text(
 json.dumps(packet,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(json.dumps({k:packet[k] for k in ('exact_segment_identity','generic_polar_period_type','new_carrier_datum','scope')},sort_keys=True))
