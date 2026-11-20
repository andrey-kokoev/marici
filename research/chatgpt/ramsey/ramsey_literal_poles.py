"""Read distinguished tetrahedral data from literal rows. Conditional pole convention: fan at stationary B; pair the two incident cross-edges through each moving R site. Hold poles AND entry sheet fixed, and compare the first turns. No distance profile or target 7+3 used."""
from ramsey_strip_prism_proof import X,P,T,r,labels,rep,cases
s,t='BRNN','BNRN';B,= [i for i,(a,b) in enumerate(zip(s,t)) if a==b=='B'];Q,=[i for i,(a,b) in enumerate(zip(s,t)) if a==b=='N'];U,V=s.index('R'),t.index('R');assert len({B,Q,U,V})==4
e=lambda a,b:X.index(tuple(sorted((a,b))));pair=lambda a,b:tuple(sorted((a,b)));fan=pair(e(B,U),e(B,V));through=tuple(sorted([pair(e(B,k),e(k,Q)) for k in (U,V)]+[pair(e(B,Q),e(U,V))]));cross=tuple(sorted([pair(e(B,k),e(l,Q)) for k,l in [(U,V),(V,U)]]+[pair(e(B,Q),e(U,V))]));p=P.index(fan);q=15+T.index(through);alt=15+T.index(cross);assert (p,q,alt)==(0,26,29)
# Lift all normalized examples with exactly the same first moving partition, not its reflected copy.
adj=[set() for _ in range(30)]
for i,d in enumerate(P):
 for j,m in enumerate(T,15):
    if d in m:adj[i].add(j);adj[j].add(i)
for path,_,__,turns,ok in cases:
    lift=[p,16];assert 16 in adj[p]
    for name in path[1:]:
        x,=[y for y in adj[lift[-1]] if labels.get(rep(y))==name];lift.append(x)
    assert q in adj[lift[-1]]; print('fixed literal poles and entry',lift+[q],turns,ok)
