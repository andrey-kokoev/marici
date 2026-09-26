from fuel_scanner import FuelScanner
from copy import deepcopy
checks=0
for bits,c,f,tag in [((1,),0,4,'FOUND'),((),3,0,'EXHAUSTED')]:
 net=FuelScanner(bits,c,f)
 assert net.observe()=={'outcome':None,'complete':False,'word':None}
 while net.observe()['outcome'] is None:net.step(net.enabled()[0])
 before=deepcopy(net.__dict__)
 assert net.observe()=={'outcome':tag,'complete':False,'word':None}
 assert before==net.__dict__ and any(net.kind(x)=='EA' for x in net.enabled())
 while net.enabled():
  assert net.observe()['outcome']==tag and not net.observe()['complete']
  net.step(net.enabled()[0]);checks+=1
 assert net.observe()=={'outcome':tag,'complete':True,'word':bits}
print({'passed':True,'terminal_cleanup_steps_observed':checks,'cases':2})
