"""All redex orders for a bounded grammar; quotient preserves stages and OUT order."""
from sequenced_set import SequencedSet
from pipeline_contract import validate
from pipeline_denotation import observe
from pipeline_canonical import key
from copy import deepcopy
from itertools import product
from pathlib import Path
import json

def oracle(w,p):
 w=list(w);ans=[]
 for op,a in p:
  if op=='member':ans.append(a<len(w) and bool(w[a]))
  elif op=='add':w.extend([0]*max(0,a+1-len(w)));w[a]=1
  else:w=[int((i<len(w) and w[i]) or (i<len(a) and a[i])) for i in range(max(len(w),len(a)))]
 return tuple(w),tuple(ans)
alphabet=(('add',0),('add',2),('member',0),('member',2),('union',()),('union',(0,1)))
fixtures=states=edges=0
for length in range(3):
 for p in product(alphabet,repeat=length):
  for w in ((),(0,),(1,)):
   expected=oracle(w,p);pending=[SequencedSet(w,p)];seen=set();ends=set()
   while pending:
    net=pending.pop();assert validate(net);assert observe(net)==expected
    k=key(net)
    if k in seen:continue
    seen.add(k);choices=net.enabled()
    if not choices:
     assert net.execute()==expected;ends.add(k)
    for a in choices:
     child=deepcopy(net);child.step(a);assert validate(child) and observe(child)==expected
     pending.append(child);edges+=1
   assert len(ends)==1
   states+=len(seen);fixtures+=1
report={'passed':True,'fixtures':fixtures,'labelled_classes':states,'edges':edges,'alphabet':alphabet,'maximum_program_length':2,'inputs':[[],[0],[1]],'key':'forest kind/port plus stage and ordered output identity','scope':'All individual choices within bounded grammar only. Earlier unlabelled pipeline quotients did not preserve output order and should not certify snapshot-sensitive exhaustive coverage.'}
out=Path(__file__).resolve().parents[1]/'results/pipeline-program-grammar.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
