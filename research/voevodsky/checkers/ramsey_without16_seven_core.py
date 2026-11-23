"""Find deletion-minimal 7-groups on the chart without address 16. Hold triangle and smaller coverage clauses fixed. Test both mismatch directions together. Lazy separation uses no archived wiring as a premise."""
import json,z3
from pathlib import Path
from itertools import combinations
D=Path(__file__).resolve().parents[1];src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=src['address_masks'];E={tuple(e):i for i,e in enumerate(src['edge_order'])};v=[z3.Bool('x%d'%i) for i in range(len(E))];idx=[i for i,a in enumerate(S) if a!=66];assert len(idx)==18
s=z3.Solver();s.add(v[4]!=v[74]);bad=set();seven=[]
for k in range(3,8):
 for J in combinations(idx,k):
  slots=[E[e] for e in combinations(J,2) if e in E];u=0
  for j in J:u|=S[j]
  if k==3 and len(slots)==3:s.add(z3.Or(*[~v[i] for i in slots]))
  if k<7 and u.bit_count()>=k:continue
  jm=sum(1<<j for j in J);keep=not any(jm^(1<<j) in bad for j in J);bad.add(jm)
  if not keep:continue
  if k==7:seven.append((J,slots,sum(1<<i for i in slots)))
  else:s.add(z3.Or(*[v[i] for i in slots]))
seven.sort(key=lambda g:(len(g[1]),g[0]));active=[];guard={}
def model():return sum(1<<i for i,x in enumerate(v) if z3.is_true(s.model().eval(x,model_completion=True)))
while s.check(*[guard[i] for i in active])==z3.sat:
 w=model();i=next(i for i,g in enumerate(seven) if not w&g[2]);assert i not in guard;guard[i]=z3.Bool(f'g{i}');s.add(z3.Implies(guard[i],z3.Or(*[v[k] for k in seven[i][1]])));active.append(i)
assert s.check(*[guard[i] for i in active])==z3.unsat;core=set(s.unsat_core());active=[i for i in active if guard[i] in core];
for i in active[:]:
 if s.check(*[guard[j] for j in active if j!=i])==z3.unsat:active.remove(i)
rows=[]
for i in active:
 assert s.check(*[guard[j] for j in active if j!=i])==z3.sat;w=model();J,slots,m=seven[i];assert not w&m;rows.append(dict(addresses=[''.join(str(j) for j in range(7) if S[a]>>j&1) for a in J],slots=slots,without_this_group=w))
assert active and s.check(*[guard[j] for j in active])==z3.unsat;print(len(rows),rows[:2]);(D/'results/ramsey_without16_seven_core.json').write_text(json.dumps(rows,indent=2)+'\n')
