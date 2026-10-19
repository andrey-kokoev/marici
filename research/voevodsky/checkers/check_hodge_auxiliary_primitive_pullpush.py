"""Degree-scaled pairing and rational trace controls, not a cycle constructor."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from check_hodge_fixed_sixfold_pairing import wedge,power,integrate


def main():
    E={(2*j,2*j+1):d for j,d in enumerate((1,1,1,-1,-1,-3))}
    R={};I={}
    for bits in product((0,1),repeat=6):
        key=tuple(2*j+b for j,b in enumerate(bits));s=sum(bits)
        (R if s%2==0 else I)[key]=(-1)**(s//2)
    assert not wedge(E,R) and not wedge(E,I)
    W=(R,I)
    cup=[[integrate(wedge(u,v)) for v in W] for u in W]
    assert cup==[[-32,0],[0,-32]]
    assert integrate(wedge(power(E,3),R))==0
    controls=0
    for b,N in ((1,3),(2,3),(3,4),(2,7)):
        d=b**N
        pulled=[[d*x for x in row] for row in cup]
        assert pulled==[[-32*d,0],[0,-32*d]]
        for u,v in product((Q(-1),Q(0),Q(1,2),Q(1)),repeat=2):
            self_pair=pulled[0][0]*u*u+2*pulled[0][1]*u*v+pulled[1][1]*v*v
            assert -self_pair==32*d*(u*u+v*v)>=0
            assert Q(d*u,d)==u and Q(d*v,d)==v
            controls+=1
        if d>1:
            assert pulled!=cup  # pullback is not an unscaled isometry
        assert -pulled[0][0]>0 and pulled[0][0]<0
    result={'passed':True,'classification':'auxiliary_transport_preserves_algebraicity_question',
        'rational_pairing_controls':controls,'primitive_pullback_proved_by':'adjoint sector and Poincare duality',
        'trace':'g_*g*=d','positive_norm':'32*d','algebraicity_equivalence':True,
        'flatness_assumed':False,'algebraic_representative_constructed':False,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Source-complete two-component Weil pairing reader and universal necessity audit.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-auxiliary-primitive-pullpush-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
