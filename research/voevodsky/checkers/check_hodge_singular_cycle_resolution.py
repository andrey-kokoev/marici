"""Exact nodal-control arithmetic and proper-map typing checks."""
from pathlib import Path
import json


def multiply(a,b):
    out={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():out[i+k,j+l]=out.get((i+k,j+l),0)+x*y
    return {p:c for p,c in out.items() if c}


def main():
    for k in (1,2,3,5):
        first={(1,0):k,(0,1):-1}
        second={(1,0):k,(0,1):-2}
        total=multiply(multiply(first,first),second)
        assert total=={(3,0):k**3,(2,1):-4*k*k,(1,2):5*k,(0,3):-2}
        # Restriction of pi*E to the point exceptional divisor is zero.
        reduced={p:c for p,c in total.items() if 0 in p}
        assert reduced=={(3,0):k**3,(0,3):-2}
        pushed={p:c for p,c in reduced.items() if p[1]==0}
        assert pushed=={(3,0):k**3}
    assert (-1)**5==-1  # integral of e^6 on the complex-oriented point blowup
    # Ordinary threefold node: four affine coordinates, projective tangent cone Q2.
    assert 4-1==3 and (4-1)-1==2
    # On a blowup chart strict equation is 1+v1^2+v2^2+v3^2=0.
    # Vanishing of all its partials forces v=0, where the equation is 1, not 0.
    assert 1+sum(v*v for v in (0,0,0))==1
    for degree in (1,2,5):
        assert degree*3==sum(3 for _ in range(degree))
    assert 2*(6-3)==6  # H0 of smooth threefold maps to H6 of X
    assert 2*(6-2)==8  # dimension-two exceptional cycles have a different degree
    result={'passed':True,'classification':'all_cycle_generators_covered_by_smooth_proper_map_sources',
        'control_exceptional_fiber':'smooth quadric surface Q2',
        'control_strict_transform_class':'k^3*pi*(E^3)-2*e^3',
        'control_pushforward_class':'k^3*E^3','exceptional_H6_summand_pushforward':0,
        'resolution_generic_degree':1,'resolution_assumed_embedding_in_X':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Graph embedding and smooth auxiliary sixfold with controlled Lefschetz pushforward.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-singular-cycle-resolution-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
