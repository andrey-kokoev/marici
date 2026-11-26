"""Detect single-edge contradictions across five-label tests, keeping all <=4 constraints and degrees. SAT entailment by opposing a model; intersect forbidden decisions for each independently feasible region. Factor the region-vs-region graph into edge switch bicliques; distinguish individual failures, switch conflicts, and joint-only conflicts."""
from ramsey_unsaturated_conflict_trace import nodes,ts,P,CardEnc,Solver,pairs,itertools,json,Counter
from concurrent.futures import ProcessPoolExecutor

def work(arg):
 idx,m=arg;E={p:k+1 for k,p in enumerate(p for p in pairs(range(26),2) if not m[p[0]]&m[p[1]])};es=list(E);n=len(E);cs=[];rg={};
 for i,s in enumerate(m):
  b=CardEnc.equals([w for p,w in E.items() if i in p],8-s.bit_count(),top_id=n);n=max(n,b.nv);cs+=b.clauses
 for x in pairs(range(26),3):
  p=list(pairs(x,2));
  if all(z in E for z in p):cs.append([-E[z] for z in p])
 for t in range(256):
  k=t.bit_count();guard=[]
  if k>5:continue
  if k==5:n+=1;rg[t]=n;guard=[-n]
  for xs in pairs([i for i,s in enumerate(m) if not s&~t],k+1):cs.append(guard+[E[p] for p in pairs(xs,2) if p in E])
 with Solver(name='cadical195',bootstrap_with=cs) as sl:
  def fixed(ass,candidates):
   if not sl.solve(assumptions=ass):return None
   sol=set(sl.get_model());todo={v if v in sol else -v for v in candidates};yes=[]
   while todo:
    v=todo.pop()
    if not sl.solve(assumptions=ass+[-v]):yes.append(v)
    else:todo.intersection_update(sl.get_model())
   return yes
  base=fixed([],list(E.values()));cand=set(E.values())-{abs(v) for v in base};fs={t:fixed([tag],cand) for t,tag in rg.items()};fail=[t for t in fs if fs[t] is None];ok=[t for t in fs if t not in fail];switch=[];other=[]
  for a,b in pairs(ok,2):
   cl=set(fs[a])&{-v for v in fs[b]}
   if cl:switch.append([a,b,[[*es[abs(v)-1],v>0] for v in sorted(cl)]])
   elif not sl.solve(assumptions=[rg[a],rg[b]]):other.append([a,b])
 return dict(idx=idx,individually_failed=fail,switch=switch,other=other,baseline_fixed=len(base))
if __name__=='__main__':
 import sys
 tasks=[(i,z['m']) for i,z in enumerate(nodes) if max(sum(not s&t for s in z['m']) for t in ts)<=8];out=[]
 with ProcessPoolExecutor(6) as ex:
  for r in ex.map(work,tasks):out.append(r);print(r['idx'],len(r['individually_failed']),len(r['switch']),len(r['other']),flush=True);(P/'ramsey_unsaturated_switches.json').write_text(json.dumps(out)+'\n')
