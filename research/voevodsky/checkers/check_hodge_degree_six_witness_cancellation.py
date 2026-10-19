"""Actual degree-six summands and replacement divisor witness on the test path."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from check_hodge_product_witness_first_order import real_imag_pair,derivation,J,add
from check_hodge_fixed_sixfold_pairing import wedge
from check_hodge_deligne_lift_image import rank


def triple(a,b,c):return wedge(wedge(a,b),c)


def form_rank(forms):
    keys=sorted(set().union(*(set(f) for f in forms)))
    return rank([[f.get(k,0) for k in keys] for f in forms])


def main():
    r1,s1=real_imag_pair(0,3);r2,s2=real_imag_pair(1,4);r3,s3=real_imag_pair(2,5)
    v=[triple(r1,r2,r3),triple(r1,s2,s3),triple(s1,r2,s3),triple(s1,s2,r3)]
    assert form_rank(v)==4
    K1=add((1,v[3]),(-1,v[0]));K2=add((1,v[1]),(1,v[2]))
    R={};I={}
    for bits in product((0,1),repeat=6):
        n=sum(bits);key=tuple(2*j+b for j,b in enumerate(bits))
        (R if n%2==0 else I)[key]=(-1)**(n//2)
    assert add((1,K1),(1,K2))==R
    dot={2:{(7,):2},3:{(6,):-2},6:{(3,):-2},7:{(2,):2}}
    dv=[derivation(f,dot) for f in v]
    assert [len(f) for f in dv]==[8]*4 and form_rank(dv)==2
    assert dv[0]==dv[3] and dv[1]==add((-1,dv[2]))
    # Replacement complex factors c1,c2,c3 are represented by exact real pairs.
    a,b=real_imag_pair(0,4);c,d=real_imag_pair(1,3)
    real12=add((1,wedge(a,c)),(-1,wedge(b,d)))
    imag12=add((1,wedge(a,d)),(1,wedge(b,c)))
    assert wedge(real12,r3)==K1 and add((-1,wedge(imag12,s3)))==K2
    assert add((1,wedge(real12,r3)),(-1,wedge(imag12,s3)))==R
    assert add((1,wedge(real12,s3)),(1,wedge(imag12,r3)))==I
    for t in (Q(0),Q(1,8),Q(-1,8)):
        op=J(t)
        assert all(not derivation(f,op) for f in (a,b,c,d,r3,s3,K1,K2,R,I))
        images=[derivation(f,op) for f in v]
        if t:
            assert all(images) and form_rank(images)==2
            assert images[0]==images[3] and images[1]==add((-1,images[2]))
        else:assert not any(images)
    result={'passed':True,'classification':'summand_obstructions_cancel_with_replacement_algebraic_witness',
        'summand_span_dimension':4,'first_order_rank':2,'kernel_dimension':2,
        'individual_summands_obstructed':4,'replacement_factor_pairs':[[1,5],[2,4],[3,6]],
        'pointwise_algebraicity_on_test_path':True,'relative_cycle_family_constructed':False,
        'fixed_endpoint_realization_decided':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Rational divisor Hodge space and degree-six product span in the joint two-parameter family.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-degree-six-witness-cancellation-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
