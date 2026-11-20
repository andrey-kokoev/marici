"""Construct reciprocal moves directly from the two poles of an oriented ten-cycle and its unique spoke layers. No automorphism list is used until comparison."""
from ramsey_strip_layer_quarter_turn import C,M,D,N,r
maps=[]
for name,sign in [('keep cyclic direction',1),('reverse cyclic direction',-1)]:
    g={L[i]:L[(5+sign*i)%10] for L in (C,M,D) for i in range(10)};maps.append(g)
    assert all({g[y] for y in N[x]}==N[g[x]] and g[g[x]]==x for x in range(30))
    assert g[0]==29 and g[29]==0 and all((x<15)!=(g[x]<15) for x in range(30))
    print(name,'port action',[g[x] for x in (16,17,4,7)])
T,S=maps;assert all(S[T[x]]==T[S[x]]==r[x] for x in range(30))
from ramsey_strip_phase_moving_frame import S as knownS,T as knownT
assert all(S[x]==knownS[x] and T[x]==knownT[x] for x in knownS)
print('direct cycle constructions agree with both reciprocal frame moves on all sixteen states')
