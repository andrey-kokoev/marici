"""Original support suffix remains owned by COPY, never query or eraser."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_copy_two_queries_interleavings import ScheduledTwin

class Separated(ScheduledTwin):
 def __init__(self,bits,i,j):
  super().__init__(bits,i,j)
  head=self.wires['COPY.p'].split('.')[0];origin=[]
  while True:
   origin.append(head)
   if head.startswith('N_'):break
   head=self.wires[head+'.a'].split('.')[0]
  self.origin=tuple(origin);self.checks=0
 def invariant(self):
  live=[name for name in self.origin if name in self.types]
  copiers=[name for name in self.types if name.startswith('COPY')]
  if copiers:
   assert len(copiers)==1 and live
   assert self.wires[copiers[0]+'.p']==live[0]+'.p'
  else:assert not live
  for j,name in enumerate(live):
   if j+1<len(live):assert self.wires[name+'.a']==live[j+1]+'.p'
  for name in self.types:
   if name.startswith(('E_','Q1','Q2')):
    assert self.wires[name+'.p'].split('.')[0] not in self.origin
  self.checks+=1
 def replace(self,names,connections,new_agents):
  if hasattr(self,'origin'):self.invariant()
  super().replace(names,connections,new_agents)
  if hasattr(self,'origin'):self.invariant()

cases=0;checks=0
for n in range(5):
 for bits in product((0,1),repeat=n):
  for i in range(n+3):
   for j in range(n+3):
    net=Separated(bits,i,j)
    answers,_=net.run_order((2,1,3,0))
    assert answers==(i<n and bool(bits[i]),j<n and bool(bits[j]))
    checks+=net.checks;cases+=1
report={'passed':True,'cases':cases,'invariant_checks':checks,'original_chain':'live original B/N is a suffix: COPY.p at head, each aux to next principal; no live original remains after COPY','exclusion':'neither Q nor E principal ever touches an original support node','scope':'Instrumented bounded runs and intended constructor only; full inductive grammar and arbitrary scheduling theorem not established.'}
out=Path(__file__).resolve().parents[1]/'results/original-chain-separation.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
