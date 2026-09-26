"""Atomic rejection controls; must also pass under python -O."""
from copy import deepcopy
from dataclasses import replace
from pathlib import Path
import json,hashlib
from reference import Package,Admission,Rule,Step,unit
from local_net import Net
p=Package('P');s=unit(Admission(p,'proof'));r=Rule('u',(p,),p,'w')
fixture=Step(r,(unit(s),));rejected=0

def snapshot(net):return deepcopy((net.agents,net.wires,net.next_id))
def reject(net,pair,error=ValueError):
 global rejected
 before=snapshot(net)
 try:net.rewrite(pair)
 except error:pass
 else:raise RuntimeError('invalid operation succeeded')
 if snapshot(net)!=before:raise RuntimeError('failure mutated published state')
 rejected+=1
for mutate in ('layer','payload','wire','allocator','mutable-package','nested-F'):
 net=Net(fixture);f,d=net.active()[0]
 if mutate=='layer':net.agents[f]=replace(net.agents[f],level=0)
 elif mutate=='payload':net.agents[d]=replace(net.agents[d],payload='not a rule')
 elif mutate=='wire':net.wires[0,0]=(999,0)
 elif mutate=='allocator':net.next_id=1
 elif mutate=='mutable-package':net.agents[d]=replace(net.agents[d],payload=Rule('bad',(p,),Package('bad',[]),'w'))
 else:net.agents[d]=replace(net.agents[d],kind='flatten',payload=None)
 reject(net,(f,d))
for pair in ((999,1000),(0,0),('x',1),[1,2]):reject(Net(fixture),pair)
# Inject a failure AFTER a valid private rewrite to test discard of staged edits.
class Broken(Net):
 def _rewrite_in_place(self,pair):
  super()._rewrite_in_place(pair)
  raise RuntimeError('injected post-mutation fault')
net=Broken(fixture);reject(net,net.active()[0],RuntimeError)
# Ensure evaluator/admission do not use the semantic oracle at any depth.
import reference
def forbidden(*args):raise RuntimeError('flatten oracle invoked')
reference.flatten=forbidden
net=Net(fixture)
while net.active():net.rewrite(net.active()[0])
if net.readback()!=Step(r,(s,)):raise RuntimeError('wrong result')
root=Path(__file__).parent
report={'passed':True,'atomic_rejection_controls':rejected,'reference_oracle_disabled_execution':True,'assertions_enabled':__debug__,'source_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ('admission.py','local_net.py','check_admission.py')},'scope':'In-memory single-process rewrite admission and staged commit. Not concurrency/CAS, persistence transactions, private-method security or external proof-witness verification.'}
name='admission.json' if __debug__ else 'admission-optimized.json'
(root/'results'/name).write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
