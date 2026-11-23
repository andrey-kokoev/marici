"""Test a candidate two-spoke relation without assuming 4=74 or the opposed pins. Hub 14 case; its mirror follows by (45). Distinguish a global derived invariant from a local clause. Use source clauses only up to size six, as before. Test every unequal assignment to each proposed equality separately."""
from itertools import combinations
from pathlib import Path
import json,z3
D=Path(__file__).resolve().parents[1];r=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=r['address_masks'];E={tuple(x):j for j,x in enumerate(r['edge_order'])};v=[z3.Bool(f'x{i}') for i in range(len(E))];hub=S.index((1<<1)|(1<<4));families={'full':[],'hub_only':[],'tri5':[]};banned=set()
scoped=[]
for k in range(3,7):
 for J in combinations(range(len(S)),k):
  terms=[v[E[e]] for e in combinations(J,2) if e in E];u=0
  for i in J:u|=S[i]
  if k==3 and len(terms)==3:f=z3.Or(*[~x for x in terms]);
  elif u.bit_count()<k:
   mask=sum(1<<i for i in J);keep=not any(mask^(1<<i) in banned for i in J);banned.add(mask)
   if not keep:continue
   f=z3.Or(*terms)
  else:continue
  families['full'].append(f);scoped.append((J,f))
  if hub in J:families['hub_only'].append(f)
  if k<=5:families['tri5'].append(f)
rows={}
for name,cs in families.items():
 s=z3.SolverFor('QF_FD');s.add(cs);rows[name]={}
 for i,j,opposite in [(55,57,True),(4,57,False),(74,55,True)]:
  s.push();s.add((v[i]==v[j]) if opposite else (v[i]!=v[j]));res=s.check();rows[name][f'{i},{j}']=str(res);s.pop()
# Delete all clauses using the omitted address, not just its incident edge variables. Keep the original slots addressable so relations with missing endpoints do not become vacuously true.
drops=[]
for t in range(len(S)):
 solver=z3.SolverFor('QF_FD');solver.add([f for J,f in scoped if t not in J]);result={}
 for i,j,opp in [(55,57,True),(4,57,False),(74,55,True)]:
  solver.push();solver.add(v[i]==v[j] if opp else v[i]!=v[j]);status=solver.check();assert status in (z3.sat,z3.unsat);result[f'{i},{j}']={'status':str(status)}
  if status==z3.sat:result[f'{i},{j}']['model']=sum(1<<k for k,x in enumerate(v) if z3.is_true(solver.model().eval(x,model_completion=True)))
  solver.pop()
 drops.append(dict(omit=t,mask=S[t],tests=result))
print('removable',[(key,[d['omit'] for d in drops if d['tests'][key]['status']=='unsat']) for key in result]);(D/'results/ramsey_hub_address_deletion.json').write_text(json.dumps(drops,indent=2)+'\n');print(rows);(D/'results/ramsey_hub_relation.json').write_text(json.dumps(rows,indent=2)+'\n')
