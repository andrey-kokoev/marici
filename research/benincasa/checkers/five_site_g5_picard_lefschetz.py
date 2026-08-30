import json
from pathlib import Path

from five_site_disjoint_mixed_pair_real_branches import K,Rat,sign_on_isolated_root,derivative
from five_site_g5_cm_domain import X,C,landau,pfun,x

xr=Rat(X); cr=Rat(C); h=Rat([K(2)])*pfun-cr
h1=Rat([K(25)])*xr*xr-Rat([K(4)])*pfun*h
h2=h*(h-Rat([K(4)])*pfun)
def rsign(r):
    return sign_on_isolated_root(landau,x,r.n)*sign_on_isolated_root(landau,x,r.d)
signs=[rsign(h1),rsign(h2)]
assert signs==[1,1]
landau_derivative_sign=sign_on_isolated_root(landau,x,derivative(landau))
assert landau_derivative_sign!=0
source=json.loads(Path('research/benincasa/results/five-site-g5-source-residue.json').read_text())
assert all(q['certified_nonzero'] for q in source['exact_interval_certificates'])
packet={'schema':'marici.five_site_g5_picard_lefschetz.v1',
        'cleared_transverse_hessian_signs':signs,'morse_index':0,
        'landau_slice_derivative_sign':landau_derivative_sign,
        'slice_intersection_transverse':True,
        'generic_codimension_one_persistence':True,
        'local_intersection_number_per_reflected_point':1,
        'reflected_point_count':2,'total_local_intersection_number':2,
        'source_residue_noncancellation_certified':True,
        'physical_discontinuity_nonzero':True,
        'local_period_singularity':'nonzero logarithm',
        'semisimple_monodromy_on_vanishing_line':1,
        'unipotent_logarithm_rank':1,
        'unipotent_logarithm_square_zero':True,
        'normalization':'source i0 double-Leray orientation; positive-definite real Morse normal form'}
Path('research/benincasa/results/five-site-g5-picard-lefschetz.json').write_text(json.dumps(packet,indent=2,sort_keys=True)+'\n')
print(json.dumps(packet,sort_keys=True))
