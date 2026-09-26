"""Instrument unit potential at every production rewrite across priority schedules."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_runtime_original_copy_tags import Tagged

def potential(net):return sum(3 if t=='ORIGINAL' else 1 for t in net.tags.values())
class Counted(Tagged):
 def replace(self,names,connections,new_agents):
  if not hasattr(self,'tags'):return super().replace(names,connections,new_agents)
  before=potential(self)
  super().replace(names,connections,new_agents)
  assert potential(self)==before-1,(names,before,potential(self))

runs=rewrites=0
orders=((0,1,2,3),(1,2,0,3),(2,1,3,0),(3,2,1,0))
for n in range(5):
 for bits in product((0,1),repeat=n):
  for i,j in product(range(n+3),repeat=2):
   for order in orders:
    net=Counted(bits,i,j);expected=3*n+i+j+5
    assert potential(net)==expected
    answer,history=net.run_order(order)
    assert potential(net)==0 and net.steps==len(history)==expected
    assert answer==(i<n and bool(bits[i]),j<n and bool(bits[j]))
    runs+=1;rewrites+=net.steps
report={'passed':True,'runs':runs,'rewrite_delta_checks':rewrites,'schedules':len(orders),'formula':'complete rewrite count = 3*n+i+j+5','scope':'All words n<=4, indices through n+2, four priority schedules; arithmetic argument remains conditional on universal structural closure.'}
out=Path(__file__).resolve().parents[1]/'results/exact-normalization-count.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
