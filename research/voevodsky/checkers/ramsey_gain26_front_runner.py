"""Resolve all panels at top screen score for the fixed-order pilot's selected core. Maximalizing individual supports is harmless. Check endpoint explicitly."""
import itertools,json,collections,igraph as ig
from ramsey_retention_slice import D,check
P=D.parent;rows=json.loads((P/'ramsey_gain26_rewire.json').read_text())['records'];d=max(r['packing_at_least'] for r in rows);out=[]
for r in rows:
 if r['packing_at_least']!=d:continue
 a=r['adj'];I=[0]
 for j,v in enumerate(a):I.extend([t|1<<j for t in I if not t&v]);
 S=[t for t in I if all(t&(1<<j|v) for j,v in enumerate(a))];Q=[t for t in I if t.bit_count()==7];M=[sum(1<<j for j,q in enumerate(Q) if not s&q) for s in S];assert all(M);g=ig.Graph(len(S),[(j,k) for j,m in enumerate(M) for k in range(j) if not m&M[k]]);panels=g.cliques(min=d,max=d);stats=[len(panels)]
 for k in range(6,8-d,-1):
  qs=[t for t in I if t.bit_count()==k];panels=[p for p in panels if all(q.bit_count()+sum(not q&S[i] for i in p)<=8 for q in qs)];stats.append(len(panels))
 w=[S[i] for i in panels[0]] if panels else None
 if w:
  b=a[:]+[0]*(d+1)
  for j,s in enumerate(w,26):
   b[j]=s|1<<(26+d);b[-1]|=1<<j
   for i in range(26):b[i]|=(s>>i&1)<<j
  assert check(b,(1<<len(b))-1,3,9)
 print(r['seed'],stats,bool(w));out.append(dict(adj=a,packing=d,counts=stats,witness=w))
(P/'ramsey_gain26_front_runner.json').write_text(json.dumps(out)+'\n')
