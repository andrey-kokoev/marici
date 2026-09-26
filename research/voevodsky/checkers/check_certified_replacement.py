from certified_replacement import checked_replace
from scanning_set_program import ScanningSetProgram
from pathlib import Path
from copy import deepcopy
import json
# Explicit audit table, not generated from each captured production replacement.
source=Path(__file__).resolve().parents[1]/'results/combined-signature.json'
table=json.loads(source.read_text());signature=table['signature'];allowed=table['allowed_pairs'];checks=0
class Checked(ScanningSetProgram):
 def step(self,n):
  self.before_step=self.serial
  return super().step(n)
 def replace(self,names,edges,new):
  global checks
  expected=checked_replace(self.types,self.wires,names,edges,new,before=self.before_step,after=self.serial,signature=signature,allowed=allowed,protected=['RET','ACK']+self.outputs)
  super().replace(names,edges,new);assert expected==(self.types,self.wires);checks+=1
for bits in ((),(0,1),(1,)):
 net=Checked(bits,[('scan',(0,3)),('ifadd',(1,0,2)),('member',0),('union',())])
 while net.enabled():net.step(net.enabled()[0])
# Fixed minimal EA--N certificate, and targeted witness/schema tampering.
t={'EA_1':('p','r'),'N_2':('p',),'ACK':('p',)};w={'EA_1.p':'N_2.p','N_2.p':'EA_1.p','EA_1.r':'ACK.p','ACK.p':'EA_1.r'}
args=dict(types=t,wires=w,names=('EA_1','N_2'),edges=[('EA_1.r','DONE_3.p')],new=[('DONE_3',('p',))],before=2,after=3,signature=signature,allowed=allowed)
snapshot=deepcopy((t,w));checked_replace(**args)
mutants=[{'before':1},{'after':4},{'new':[('DONE_3',('p','a'))]},{'allowed':{}},{'new':[('DONE_03',('p',))]}, {'new':[('DONE_1',('p',))]}]
for change in mutants:
 try:checked_replace(**(args|change))
 except ValueError:pass
 else:raise AssertionError('bad certificate admitted')
 assert snapshot==(t,w)
report={'passed':True,'production_certificates':checks,'rejected_tampered_certificates':len(mutants),'scope':'Consumes explicit audit artifact tables; authentic history and exact rule wiring remain caller/reviewer obligations.'}
p=source.parent/'certified-replacement.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
