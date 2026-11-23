"""Try a signed reduction WITHOUT assuming slot 4 = slot 74. Use only source coverage up to size 6 plus the triangle ban. Test whether swapping labels 4 and 5 complements each individual observable, including controls with smaller families."""
from pathlib import Path
from itertools import combinations
import json,z3
D=Path(__file__).resolve().parents[1];src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=src['address_masks'];E=list(map(tuple,src['edge_order']));v=[z3.Bool(f's{i}') for i in range(len(E))];p=[0,1,2,3,5,4,6];addr=[S.index(sum(1<<p[i] for i in range(7) if s>>i&1)) for s in S];edge=[E.index(tuple(sorted((addr[a],addr[b])))) for a,b in E];assert [edge[j] for j in edge]==list(range(len(E)));tri=[];cover={5:[],6:[]};banned=set()
for k in range(3,7):
 for J in combinations(range(len(S)),k):
  slots=[E.index(x) for x in combinations(J,2) if x in E];u=0
  for j in J:u|=S[j]
  if k==3 and len(slots)==3:tri.append(z3.Or(*[~v[t] for t in slots]))
  if u.bit_count()>=k:continue
  mask=sum(1<<j for j in J)
  if not any(mask^(1<<j) in banned for j in J):cover[k].append(z3.Or(*[v[t] for t in slots]))
  banned.add(mask)
rows=[]
for name,clauses in [('tri5',tri+cover[5]),('tri6',tri+cover[6]),('cover56',cover[5]+cover[6]),('tri56',tri+cover[5]+cover[6])]:
 solver=z3.SolverFor('QF_FD');solver.add(clauses)
 for slot in [4,74]:
  statuses=[]
  for b in [False,True]:
   solver.push();solver.add(v[slot]==b,v[edge[slot]]==b);statuses.append(str(solver.check()));solver.pop()
  rows.append(dict(family=name,slot=slot,image=edge[slot],both_zero= statuses[0],both_one=statuses[1]))
print(rows);(D/'results/ramsey_mismatch_symmetry.json').write_text(json.dumps(rows,indent=2)+'\n')
