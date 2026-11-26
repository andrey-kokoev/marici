"""Search beyond the proven six-anchor regime. Forbid any missing row that restores a cube row relative to the retained five (then the exact two-erasure theorem already forces a cube). Split by the multiset of masks on vertices untouched by all five anchors, up to permutation of the three free labels. Units for neighbor domination by each retained row follow from triangle-freeness and alpha<=8: N(v) is an independent eight and every non-neighbor must see it. Relax to small blue demands; bounded SAT statuses are never called exclusions."""
import sys,itertools,collections,json,math,time,concurrent.futures as cf
from pysat.card import CardEnc
from pysat.solvers import Solver
from ramsey_retention_slice import D,check
P=D.parent;REPS=[(0,1,2),(0,1,7),(0,3,5)];M=[sum(1<<i for i in range(8) if i&k==v) for k in range(1,8) for v in range(8) if not v&~k];
def subdata(f):
 fm=sum(1<<l for l in f);h=[s&~fm for s in M];groups=[[i for i,s in enumerate(h) if s==t] for t in sorted(set(h))];return fm,h,groups
perms=[[sum(1<<p[k] for k in range(3) if x>>k&1) for x in range(8)] for p in itertools.permutations(range(3))];V=lambda i,j:1+26*j+i

def options(f):
 fm,h,gs=subdata(f);g=gs[0];assert h[g[0]]==0
 for o in itertools.combinations_with_replacement(range(1,8),len(g)):
  if o!=min(tuple(sorted(p[x] for x in o)) for p in perms):continue
  yield o

def encode(f,stage):
 fm,h,gs=subdata(f);E={(i,j):79+k for k,(i,j) in enumerate(itertools.combinations(range(26),2)) if not h[i]&h[j]};top=max(E.values());cs=[];e=lambda i,j:E.get(tuple(sorted((i,j))))
 for i,j,k in itertools.combinations(range(26),3):
  if (i,j) in E and (i,k) in E and (j,k) in E:cs.append([-E[i,j],-E[i,k],-E[j,k]])
 for (i,j),w in E.items():
  for k in range(3):cs.append([-w,-V(i,k),-V(j,k)])
 for i,s in enumerate(h):
  for l in range(8):
   if (s|fm)>>l&1:continue
   cs.append([e(i,j) for j,t in enumerate(h) if t>>l&1 and e(i,j)])
 for g in gs:
  for i,j in zip(g,g[1:]):
   for a in range(8):
    for b in range(a):cs.append([V(v,k)*(-1 if x>>k&1 else 1) for v,x in [(i,a),(j,b)] for k in range(3)])
 for xs,k in [([w for pair,w in E.items() if i in pair]+[V(i,j) for j in range(3)],8-s.bit_count()) for i,s in enumerate(h)]+[([V(i,j) for i in range(26)],7) for j in range(3)]:
  z=CardEnc.equals(xs,k,top_id=top);top=max(top,z.nv);cs.extend(z.clauses)
 block=set()
 for label in f:
  for parts in itertools.product(*(itertools.combinations(g,sum(M[i]>>label&1 for i in g)) for g in gs)):
   block.add(tuple(sorted(itertools.chain.from_iterable(parts))))
 for row in block:
  for j in range(3):cs.append([-V(i,j) for i in row])
 # Factor long demand clauses using shared proposition for 'Q has a core edge', only when multiple missing-label subsets give the same Q.
 for t in range(256):
  k=t.bit_count()
  if k>stage:continue
  vs=[i for i,s in enumerate(h) if not s&~t];js=[j for j,l in enumerate(f) if not t>>l&1]
  for q in itertools.combinations(vs,k+1):
   if (t&~fm)!=__import__('functools').reduce(int.__or__,(h[i] for i in q),0):continue
   cs.append([E[p] for p in itertools.combinations(q,2) if p in E]+[V(i,j) for i in q for j in js]);
 return cs,E,gs,len(block)

def run(item):
 f,stage,budget,chunk=item;cs,E,gs,nb=encode(f,stage);fm,h,_=subdata(f);rs=[]
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  for o in chunk:
   ass=[V(i,j)*(1 if x>>j&1 else -1) for i,x in zip(gs[0],o) for j in range(3)];sl.conf_budget(budget);start=time.perf_counter();ok=sl.solve_limited(assumptions=ass);rec=dict(masks=o,ok=ok,elapsed=round(time.perf_counter()-start,3));
   if ok:
    model=set(sl.get_model());mask=[s|sum((V(i,j) in model)<<l for j,l in enumerate(f)) for i,s in enumerate(h)];red=[p for p,v in E.items() if v in model];a=[sum(1<<j for j in range(26) if tuple(sorted((i,j))) in red) for i in range(26)];I=[(0,0)]
    for i,v in enumerate(a):I.extend([(q|1<<i,u|mask[i]) for q,u in I if not q&v]);
    bad=[(q,u) for q,u in I if q.bit_count()>min(7,u.bit_count())];assert not any(u.bit_count()<=stage for q,u in bad);rec.update(example=dict(m=mask,red=red,bad=len(bad)))
   rs.append(rec)
 return dict(f=f,blocked_rows=nb,cases=rs)
if __name__=='__main__':
 stage,budget=map(int,sys.argv[1:3]);tasks=[];path=P/f'ramsey_three_gate_{stage}_{budget}.json';out=json.loads(path.read_text()) if path.exists() else [];seen={(tuple(t['f']),tuple(c['masks'])) for t in out for c in t['cases']}
 prior=None
 if len(sys.argv)>3:
  prior={(tuple(t['f']),tuple(c['masks'])) for t in json.loads((P/sys.argv[3]).read_text()) for c in t['cases'] if c['ok'] is not False}
 for f in REPS:
  if len(sys.argv)>4 and ''.join(map(str,f))!=sys.argv[4]:continue
  opts=[o for o in options(f) if (f,o) not in seen and (prior is None or (f,o) in prior)];print(f,len(opts),flush=True)
  stride=1 if len(sys.argv)>4 else 12
  for i in range(0,len(opts),stride):tasks.append((f,stage,budget,opts[i:i+stride]))
 with cf.ProcessPoolExecutor(6) as ex:
  for fut in cf.as_completed([ex.submit(run,t) for t in tasks]):out.append(fut.result());path.write_text(json.dumps(out)+'\n')
 print({str(f):dict(collections.Counter(c['ok'] for t in out if tuple(t['f'])==f for c in t['cases'])) for f in REPS})
