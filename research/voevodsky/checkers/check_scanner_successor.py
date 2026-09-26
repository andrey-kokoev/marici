"""Scanner completion into a prewired strict query; no host release."""
from fuel_scanner import FuelScanner
from itertools import product
from random import Random
from pathlib import Path
import json
class Followed(FuelScanner):
 def __init__(self,w,c,f,j):
  super().__init__(w,c,f);self.releases=[]
  g=self.fresh('GM');o=self.fresh('OUT');self.successor=g;self.out=o
  self.add(g,('p','s','r','b','c','o'));self.add(o,('p',))
  s=self.wires.pop('RET.p');del self.wires[s]
  a=self.wires.pop('ACK.p');del self.wires[a]
  for p,q in [('s',s),('p',a),('r','RET.p'),('c','ACK.p'),('b',self.chain(('K',)*j)),('o',o+'.p')]:self.link(g+'.'+p,q)
  self.audit()
def oracle(w,c,f):
 w=list(w);cost=0
 for it in range(f):
  if c<len(w) and w[c]:return tuple(w),'FOUND',cost+2*len(w)+5*c+f-it-1+18
  cost+=2*len(w)+5*c+14;w.extend([0]*max(0,c+1-len(w)));w[c]=1;c+=1
 return tuple(w),'EXHAUSTED',cost+c+4
rng=Random(100);runs=steps=early=0
for n in range(3):
 for w in product((0,1),repeat=n):
  for c,f,j in product(range(3),range(5),range(3)):
   expected,tag,cost=oracle(w,c,f);net=Followed(w,c,f,j);published=None
   while net.enabled():
    view=net.observe();assert not view['complete'] and view['word'] is None
    if view['outcome'] is not None:
     peer=net.wires['OUTCOME.p']
     if published is None:
      published=peer;early+=1
      assert net.successor not in net.enabled() and not net.releases
      assert any(net.kind(x)=='EA' for x in net.enabled())
     assert peer==published and view['outcome']==tag
    if net.successor in net.enabled():
     assert all(net.kind(x) in ('GM','OUT','OUTCOME','RET','ACK','FOUND','EXHAUSTED','B0','B1','K','N','DONE') for x in net.types)
     assert len(net.types)==len(expected)+j+9
    net.step(rng.choice(net.enabled()))
   assert net.releases==[net.successor] and net.retained()==expected
   assert net.answer(net.out)==(j<len(expected) and bool(expected[j]))
   assert net.observe()=={'outcome':tag,'complete':True,'word':expected}
   assert net.steps==cost+1+2*len(expected)+j+3
   used=set()
   for root,size in [('RET',len(expected)+2),('ACK',2),('OUTCOME',2),(net.out,2)]:
    todo=[root];part=set()
    while todo:
     x=todo.pop()
     if x in part:continue
     part.add(x);todo.extend(net.wires[x+'.'+p].split('.')[0] for p in net.types[x])
    assert len(part)==size and not used&part;used|=part
   assert used==set(net.types)
   runs+=1;steps+=net.steps
report={'passed':True,'runs':runs,'rewrites':steps,'early_outcome_with_cleanup_pending':early,'seed':100,'scope':'Words n<=2, cursor0..2, fuel0..4, successor index0..2; seeded schedules; exact four-component accounting and combined costs.'}
p=Path(__file__).resolve().parents[1]/'results/scanner-successor.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
