from initial_net_recognizer import recognize
from scanning_set_program import ScanningSetProgram
from itertools import product
from copy import deepcopy
from pathlib import Path
import json
runs=0
for length in range(4):
 for ops in product([('member',1),('add',0),('union',(0,1)),('ifadd',(0,1,2)),('scan',(1,2))],repeat=length):
  for bits in ((),(0,1)):
   net=ScanningSetProgram(bits,ops);before=deepcopy(net.__dict__)
   recognize(net.types,net.wires,bits,ops,net.outputs,net.output_types)
   assert before==net.__dict__;runs+=1
net=ScanningSetProgram((0,),[('scan',(0,2)),('member',0)])
wrong=[((1,),[('scan',(0,2)),('member',0)],net.outputs,net.output_types),((0,),[('scan',(0,1)),('member',0)],net.outputs,net.output_types),((0,),[('scan',(0,2)),('member',0)],list(reversed(net.outputs)),net.output_types)]
for bits,ops,outs,tags in wrong:
 try:recognize(net.types,net.wires,bits,ops,outs,tags)
 except ValueError:pass
 else:raise AssertionError('false declaration accepted')
report={'passed':True,'recognized_constructors':runs,'false_declarations_rejected':len(wrong),'scope':'Structure checked without compiler calls inside recognizer; no allocator-history authentication.'}
p=Path(__file__).resolve().parents[1]/'results/initial-recognizer.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
