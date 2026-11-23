"""Recover timing equalities from offers alone, independently of complete-cover labels. Verify per-address multiplicity and both-column cancellation on every timing mask."""
import json,itertools
from collections import Counter
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results';rows=json.loads((D/'pne_four_cover_realizations.json').read_text());out=[]
for r in rows:
 if r['late']:continue
 l=next(s for s in rows if s['late'] and (s['perm'],s['prep'])==(r['perm'],r['prep']));a,b=r['contacts'],l['contacts'];assert a[::2]==b[::2];entries=[p[0] for p in a[::2]];ex=[p[0] for p in a[1::2]];assert set(entries)=={p[1] for p in a[::2]} and len(set(entries+ex))==10
 edges=[]
 for i,k in enumerate(ex):
  j,=[h for h,p in enumerate(b[1::2]) if p[0]==k];assert a[2*i+1][1]!=k and a[2*j+1][1]==k;edges.append((i,j,k))
 u=0;cycle=[]
 while u not in cycle:cycle.append(u);u=edges[u][1]
 assert len(cycle)==5 and u==0
 hist=Counter();solutions=[]
 for t in itertools.product(range(2),repeat=5):
  cs=a[::2]+[(b if t[i] else a)[2*i+1] for i in range(5)];X,H=[Counter(p[h] for p in cs) for h in range(2)];
  for i,j,k in edges:assert (X[k],H[k])==(1-t[i]+t[j],1+t[i]-t[j])
  defects=sum(t[i]!=t[j] for i,j,k in edges);assert defects==sum(X[k]!=1 for k in entries+ex)==sum(H[k]!=1 for k in entries+ex);hist[defects]+=1
  if not defects:solutions.append(t)
 out.append(dict(perm=r['perm'],prep=r['prep'],edges=edges,cycle=cycle,hist=hist,solutions=solutions))
print(len(out),out[0]);(D/'pne_exit_timing_cycle.json').write_text(json.dumps(out,indent=2)+'\n')
