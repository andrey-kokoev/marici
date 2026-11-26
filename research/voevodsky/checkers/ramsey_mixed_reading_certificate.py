"""Smallest mixed set of exact pair counts forcing each residual chord, under the frozen marked context. CEGIS: every counterassignment adds a necessary hitting clause. An optimal hitting set that is also UNSAT in the attachment solver proves minimum size."""
import itertools,json,time
from pysat.solvers import Solver
from pysat.card import CardEnc
from pysat.formula import IDPool,WCNF
from pysat.examples.rc2 import RC2
from ramsey_retention_slice import D
P=D.parent;prev=json.loads((P/'ramsey_exact_overlap_transfer.json').read_text());marks={r['core_index']:r for r in json.loads((P/'ramsey_attachment_rule_transfer.json').read_text()) if r['status']=='tested'};cores=json.loads((P/'ramsey_37_catalogue_free.json').read_text())['certificates'];out=[]
for r in prev:
 for e in map(tuple,r['exact_neighbor']):
  idx=r['core'];a=cores[idx]['core'];z=marks[idx];old=list(map(set,z['red_supports']));C=range(16);J=range(6);p=IDPool();V={(i,j):p.id((i,j)) for i in C for j in J};cs=[]
  for i in C:cs+=CardEnc.equals([V[i,j] for j in J],len(old[i]),vpool=p).clauses
  for j in J:cs+=CardEnc.equals([V[i,j] for i in C],5,vpool=p).clauses;cs.extend([[-V[i,j],-V[h,j]] for i,h in itertools.combinations(C,2) if a[i]>>h&1])
  for f in itertools.product(*z['mark']):cs.append([V[f] if f==e else -V[f]])
  gates=[];spec=[];inputs=[]
  for side,ids,other in [('C',C,J),('J',J,C)]:
   for i,h in itertools.combinations(ids,2):
    if side=='C' and a[i]>>h&1:continue
    gate=p.id();pairs=[((i,j),(h,j)) if side=='C' else ((j,i),(j,h)) for j in other];ys=[];k=sum(v in old[u] and y in old[x] for (u,v),(x,y) in pairs)
    for f,b in pairs:
     y=p.id();u,v=V[f],V[b];cs.extend([[-y,u],[-y,v],[y,-u,-v]]);ys.append(y)
    cs.extend([[-gate,*cl] for cl in CardEnc.equals(ys,k,vpool=p).clauses]);gates.append(gate);spec.append([side,i,h,k]);inputs.append(ys)
  hard=[];cuts=[];start=time.monotonic()
  with Solver(name='g4',bootstrap_with=cs) as s:
   assert not s.solve(assumptions=gates);ub=s.get_core()
   for t in ub[:]:
    if not s.solve(assumptions=[u for u in ub if u!=t]):ub.remove(t)
   best=[gates.index(v) for v in ub];lb=2
   while time.monotonic()-start<25 and lb<len(best):
    form=WCNF();form.extend(hard);[form.append([-i-1],weight=1) for i in range(len(gates))];
    with RC2(form) as solver:m=solver.compute()
    ids=[v-1 for v in m if 1<=v<=len(gates)];lb=max(lb,len(ids));
    if lb>=len(best):break
    if not s.solve(assumptions=[gates[i] for i in ids]):best=ids;break
    pos=set(s.get_model());hard.append([i+1 for i,vs in enumerate(inputs) if sum(v in pos for v in vs)!=spec[i][-1]]);cuts.append([[i,j] for (i,j),v in V.items() if v in pos])
   assert not s.solve(assumptions=[gates[i] for i in best]);assert all(s.solve(assumptions=[gates[h] for h in best if h!=i]) for i in best)
  res=dict(core=idx,edge=e,lower=lb,upper=len(best),readings=[spec[i] for i in best],counterassignments=cuts);out.append(res);print(idx,e,lb,len(best),res['readings'],len(cuts),flush=True)
(P/'ramsey_mixed_reading_certificate.json').write_text(json.dumps(out)+'\n')
