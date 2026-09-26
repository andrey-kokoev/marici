from copy import deepcopy
from pathlib import Path
import json,random,hashlib
from reference import Package,Admission,Rule,Step,unit
from pending import Hole,Branch
from open_net import OpenNet
p=Package('P');u=Rule('u',(p,),p,'u');v=Rule('v',(p,p),p,'v')
def context(n):
 holes=[Hole(str(i),p) for i in range(n)]
 if n==2:return Branch(v,tuple(holes))
 return Branch(v,(Branch(v,tuple(holes[:2])),Branch(v,tuple(holes[2:]))))
def evidence(i):return Step(u,(unit(Admission(p,'proof-'+i)),))
def expected(n):
 h=[evidence(str(i)) for i in range(n)]
 return Step(v,tuple(h)) if n==2 else Step(v,(Step(v,tuple(h[:2])),Step(v,tuple(h[2:]))))
def choices(net):return [('rewrite',pair) for pair in net.active()]+[('arrive',slot) for slot,_ in net.boundaries.values()]
def apply(net,event):
 kind,value=event
 if kind=='rewrite':net.rewrite(value)
 else:net.arrive(value,'ticket-'+value,evidence(value))
paths=states=0

def explore(net):
 global paths,states
 states+=1
 events=choices(net)
 if not events:
  if not net.released() or net.readback()!=expected(2):raise RuntimeError('wrong terminal state')
  paths+=1;return
 if net.released():raise RuntimeError('premature release')
 for event in events:
  child=deepcopy(net);apply(child,event);explore(child)
explore(OpenNet(context(2)))
rng=random.Random(107)
for trial in range(200):
 net=OpenNet(context(4));steps=0;arrivals=0
 while choices(net):
  event=rng.choice(choices(net));apply(net,event)
  steps+=event[0]=='rewrite';arrivals+=event[0]=='arrive'
 if net.readback()!=expected(4) or steps!=7 or arrivals!=4:raise RuntimeError('schedule failure')
# Normalize completely with no evidence: normal but NOT released.
net=OpenNet(context(4))
while net.active():net.rewrite(net.active()[0])
if net.released() or len(net.boundaries)!=4:raise RuntimeError('normality conflated with release')
try:net.readback()
except ValueError:pass
else:raise RuntimeError('readback accepted holes')
# Inserting a pure history after normalization must not create more F work.
for i in range(4):net.arrive(str(i),'ticket-'+str(i),evidence(str(i)))
if net.active() or net.readback()!=expected(4):raise RuntimeError('late splice wrong')
# Failure leaves all stores/receipts unchanged.
rejected=0
for op in (lambda:net.arrive('0','new',evidence('0')),lambda:net.arrive('missing','ticket-0',evidence('0'))):
 before=deepcopy(net.__dict__)
 try:op()
 except ValueError:rejected+=1
 else:raise RuntimeError('invalid arrival accepted')
 if net.__dict__!=before:raise RuntimeError('failed arrival mutated state')
wrong=OpenNet(context(2));before=deepcopy(wrong.__dict__)
try:wrong.arrive('0','t',Admission(Package('Q'),'wrong'))
except ValueError:rejected+=1
else:raise RuntimeError('wrong package accepted')
if wrong.__dict__!=before:raise RuntimeError('wrong package mutated net')
root=Path(__file__).parent
report={'passed':True,'exhaustive_two_slot_paths':paths,'exhaustive_states':states,'four_slot_random_schedules':200,'normal_without_release_verified':True,'atomic_arrival_rejections':rejected,'new_agent_signatures':0,'new_local_rewrite_schemas':0,'new_boundary_operations':1,'source_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ('open_net.py','admission.py','local_net.py','pending.py','check_open_net.py')},'scope':'Mixed arrivals and structural rewrites for typed tree interfaces. Pure level0 history insertion only; release observer, not emitted linear token. No global ticket authority or general open-net confluence certification.'}
(root/'results/open-net.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
