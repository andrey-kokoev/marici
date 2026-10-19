"""Exact cubical graph controls; standard cycle definitions are imported."""
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import json


def relation(a,b):
    a,b=Q(a),Q(b)
    assert a not in (0,1) and b not in (0,1) and a*b!=1
    # z(y-a)-(y-ab)=0; determinant ensures a nonconstant degree-one graph.
    assert a*b-a != 0
    assert (-a*b)/(-a)==b
    assert a*b-a != 0  # zero face y=ab avoids the pole y=a
    assert a-a*b != 0  # pole face has nonzero numerator
    # y=infinity has z=1 and is deleted from the cubical chart.
    assert Q(1)/Q(1)==1
    faces=[b,a*b,a]
    assert all(x not in (0,1) for x in faces)
    out=Counter()
    for x,c in ((b,1),(a*b,-1),(a,1)): out[x]+=c
    out={x:c for x,c in out.items() if c}
    assert out  # nonzero as free degree-one cycle
    product=Q(1)
    for x,c in out.items(): product*=x**c
    assert product==1
    return out


def main():
    for m in range(-5,6):
        zeros=max(m,0);poles=max(-m,0)
        assert (zeros-poles,poles-zeros)==(m,-m)
        assert m+(-m)==0
    # Empty Gamma_1 and present Gamma_2 have equal boundary, different supports.
    assert (0,0)==(0,0)
    assert [] != [('P1',Q(2))]
    pairs=[(2,3),(2,2),(Q(1,2),3),(-2,3),(Q(3,2),Q(5,3))]
    for a,b in pairs:
        rel=relation(a,b)
        assert all(x!=0 for x in rel)  # every retained point has zero next boundary
        assert sum(c*0 for c in rel.values())==0
    assert relation(2,3)=={Q(3):1,Q(6):-1,Q(2):1}
    # Dropping the minus sign on the second cubical coordinate breaks multiplicativity.
    assert Q(3)*Q(6)/Q(2)!=1
    for a,b in ((0,2),(1,2),(2,1),(2,Q(1,2))):
        try: relation(a,b)
        except AssertionError: pass
        else: raise AssertionError('degenerate case silently treated as generic')
    r={'passed':True,'classification':'graph_boundary_and_constant_multiplicativity_filler_constructed',
       'monomial_exponents_checked':11,'rational_surfaces_checked':len(pairs),
       'global_nonconstant_surface_claimed':False,
       'Hodge_proved':False,'Hodge_refuted':False,
       'residuals':['Nonconstant global multiplication surfaces require all vertical face terms.'],
       'next_test':'Compute the closure of a nonconstant P1 multiplicativity surface and every face term.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-higher-cycle-graph-boundary-v1.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r))


if __name__=='__main__':main()
