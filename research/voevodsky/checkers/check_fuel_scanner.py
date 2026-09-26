from fuel_scanner import FuelScanner
from itertools import product
from random import Random
from collections import Counter
from pathlib import Path
import json
rng=Random(98);runs=steps=0
class Audited(FuelScanner):
 def replace(self,names,edges,new):
  old=set(names);boundary={n+'.'+p for n in names for p in self.types[n] if self.wires[n+'.'+p].split('.')[0] not in old}
  fresh={n+'.'+p for n,ps in new for p in ps}
  assert Counter(p for e in edges for p in e)==Counter(boundary|fresh)
  super().replace(names,edges,new)
for n in range(3):
 for bits in product((0,1),repeat=n):
  for c,f in product(range(3),range(5)):
   w=list(bits);cursor=c;outcome='EXHAUSTED';queries=0;cost=0
   for iteration in range(f):
    queries+=1
    if cursor<len(w) and w[cursor]:
     outcome='FOUND';cost+=2*len(w)+5*cursor+(f-iteration-1)+18;break
    cost+=2*len(w)+5*cursor+14
    w.extend([0]*max(0,cursor+1-len(w)));w[cursor]=1;cursor+=1
   if outcome=='EXHAUSTED':cost+=cursor+4
   net=Audited(bits,c,f);starts=0
   while net.enabled():
    assert not net.acknowledged()
    a=rng.choice(net.enabled());starts+=net.kind(a)=='START';net.step(a)
    assert net.steps<10000
   assert net.steps==cost
   assert starts==queries and net.retained()==tuple(w) and net.acknowledged()
   assert net.kind(net.wires['OUTCOME.p'].split('.')[0])==outcome
   used=set()
   for root,size in [('RET',len(w)+2),('ACK',2),('OUTCOME',2)]:
    todo=[root];part=set()
    while todo:
     x=todo.pop()
     if x in part:continue
     part.add(x);todo.extend(net.wires[x+'.'+p].split('.')[0] for p in net.types[x])
    assert not used&part and len(part)==size;used|=part
   assert used==set(net.types)
   runs+=1;steps+=net.steps
report={'passed':True,'runs':runs,'rewrites':steps,'scope':'All words n<=2, cursor0..2, fuel0..4; seeded random schedules; exact final components and query count, not formal verification.'}
p=Path(__file__).resolve().parents[1]/'results/fuel-scanner.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
