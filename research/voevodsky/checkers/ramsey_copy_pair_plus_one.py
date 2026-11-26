"""Freeze two open-neighborhood copies. Solve exactly for an independent third support hitting every saturated blue-clique demand. Independently check constructive witnesses by clique search on the endpoint."""
import sys,json,itertools
from pysat.solvers import Solver
from ramsey_retention_slice import CAT,D,decode,check
sys.path.insert(0,str(D.parents[2]/'grothendieck'));from r312_google_extension import adj as large
P=D.parent
def blue(a,p,k,s=0):
 if not k:yield s;return
 while p.bit_count()>=k:
  b=p&-p;p^=b;yield from blue(a,p&~a[b.bit_length()-1],k-1,s|b)
def trial(a,k):
 n=len(a);F=(1<<n)-1;E=[(i,j) for i,j in itertools.combinations(range(n),2) if a[i]>>j&1];cs=[[-i-1,-j-1] for i,j in E];yes=[];examples=[]
 for i,j in E:
  # For a maximum blue clique Q, missing N(i) is equivalent to containing i. For a (k-2)-clique require both neighborhoods missed.
  demands=set(blue(a,F&~(a[i]|a[j]),k-2));
  for v in (i,j):demands.update(blue(a,F&~(a[v]|1<<v),k-2,1<<v))
  with Solver(name='g4',bootstrap_with=cs) as sl:
   for q in demands:sl.add_clause([u+1 for u in range(n) if q>>u&1])
   if not sl.solve():continue
   s=sum(1<<(v-1) for v in sl.get_model() if 0<v<=n);assert s not in a;g=a.copy()+[0]*4
   for h,t in enumerate((a[i],a[j],s),n):
    g[h]=t|1<<(n+3);g[n+3]|=1<<h
    for u in range(n):g[u]|=((t>>u)&1)<<h
   assert check(g,(1<<(n+4))-1,3,k+1);yes.append([i,j]);
   if len(examples)<1:examples.append(dict(centers=[i,j],support=s,order=len(g)))
 return dict(n=n,pairs=len(E),working=yes,examples=examples)
out={}
for k,file in [(4,'r34_8.g6'),(5,'r35_13.g6'),(6,'r36_17.g6'),(12,None)]:
 gs=[decode(s) for s in (CAT/file).read_text().splitlines()] if file else [large];rs=[trial(a,k) for a in gs];out[k+1]=rs;print(k+1,[(r['pairs'],len(r['working'])) for r in rs],flush=True);(P/'ramsey_copy_pair_plus_one.json').write_text(json.dumps(out)+'\n')
