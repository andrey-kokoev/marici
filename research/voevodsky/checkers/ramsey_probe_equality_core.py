"""Extract source clause cores for 4!=74. Save replayable unit/branch refutations with addresses and 0-based slots. No saved wirings used in clause selection. Core is inclusion-minimal for this mismatch, not globally smallest."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,z3
D=Path(__file__).resolve().parents[1];src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=src['address_masks'];E=list(map(tuple,src['edge_order']));v=[z3.Bool(f'x{i}') for i in range(len(E))];rows=[]
def add(J,positive):
 slots=[E.index(e) for e in combinations(J,2) if e in E];rows.append(dict(rule=f'cover{len(J)}' if positive else 'triangle',addresses=J,slots=slots,positive=positive))
for J in combinations(range(len(S)),3):
 if all(e in E for e in combinations(J,2)):add(J,False)
banned=set()
for size in range(1,7):
 for J in combinations(range(len(S)),size):
  u=0
  for j in J:u|=S[j]
  if u.bit_count()>=size:continue
  mask=sum(1<<j for j in J)
  if not any(mask^(1<<j) in banned for j in J):add(J,True)
  banned.add(mask)
sel=[z3.Bool(f's{i}') for i in range(len(rows))];sol=z3.Solver();sol.add([z3.Implies(s,z3.Or(*[v[i] if r['positive'] else ~v[i] for i in r['slots']])) for r,s in zip(rows,sel)]);out=[]
for b in (0,1):
 sol.push();sol.add(v[4]==bool(b),v[74]!=bool(b));assert sol.check(*sel)==z3.unsat;ids=sorted(int(str(s)[1:]) for s in sol.unsat_core());
 for i in ids[:]:
  rest=[j for j in ids if j!=i];status=sol.check(*(sel[j] for j in rest));assert status in (z3.sat,z3.unsat)
  if status==z3.unsat:ids=rest
 core=[rows[j] for j in ids];stats=Counter()
 def prove(a):
  forced=[]
  while True:
   short=None;progress=False
   for k,r in enumerate(core):
    val=int(r['positive']);ss=r['slots'];free=[i for i in ss if i not in a];
    if any(a.get(i)==val for i in ss):continue
    if not free:stats['leaves']+=1;return dict(forced=forced,conflict=k)
    if len(free)==1:i=free[0];a[i]=val;forced.append([i,val,k]);progress=True;break
    if short is None or len(free)<len(short):short=free
   if not progress:break
  assert short;i=short[0];return dict(forced=forced,split=i,branches=[prove({**a,i:t}) for t in (0,1)])
 tree=prove({4:b,74:1-b});sol.pop();print(b,Counter(r['rule'] for r in core),stats,tree['forced'][:6]);out.append(dict(slot4=b,slot74=1-b,core=core,tree=tree))
(D/'results/ramsey_probe_equality_core.json').write_text(json.dumps(out,indent=2)+'\n')
