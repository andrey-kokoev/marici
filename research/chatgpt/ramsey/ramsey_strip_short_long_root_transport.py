"""Does shortest-to-longest output isomorphism require changing root? If rooted, recover its six-ground-label permutation and compare transported row swaps."""
from ramsey_strip_short_long_control import long,B,iso,G,turn
from ramsey_strip_unbiased_three_constraints import selected,allms
from ramsey_strip_matching_restart import P,T
short=allms[next(iter(selected))[0]];assert G[0]==__import__('ramsey_strip_short_output_isomorphism').graph(short)
f=iso(G[0],B,{0:0});print('rooted shortest-longest isomorphism exists',f is not None)
if f is not None:
 p=tuple(f[1+i]-1 for i in range(6));assert set(p)==set(range(6));tr=lambda d:tuple(sorted(p[x] for x in d));H=[P.index(tr(d)) for d in P]+[15+T.index(tuple(sorted(map(tr,t)))) for t in T]
 transported=frozenset(tuple(sorted((H[i],H[j]))) for i,j in short);assert transported==long
 from ramsey_strip_matching_restart import r
 inv=[H.index(i) for i in range(30)];rprime=[H[r[inv[i]]] for i in range(30)];moved=lambda m,a:frozenset(tuple(sorted((a[i],a[j]))) for i,j in m)
 assert len(long^moved(long,rprime))==10
 print('six-label permutation',p,'transports row swap unchanged',rprime==r,'cycle length with transported swap',len(long^moved(long,rprime)),'with original swap',len(long^turn(long)))
 print('first matching transported correctly',True,'second matching remains original longest partner',moved(long,rprime)==turn(long))
else:
 f=iso(G[0],B,{});print('unrooted image of distinguished vertex',f[0])
