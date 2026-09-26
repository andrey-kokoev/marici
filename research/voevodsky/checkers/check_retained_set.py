from retained_set import RetainedSet
from itertools import product
from pathlib import Path
import json
from check_port_multigraph_forest import forest

def update(w,i):
 result=list(w)+[0]*max(0,i+1-len(w));result[i]=1;return tuple(result)

def insert_checked(net,i):
 before=net.steps;net.insert(i)
 while net.enabled():
  choices=net.enabled();assert len(choices)==1
  assert forest(net);net.step(choices[0])
 assert forest(net) and net.steps-before==2*i+2
 return net.retained()

cases=0;rule_steps=0
for n in range(5):
 for w in product((0,1),repeat=n):
  for i,j in product(range(n+3),repeat=2):
   net=RetainedSet(w)
   w1=update(w,i);assert insert_checked(net,i)==w1
   out1=net.start(j);net.run();assert net.retained()==w1
   assert net.answer(out1)==(j==i or (j<n and bool(w[j])))
   w2=update(w1,j);assert insert_checked(net,j)==w2
   out2=net.start(i);net.run();assert net.answer(out2) and net.retained()==w2
   assert net.answer(out1)==(j==i or (j<n and bool(w[j])))
   assert insert_checked(net,j)==w2 # idempotence
   cases+=1;rule_steps+=net.steps
report={'passed':True,'composed_programs':cases,'total_rewrites':rule_steps,'program':'add(i); member(j); add(j); member(i); add(j) again','checks':['retained words','update-query law','old answers unchanged','idempotence','insertion forest at every step','exact insertion cost 2*i+2'],'scope':'All words n<=4, indices through n+2; host-side sequential plugging, not concurrent or autonomous sequencing.'}
out=Path(__file__).resolve().parents[1]/'results/retained-set.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
