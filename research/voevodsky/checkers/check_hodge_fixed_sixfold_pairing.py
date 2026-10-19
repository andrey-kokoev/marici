"""Exact exterior pairing on the fixed marking; Hodge theory is imported."""
from collections import Counter
from itertools import product
from pathlib import Path
import json


def wedge(a,b):
    out=Counter()
    for i,x in a.items():
        for j,y in b.items():
            if set(i)&set(j):continue
            sign=(-1)**sum(s>t for s in i for t in j)
            out[tuple(sorted(i+j))]+=sign*x*y
    return {i:x for i,x in out.items() if x}


def power(a,n):
    out={():1}
    for _ in range(n):out=wedge(out,a)
    return out


def integrate(form):
    return -form.get(tuple(range(12)),0)


def main():
    ds=(1,1,1,-1,-1,-3)
    E={(2*j,2*j+1):d for j,d in enumerate(ds)}
    R,I={},{}
    for bits in product((0,1),repeat=6):
        indices=tuple(2*j+b for j,b in enumerate(bits));k=sum(bits)
        if k%2:R_or_I=I;coefficient=(-1)**((k-1)//2)
        else:R_or_I=R;coefficient=(-1)**(k//2)
        R_or_I[indices]=coefficient
    assert len(R)==len(I)==32
    assert wedge(E,R)==wedge(E,I)=={}
    E3=power(E,3);basis=(E3,R,I)
    gram=[[integrate(wedge(a,b)) for b in basis] for a in basis]
    assert gram==[[2160,0,0],[0,-32,0],[0,0,-32]]
    raw=power(E,6)[tuple(range(12))]
    assert raw==-2160 and integrate(power(E,6))==2160
    # Wrong marked orientation fails positivity of the polarization volume.
    assert raw<0
    star_signs=(1,-1,-1)
    positive=[[gram[i][j]*star_signs[j] for j in range(3)] for i in range(3)]
    assert positive==[[2160,0,0],[0,32,0],[0,0,32]]
    count=0
    for a,b,c in product(range(-2,3),repeat=3):
        q=2160*a*a+32*b*b+32*c*c
        assert (q==0)==((a,b,c)==(0,0,0))
        count+=1
    norm=lambda v:sum(positive[i][j]*v[i]*v[j] for i in range(3) for j in range(3))
    alpha,minus_alpha=(0,1,0),(0,-1,0)
    assert norm(alpha)==norm(minus_alpha)==32 and alpha!=minus_alpha
    assert gram[1][0]==gram[2][0]==0 and positive[1][1]>0
    # Ordinary intersection is nondegenerate but has both signs.
    assert gram[0][0]>0 and gram[1][1]<0
    assert gram[0][0]*gram[1][1]*gram[2][2]!=0
    r={'passed':True,'classification':'full_Hodge_norm_faithful_divisor_observer_has_Weil_kernel',
       'cup_matrix':gram,'positive_matrix':positive,'complex_orientation_relative_to_mark':-1,
       'rational_integer_grid_controls':count,'alpha_norm':32,
       'full_positive_pairing_radical_dimension':0,'divisor_reader_kernel_dimension':2,
       'full_pairing_dark_mode_binding':'rejected_at_scope',
       'Hodge_proved':False,'Hodge_refuted':False,
       'residuals':['Divisor probe completeness for all algebraic classes is not established.']}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-fixed-sixfold-quadratic-pairing-v1.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r))


if __name__=='__main__':main()
