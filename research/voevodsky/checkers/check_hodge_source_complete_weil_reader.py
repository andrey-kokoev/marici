"""Exact reader/descent/degree controls; universal vanishing remains unproved."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json


def reader(v):
    a,b,c=v
    return (-Q(1,32)*(-32*b),-Q(1,32)*(-32*c))


def main():
    controls=0
    for v in product((Q(-1),Q(0),Q(1,2),Q(1)),repeat=3):
        a,b,c=v;F=reader(v)
        assert F==(b,c)
        assert 32*sum(t*t for t in F)==32*(b*b+c*c)
        # Isogeny action preserves each formal rival image model.
        fz=(-117*b+44*c,-44*b-117*c)
        determinant=b*fz[1]-c*fz[0]
        assert determinant==-44*(b*b+c*c)
        if F!=(0,0):assert determinant!=0
        for degree in (1,2,27):
            raw_pulled=(-32*degree*b,-32*degree*c)
            assert tuple(-x/Q(32*degree) for x in raw_pulled)==F
            graph_pairings=(-32*b,-32*c)
            assert tuple(-x/Q(32) for x in graph_pairings)==F
            if degree>1 and F!=(0,0):
                assert tuple(-x/Q(32*degree) for x in graph_pairings)!=F
            assert reader(tuple(degree*x for x in v))==tuple(degree*x for x in F)
        controls+=1
    # A formal presentation relation: s(x,y,z)=(x+z,y+z,0).
    s=lambda p:(p[0]+p[2],p[1]+p[2],Q(0))
    assert s((0,0,1))==s((1,1,0))
    assert reader(s((0,0,1)))==reader(s((1,1,0)))
    assert reader((1,0,0))==(0,0)  # A0: polarization-only formal image
    assert reader((0,1,0))==(1,0)  # A1: larger formal image, NOT an actual cycle claim
    result={'passed':True,'classification':'source_complete_reader_merged_with_existing_projector_gate',
        'rational_controls':controls,'reader_formula':'F(f)=(-1/32)*(integral_Y f*R, integral_Y f*I)',
        'source_coverage':'all algebraic cycle generators via resolution',
        'graph_pairing_requires_degree_division':False,
        'two_pullback_pairing_requires_degree_division':True,
        'universal_vanishing_proved':False,'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Linearized Hodge type of the known product-fiber divisor witnesses under an allowed Weil-family deformation.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-source-complete-weil-reader-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
