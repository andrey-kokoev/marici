from conditional_set_program import ConditionalSetProgram
from copy import deepcopy
from pathlib import Path
import json
checks=0

def observe(net):
 global checks
 before=deepcopy(net.__dict__);result=net.observe();assert before==net.__dict__;checks+=1
 assert result['complete']==net.acknowledged()
 if not result['complete']:assert result['word'] is None
 return result

for bit in (0,1):
 # Choose index0, reject index7 in both cases; delay EA after PICK.
 args=(0,0,7) if bit else (0,7,0)
 net=ConditionalSetProgram((bit,),[('ifadd',args),('member',0)])
 assert observe(net)['snapshots']==(None,None)
 while not any(net.kind(a)=='PICK' for a in net.enabled()):
  net.step(net.enabled()[0]);assert observe(net)['snapshots']==(None,None)
 pick=next(a for a in net.enabled() if net.kind(a)=='PICK');net.step(pick)
 assert observe(net)=={'snapshots':(bool(bit),None),'complete':False,'word':None}
 while any(net.kind(a) in ('ABc','ASc','ARc','JOIN') for a in net.enabled()):
  a=next(a for a in net.enabled() if net.kind(a) in ('ABc','ASc','ARc','JOIN'));net.step(a)
  assert observe(net)['snapshots']==(bool(bit),None)
 assert any(net.kind(a)=='EA' for a in net.enabled())
 assert len(net.releases)==1 and not observe(net)['complete']
 while net.enabled():
  net.step(net.enabled()[0]);assert observe(net)['snapshots'][0] is bool(bit)
 assert observe(net)=={'snapshots':(bool(bit),True),'complete':True,'word':(1,)}

# Ordinary membership can publish while query-side cleanup is pending.
net=ConditionalSetProgram((0,1,1),[('member',0)])
while observe(net)['snapshots']==(None,):net.step(net.enabled()[0])
assert observe(net)['snapshots']==(False,) and not observe(net)['complete']
assert net.enabled()
while net.enabled():net.step(net.enabled()[0]);observe(net)
assert observe(net)=={'snapshots':(False,),'complete':True,'word':(0,1,1)}
assert observe(ConditionalSetProgram((),[]))=={'snapshots':(),'complete':True,'word':()}
net=ConditionalSetProgram((),[('add',2)])
assert observe(net)=={'snapshots':(),'complete':False,'word':None}
while net.enabled():net.step(net.enabled()[0]);observe(net)
assert observe(net)['word']==(0,0,1)
report={'passed':True,'read_only_observations':checks,'cases':['conditional true/false with delayed rejected cleanup and successor','ordinary early false','empty program','no-output pending program'],'scope':'Targeted prefix-time checks on constructor-generated nets; not imported-state validation.'}
p=Path(__file__).resolve().parents[1]/'results/program-observation.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
