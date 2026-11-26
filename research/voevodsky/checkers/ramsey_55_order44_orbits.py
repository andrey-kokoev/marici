"""Bounded symmetry search for a 44-vertex (5,5) witness. All invariant colorings under simultaneous cyclic shifts on equal-sized blocks. Lazy exact clique constraints; a conflict-budget exit is UNKNOWN, not an exclusion. Replay learned clauses in a second solver for UNSAT."""
import itertools,json,time,sys
from pathlib import Path
from pysat.solvers import Solver
P=Path(__file__).resolve().parents[1]/'results';n=44;m=int(sys.argv[1]);limit=float(sys.argv[2]);assert n%m==0;E=list(itertools.combinations(range(n),2));shift=lambda i,k:i//m*m+(i%m+k)%m
orbits={};idx={}
for i,j in E:
 key=min(tuple(sorted((shift(i,k),shift(j,k)))) for k in range(m));idx[i,j]=orbits.setdefault(key,len(orbits)+1)
def cliques(a,p,k,sel):
 if not k:yield sel;return
 while p.bit_count()>=k:
  b=p&-p;p^=b;i=b.bit_length()-1;yield from cliques(a,p&a[i],k-1,sel+(i,))
clauses={(1,)};start=time.monotonic();status='unknown';steps=0;F=(1<<n)-1
with Solver(name='g4',bootstrap_with=clauses) as sl:
 while time.monotonic()-start<limit:
  sl.conf_budget(5000);v=sl.solve_limited()
  if v is None:continue
  if not v:status='unsat';break
  pos=set(sl.get_model());a=[0]*n
  for (i,j),u in idx.items():
   if u in pos:a[i]|=1<<j;a[j]|=1<<i
  new=set();steps+=1
  for g,sign in [(a,-1),([F^(v|1<<i) for i,v in enumerate(a)],1)]:
   for i in range(0,n,m): # any monochromatic five can be shifted so its least block contains that block's zero vertex
    for q in itertools.islice(cliques(g,g[i]&~((1<<i)-1),4,(i,)),256):new.add(tuple(sorted({sign*idx[min(x,y),max(x,y)] for x,y in itertools.combinations(q,2)})))
  if not new:
   assert not any(all(bool(a[i]>>j&1)==col for i,j in itertools.combinations(q,2)) for q in itertools.combinations(range(n),5) for col in (False,True));status='sat';break
  assert not clauses&new
  for c in sorted(new):sl.add_clause(c)
  clauses.update(new)
replay=None
if status=='unsat':
 with Solver(name='m22',bootstrap_with=sorted(clauses)) as verify:replay=not verify.solve();assert replay
out=dict(blocks=n//m,period=m,orbit_variables=len(orbits),status=status,replay_unsat=replay,clauses=len(clauses),models_cut=steps,seconds=time.monotonic()-start)
if status=='sat':out['adjacency']=a
print(out,flush=True);(P/f'ramsey_55_order44_cyclic_{m}.json').write_text(json.dumps(out)+'\n')
