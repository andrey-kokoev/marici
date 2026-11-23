"""Test direct source-clause conflicts with both exactly-one pairs pinned, then exhaust unit propagation. Try every single extra bit by failed-literal propagation if the unsplit test stalls. No catalogue wiring used as a premise."""
from itertools import combinations
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1];src=json.loads((D.parent/'chatgpt/ramsey/ramsey_seven_all_wirings.json').read_text());S=src['address_masks'];E={tuple(t):i for i,t in enumerate(src['edge_order'])};clauses=[];banned=set()
def add(J,v):clauses.append((sum(1<<E[e] for e in combinations(J,2) if e in E),v,J))
for J in combinations(range(len(S)),3):
 if all(e in E for e in combinations(J,2)):add(J,0)
for k in range(1,8):
 for J in combinations(range(len(S)),k):
  u=0
  for j in J:u|=S[j]
  if k<7 and u.bit_count()>=k:continue
  mask=sum(1<<j for j in J)
  if not any(mask^(1<<j) in banned for j in J):add(J,1)
  banned.add(mask)
def closure(a,cs):
 a=a[:];steps=[]
 while True:
  count=len(steps)
  for mask,v,J in cs:
   if a[v]&mask:continue
   left=mask&~(a[0]|a[1]);
   if not left:return a,steps,list(J)
   if left&(left-1)==0:a[v]|=left;steps.append([left.bit_length()-1,v,list(J)])
  if len(steps)==count:return a,steps,None
out=[];hub_back=[]
for b in [0,1]:
 vals={4:b,5:1-b,74:1-b,71:b};a=[sum(1<<i for i,val in vals.items() if val==v) for v in (0,1)];direct=sum(mask&~a[1-v]==0 for mask,v,J in clauses);d,steps,conf=closure(a,clauses);branches=[]
 if conf is None:
  for i in range(len(E)):
   if ((d[0]|d[1])>>i)&1:continue
   tests=[]
   for v in (0,1):
    h=d[:];h[v]|=1<<i;_,proof,end=closure(h,clauses);tests.append(end)
   if i==(2 if b else 1):
    for z in (0,1):
     h=d[:];h[z]|=1<<i;f,chain,end=closure(h,clauses);pending=[mask&~(f[0]|f[1]) for mask,value,_ in clauses if not mask&f[value]];second=[];j=60 if b else 55
     if end is None:
      assert not (f[0]|f[1])&(1<<j)
      for w in (0,1):
       a2=f[:];a2[w]|=1<<j;_,_,conf2=closure(a2,clauses);assert conf2 is not None;second.append(conf2)
     hub_back.append(dict(slot4=b,split=i,value=z,forced=chain,conflict=end,remaining_bits=len(E)-(f[0]|f[1]).bit_count(),min_open=min(x.bit_count() for x in pending),second_slot=j,second_conflicts=second))
   if all(tests):
    chains=[]
    for v in (0,1):
     h=d[:];h[v]|=1<<i;_,proof,end=closure(h,clauses);chains.append(dict(value=v,steps=proof,conflict=end))
    branches.append(dict(split=i,chains=chains))
 out.append(dict(slot4=b,clauses=len(clauses),direct=direct,steps=steps,conflict=conf,one_split=branches));print(b,direct,len(steps),conf,len(branches),[(t['value'],len(t['steps']),t['conflict']) for t in branches[0]['chains']])
(D/'results/ramsey_back_spoke.json').write_text(json.dumps(hub_back,indent=2)+'\n');(D/'results/ramsey_opposed_choices.json').write_text(json.dumps(out,indent=2)+'\n')
