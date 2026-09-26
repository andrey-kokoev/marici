from pathlib import Path
from copy import deepcopy
import hashlib,json,random
from reference import Package, Admission, Rule, Step, unit, flatten, map_seeds
from local_net import Net
p=Package('P',('payload',));s=unit(Admission(p,'seed'))
u=Rule('u',(p,),p,'witness-u');u2=Rule('u',(p,),p,'other-witness');v=Rule('v',(p,p),p,'witness-v')
a=Step(u,(s,));b=Step(u2,(s,))
fixture=Step(v,(Step(u,(unit(a),)),Step(u2,(unit(b),))))
# Readback compared with reference only outside the evaluator.
normal=flatten(fixture);leaves=0;transitions=0

def explore(net):
 global leaves,transitions
 pairs=net.active()
 if not pairs:
  assert net.readback()==normal;leaves+=1;return
 for pair in pairs:
  child=deepcopy(net);child.rewrite(pair);transitions+=1;explore(child)
explore(Net(fixture))

rng=random.Random(101);runs=0;steps=0
base=[s,a,b,Step(v,(a,b))]
for x in base:
 for y in base:
  for history in (unit(Step(v,(x,y))),Step(v,(unit(x),unit(y))),map_seeds(unit,Step(v,(x,y))),unit(unit(Step(v,(x,y))))):
   for trial in range(10):
    net=Net(history)
    while net.active():net.rewrite(rng.choice(net.active()));steps+=1
    assert net.readback()==flatten(history);runs+=1
inside=unit(a);outside=Step(u,(unit(s),))
assert inside!=outside
for history in (inside,outside):
 net=Net(history)
 while net.active():net.rewrite(net.active()[0])
 assert net.readback()==a
# Local cut safety: refuse an occupied-port wire and premature readback.
net=Net(fixture);negative=0
for action in (lambda:net.connect((0,0),(0,0)),lambda:net.readback(),lambda:Net(s)):
 try:action()
 except ValueError:negative+=1
 else:raise AssertionError('invalid action accepted')
root=Path(__file__).parent
report={'passed':True,'exhaustive_fixture_schedules':leaves,'exhaustive_transitions':transitions,'randomized_runs':runs,'randomized_transitions':steps,'negative_controls':negative,'agent_signatures':['flatten/1','seed/0','seed/1','step/1','step/2'],'local_rewrite_schemas':3,'no_reference_flatten_calls_in_evaluator': 'flatten(' not in (root/'local_net.py').read_text(),'source_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ('reference.py','local_net.py','check_local_net.py')},'scope':'Tree-port prototype, bounded schedule simulation and ownership checks. Not a general confluence theorem, dependent-type validation, sharing calculus or legacy equivalence.'}
assert report['no_reference_flatten_calls_in_evaluator']
(root/'results/local-net.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
