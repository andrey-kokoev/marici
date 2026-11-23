"""Delete address 16 throughout. Retain every smaller source constraint. Partition ALL seven-address groups by membership of Q=2345. Separate constraints lazily but recheck SAT bitsets against every retained group and both pinned values."""
from itertools import combinations
from pathlib import Path
import json,sys,z3
D=Path(__file__).resolve().parents[1];r=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=r['address_masks'];E={tuple(e):i for i,e in enumerate(r['edge_order'])};idx=[i for i,m in enumerate(S) if m!=66];Q=S.index(60);v=[z3.Bool('e%d'%i) for i in range(len(E))];base=[];groups=[];banned=set()
for k in range(3,8):
 for J in combinations(idx,k):
  slots=[E[e] for e in combinations(J,2) if e in E];m=sum(1<<i for i in slots);jm=sum(1<<j for j in J);u=0
  for j in J:u|=S[j]
  if k==7:groups.append((Q in J,m,slots));continue
  if k==3 and len(slots)==3:base.append((m,False,slots))
  if u.bit_count()<k:
   if not any(jm^(1<<j) in banned for j in J):base.append((m,True,slots))
   banned.add(jm)
link_test='--incident-link' in sys.argv; special=E[tuple(sorted((Q,S.index(65))))];assert all(not (m>>special&1) for m,pos,_ in base if not pos);rows=[]
for wanted in (False,True):
 s=z3.SolverFor('QF_FD');s.add([z3.Or(*[v[i] if pos else ~v[i] for i in ls]) for _,pos,ls in base]);gs=[g for g in groups if g[0]==wanted];learned=set()
 if link_test:
  # In the link-free arm remove even small clauses using the special slot.
  usebase=[x for x in base if wanted or not (x[0]>>special&1)];s=z3.SolverFor('QF_FD');s.add([z3.Or(*[v[i] if pos else ~v[i] for i in ls]) for _,pos,ls in usebase]);gs=[g for g in groups if g[0] and bool(g[1]>>special&1)==wanted]
 else:usebase=base
 for b in (0,1):
  while True:
   s.push();s.add(v[4]==bool(b),v[74]!=bool(b));res=s.check();assert res in (z3.sat,z3.unsat);row=dict(with_Q=wanted,retained=len(gs),slot4=b,slot74=1-b,status=str(res))
   if link_test:row=dict(uses_Q06=wanted,slot=special,retained=len(gs),small=len(usebase),slot4=b,slot74=1-b,status=str(res))
   if res==z3.unsat:s.pop();break
   w=sum(1<<i for i,x in enumerate(v) if z3.is_true(s.model().eval(x,model_completion=True)));s.pop();failed=[g for g in gs if not g[1]&w];
   if not failed:
    assert all((m&w if pos else m&~w) for m,pos,ls in usebase) and (w>>4&1)==b and (w>>74&1)==1-b;row.update(model=w,violated_full_sevens=sum(not (m&w) for q,m,ls in groups));break
   for _,m,ls in failed:
    if m not in learned:s.add(z3.Or(*[v[i] for i in ls]));learned.add(m)
  rows.append(row)
print(rows);(D/'results'/('ramsey_without16_incident_link.json' if link_test else 'ramsey_without16_quad_sevens.json')).write_text(json.dumps(rows,indent=2)+'\n')
