"""Second split on an indistinguishable block of singly anchored cells. They share a retained label, hence are blue and every subset needs |subset|-1 distinct new labels. Sort masks within the block; quotient by missing-label permutations preserving the first block as a multiset. Other constraints from the same noncube SAT gate. Reuses solver per shard; no extrapolation from unknowns."""
import json,sys,collections,itertools,functools,concurrent.futures as cf,time
from ramsey_cube_three_gate import P,REPS,subdata,encode,perms,V
from pysat.solvers import Solver

def second(f,o):
 _,h,gs=subdata(f);g=max((g for g in gs if h[g[0]].bit_count()==1),key=len);ps=[p for p in perms if tuple(sorted(p[x] for x in o))==o];allc=[];passes=[]
 for x in itertools.combinations_with_replacement(range(8),len(g)):
  if x!=min(tuple(sorted(p[v] for v in x)) for p in ps):continue
  allc.append(x)
  if any(functools.reduce(int.__or__,t,0).bit_count()+1<len(t) for k in range(2,len(g)+1) for t in itertools.combinations(x,k)):continue
  passes.append(x)
 return g,len(allc),passes

def run(t):
 f,o,g,xs,k,stage=t;cs,E,gs,nb=encode(f,stage);rs=[]
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  for x in xs:
   ass=[V(i,j)*(1 if v>>j&1 else -1) for b,n in ((gs[0],o),(g,x)) for i,v in zip(b,n) for j in range(3)];sl.conf_budget(k);tick=time.perf_counter();ok=sl.solve_limited(assumptions=ass);rs.append(dict(x=x,ok=ok,seconds=round(time.perf_counter()-tick,2)))
 return dict(f=f,o=o,g=g,rows=rs)
if __name__=='__main__':
 f=tuple(map(int,sys.argv[1]));o=tuple(map(int,sys.argv[2]));k=int(sys.argv[3]);stage=int(sys.argv[4]);g,n,opts=second(f,o);print(g,'canonical',n,'Hall survivors',len(opts),flush=True);path=P/f'ramsey_three_refine_{sys.argv[1]}_{sys.argv[2]}_{k}_{stage}.json';out=json.loads(path.read_text()) if path.exists() else [];done={tuple(c['x']) for z in out for c in z['rows']};
 if len(sys.argv)>5:
  prior=json.loads((P/sys.argv[5]).read_text());done.update(tuple(c['x']) for z in prior for c in z['rows'] if c['ok'] is False)
 xs=[x for x in opts if x not in done];shards=min(len(xs),12)
 if shards:
  with cf.ProcessPoolExecutor(6) as ex:
   for z in cf.as_completed([ex.submit(run,(f,o,g,xs[i::shards],k,stage)) for i in range(shards)]):out.append(z.result());path.write_text(json.dumps(out)+'\n')
 print(collections.Counter(c['ok'] for z in out for c in z['rows']))
