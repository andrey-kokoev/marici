"""Single-address deletion with all source rules. Separate size-7 clauses lazily: SAT requires checking every retained 7-set; UNSAT of a subset suffices. Validate saved models directly against triangle, small coverage and 7-set masks. Use original slots to compare with the previous deletion experiment."""
from itertools import combinations
from pathlib import Path
import json,z3
D=Path(__file__).resolve().parents[1];src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=src['address_masks'];E={tuple(t):i for i,t in enumerate(src['edge_order'])};v=[z3.Bool(f's{i}') for i in range(len(E))];cs=[];seven=[];banned=set()
for k in range(3,8):
 for J in combinations(range(len(S)),k):
  u=0
  for j in J:u|=S[j]
  jm=sum(1<<j for j in J);slots=tuple(E[e] for e in combinations(J,2) if e in E);m=sum(1<<i for i in slots)
  if k==7:seven.append((jm,m,slots));continue
  if k==3 and len(slots)==3:cs.append((jm,m,False,z3.Or(*[~v[i] for i in slots])))
  if u.bit_count()<k:
   keep=not any(jm^(1<<j) in banned for j in J);banned.add(jm)
   if keep:cs.append((jm,m,True,z3.Or(*[v[i] for i in slots])))
rows=[]
for t in range(len(S)):
 small=[c for c in cs if not c[0]>>t&1];big=[c for c in seven if not c[0]>>t&1];s=z3.SolverFor('QF_FD');s.add([c[3] for c in small]);learned=set();out={}
 for i,j,opp in [(55,57,True),(4,57,False),(74,55,True),(4,74,False)]:
  bad=(v[i]==v[j]) if opp else (v[i]!=v[j]);
  while True:
   s.push();s.add(bad);status=s.check();assert status in (z3.sat,z3.unsat)
   if status==z3.unsat:s.pop();out[f'{i},{j}']=None;break
   model=s.model();w=sum(1<<h for h,x in enumerate(v) if z3.is_true(model.eval(x,model_completion=True)));s.pop();failed=[c for c in big if not c[1]&w];
   if not failed:
    assert all((m&w if pos else m&~w) for _,m,pos,_ in small);assert (((w>>i)^(w>>j))&1)!=int(opp);out[f'{i},{j}']=w;break
   for _,m,slots in failed:
    if m not in learned:learned.add(m);s.add(z3.Or(*[v[h] for h in slots]))
 rows.append(dict(omit=t,mask=S[t],counterexamples=out));
print({k:[r['omit'] for r in rows if r['counterexamples'][k] is None] for k in out});(D/'results/ramsey_hub_seven_deletion.json').write_text(json.dumps(rows,indent=2)+'\n')
