from triple_cursor import TripleCursor
from collections import Counter
from pathlib import Path
import json
class Audited(TripleCursor):
 def replace(self,names,edges,new):
  old=set(names);boundary={n+'.'+p for n in names for p in self.types[n] if self.wires[n+'.'+p].split('.')[0] not in old}
  fresh={n+'.'+p for n,ps in new for p in ps}
  assert Counter(p for e in edges for p in e)==Counter(boundary|fresh)
  super().replace(names,edges,new)
def chain(net,root):
 seen=set();length=0;p=net.wires[root]
 while True:
  n,port=p.split('.');assert port=='p' and n not in seen;seen.add(n)
  if net.kind(n)=='N':return length,seen
  assert net.kind(n)=='K';length+=1;p=net.wires[n+'.a']
runs=steps=0
for size in range(65):
 for cyclic in (False,True):
  net=Audited(size,cyclic);phases=[]
  while net.enabled():
   assert len(net.enabled())==1
   assert net.kind(net.wires[net.roots[3]].split('.')[0])!='DONE'
   assert all(net.kind(net.wires[r].split('.')[0]) in ('PREP','READY') for r in net.roots[:3])
   a=net.enabled()[0]
   if net.kind(a) in ('PREP','READY'):phases.append(net.kind(a));assert not any(net.kind(x)=='DC' for x in net.types)
   net.step(a)
  assert phases==['PREP','READY']
  used={p.split('.')[0] for p in net.roots}
  for r in net.roots[:3]:
   length,nodes=chain(net,r);assert length==size and not used&nodes;used|=nodes
  done=net.wires[net.roots[3]].split('.')[0];assert net.kind(done)=='DONE' and done not in used;used.add(done)
  assert used==set(net.types) and net.steps==2*size+4
  runs+=1;steps+=net.steps
report={'passed':True,'runs':runs,'rewrites':steps,'lengths':'0..64','contexts':['separate roots','passive cyclic four-port boundary'],'checks':['two local completion latches','no public prefixes','disjoint complete cursors','linear replacement','exact node accounting','2n+4 cost']}
p=Path(__file__).resolve().parents[1]/'results/triple-cursor.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
