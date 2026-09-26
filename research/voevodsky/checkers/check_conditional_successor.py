"""Prewire a strict successor; account for every final node by rooted components."""
from conditional_insertion import ConditionalInsertion
from itertools import product
from pathlib import Path
import json

class Followed(ConditionalInsertion):
 def __init__(self,w,i,t,f,j):
  super().__init__(w,i,t,f)
  self.releases=[];g=self.fresh('GM');o=self.fresh('OUT');self.successor=g;self.second_out=o
  self.add(g,('p','s','r','b','c','o'));self.add(o,('p',))
  support=self.wires.pop('RET.p');del self.wires[support]
  ack=self.wires.pop('ACK.p');del self.wires[ack]
  for p,q in [('s',support),('p',ack),('r','RET.p'),('c','ACK.p'),('b',self.chain(('K',)*j)),('o',o+'.p')]:self.link(g+'.'+p,q)
  self.audit()

def components(net):
 remaining=set(net.types);result=[]
 while remaining:
  todo=[next(iter(remaining))];found=set()
  while todo:
   n=todo.pop()
   if n in found:continue
   found.add(n);todo.extend(net.wires[n+'.'+p].split('.')[0] for p in net.types[n])
  remaining-=found;result.append(found)
 return result

def final_audit(net,word,b,answer):
 assert net.retained()==tuple(word) and net.answer(net.out)==b and net.answer(net.second_out)==answer and net.acknowledged()
 parts=components(net);assert len(parts)==4
 for root,size in [('RET',len(word)+2),('ACK',2),(net.out,2),(net.second_out,2)]:
  matches=[c for c in parts if root in c];assert len(matches)==1 and len(matches[0])==size
 assert len(net.types)==len(word)+8

runs=steps=releases=0
for n in range(3):
 for w in product((0,1),repeat=n):
  for i,t,f,j in product(range(3),repeat=4):
   b=i<n and bool(w[i]);k=t if b else f;l=f if b else t
   word=list(w);word.extend([0]*max(0,k+1-n));word[k]=1
   for cleanup_first in (True,False):
    net=Followed(w,i,t,f,j);snapshot=None
    while net.enabled():
     choices=net.enabled();assert not net.acknowledged()
     if net.successor in choices:
      assert not any(net.kind(x) in net.work|{'WAIT','PICK','JOIN','JOINR'} for x in net.types)
      # Only returned word, prior Boolean, pending GM, budget, and roots remain.
      assert len(net.types)==len(word)+j+9 # includes the gate's incoming DONE
      assert net.answer(net.out)==b;releases+=1
     if net.releases:
      current=net.wires[net.out+'.p']
      if snapshot is None:snapshot=current
      assert current==snapshot
     a=min(choices,key=lambda x:(net.kind(x)!='EA') if cleanup_first else (net.kind(x) not in ('ABc','ASc','ARc','JOIN')))
     net.step(a)
    final_audit(net,word,b,j<len(word) and bool(word[j]))
    assert net.releases==[net.successor]
    assert net.steps==2*n+i+2*k+l+10+1+2*len(word)+j+3
    runs+=1;steps+=net.steps
report={'passed':True,'runs':runs,'rewrites':steps,'successor_releases':releases,'final_components':4,'scope':'Words n<=2; all four indices0..2; cleanup-first and insertion-first priorities. Rooted component partition excludes detached garbage; not exhaustive schedules.'}
p=Path(__file__).resolve().parents[1]/'results/conditional-successor.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
