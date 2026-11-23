"""Use only the 39 certified coverage groups, drop the isolated Q, then discard groups hit by the red mismatch pin. Prune each polarity's list by SAT with the smaller rules held fixed. A failed clause returns its six addresses without any search outside the list."""
import json,z3
from itertools import combinations
from pathlib import Path
D=Path(__file__).resolve().parents[1];load=lambda n:json.loads((D/'results'/n).read_text());src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=src['address_masks'];E={tuple(e):i for i,e in enumerate(src['edge_order'])};idx=[i for i,s in enumerate(S) if s!=66];v=[z3.Bool(f'x{i}') for i in range(len(E))];s=z3.Solver();banned=set();
for k in range(3,7):
 for J in combinations(idx,k):
  ls=[E[e] for e in combinations(J,2) if e in E];u=0
  for a in J:u|=S[a]
  if k==3 and len(ls)==3:s.add(z3.Or(*[~v[i] for i in ls]))
  if u.bit_count()>=k:continue
  m=sum(1<<a for a in J)
  if not any(m^(1<<a) in banned for a in J):s.add(z3.Or(*[v[i] for i in ls]))
  banned.add(m)
qs=[];guards=[]
for i,q in enumerate(load('ramsey_without16_seven_core.json')):
 group=[S.index(sum(1<<int(c) for c in a)) for a in q['addresses'] if a!='2345'];assert len(group)==6 and all(S[j] not in (65,66) for j in group);ls=[E[e] for e in combinations(group,2) if e in E];assert ls==q['slots'];qs.append(dict(six=[a for a in q['addresses'] if a!='2345'],slots=ls));g=z3.Bool(f'g{i}');guards.append(g);s.add(z3.Implies(g,z3.Or(*[v[j] for j in ls])))
out=[]
for b in (0,1):
 s.push();s.add(v[4]==bool(b),v[74]!=bool(b));red=4 if b else 74;live=[i for i,q in enumerate(qs) if red not in q['slots']];start=len(live);check=lambda l:s.check(*(guards[i] for i in l));assert check(live)==z3.unsat
 for i in live[:]:
  rest=[j for j in live if j!=i];status=check(rest);assert status in (z3.sat,z3.unsat)
  if status==z3.unsat:live=rest
 assert check(live)==z3.unsat;s.pop();rows=[qs[i] for i in live];print(b,start,len(rows),len(set(j for r in rows for j in r['slots'])));out.append(dict(slot4=b,slot74=1-b,after_red_filter=start,tests=rows))
(D/'results/ramsey_short_six_list.json').write_text(json.dumps(out,indent=2)+'\n')
