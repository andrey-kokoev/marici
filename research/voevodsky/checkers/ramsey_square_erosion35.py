"""Exact minimum induced deletions making a two-red-diagonal lift legal on the 35-seed. Keep corners; remove common footprint and separately hit all blue sixes of untouched exterior. Minimize sum across induced matching pairs."""
import json,itertools,collections,functools
from ramsey_retention_slice import D,decode,check
P=D.parent;a=decode(next(r['graph6'] for r in json.loads(D.read_text()) if (r['l'],r['k'])==(3,9)));n=len(a);F=(1<<n)-1;E=[(i,j,a[i]|a[j]) for i in range(n) for j in range(i) if a[i]>>j&1];
def clique(p,k,sel=0):
 if not k:return sel
 while p.bit_count()>=k:
  b=p&-p;p^=b;x=clique(p&~a[b.bit_length()-1],k-1,sel|b)
  if x:return x
 return 0
@functools.lru_cache(None)
def cut(p):
 q=clique(p,6)
 if not q:return 0
 opts=[]
 while q:
  b=q&-q;q^=b;opts.append(b|cut(p^b))
 return min(opts,key=int.bit_count)
hist=collections.Counter();best=n;example=None
for (i,j,b),(u,v,c) in itertools.combinations(E,2):
 if (b>>u|b>>v|c>>i|c>>j)&1:continue
 dels=(b&c)|cut(F&~(b|c));d=dels.bit_count();hist[d]+=1
 if d<best:
  best=d;C=(i,u,j,v);keep=[i for i in range(n) if not dels>>i&1];g=a.copy()+[0]*5
  for h in range(4):
   t=(a[C[(h+2)%4]]|1<<C[(h+1)%4])&~dels;g[n+h]=t|1<<(n+4);g[n+4]|=1<<(n+h)
   for z in keep:g[z]|=((t>>z)&1)<<(n+h)
  assert check(g,((1<<(n+5))-1)&~dels,3,10);example=dict(cycle=C,deleted=[z for z in range(n) if dels>>z&1],overlap=(b&c).bit_count())
print(best,hist,example);(P/'ramsey_square_erosion35.json').write_text(json.dumps(dict(minimum=best,histogram=hist,example=example))+'\n')
