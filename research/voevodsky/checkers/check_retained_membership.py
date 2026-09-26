from retained_membership import RetainedMembership as Net
from forest_canonical import canonical
from itertools import product
from copy import deepcopy
from pathlib import Path
import json
runs=0
for n in range(5):
 for word in product((0,1),repeat=n):
  for i,j in product(range(n+3),repeat=2):
   for priority in [('COPY','QB','QS','QR','E'),('E','QB','QS','QR','COPY')]:
    net=Net(word);outputs=[]
    for index in (i,j):
     before=net.steps;out=net.start(index);outputs.append(out)
     net.run(priority)
     assert net.steps-before==2*n+index+3
     assert net.retained()==word
     assert net.answer(out)==(index<n and bool(word[index]))
    assert net.answer(outputs[0])==(i<n and bool(word[i]))
    assert len(net.types)==n+6 # retained n bits/N + RET + two BOOL/OUT pairs
    runs+=1
# Exhaust all individual enabled reductions for single calls on small words.
states=edges=fixtures=0
for n in range(3):
 for word in product((0,1),repeat=n):
  for index in range(n+3):
   net=Net(word);out=net.start(index);pending=[net];seen=set();ends=set();fixtures+=1
   while pending:
    net=pending.pop();key=canonical(net)
    if key in seen:continue
    seen.add(key);choices=net.enabled()
    if not choices:
     assert net.retained()==word and net.answer(out)==(index<n and bool(word[index]))
     assert net.steps==2*n+index+3;ends.add(key)
    for agent in choices:
     child=deepcopy(net);child.step(agent);pending.append(child);edges+=1
   assert len(ends)==1;states+=len(seen)
report={'passed':True,'two_call_runs':runs,'small_single_call_fixtures':fixtures,'exact_states':states,'edges':edges,'step_count_per_call':'2*n+i+3','scope':'Caller plugs each subsequent query into the actual returned RET chain; not an internal continuation rule or concurrent calls.'}
out=Path(__file__).resolve().parents[1]/'results/retained-membership.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
