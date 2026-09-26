from sequenced_set import SequencedSet
from pipeline_contract import validate
from itertools import product
from pathlib import Path
import json
runs=checks=0
for n in range(4):
 for w in product((0,1),repeat=n):
  for i,j in product(range(n+3),repeat=2):
   for reverse in (False,True):
    net=SequencedSet(w,[('member',j),('add',i),('member',j),('union',(0,1,0)),('add',j),('member',i)])
    while True:
     assert validate(net);checks+=1
     choices=net.enabled()
     if not choices:break
     net.step((max if reverse else min)(choices,key=lambda n:net.stage[n]))
    net.execute();runs+=1
bad=SequencedSet((1,),[('member',0)])
c=next(n for n in bad.types if bad.kind(n)=='COPY')
a,b=c+'.a',c+'.b';x,y=bad.wires[a],bad.wires[b]
bad.wires[a]=y;bad.wires[y]=a;bad.wires[b]=x;bad.wires[x]=b
try:validate(bad)
except AssertionError as e:rejection=str(e)
else:raise AssertionError('private/public swap accepted')
from copy import deepcopy
base=SequencedSet((1,),[('member',0),('add',1)])
controls={}
for label in ('arity','stage bounds','stage control','output duplication'):
 bad=deepcopy(base)
 c=next(n for n in bad.types if bad.kind(n)=='COPY')
 if label=='arity':bad.types[c]=('p','a','b','extra')
 elif label=='stage bounds':bad.stage[c]=99
 elif label=='stage control':bad.stage[c]=1
 else:bad.outputs.append(bad.outputs[0])
 try:validate(bad)
 except AssertionError as e:assert str(e)==label;controls[label]=str(e)
 else:raise AssertionError(label+' forgery accepted')
assert validate(SequencedSet((),[]))
report={'negative_controls':controls,'passed':True,'runs':runs,'state_checks':checks,'branch_swap_rejection':rejection,'scope':'Includes arities, operation-stage compatibility, cardinalities, declared outputs and ownership/coverage. Stage tuple is diagnostic, not tamper-proof; allocator premise and universal proof certification remain separate.'}
out=Path(__file__).resolve().parents[1]/'results/pipeline-contract.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
