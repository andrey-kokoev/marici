"""Separate regional SAT solutions by edge-color projections. Compute all forced literals of each region, test the other region against them together, and shrink a rejected conjunction. Then look for disjoint projections on 2 or 3 edges by model screening followed by exact queries. A demonstrated separator need not be globally minimum."""
from ramsey_unsaturated_conflict_trace import nodes,P,json,setup,Solver,pairs
from concurrent.futures import ProcessPoolExecutor
import itertools,random,collections
prior=json.loads((P/'ramsey_unsaturated_switches.json').read_text())
def run(r):
 idx,a,b=r;m=nodes[idx]['m'];es=list(p for p in pairs(range(26),2) if not m[p[0]]&m[p[1]]);N=len(es);cs,gs=setup(m,[a,b]);ass=lambda t:[x for x,k in gs.items() if k[0]!='cover' or k[1].bit_count()<5 or k[1]==t];sols=[Solver(name='cadical195',bootstrap_with=cs+[ [x] for x in ass(t)]) for t in (a,b)];rnd=random.Random(371);samples=[[],[]];forced=[]
 for si,sl in enumerate(sols):
  def sample():
   v={x for x in sl.get_model() if 0<x<=N};samples[si].append(v);return v
  assert sl.solve();v=sample();todo={j if j in v else -j for j in range(1,N+1)};fixed=[]
  while todo:
   x=todo.pop()
   if not sl.solve(assumptions=[-x]):fixed.append(x)
   else:
    v=sample();todo={y for y in todo if (abs(y) in v)==(y>0)}
  forced.append(fixed)
 candidates=[]
 for si,sl in enumerate(sols):
  opp=forced[1-si];
  if not sl.solve(assumptions=opp):
   for it in range(12):
    rnd.shuffle(opp);assert not sl.solve(assumptions=opp);c=sl.get_core()
    for x in c[:]:
     if x in c and not sl.solve(assumptions=[y for y in c if x!=y]):c=sl.get_core()
    candidates.append(tuple(sorted(map(abs,c))))
 # Screen all 2-edge projections using model-bitsets before exact replay. No exhaustive 3-edge search.
 cols=[[sum(1<<i for i,v in enumerate(ss) if j in v) for j in range(1,N+1)] for ss in samples];full=[(1<<len(s))-1 for s in samples];small=None
 for j,k in pairs(range(N),2):
  if any(all((cols[s][j]^(0 if u else full[s]))&(cols[s][k]^(0 if v else full[s])) for s in (0,1)) for u,v in itertools.product(range(2),repeat=2)):continue
  if not any(all(sl.solve(assumptions=[(j+1)*u,(k+1)*v]) for sl in sols) for u,v in itertools.product((-1,1),repeat=2)):
   small=(j+1,k+1);break
 if small:candidates.append(small)
 if not candidates:
  # Two independent SAT copies, allow their regional completions to disagree outside a trial set of edges.
  shift=max(max(map(abs,c)) for c in cs);lift=lambda x:x+shift if x>0 else x-shift;eq=lambda j:2*shift+j
  with Solver(name='cadical195',bootstrap_with=cs+[[lift(x) for x in c] for c in cs]+[[x] for x in ass(a)]+[[lift(x)] for x in ass(b)]) as shared:
   ids=list(range(1,N+1))
   for j in ids:shared.add_clause([-eq(j),j,-lift(j)]);shared.add_clause([-eq(j),-j,lift(j)])
   for it in range(6):
    rnd.shuffle(ids);assert not shared.solve(assumptions=list(map(eq,ids)));c=shared.get_core()
    for x in c[:]:
     if x in c and not shared.solve(assumptions=[y for y in c if x!=y]):c=shared.get_core()
    candidates.append(tuple(sorted(x-2*shift for x in c)))
 c=min(candidates,key=len);proj=[]
 if len(c)<=10:
  for sl in sols:proj.append([p for p in range(1<<len(c)) if sl.solve(assumptions=[v if p>>j&1 else -v for j,v in enumerate(c)])]);
  assert not set(proj[0])&set(proj[1]);
 for sl in sols:sl.delete()
 return dict(node=idx,regions=[a,b],edges=[es[j-1] for j in c],projections=proj,has_pair=bool(small))
if __name__=='__main__':
 tasks=[(r['idx'],a,b) for r in prior for a,b in r['other']];out=[]
 with ProcessPoolExecutor(6) as ex:
  for z in ex.map(run,tasks):out.append(z);print(z['node'],z['regions'],len(z['edges']),flush=True);(P/'ramsey_unsaturated_projection.json').write_text(json.dumps(out)+'\n')
