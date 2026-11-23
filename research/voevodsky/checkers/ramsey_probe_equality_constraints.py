"""No archived wirings as hypotheses. Load the source solver, group its positive clauses by the minimum address-set sizes used in synthesis; test both mismatches with and without constraint families. Save full SAT countermodels as bitsets."""
from pathlib import Path
from itertools import combinations
import json,sys,z3
D=Path(__file__).resolve().parents[1];sys.path.insert(0,str(D.parent/'chatgpt/ramsey'));import ramsey_seven_transport_synthesis as m
E=list(m.E.values());tri=[z3.Or(*[z3.Not(m.E[e]) for e in combinations(J,2)]) for J in combinations(range(m.n),3) if all(e in m.E for e in combinations(J,2))];groups={k:[] for k in range(1,8)};banned=set();bad=[]
for k in groups:
 for J in combinations(range(m.n),k):
  u=0
  for j in J:u|=m.S[j]
  if k<7 and u.bit_count()>=k:continue
  mask=sum(1<<i for i in J);keep=not any(mask^(1<<i) in banned for i in J);banned.add(mask)
  if keep:groups[k].append(z3.Or(*m.bad[len(bad)]));bad.append(J)
assert len(bad)==len(m.bad);rows={}
for name,T,sizes in [('triangles_only',True,[]),('coverage_only',False,list(groups)),('size6_only_with_triangles',True,[6]),('size7_only_with_triangles',True,[7])]+[(f'through_{k}',True,list(range(1,k+1))) for k in range(4,8)]:
 solver=z3.SolverFor('QF_FD');solver.add(tri if T else []);solver.add([f for k in sizes for f in groups[k]]);r=[]
 for b in [0,1]:
  solver.push();solver.add(E[4]==bool(b),E[74]!=bool(b));status=solver.check();row={'slot4':b,'status':str(status)}
  if status==z3.sat:row['model']=sum(1<<j for j,v in enumerate(E) if z3.is_true(solver.model().eval(v,model_completion=True)))
  r.append(row);solver.pop()
 rows[name]=r
assert all(t['status']=='unsat' for t in rows['through_7']);print({k:[t['status'] for t in v] for k,v in rows.items()});print({k:len(v) for k,v in groups.items()});(D/'results/ramsey_probe_equality_constraints.json').write_text(json.dumps(rows,indent=2)+'\n')
