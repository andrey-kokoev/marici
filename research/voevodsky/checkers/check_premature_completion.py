"""Find executable counterexamples to Boolean/head/full-word completion barriers."""
from sequenced_set import SequencedSet
from pipeline_canonical import key
from pipeline_contract import validate
from collections import deque
from copy import deepcopy
from pathlib import Path
import json
net=SequencedSet((1,0),[('member',0)])
queue=deque([(net,())]);seen=set();witnesses={}
while queue and len(witnesses)<3:
 net,trace=queue.popleft();k=key(net)
 if k in seen:continue
 seen.add(k);assert validate(net)
 active=[n for n in net.types if net.kind(n) in {'COPY','QB','QS','QR','E'}]
 head=net.wires['RET.p'].split('.')[0]
 boolean=net.kind(net.wires[net.outputs[0]+'.p'].split('.')[0]) in ('TRUE','FALSE')
 try:net.retained();complete=True
 except AssertionError:complete=False
 predicates={'head_not_complete':net.kind(head) in ('B0','B1') and not complete,'boolean_before_copy_done':boolean and any(net.kind(n)=='COPY' for n in active),'word_and_boolean_before_cleanup':complete and boolean and any(net.kind(n)=='E' for n in active)}
 for label,holds in predicates.items():
  if holds and label not in witnesses:
   witnesses[label]={'trace':trace,'live_controls':active,'wires':dict(sorted(net.wires.items()))}
 for n in net.enabled():
  child=deepcopy(net);other=net.wires[n+'.p'].split('.')[0]
  child.step(n);queue.append((child,trace+((n,other),)))
assert len(witnesses)==3
report={'passed':True,'input':[1,0],'program':[['member',0]],'searched_classes':len(seen),'witnesses':witnesses,'scope':'Concrete legal schedules refute three premature readiness predicates. No barrier implementation.'}
out=Path(__file__).resolve().parents[1]/'results/premature-completion.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'passed':True,'searched_classes':len(seen),'witness_trace_lengths':{k:len(v['trace']) for k,v in witnesses.items()}}))
