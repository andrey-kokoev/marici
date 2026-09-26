from acknowledged_unary_copy import AcknowledgedUnaryCopy
from collections import Counter
from pathlib import Path
import json
class Audited(AcknowledgedUnaryCopy):
 def replace(self,names,edges,new):
  old=set(names);boundary={n+'.'+p for n in names for p in self.types[n] if self.wires[n+'.'+p].split('.')[0] not in old}
  fresh={n+'.'+p for n,ps in new for p in ps}
  assert Counter(p for e in edges for p in e)==Counter(boundary|fresh)
  super().replace(names,edges,new)
def chain(net,root):
 nodes=set();p=net.wires[root];count=0
 while True:
  n,port=p.split('.');assert port=='p' and n not in nodes;nodes.add(n)
  if net.kind(n)=='N':return count,nodes
  assert net.kind(n)=='K';count+=1;p=net.wires[n+'.a']
runs=steps=0
for size in range(65):
 for cyclic in (False,True):
  net=Audited(size,cyclic)
  while net.enabled():
   assert net.kind(net.wires[net.roots[2]].split('.')[0])!='DONE'
   assert len(net.enabled())==1;net.step(net.enabled()[0])
  a,left=chain(net,net.roots[0]);b,right=chain(net,net.roots[1])
  assert a==b==size and not left&right
  done=net.wires[net.roots[2]].split('.')[0];assert net.kind(done)=='DONE'
  roots={p.split('.')[0] for p in net.roots}
  assert left|right|roots|{done}==set(net.types)
  assert net.steps==size+1
  runs+=1;steps+=net.steps
report={'passed':True,'runs':runs,'rewrites':steps,'lengths':'0..64','contexts':['distinct passive leaves','single three-port passive cyclic boundary'],'scope':'Two fixed rules; bounded constructor-context tests, not arbitrary contextual equivalence.'}
p=Path(__file__).resolve().parents[1]/'results/acknowledged-unary-copy.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
