from sequenced_set import SequencedSet
from pipeline_denotation import observe
from itertools import product
from random import Random
from pathlib import Path
import json

def oracle(word,program):
 w=list(word);answers=[]
 for op,arg in program:
  if op=='member':answers.append(arg<len(w) and bool(w[arg]))
  elif op=='add':
   w.extend([0]*max(0,arg+1-len(w)));w[arg]=1
  else:w=[int((i<len(w) and w[i]) or (i<len(arg) and arg[i])) for i in range(max(len(w),len(arg)))]
 return tuple(w),tuple(answers)
rng=Random(7301);runs=checks=0
for n in range(4):
 for w in product((0,1),repeat=n):
  for i,j in product(range(n+3),repeat=2):
   p=[('member',j),('add',i),('member',j),('union',(0,1,0)),('add',j),('member',i)]
   expected=oracle(w,p)
   for order in ('forward','reverse','random'):
    net=SequencedSet(w,p)
    while True:
     assert observe(net)==expected,(w,p,order,net.history,observe(net),expected)
     checks+=1;choices=net.enabled()
     if not choices:break
     if order=='random':agent=rng.choice(choices)
     else:agent=(min if order=='forward' else max)(choices,key=lambda x:net.stage[x])
     net.step(agent)
    assert net.execute()==expected;runs+=1
report={'passed':True,'program_runs':runs,'intermediate_observation_checks':checks,'random_seed':7301,'scope':'Live RET and every pending/completed membership snapshot, three schedules on bounded six-stage programs; not mechanized universal proof.'}
out=Path(__file__).resolve().parents[1]/'results/pipeline-denotation.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
