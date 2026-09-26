from sequenced_set import SequencedSet
from pipeline_phase_interfaces import validate
from itertools import product
from pathlib import Path
import json
runs=checks=0
for n in range(4):
 for word in product((0,1),repeat=n):
  for i,j in product(range(n+3),repeat=2):
   program=[('member',j),('add',i),('member',j),('union',(0,1,0)),('add',j),('member',i)]
   for reverse in (False,True):
    net=SequencedSet(word,program)
    while True:
     assert validate(net);checks+=1
     choices=net.enabled()
     if not choices:break
     net.step((max if reverse else min)(choices,key=lambda n:net.stage[n]))
    net.execute();runs+=1
report={'passed':True,'runs':runs,'checked_states':checks,'clauses':'principal and saved-tail types/stage ownership, producer port waits, same-stage COPY restriction, minimal-rank active witness','scope':'Two priority schedules, necessary interfaces only; universal preservation and terminal shape not established by this test.'}
out=Path(__file__).resolve().parents[1]/'results/pipeline-phase-interfaces.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
