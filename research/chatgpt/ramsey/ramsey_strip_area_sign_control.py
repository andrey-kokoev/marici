"""Controls for chirality reinforcement. Also test allowing retrace: its candidate wedge is zero, but primary imbalance wins regardless of secondary alignment."""
from ramsey_strip_area_tiebreak import V,G,K,wedge,inner,add
for sign in (1,-1,0):
 for exclude in (True,False):
    q=(2,0);A=V[q][:];W=[0]*3;seq=[q];areas=[];stop='budget'
    for _ in range(23):
        E={p:inner(add(A,v),add(A,v),G) for p,v in V.items() if p[1]!=q[1] and (not exclude or p[0]!=q[0])};best=[p for p,e in E.items() if e==min(E.values())]
        if len(best)>1:
            scores={p:sign*inner(W,wedge(V[q],V[p]),K) for p in best};best=[p for p,e in scores.items() if e==max(scores.values())]
        if len(best)!=1:stop='tie';break
        q,=best;W=add(W,wedge(A,V[q]));A=add(A,V[q]);seq.append(q)
        if len(seq)%6==0:areas.append(W[:])
    print('area sign',sign,'exclude retrace',exclude,'steps',len(seq),'stop',stop,'areas at 6-step boundaries',areas)
    if not exclude:assert len(seq)==2
    elif sign==1:assert len(seq)==24
    elif sign==0:assert len(seq)==6
    else:assert len(seq)==12 and W==[0]*3 and A==[0]*3
