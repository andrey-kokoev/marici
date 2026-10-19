"""Fixed-source arithmetic for the written Lefschetz/normal-bundle argument."""
from itertools import product
from pathlib import Path
import json
from check_hodge_fixed_sixfold_pairing import wedge,power,integrate


def main():
    E={(2*j,2*j+1):d for j,d in enumerate((1,1,1,-1,-1,-3))}
    R={};I={}
    for bits in product((0,1),repeat=6):
        key=tuple(2*j+b for j,b in enumerate(bits));n=sum(bits)
        (R if n%2==0 else I)[key]=(-1)**(n//2)
    E3=power(E,3)
    assert not wedge(E,R) and not wedge(E,I)
    assert R[tuple(range(0,12,2))]==1
    assert wedge(E,power(E,2))==E3
    assert integrate(wedge(E3,E3))==2160
    assert integrate(wedge(R,R))==-32
    # Polynomial coefficient arithmetic, not numerical very-ampleness bounds.
    controls=0
    for k in (1,2,3,5):
        class_Z={key:k**3*v for key,v in E3.items()}
        degree=integrate(wedge(class_Z,E3))
        assert degree==2160*k**3 and degree>0
        for m in (k,k+1,2*k,3*k):
            # c3((A^-1 tensor O(D))^3)=(m-k)^3 E^3|Z.
            top=(m-k)**3*degree
            expanded=(m**3-3*m*m*k+3*m*k*k-k**3)*degree
            assert top==expanded
            assert (top==0)==(m==k)
            if m>k:assert top>0
            controls+=1
    result={'passed':True,'classification':'smooth_envelope_exclusion_not_all_support_exclusion',
        'primitive_checks':['R','I'],'chern_polynomial_controls':controls,
        'smooth_envelope_image':'E cup H4(X,Q)',
        'known_algebraic_countercontrol':'CI(kE,kE,kE) forces singularities in every containing divisor mE with m>k',
        'singularity_number_or_type_proved':False,'all_supports_excluded':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Generic normal derivative transversality and local Hessian on the complete-intersection control.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-smooth-ample-envelope-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
