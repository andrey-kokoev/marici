"""Independent folded-prism walks. For each residual perfect matching compare the parity of visits on the non-endpoint side with its number of cross-cut links. Keep availability distinct from use; a failed strip has no matching flux."""
from collections import Counter
from ramsey_strip_prism_proof import V,E
N={v:{y if x==v else x for x,y in E if v in (x,y)} for v in V};col=lambda v:v[0].upper()
def matches(S):
 if not S:yield ();return
 x=min(S)
 for y in N[x]&S:
    for tail in matches(S-{x,y}):yield ((x,y),)+tail
H=Counter();G=Counter()
def walk(p,t):
 if p[-1]!=t:
    for y in N[p[-1]]-set(p):walk(p+(y,),t)
    return
 S=V-set(p);off=lambda v:col(v) not in (p[0],t);b=sum(map(off,p))%2;cross=lambda e:off(e[0])!=off(e[1]);links=[e for e in E if set(e)<=S];ms=list(matches(S));costs=tuple(sorted({sum(map(cross,m)) for m in ms}));assert all(c%2==b for c in costs);H[len(p),bool(ms),costs]+=1;G[len(p),bool(ms),sum(map(cross,links))]+=1
for s in ('A','C'):
 for t in ('B','D'):walk((s,),t)
assert sum(H.values())==96
print('crossings used by completions (routes):',sorted(H.items()));print('available crossing edges:',sorted(G.items()))
