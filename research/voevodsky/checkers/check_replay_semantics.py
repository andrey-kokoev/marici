from scanning_set_program import ScanningSetProgram
from offline_replay import replay,contract,digest
from source_interpreter import interpret
from itertools import product
from copy import deepcopy
from pathlib import Path
import json
class Recorded(ScanningSetProgram):
 def step(self,n):self.before=self.serial;return super().step(n)
 def replace(self,names,edges,new):
  self.certificates.append(deepcopy(dict(names=names,edges=edges,new=new,before=self.before,after=self.serial)))
  super().replace(names,edges,new)
# Literal semantic witnesses independent of graph output.
assert interpret((0,0,1),[('scan',(0,2))])=={'word':(1,1,1),'observations':(('scan','EXHAUSTED'),)}
assert interpret((0,0,1),[('scan',(0,3))])['observations']==(('scan','FOUND'),)
assert interpret((),[('ifadd',(0,0,1)),('member',0)])['observations']==(('boolean',False),('boolean',False))
assert interpret((1,),[('scan',(0,0))])['observations']==(('scan','EXHAUSTED'),)
runs=steps=0;binding=digest(contract())
for length in range(3):
 for ops in product([('scan',(0,2)),('ifadd',(0,1,2)),('member',0),('add',1),('union',(0,1))],repeat=length):
  for bits in ((),(0,),(1,)):
   net=Recorded(bits,ops);net.certificates=[];initial=deepcopy(dict(types=net.types,wires=net.wires,serial=net.serial))
   while net.enabled():net.step(net.enabled()[0])
   trace=dict(schema='recurrent-trace-v3',provenance_status='unverified-constructor',declaration=dict(bits=bits,program=ops),output_types=net.output_types,outputs=net.outputs,contract_digest=binding,initial=initial,steps=net.certificates,complete=True,final_digest=digest(dict(types=net.types,wires=net.wires,serial=net.serial)))
   result=replay(json.loads(json.dumps(trace)))
   assert result['terminal']==interpret(bits,ops)
   runs+=1;steps+=len(net.certificates)
report={'passed':True,'traces':runs,'replayed_steps':steps,'literal_semantic_witnesses':4,'scope':'Independent direct source algorithm shares normalization only; bounded corpus, not an independent author or formal proof.'}
p=Path(__file__).resolve().parents[1]/'results/replay-semantics.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
