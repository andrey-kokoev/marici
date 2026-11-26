"""Enumerate simultaneously triangle-free recolorings; measure maximum size and blue-four coverage, separately and jointly. Never change the graphs used for the original extension verdict."""
import itertools,json,collections
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'results';rows=[r for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==11 and r['d']==4];out=[]
for idx,r in enumerate(rows):
 a=list(r['core']);edges=[(i,j) for i in range(11) for j in range(i) if not(a[i]>>j&1 or a[i]&a[j])];Q=[set(q) for q in itertools.combinations(range(11),4) if all(not a[i]>>j&1 for i,j in itertools.combinations(q,2))];hits=[sum(1<<j for j,q in enumerate(Q) if {u,v}<=q) for u,v in edges];best={};w={};hist=collections.Counter()
 def rec(i,used,mask):
  k=len(used);h=mask.bit_count();hist[k]+=1
  if h>best.get(k,-1):best[k]=h;w[k]=list(used)
  for j in range(i,len(edges)):
   u,v=edges[j]
   if a[u]&a[v]:continue
   a[u]^=1<<v;a[v]^=1<<u;rec(j+1,used+[j],mask|hits[j]);a[u]^=1<<v;a[v]^=1<<u
 rec(0,[],0);k=max(best);out.append(dict(row=idx,actual=r['full'],addable=len(edges),max_joint=k,blue4=len(Q),max_hit=max(best.values()),best_by_size=best,legal_counts=hist,edges=edges,witness_by_size=w))
(P/'ramsey_recolor_joint.json').write_text(json.dumps(out)+'\n');z=[r for r in out if r['addable']>=4];print('joint>=4',collections.Counter((r['max_joint']>=4,r['actual']) for r in z));
for f in z:
 if f['actual']:continue
 print('false',[(k,f[k]) for k in ('row','addable','max_joint','blue4','max_hit','best_by_size','legal_counts')]);match=[r for r in z if r['actual'] and r['addable']==f['addable']];print('matched',[(r['row'],r['max_joint'],r['max_hit'],r['blue4']) for r in match]);print('exact_profile_matches',[r['row'] for r in match if all(r[k]==f[k] for k in ('blue4','best_by_size','legal_counts'))])
