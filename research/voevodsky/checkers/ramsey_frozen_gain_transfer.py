"""Retrospective transfer: rank only the two largest predecessor orders, independently within each by count of individually red-addable edges. Choose one per order, breaking ties by minimum canonical edge mask (igraph). Grow without endpoint data or target-size stopping; test every increasing degree until first infeasible or d=k. Directly verify each constructed endpoint."""
import json,gzip,itertools,sys,igraph as ig
from pysat.solvers import Solver
from ramsey_retention_slice import CAT,D,decode,check
P=D.parent

def score(a):return sum(not(a[i]>>j&1 or a[i]&a[j]) for i in range(len(a)) for j in range(i))
def key(a):
 g=ig.Graph(len(a),[(i,j) for i in range(len(a)) for j in range(i) if a[i]>>j&1]);return sum(1<<(max(i,j)*(max(i,j)-1)//2+min(i,j)) for i,j in g.permute_vertices(g.canonical_permutation()).get_edgelist())
def grow(a,k):
 n=len(a);assert check(a,(1<<n)-1,3,k);I=[0];best=None;log=[]
 for i,v in enumerate(a):I.extend([q|1<<i for q in I if not q&v])
 V=lambda j,i:1+j*n+i
 for d in range(1,k+1):
  cs=[[-V(j,i),-V(j,h)] for j in range(d) for i in range(n) for h in range(i) if a[i]>>h&1];
  for q in I:
   for slots in itertools.combinations(range(d),k+1-q.bit_count()):cs.append([V(j,i) for j in slots for i in range(n) if q>>i&1])
  with Solver(name='g4',bootstrap_with=cs) as sl:
   ok=sl.solve();log.append(ok)
   if not ok:break
   pos=set(sl.get_model());w=[sum(1<<i for i in range(n) if V(j,i) in pos) for j in range(d)];root=n+d;g=list(a)+[0]*(d+1)
   for j,t in enumerate(w,n):
    g[j]=t|1<<root;g[root]|=1<<j
    for i in range(n):g[i]|=(t>>i&1)<<j
   assert check(g,(1<<len(g))-1,3,k+1);best=dict(order=len(g),supports=w,endpoint=g)
 return dict(core=a,score=score(a),tests=log,**best)

def load(k):
 if k==5:return [list(t) for t in sorted({tuple(r['core']) for r in json.loads((P/'ramsey_frontier_transfer.json').read_text()) if r['n']==12})],[decode(s) for s in (CAT/'r35_13.g6').read_text().splitlines()]
 return [decode(s.strip()) for s in gzip.open(CAT.parent/'r36_16.g6.gz','rt')],[decode(s) for s in (CAT/'r36_17.g6').read_text().splitlines()]
if '--square' in sys.argv:
 import hashlib
 source=CAT.parent/'r37_21.g6.gz';out=[]
 for path in (source,CAT/'r37_22.g6'):
  layer_size=0;top=[];mx=-1
  with (gzip.open(path,'rt') if path.suffix=='.gz' else path.open()) as f:
   for line in f:
    a=decode(line.strip());layer_size+=1;s=score(a)
    if s>mx:mx=s;top=[]
    if s==mx:top.append(a)
  def squares(a):
   g=[sum(1<<j for j in range(len(a)) if i!=j and not(a[i]>>j&1 or a[i]&a[j])) for i in range(len(a))];return sum((t:=(x&y).bit_count())*(t-1)//2 for x,y in itertools.combinations(g,2))//2
  ranked=sorted(top,key=lambda a:(-squares(a),key(a)));old=min(top,key=key);r=grow(ranked[0],7);base=r if key(old)==key(ranked[0]) else grow(old,7);r.update(layer=layer_size,edges_tied=len(top),cycles=squares(ranked[0]),cycle_tied=sum(squares(a)==squares(ranked[0]) for a in top),old_order=base['order'],old_cycles=squares(old),same_choice=old==ranked[0],sha256=hashlib.sha256(path.read_bytes()).hexdigest());r['tie_control']=[(squares(a),r['order'] if a==ranked[0] else grow(a,7)['order']) for a in ranked];out.append(r);print({k:v for k,v in r.items() if k not in ('core','supports','endpoint')},flush=True)
 (P/'ramsey_square_gain_transfer.json').write_text(json.dumps(out)+'\n');sys.exit()
if '--control' in sys.argv:
 low,high=load(6);groups=[sorted((a for a in low if score(a)==max_score),key=key) for max_score in [max(map(score,low))]]+[sorted(high,key=key)];rs=[[grow(a,6) for a in group] for group in groups];print([[(r['score'],r['order']) for r in g] for g in rs]);(P/'ramsey_frozen_gain_control.json').write_text(json.dumps(rs)+'\n');sys.exit()
out={}
for k in (5,6):
 res=[]
 for layer in load(k):
  mx=max(map(score,layer));top=[a for a in layer if score(a)==mx];r=grow(min(top,key=key),k);r.update(layer=len(layer),tied=len(top));res.append(r);print(k,len(layer),len(top),mx,r['order'],r['tests'],flush=True)
 out[k]=res
(P/'ramsey_frozen_gain_transfer.json').write_text(json.dumps(out)+'\n')
