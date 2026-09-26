from strict_set_program import StrictSetProgram
from itertools import product
from random import Random
from pathlib import Path
import json
rng=Random(86)
def oracle(word,program):
 w=list(word);ans=[];cost=len(program)
 for op,a in program:
  if op=='member':cost+=2*len(w)+a+3;ans.append(a<len(w) and bool(w[a]))
  elif op=='add':cost+=2*a+2;w.extend([0]*max(0,a+1-len(w)));w[a]=1
  else:
   n,m=len(w),len(a);cost+=2*n+1 if n<=m else 2*m+2
   w=[int((i<n and w[i]) or (i<m and a[i])) for i in range(max(n,m))]
 return tuple(w),tuple(ans),cost
alphabet=(('member',0),('member',2),('add',0),('add',2),('union',()),('union',(0,1)))
runs=rewrites=0
for count in range(4):
 for program in product(alphabet,repeat=count):
  for word in ((),(0,),(1,)):
   net=StrictSetProgram(word,program);expected,answers,cost=oracle(word,program)
   while net.enabled():
    choices=net.enabled()
    for g in choices:
     if net.kind(g) in net.gates_kinds:
      assert g==net.gates[len(net.releases)]
      assert not any(net.kind(n) in net.work for n in net.types)
    assert not net.acknowledged()
    net.step(rng.choice(choices))
   assert net.releases==net.gates
   assert net.acknowledged() and net.retained()==expected
   assert tuple(net.answer(o) for o in net.outputs)==answers
   assert net.steps==cost
   assert not any(net.kind(n) in net.work|net.gates_kinds for n in net.types)
   runs+=1;rewrites+=net.steps
report={'passed':True,'program_runs':runs,'rewrites':rewrites,'alphabet':alphabet,'max_length':3,'seed':86,'checks':['release order','no operation work at gate eligibility','final DONE','word and ordered snapshots','exact total count'],'scope':'One seeded random schedule per bounded mixed program/input, not exhaustive reductions or formal verification.'}
out=Path(__file__).resolve().parents[1]/'results/strict-set-program.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
