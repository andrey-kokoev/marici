"""Does the area-opposing 12-step history erase higher ordered memory? Compute its truncated tensor signature through degree three using exact fractions. This is a diagnostic, not another tie breaker."""
from fractions import Fraction as F
from itertools import product
from ramsey_strip_area_tiebreak import V,G,K,wedge,inner,add
q=(2,0);A=V[q][:];W=[0]*3;seq=[q]
while len(seq)<12:
    E={p:inner(add(A,v),add(A,v),G) for p,v in V.items() if p[1]!=q[1] and p[0]!=q[0]};best=[p for p,e in E.items() if e==min(E.values())]
    if len(best)>1:
        score={p:inner(W,wedge(V[q],V[p]),K) for p in best};best=[p for p,e in score.items() if e==min(score.values())]
    q,=best;W=add(W,wedge(A,V[q]));A=add(A,V[q]);seq.append(q)
S={():F(1)}
for q in seq:
    i,b=q;j=(2,3,5).index(i);sign=1-2*b;exp={():F(1),(j,):F(sign),(j,j):F(1,2),(j,j,j):F(sign,6)};new={}
    for w,a in S.items():
        for z,c in exp.items():
            if len(w+z)<=3:new[w+z]=new.get(w+z,F(0))+a*c
    S={w:a for w,a in new.items() if a}
assert A==W==[0,0,0] and all(len(w) in (0,3) for w in S);assert len(S)>1
print('12-step sequence',seq);print('nonzero signature coordinates by degree',[sum(len(w)==d for w in S) for d in (1,2,3)]);print('degree three',{''.join(str((2,3,5)[i]) for i in w):str(a) for w,a in S.items() if len(w)==3})
