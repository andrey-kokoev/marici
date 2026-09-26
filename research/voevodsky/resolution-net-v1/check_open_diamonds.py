from copy import deepcopy
from pathlib import Path
import json,hashlib,itertools
from reference import Package,Admission,Rule,Step,unit
from pending import Hole,Branch
from open_net import OpenNet
from open_observer import encode,substitute,observe
p=Package('P');u=Rule('u',(p,),p,'u');v=Rule('v',(p,p),p,'v')
contexts=[Hole('a',p),Branch(v,(Hole('a',p),Hole('b',p))),Branch(v,(Branch(u,(Hole('a',p),)),Hole('b',p)))]
inputs={slot:Step(u,(unit(Admission(p,'evidence-'+slot)),)) for slot in ('a','b')}
counts={'states':0,'steps':0,'RR':0,'RA':0,'AA':0,'AA_distinct_receipt_orders':0,'adjacent_RA':0}
def events(net):return [('R',pair) for pair in net.active()]+[('A',slot) for slot,_ in net.boundaries.values()]
def apply(net,event):
 kind,value=event
 if kind=='R':net.rewrite(value)
 else:net.arrive(value,'ticket-'+value,inputs[value])
for context in contexts:
 start=OpenNet(context);expected=substitute(observe(start)['denotation'],inputs)
 def explore(net):
  before=observe(net);counts['states']+=1
  if substitute(before['denotation'],inputs)!=expected:raise RuntimeError('substitution simulation failed')
  if before['released']!=(not before['missing'] and before['pending_work']==0):raise RuntimeError('availability invariant')
  actions=events(net)
  for first,second in itertools.combinations(actions,2):
   left=deepcopy(net);apply(left,first);apply(left,second)
   right=deepcopy(net);apply(right,second);apply(right,first)
   l,r=observe(left),observe(right)
   for field in ('shape','denotation','missing','pending_work','released'):
    if l[field]!=r[field]:raise RuntimeError(('diamond',field,first,second))
   category='AA' if first[0]==second[0]=='A' else ('RR' if first[0]==second[0]=='R' else 'RA')
   counts[category]+=1
   if category=='AA':
    if l['receipts']==r['receipts']:raise RuntimeError('receipt histories accidentally identified')
    if {x[0]:x[1:] for x in l['receipts']}!={x[0]:x[1:] for x in r['receipts']}:raise RuntimeError('receipt maps differ')
    counts['AA_distinct_receipt_orders']+=1
   elif l['receipts']!=r['receipts']:raise RuntimeError('non-arrival reorder changed receipts')
   if category=='RA':
    rewrite=first if first[0]=='R' else second;arrival=second if first[0]=='R' else first
    d=rewrite[1][1]
    boundary=next(i for i,(slot,_) in net.boundaries.items() if slot==arrival[1])
    if net.agents[d].kind=='seed' and net.wires[d,1]==(boundary,0):counts['adjacent_RA']+=1
  for event in actions:
   child=deepcopy(net);apply(child,event);after=observe(child)
   if after['pending_work']+len(after['missing'])!=before['pending_work']+len(before['missing'])-1:raise RuntimeError('event measure failed')
   if event[0]=='R' and after['denotation']!=before['denotation']:raise RuntimeError('rewrite changed denotation')
   if event[0]=='A' and after['denotation']!=substitute(before['denotation'],{event[1]:inputs[event[1]]}):raise RuntimeError('arrival not substitution')
   counts['steps']+=1;explore(child)
 explore(start)
if not counts['adjacent_RA']:raise RuntimeError('critical adjacent case not exercised')
root=Path(__file__).parent
report={'passed':True,**counts,'scope':'Bounded open-event critical diamonds modulo IDs; AA agrees on shape/assignment but NOT receipt chronology. Fixed pure inputs and distinct slots/tickets only. Written general argument separate.','source_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ('open_net.py','open_observer.py','check_open_diamonds.py','admission.py','local_net.py')}}
(root/'results/open-diamonds.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
