"""Try to destroy ALL one-row one-edge patches after one core deletion. Keep square footprints' membership and exterior induced graph unchanged on surviving vertices. Add triangle-free edges v--w, v a common blocker, w an existing noncorner red neighbor of a corner. Exhaust branch choices for each required length-two path; no arbitrary search cutoff."""
import json,gzip,collections,itertools,functools
from ramsey_retention_slice import CAT,D,decode,check
P=D.parent;R=json.loads((P/'ramsey_patch_corner27.json').read_text());ids={r['row'] for r in R};A={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};F=(1<<27)-1;out=[];count=collections.Counter();first=None
for r in R:
 a=A[r['row']];c=r['c'];C=sum(1<<i for i in c)
 for dl in range(27):
  if dl in c:continue
  mask=F^(1<<dl);Q=[q for q in r['quintuples'] if not q>>dl&1];
  if not Q:continue
  T=functools.reduce(int.__and__,Q);b=[v&mask for v in a];b[dl]=0
  def dfs(edges):
   unmet=[]
   for v in range(27):
    if not T>>v&1:continue
    for i in c:
     if b[i]&b[v]:continue
     cand=[(v,w) for w in range(27) if b[i]>>w&1 and not C>>w&1 and not b[w]&b[v]];unmet.append(cand)
   if not unmet:return edges
   for v,w in min(unmet,key=len):
    b[v]^=1<<w;b[w]^=1<<v;z=dfs(edges+[(v,w)])
    if z is not None:return z
    b[v]^=1<<w;b[w]^=1<<v
   return None
  z=dfs([]);count[z is not None]+=1
  if z is not None:
   assert check(b,mask,3,8);out.append(dict(row=r['row'],c=c,dl=dl,add=z,q=Q));
   if first is None:first=out[-1]
print(count,'success types',len(set(z['row'] for z in out)),first);(P/'ramsey_block_patch26.json').write_text(json.dumps(dict(tested=sum(count.values()),solutions=out))+'\n')
