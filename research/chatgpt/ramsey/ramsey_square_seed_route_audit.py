"""Catalogue-free audit of all 81 local square seeds. Count undirected Hamiltonian cycles of the prescribed red graph only. Derive forced blue edges, retaining their common-red-neighbor certificates. Separate post-check of the previously constructed completion."""
from itertools import product,combinations
from collections import Counter
from pathlib import Path
import json
H=Path(__file__).parent;V=range(4);arcs=[(i,j) for i in V for j in V if i!=j];edges=list(combinations(V,2));pos=lambda i,j:4+arcs.index((i,j));pair=lambda a,b:tuple(sorted((a,b)))
def audit(f):
    R=set();B=set()
    for i in V:
        p=pos(i,f[i]);other=[pos(i,j) for j in V if j not in (i,f[i])];B.update([pair(i,p),pair(*other)]);R.update(pair(a,b) for a in (i,p) for b in other)
    for m,(i,j) in enumerate(edges,16):
        u,v=pos(i,j),pos(j,i);R.update([pair(m,u),pair(m,v)]);B.add(pair(u,v))
    N=[set() for _ in range(22)]
    for u,v in R:N[u].add(v);N[v].add(u)
    cert={pair(i,j):sorted(N[i]&N[j]) for i,j in combinations(range(22),2) if N[i]&N[j]};assert set(cert)>=B and not R&set(cert)
    def paths(path,remaining):
        if not remaining: return int(0 in N[path[-1]] and path[1]<path[-1])
        return sum(paths(path+[v],remaining-{v}) for v in N[path[-1]]&remaining)
    return R,B,cert,paths([0],set(range(1,22)))
rows=[]
for f in product(*[[j for j in V if j!=i] for i in V]):
    R,B,c,h=audit(f);rows.append(dict(f=f,ham=h,extra=len(c)-len(B)))
R,B,c,h=audit((1,0,3,2));complete={tuple(e) for e in json.loads((H/'ramsey_square_seed_blind.json').read_text())['edges']};assert R<=complete and not complete&set(c)
print('hist',Counter((r['ham'],r['extra']) for r in rows),'fixed',len(R),len(B),len(c),h);(H/'ramsey_square_seed_route_audit.json').write_text(json.dumps(dict(rows=rows,mutual_pair_certificates=[[i,j,x] for (i,j),x in sorted(c.items())]),indent=2)+'\n')
