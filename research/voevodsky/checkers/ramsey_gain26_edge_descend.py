"""Exact one/two-edge red augmentation shell of all 32 verified capacity-five cores. Every candidate is legal: no red triangle introduced and blue cliques can only disappear. Isomorphism dedup; unfrozen exact seven packing for six. Resolve all passing six-panels through all lower demands."""
import json,collections,itertools,subprocess,sys,igraph as ig
from ramsey_retention_slice import D,check
P=D.parent;R=json.loads((P/'ramsey_gain26_rewire.json').read_text())['records'];parents=[r['idx'] for r in json.loads((P/'ramsey_gain26_verify_five.json').read_text()) if r['min_nines']==0];pool={};raw=collections.Counter()
def key(a):
 g=ig.Graph(26,[(i,j) for i,v in enumerate(a) for j in range(i) if v>>j&1]);return tuple(sorted(tuple(sorted(e)) for e in g.permute_vertices(g.canonical_permutation()).get_edgelist()))
for idx in parents:
 a=R[idx]['adj'];free=[(i,j) for i,v in enumerate(a) for j in range(i) if not v>>j&1 and not v&a[j]]
 for k in [1,2]:
  for edges in itertools.combinations(free,k):
   b=a[:]
   for i,j in edges:
    if b[i]&b[j]:break
    b[i]|=1<<j;b[j]|=1<<i
   else:
    raw[k]+=1;q=key(b);z=pool.get(q)
    if z is None or k<len(z['edges']):pool[q]=dict(idx=idx,edges=edges,adj=b)
rows=list(pool.values());print('generated',raw,len(rows),flush=True);out=[];by=collections.Counter()
for j in range(0,len(rows),256):
 chunk=rows[j:j+256];scores=list(map(int,subprocess.check_output([sys.argv[1],'7','6'],input=''.join(' '.join(map(str,r['adj']))+'\n' for r in chunk),text=True).splitlines()))
 for r,score in zip(chunk,scores,strict=True):
  by[len(r['edges']),score]+=1
  if not score:continue
  a=r['adj'];I=[0]
  for i,v in enumerate(a):I.extend([t|1<<i for t in I if not t&v]);
  S=[t for t in I if all(t&(1<<i|v) for i,v in enumerate(a))];M={k:[sum(1<<i for i,q in enumerate([q for q in I if q.bit_count()==k]) if not q&s) for s in S] for k in range(3,8)};assert all(M[7]);g=ig.Graph(len(S),[(i,j) for i,m in enumerate(M[7]) for j in range(i) if not m&M[7][j]]);panels=g.cliques(min=6,max=6);counts=[len(panels)]
  for k in (6,5,4,3):
   from functools import reduce
   from operator import and_
   panels=[p for p in panels if all(not reduce(and_,(M[k][i] for i in sub)) for sub in itertools.combinations(p,9-k))];counts.append(len(panels))
  w=[S[i] for i in panels[0]] if panels else None
  if w:
   b=a[:]+[0]*7
   for i,s in enumerate(w,26):
    b[i]=s|1<<32;b[32]|=1<<i
    for l in range(26):b[l]|=(s>>l&1)<<i
   assert check(b,(1<<33)-1,3,9)
  out.append(dict(**r,counts=counts,rows=w))
print('screen',by,'final',sum(bool(r['rows']) for r in out),flush=True);(P/'ramsey_gain26_edge_descend.json').write_text(json.dumps(dict(raw=raw,screen={str(k):v for k,v in by.items()},passing=out))+'\n')
