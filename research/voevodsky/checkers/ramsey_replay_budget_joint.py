"""Pure-integer replay without LP libraries. Verify weighted costs on all possible size-six/seven rows and all possible red additions, and compare capacity with demand eight."""
import json,collections
from ramsey_retention_slice import D
P=D.parent;R=json.loads((P/'ramsey_gain26_minimal.json').read_text());C=json.loads((P/'ramsey_gain26_budget_joint.json').read_text());count=0
for z in C:
 if not z['excluded']:continue
 a=R[z['idx']]['adj'];e=sum(v.bit_count() for v in a)//2;E=[1<<i|1<<j for i,v in enumerate(a) for j in range(i) if not v>>j&1 and not v&a[j]];I=[0]
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v]);
 S=[s for s in I if s.bit_count() in (6,7)];cx=[0]*len(S);cy=[0]*len(E);cap=0
 for key,w in z['weights']:
  assert type(w) is int and w>0
  if key=='budget':cap+=(80-e)*w;cy=[y+w for y in cy];continue
  kind,h=key
  if kind in ('vertex','minvertex'):
   sgn=1 if kind=='vertex' else -1;cap+=w*((8 if sgn==1 else 7)-a[h].bit_count())*sgn;cx=[x+w*sgn*((s>>h)&1) for x,s in zip(cx,S)];cy=[y+w*sgn*((v>>h)&1) for y,v in zip(cy,E)]
  elif kind=='edit':assert h in E;cap+=8*w;cx=[x+w*((s&h)==h) for x,s in zip(cx,S)];cy[E.index(h)]+=8*w
  else:
   assert kind=='miss' and h in I;k=h.bit_count();cap+=w*(8-k);cx=[x+w*(not s&h) for x,s in zip(cx,S)];cy=[y-k*w*((v&h)==v) for y,v in zip(cy,E)]
 assert min(cy,default=0)>=0 and min(cx)==z['den'] and cap==z['num'] and 8*min(cx)>cap;count+=1
print('verified',count)
