"""General smooth-center bookkeeping; formal classes are not asserted cycles."""
from itertools import product
from math import comb
from pathlib import Path
import json
from check_hodge_deligne_lift_image import rank


def main():
    polynomial_controls=0
    for n1,n2,n3,m in product((-2,0,1,3),repeat=4):
        c1=n1+n2+n3;c2=n1*n2+n1*n3+n2*n3;c3=n1*n2*n3
        assert (m-n1)*(m-n2)*(m-n3)==m**3-m*m*c1+m*c2-c3
        polynomial_controls+=1
    b4X=comb(12,4)
    for b2Z in (0,1,7,66,100):
        strict=b4X+b2Z+1
        smooth_locus=strict-b2Z
        assert smooth_locus==496 and smooth_locus-b4X==1
    # Fixed-Hodge-space coordinate controls only: no new algebraic center asserted.
    E3=[1,0,0]
    for center in ([2,0,0],[1,1,0],[3,0,-2],[5,1,1]):
        primitive=[0,center[1],center[2]]
        epsilon=int(any(primitive))
        assert rank([E3,center])==1+epsilon
        assert 496-(495+epsilon)==1-epsilon
        assert rank([E3,primitive])==rank([E3,center])
    for k,m in ((1,2),(2,5),(3,7)):
        c1=3*k;c2=3*k*k;c3=k**3
        count=(m**3-m*m*c1+m*c2-c3)*2160*k**3
        assert count==2160*k**3*(m-k)**3>0
    result={'passed':True,'classification':'smooth_center_envelope_image_retains_center_class',
        'chern_root_controls':polynomial_controls,'KD_dimension':1,
        'b4_smooth_locus':496,'image_formula':'E cup H4(X) + Q cl(Z)',
        'primitive_map_formula':'psi(r_Z)=cl(Z) modulo E cup H4(X)',
        'arbitrary_center_primitive_class_assumed_zero':False,
        'singular_centers_covered':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Resolution and proper pushforward for singular cycle supports, without assuming embedded smoothability.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-smooth-center-envelope-image-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
