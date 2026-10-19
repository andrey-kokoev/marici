"""Known algebraic control and norm/projector equivalence; not all-cycle proof."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
from check_hodge_fixed_sixfold_pairing import wedge, power, integrate


def add(*terms):
    out={}
    for scale,form in terms:
        for i,x in form.items():out[i]=out.get(i,0)+scale*x
    return {i:x for i,x in out.items() if x}


def triple(a,b,c):return wedge(wedge(a,b),c)


def main():
    rs=[];ss=[]
    for j in range(3):
        k=j+3
        rs.append({(2*j,2*k):1,(2*j+1,2*k+1):-1})
        ss.append({(2*j,2*k+1):1,(2*j+1,2*k):1})
    algebraic_R=add((-1,triple(*rs)),(1,triple(rs[0],ss[1],ss[2])),
                    (1,triple(ss[0],rs[1],ss[2])),(1,triple(ss[0],ss[1],rs[2])))
    R={tuple(2*j+b for j,b in enumerate(bits)):(-1)**(sum(bits)//2)
       for bits in product((0,1),repeat=6) if sum(bits)%2==0}
    assert algebraic_R==R and len(R)==32
    E={(2*j,2*j+1):d for j,d in enumerate((1,1,1,-1,-1,-3))}
    assert integrate(wedge(R,power(E,3)))==0
    assert -integrate(wedge(R,R))==32
    wrong=add((1,triple(*rs)),(1,triple(rs[0],ss[1],ss[2])),
              (1,triple(ss[0],rs[1],ss[2])),(1,triple(ss[0],ss[1],rs[2])))
    assert wrong!=R
    count=0
    for a,b,c in product((Q(-1),Q(0),Q(1,2),Q(1)),repeat=3):
        B=2160*a;q=2160*a*a+32*b*b+32*c*c
        delta=q-B*B/Q(2160)
        assert delta==32*(b*b+c*c) and delta>=0
        assert (delta==0)==(b==c==0)
        # T removes only the divisor component; rational algebraic subtraction is allowed.
        assert a-B/Q(2160)==0
        count+=1
    r={'passed':True,'classification':'quadratic_binding_merged_with_existing_projector_gate',
       'rational_controls':count,'product_fiber_R_divisor_expansion_checked':True,
       'product_fiber_R_dark_for_divisor_reader':True,'product_fiber_R_defect':32,
       'fixed_X_cycle_constructed':False,'all_cycle_annihilation_proved':False,
       'Hodge_proved':False,'Hodge_refuted':False,
       'residuals':['No independent algebraic necessity follows from the norm or effective degree.']}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-restricted-observer-necessity-v1.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r))


if __name__=='__main__':main()
