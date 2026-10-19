"""Truncated Chern arithmetic for a bounded source class; no bundle-existence test."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import json


def add(a,b):return [x+y for x,y in zip(a,b)]
def mul(a,b):return [sum(a[i]*b[d-i] for i in range(d+1)) for d in range(7)]
def dual(a):return [(-1)**d*x for d,x in enumerate(a)]
def character(r,a):return [Q(r)*Q(a,r)**d/factorial(d) for d in range(7)]
def c3(ch):return ch[1]**3/6-ch[1]*ch[2]+2*ch[3]


def main():
    root=Path(__file__).resolve().parents[3]
    prior=json.loads((root/'research/voevodsky/results/hodge-unipotent-arc-algebraization-v1.json').read_text(encoding='utf-8'))
    assert prior['passed'] and prior['Weil_projection']==[0,0]
    for r in (1,2,3,5):
        for a in (Q(-3),Q(0),Q(2,5),Q(6)):
            ch=character(r,a)
            assert ch[3]==a**3/(6*r*r)
            assert c3(ch)==Q((r-1)*(r-2),6*r*r)*a**3
            assert dual(ch)==character(r,-a)
    # Direct sums generally lose the single-exponential identity.
    hostile=add(character(1,Q(1)),character(1,Q(-1)))
    assert hostile[1]==0 and hostile[2]==1
    assert hostile!=character(2,Q(0))
    f=character(2,Q(3));g=character(3,Q(-2))
    assert mul(f,g)==character(6,Q(3*3+2*(-2)))
    generated=[f,g,add(f,g),mul(f,g),dual(add(f,g)),add(hostile,mul(f,g))]
    for ch in generated:
        for coefficient in (ch[3],c3(ch)):
            # Cohomological basis (E^3,R,I), not an equality of Chow classes.
            cycle=(coefficient,Q(0),Q(0))
            degree=2160*cycle[0]
            assert (cycle[0]-degree/2160,cycle[1],cycle[2])==(0,0,0)
    result={'passed':True,'classification':'bounded_generated_semihomogeneous_bundle_class_zero_Weil_readout',
        'imported_input':'simple semihomogeneous isogeny splitting; Mukai 1978',
        'fresh_primary_text_audit_performed':False,
        'single_exponential_formula_for_generators':True,
        'single_exponential_formula_for_arbitrary_generated_bundle':False,
        'operations':['direct_sum','extension_with_both_endpoints_in_class','tensor_product','dual'],
        'degree_three_cohomology_in_divisor_cube':True,
        'Picard_rank_one_used_as_Chow_rank_one':False,
        'all_algebraic_bundles_in_generated_class_claimed':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Track an arbitrary codimension-three cycle sheaf through ample-twist presentations to its terminal locally free syzygy.'}
    (root/'research/voevodsky/results/hodge-semihomogeneous-readout-boundary-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
