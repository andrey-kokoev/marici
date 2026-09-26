from pathlib import Path
from itertools import permutations
from dataclasses import replace
import json,hashlib
from pending import Hole,Branch,Pending
from reference import Package,Admission,Rule,unit,map_seeds
from local_net import Net
p=[Package('release',(str(i),)) for i in range(4)]
def branch(left,right,name):
 def endpoint(x):return x.package if isinstance(x,Hole) else x.rule.output
 a,b=endpoint(left),endpoint(right)
 return Branch(Rule('join',(a,b),Package('release',a.data+b.data),name),(left,right))
holes=[Hole(str(i),p[i]) for i in range(4)]
context=branch(branch(holes[0],holes[1],'01'),branch(holes[2],holes[3],'23'),'0123')
initial=Pending(context);expected=None;prefixes=0;orders=0
for order in permutations(range(4)):
 current=initial
 for count,i in enumerate(order):
  before=current
  try:current.materialize()
  except ValueError:prefixes+=1
  else:raise RuntimeError('premature release')
  current=current.accept(str(i),'ticket-'+str(i),Admission(p[i],'READY-'+str(i)))
  if len(before.receipts)!=count:raise RuntimeError('mutated old revision')
 result=current.materialize()
 if expected is None:expected=result
 if result!=expected:raise RuntimeError('arrival order changed resolution history')
 net=Net(map_seeds(unit,result))
 while net.active():net.rewrite(net.active()[0])
 if net.readback()!=expected:raise RuntimeError('closed net result differs')
 orders+=1
# Each pair of distinct seed insertions commutes observationally (receipt chronology remains).
x=initial.accept('0','t0',Admission(p[0],'w0')).accept('1','t1',Admission(p[1],'w1'))
y=initial.accept('1','t1',Admission(p[1],'w1')).accept('0','t0',Admission(p[0],'w0'))
if x==y or x.missing()!=y.missing():raise RuntimeError('chronology lost or availability inconsistent')
base=initial.accept('0','t0',Admission(p[0],'w0'));rejected=0
for operation in (lambda:base.accept('0','new',Admission(p[0],'w0')),lambda:base.accept('1','t0',Admission(p[1],'w1')),lambda:base.accept('1','t1',Admission(p[0],'wrong')),lambda:base.accept('unknown','t2',Admission(p[1],'w1')),lambda:Pending(branch(holes[0],holes[0],'aliased')),lambda:base.materialize()):
 try:operation()
 except ValueError:rejected+=1
 else:raise RuntimeError('invalid admission accepted')
if len(base.receipts)!=1:raise RuntimeError('failure mutated state')
root=Path(__file__).parent
report={'passed':True,'arrival_orders':orders,'incomplete_prefixes_rejected':prefixes,'negative_controls':rejected,'receipt_chronology_retained':True,'additional_net_agent_signatures':0,'scope':'External incremental evidence contexts with closed-net materialization only after all admissions. No interleaving of rewrites with arrivals, no global ticket authority or authentication, no automatic rule-witness construction.','source_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ('pending.py','check_pending.py','reference.py','local_net.py','admission.py')}}
(root/'results/pending.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
