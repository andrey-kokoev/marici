"""Extract six-set witnesses on the 16-address induced red graph. Test whether a fixed six-set is unavoidable for one mismatch, by finding compatible small-rule countermodels with no common independent six-set. No Q sevens used in the model search."""
from pathlib import Path
from itertools import combinations
import json,z3
D=Path(__file__).resolve().parents[1];src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=src['address_masks'];E={tuple(e):i for i,e in enumerate(src['edge_order'])};v=[z3.Bool('x%d'%i) for i in range(len(E))];chart=[i for i,s in enumerate(S) if s!=66];core=[i for i in chart if S[i] not in (60,65)];assert len(core)==16
def slots(J):return [E[e] for e in combinations(J,2) if e in E]
def show(J):return [''.join(str(i) for i in range(7) if S[j]>>i&1) for j in J]
groups={J:sum(1<<i for i in slots(J)) for J in combinations(core,6)};solver=z3.SolverFor('QF_FD');banned=set()
for k in range(3,7):
 for J in combinations(chart,k):
  ls=slots(J);u=0
  for j in J:u|=S[j]
  if k==3 and len(ls)==3:solver.add(z3.Or(*[~v[i] for i in ls]))
  if u.bit_count()>=k:continue
  m=sum(1<<j for j in J)
  if not any(m^(1<<j) in banned for j in J):solver.add(z3.Or(*[v[i] for i in ls]))
  banned.add(m)
rows=[]
for old in json.loads((D/'results/ramsey_without16_incident_link.json').read_text()):
 if old['status']!='sat':continue
 b=old['slot4'];w=old['model'];solver.push();solver.add(v[4]==bool(b),v[74]!=bool(b));remaining=set(groups);models=[]
 while True:
  misses=[J for J,m in groups.items() if not w&m];assert misses;remaining.intersection_update(misses);models.append(dict(wiring=w,first_six=show(misses[0]),independent_sixes=len(misses),common_left=len(remaining)))
  if not remaining:break
  solver.push();solver.add(z3.Or(*[v[i] for J in sorted(remaining) for i in slots(J)]));st=solver.check();assert st in (z3.sat,z3.unsat)
  if st==z3.sat:w=sum(1<<i for i,x in enumerate(v) if z3.is_true(solver.model().eval(x,model_completion=True)))
  solver.pop()
  if st==z3.unsat:break
 solver.pop();rows.append(dict(slot4=b,models=models,universal=[show(J) for J in sorted(remaining)]));print(b,models,len(remaining))
(D/'results/ramsey_mismatch_six_witness.json').write_text(json.dumps(rows,indent=2)+'\n')
