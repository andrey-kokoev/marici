from acknowledging_eraser import AcknowledgingEraser
from itertools import product
from check_port_multigraph_forest import forest
from pathlib import Path
import json
cases=checks=0
for length in range(7):
 for kinds in product(('B0','B1','K'),repeat=length):
  net=AcknowledgingEraser(kinds)
  while True:
   assert forest(net)
   data=[n for n in net.types if net.kind(n) in ('B0','B1','K','N')]
   assert net.acknowledged()==(not data)
   assert sum(net.kind(n) in ('EA','DONE') for n in net.types)==1
   checks+=1
   choices=net.enabled()
   if not choices:break
   assert len(choices)==1;net.step(choices[0])
  assert net.acknowledged() and len(net.types)==2 and net.steps==length+1
  cases+=1
report={'passed':True,'chains':cases,'state_checks':checks,'scope':'Isolated finite B/K chains length<=6, exactly one cleanup acknowledgment; no query/COPY integration or strict barrier yet.'}
out=Path(__file__).resolve().parents[1]/'results/acknowledging-eraser.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
