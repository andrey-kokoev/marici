"""Five neighbors at one root. Hold any subset of the four oriented lift supports fixed, search jointly for ALL remaining supports; do not impose maximality or symmetry on free rows. On positive cases replay full graph. Baseline free feasibility and frozen-4 verdict are controls."""
import itertools,json,collections,sys
from pysat.solvers import Solver
from ramsey_retention_slice import D,decode,check
P=D.parent

def solve(a,k,d,runs):
 n=len(a);I=[0];V=lambda h,i:1+h*n+i
 for i,v in enumerate(a):I.extend([s|1<<i for s in I if not s&v])
 cs=[[-V(h,i),-V(h,j)] for h in range(d) for i in range(n) for j in range(i) if a[i]>>j&1]
 for q in I:
  for js in itertools.combinations(range(d),k+1-q.bit_count()):cs.append([V(h,i) for h in js for i in range(n) if q>>i&1])
 res={};
 with Solver(name='g4',bootstrap_with=cs) as sl:
  def query(t):
   key=tuple(sorted(t));
   if key in res:return res[key]
   if not sl.solve(assumptions=[V(h,i)*(1 if s>>i&1 else -1) for h,s in enumerate(key) for i in range(n)]):res[key]=None;return None
   pos=set(sl.get_model());w=[sum(1<<i for i in range(n) if V(h,i) in pos) for h in range(d)];g=list(a)+[0]*(d+1);root=n+d
   for h,t in enumerate(w,n):
    g[h]=t|1<<root;g[root]|=1<<h
    for i in range(n):g[i]|=((t>>i)&1)<<h
   assert check(g,(1<<len(g))-1,3,k+1);res[key]=w;return w
  stats=collections.defaultdict(lambda:[0,0]);base=query([]);cert=[]
  for z in runs:
   c=z['corners'];s=[a[c[(i+2)%4]]|1<<c[(i+1)%4] for i in range(4)]
   for b in range(1,5):
    for ix in itertools.combinations(range(4),b):
     w=query([s[j] for j in ix]) if base else None;stats[b][0]+=1;stats[b][1]+=w is not None
     if w:cert.append(dict(c=c,ix=ix,rows=w))
 return dict(free=base,stats=stats,witnesses=cert)
out=[]
for r in json.loads((P/'ramsey_extra_square_row.json').read_text()):
 z=solve(decode(r['graph']),r['k'],5,r['runs']);out.append(dict(k=r['k'],graph=r['graph'],**z));print(r['k'],bool(z['free']),dict(z['stats']),flush=True)
(P/'ramsey_square_release_rows.json').write_text(json.dumps(out)+'\n')
