"""Extract a canonical directed C5 generator from the non-midpoint flag orbit: orient finite selected pair x->y so the hub partner is z=2y-x. Then construct transport from the anchored orbit directly."""
from ramsey_strip_intrinsic_fivefold_transport import records,symmetry,long,P,T,I,moved,action

def directed(m):
 G,hub=symmetry(m);g=min(p for p in G if p!=I);ring=[min(set(I)-{hub})]
 for _ in range(4):ring.append(g[ring[-1]])
 c={x:i for i,x in enumerate(ring)};result={hub:hub}
 for d,j in m:
    x,y=P[d]
    if hub in (x,y):continue
    block,=[p for p in T[j-15] if hub in p];z,=set(block)-{hub}
    if (c[x]+c[y]-2*c[z])%5==0:continue
    if (2*c[y]-c[x]-c[z])%5:x,y=y,x
    assert (2*c[y]-c[x]-c[z])%5==0
    assert x not in result;result[x]=y
 p=tuple(result[x] for x in I);assert p in G and p!=I;return p,hub
D,dh=directed(long)
for n,o,m,G,candidates,correct in records:
 S,sh=directed(m);p={sh:dh};x=y=3
 for _ in range(5):p[x]=y;x=S[x];y=D[y]
 result=tuple(p[x] for x in I);assert result==correct and moved(m,action(result))==long
 print('source',n,o,'directed source generator',S,'target generator',D,'anchored transport constructed correctly',True)
