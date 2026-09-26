from acknowledged_membership import AcknowledgedMembership
from forest_canonical import canonical
from itertools import product
from copy import deepcopy
from pathlib import Path
import json
fixtures=states=edges=waiting=0
for length in range(3):
 for word in product((0,1),repeat=length):
  for index in range(length+3):
   pending=[AcknowledgedMembership(word,index)];seen=set();ends=set()
   while pending:
    net=pending.pop();key=canonical(net)
    if key in seen:continue
    seen.add(key)
    controls=[n for n in net.types if net.kind(n) in ('QB','QS','QR','EA')]
    done=[n for n in net.types if net.kind(n)=='DONE']
    assert len(controls)+len(done)==1
    if net.acknowledged():
     assert not controls and len(done)==1
     assert not any(net.kind(n)=='COPY' for n in net.types)
     assert net.retained()==word and net.answer(net.out)==(index<length and bool(word[index]))
     assert len(net.types)==length+6
    waiting+=sum(net.kind(n)=='EA' and net.wires[n+'.p'].startswith('COPY') for n in net.types)
    choices=net.enabled()
    if not choices:assert net.acknowledged();ends.add(key)
    for n in choices:
     child=deepcopy(net);child.step(n);pending.append(child);edges+=1
   assert len(ends)==1;states+=len(seen);fixtures+=1
report={'passed':True,'fixtures':fixtures,'states':states,'edges':edges,'eraser_COPY_waits':waiting,'finding':'Exactly one query/EA/DONE owner; DONE implies correct BOOL, complete RET and no COPY/query/eraser for these single-call fixtures.','scope':'All tiny schedules; no continuation join/gate and no multi-stage barrier theorem.'}
out=Path(__file__).resolve().parents[1]/'results/acknowledged-membership.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
