from pure_replacement import replace
from scanning_set_program import ScanningSetProgram
from copy import deepcopy
from itertools import product
from pathlib import Path
import json
checks=0
class Compared(ScanningSetProgram):
 def replace(self,names,edges,new):
  global checks
  before=deepcopy((self.types,self.wires));expected=replace(self.types,self.wires,names,edges,new,protected=['RET','ACK']+self.outputs)
  assert before==(self.types,self.wires)
  super().replace(names,edges,new)
  assert expected==(self.types,self.wires);checks+=1
runs=0
for ops in product([('scan',(0,2)),('ifadd',(1,0,2)),('union',()),('member',1)],repeat=2):
 for bits in ((),(0,1),(1,)):
  net=Compared(bits,ops)
  while net.enabled():net.step(net.enabled()[0])
  assert net.observe()['complete'];runs+=1
# Passive cyclic boundary and an outside-to-outside splice.
t={'A':('p','a','b'),'B':('p',),'ROOT':('x','y')}
w={'A.p':'B.p','B.p':'A.p','A.a':'ROOT.x','ROOT.x':'A.a','A.b':'ROOT.y','ROOT.y':'A.b'}
before=deepcopy((t,w));out=replace(t,w,('A','B'),[('A.a','A.b')],[])
assert out==({'ROOT':('x','y')},{'ROOT.x':'ROOT.y','ROOT.y':'ROOT.x'}) and before==(t,w)
invalid=[(('A','A'),[('A.a','A.b')],[]), (('A','B'),[('A.a','A.a')],[]), (('A','B'),[],[('ROOT',('p',))]), (('A','ROOT'),[],[])]
for names,edges,new in invalid:
 try:replace(t,w,names,edges,new)
 except ValueError:pass
 else:raise AssertionError('malformed certificate accepted')
 assert before==(t,w)
report={'passed':True,'programs':runs,'production_certificates_compared':checks,'malformed_rejections':len(invalid),'cyclic_splice_checked':True,'scope':'Independent replacement algorithm on production-generated certificates; no independent typed-rule semantics or historical allocation witness.'}
p=Path(__file__).resolve().parents[1]/'results/pure-replacement.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
