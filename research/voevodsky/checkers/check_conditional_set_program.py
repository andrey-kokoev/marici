from conditional_set_program import ConditionalSetProgram
from itertools import product
from collections import Counter
from random import Random
from pathlib import Path
import json
rng=Random(92);runs=steps=gc=0
class Audited(ConditionalSetProgram):
 def replace(self,names,edges,new):
  old=set(names);boundary={n+'.'+p for n in names for p in self.types[n] if self.wires[n+'.'+p].split('.')[0] not in old}
  fresh={n+'.'+p for n,ps in new for p in ps}
  assert Counter(x for e in edges for x in e)==Counter(boundary|fresh)
  super().replace(names,edges,new)
def oracle(w,program):
 w=list(w);answers=[];cost=len(program)
 for op,a in program:
  n=len(w)
  if op=='ifadd':
   i,t,f=a;b=i<n and bool(w[i]);k=t if b else f;l=f if b else t
   answers.append(b);cost+=2*n+i+2*k+l+10;a=k;op='conditional-add'
  if op=='member':answers.append(a<n and bool(w[a]));cost+=2*n+a+3
  elif op in ('add','conditional-add'):
   if op=='add':cost+=2*a+2
   w.extend([0]*max(0,a+1-n));w[a]=1
  elif op=='union':
   m=len(a);cost+=2*n+1 if n<=m else 2*m+2
   w=[int((i<n and w[i]) or (i<m and a[i])) for i in range(max(n,m))]
 return tuple(w),tuple(answers),cost
alphabet=[('ifadd',(0,2,0)),('ifadd',(2,0,3)),('member',1),('add',1),('union',(0,1))]
for length in range(4):
 for program in product(alphabet,repeat=length):
  for w in ((),(0,),(1,),(1,0)):
   net=Audited(w,program);word,answers,cost=oracle(w,program)
   while net.enabled():
    assert not net.acknowledged()
    for a in net.enabled():
     if net.kind(a) in net.gates_kinds:
      assert a==net.gates[len(net.releases)]
      assert not any(net.kind(x) in net.work for x in net.types)
    a=rng.choice(net.enabled());gc+=net.kind(a)=='GC';net.step(a)
   assert net.retained()==word and net.acknowledged()
   assert tuple(net.answer(o) for o in net.outputs)==answers and net.steps==cost
   assert net.releases==net.gates
   # Known rooted chains/pairs account for every node; no disconnected garbage.
   used=set()
   for root in ['RET','ACK']+net.outputs:
    todo=[root];part=set()
    while todo:
     x=todo.pop()
     if x in part:continue
     part.add(x);todo.extend(net.wires[x+'.'+p].split('.')[0] for p in net.types[x])
    assert not used&part;used|=part
    assert len(part)==(len(word)+2 if root=='RET' else 2)
   assert used==set(net.types)
   runs+=1;steps+=net.steps
report={'passed':True,'runs':runs,'rewrites':steps,'conditional_releases':gc,'max_program_length':3,'seed':92,'scope':'All programs over five fixtures through length3, four inputs, one seeded schedule each. Includes consecutive conditionals; not general branch bodies or loops.'}
p=Path(__file__).resolve().parents[1]/'results/conditional-set-program.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
