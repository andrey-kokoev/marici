from conditional_insertion import ConditionalInsertion
from itertools import product
from collections import Counter
from pathlib import Path
from random import Random
import json
rng=Random(90);runs=steps=0;cases=Counter();orders=Counter()
class Audited(ConditionalInsertion):
 def replace(self,names,edges,new):
  old=set(names)
  boundary={n+'.'+p for n in names for p in self.types[n] if self.wires[n+'.'+p].split('.')[0] not in old}
  fresh={n+'.'+p for n,ps in new for p in ps}
  assert Counter(p for edge in edges for p in edge)==Counter(boundary|fresh)
  cases[self.kind(names[0])+'--'+self.kind(names[1])]+=1
  super().replace(names,edges,new)
for n in range(3):
 for w in product((0,1),repeat=n):
  for i,t,f in product(range(4),repeat=3):
   b=i<n and bool(w[i]);k=t if b else f;l=f if b else t
   expected=list(w);expected.extend([0]*max(0,k+1-n));expected[k]=1
   for mode in ('cleanup-first','insert-first','random'):
    net=Audited(w,i,t,f);out=net.out;completion=[];picked=False
    while net.enabled():
     assert not net.acknowledged()
     choices=net.enabled()
     if mode=='random':a=rng.choice(choices)
     else:a=min(choices,key=lambda x:(net.kind(x)!='EA') if mode=='cleanup-first' else (net.kind(x) not in ('ABc','ASc','ARc','JOIN')))
     kind=net.kind(a)
     if kind=='WAIT':assert not any(net.kind(x) in net.work for x in net.types)
     if kind=='PICK':picked=True
     if picked and kind=='ARc':completion.append('insert')
     if picked and kind=='EA' and net.kind(net.wires[a+'.p'].split('.')[0])=='N':completion.append('cleanup')
     net.step(a)
    assert net.acknowledged() and net.retained()==tuple(expected) and net.answer(out)==b
    assert net.steps==2*n+i+2*k+l+10
    assert all(net.kind(x) in ('RET','ACK','OUT','B0','B1','N','TRUE','FALSE','DONE') for x in net.types)
    if mode!='random':assert completion==(['cleanup','insert'] if mode=='cleanup-first' else ['insert','cleanup'])
    orders['/'.join(completion)]+=1;runs+=1;steps+=net.steps
report={'passed':True,'runs':runs,'rewrites':steps,'completion_orders':dict(orders),'rule_counts':dict(sorted(cases.items())),'scope':'Bounded words n<=2 and query/branch indices0..3; two forced orders plus seeded random schedule. Not exhaustive schedule verification.'}
out=Path(__file__).resolve().parents[1]/'results/conditional-insertion.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
