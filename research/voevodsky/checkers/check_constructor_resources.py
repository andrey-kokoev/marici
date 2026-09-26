"""Instrument each add/fresh, including transient placeholder coexistence."""
from scanning_set_program import ScanningSetProgram
from program_preflight import preflight
from itertools import product
from pathlib import Path
import json
class Measured(ScanningSetProgram):
 def __init__(self,*args):
  self.allocations=0;self.highwater=0;self.fresh_calls=0
  super().__init__(*args)
 def add(self,n,ports):
  super().add(n,ports);self.allocations+=1;self.highwater=max(self.highwater,len(self.types))
 def fresh(self,k):
  self.fresh_calls+=1;return super().fresh(k)
runs=0
alphabet=[('member',0),('add',2),('union',()),('ifadd',(0,0,0)),('scan',(0,0)),('scan',(3,4))]
for length in range(5):
 for ops in product(alphabet,repeat=length):
  for bits in ((),(1,0)):
   plan=preflight(bits,ops);net=Measured(plan.bits,plan.instructions)
   assert net.highwater==plan.constructor_peak_agents
   assert net.allocations==plan.constructor_agent_allocations
   assert net.fresh_calls==net.serial==plan.constructor_fresh_names
   assert len(net.types)==plan.initial_agents;runs+=1
report={'passed':True,'constructor_runs':runs,'max_instructions':4,'scope':'All mixtures over six fixtures and two inputs; measurements at every add/fresh, not Python memory bytes. Formula proof documented separately.'}
p=Path(__file__).resolve().parents[1]/'results/constructor-resources.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
