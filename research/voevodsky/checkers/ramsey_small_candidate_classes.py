"""Freeze the 82 five-link tests. Partition smaller candidates by link count and membership of the internal/external endpoint of the known red link. Check each single-class deletion (saved countermodels); verify any simultaneous deletion explicitly."""
from pathlib import Path
from itertools import combinations
import json,z3
D=Path(__file__).resolve().parents[1];r=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=r['address_masks'];E={tuple(e):i for i,e in enumerate(r['edge_order'])};v=[z3.Bool('x%d'%i) for i in E.values()];idx=[i for i,m in enumerate(S) if m!=66];q=S.index(60);bad=set();solver=z3.SolverFor('QF_FD');groups=[]
def edges(J):return [E[e] for e in combinations(sorted(J),2) if e in E]
for k in range(3,7):
 for J in combinations(idx,k):
  u=0
  for j in J:u|=S[j]
  ls=edges(J)
  if k==3 and len(ls)==3:solver.add(z3.Or(*[~v[i] for i in ls]))
  if u.bit_count()>=k:continue
  m=sum(1<<i for i in J)
  if not any(m^(1<<i) in bad for i in J):solver.add(z3.Or(*[v[i] for i in ls]))
  bad.add(m)
for J in combinations([i for i in idx if S[i] not in (60,65)],6):
 K=(*J,q)
 if any(sum(1<<i for i in a) in bad for k in (5,6) for a in combinations(K,k)):continue
 ls=edges(J)
 if len(ls)<=5:groups.append((J,ls))
out=[]
for b,pin in enumerate((74,4)):
 ends=sorted(next(e for e,i in E.items() if i==pin),key=lambda j:bool(S[j]&~60));classes={};solver.push();solver.add(v[4]==bool(b),v[74]!=bool(b));fixed=0
 for J,ls in groups:
  if pin in ls:continue
  clause=z3.Or(*[v[i] for i in ls])
  if len(ls)==5:
   iso,=[i for i in J if all(i==j or S[i]&S[j] for j in J)];overlap=tuple((S[iso]&S[j]).bit_count() for j in ends)
   if overlap in [(0,1),(1,0),(2,0)]:solver.add(clause);fixed+=1
  else:classes.setdefault(str((len(ls),*(int(j in J) for j in ends))),[]).append(clause)
 assert fixed==82 and sum(map(len,classes.values()))==41;cases=[]
 for k in range(len(classes)+1):
  for use in combinations(sorted(classes),k):
   solver.push();solver.add([f for key in use for f in classes[key]]);st=solver.check();assert st in (z3.unsat,z3.sat);rec=dict(use=use,count=fixed+sum(len(classes[key]) for key in use),status=str(st));
   if st==z3.sat:rec['model']=sum(1<<i for i,x in enumerate(v) if z3.is_true(solver.model().eval(x,model_completion=True)))
   cases.append(rec);solver.pop()
 solver.pop();best=min((z for z in cases if z['status']=='unsat'),key=lambda z:z['count']);print(b,{k:len(c) for k,c in classes.items()},best);out.append(dict(slot4=b,sizes={k:len(c) for k,c in classes.items()},cases=cases))
(D/'results/ramsey_small_candidate_classes.json').write_text(json.dumps(out,indent=2)+'\n')
