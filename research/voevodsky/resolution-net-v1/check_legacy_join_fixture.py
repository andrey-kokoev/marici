"""Compare only the four-READY binary-join suffix, not upstream cleanup."""
from pathlib import Path
from copy import deepcopy
import sys,json,hashlib
from reference import Package,Admission,Rule,Step,unit,map_seeds
from local_net import Net
root=Path(__file__).parent;legacy=root.parent/'checkers';sys.path.insert(0,str(legacy))
from four_cell_completion_barrier_net import BarrierNet

def old_fixture():
 net=BarrierNet();leaves=[net.add('READY',str(i)) for i in range(4)];lower=[]
 for i in (0,2):
  j=net.add('JOIN');net.link((j,'p'),(leaves[i],'p'));net.link((j,'a'),(leaves[i+1],'p'));lower.append(j)
 top=net.add('JOIN');end=net.add('BARRIER')
 net.link((top,'p'),(lower[0],'o'));net.link((top,'a'),(lower[1],'o'));net.link((top,'o'),(end,'p'));net.validate();return net

def package(tokens):return Package('released',tuple(tokens))
leaves=[unit(Admission(package((str(i),)),f'actual-READY-{i}')) for i in range(4)]
def join(left,right,name):
 # Domain logic belongs in this explicit adapter, not the uniform net engine.
 if set(left.package.data)&set(right.package.data):raise ValueError('duplicate release ownership')
 output=package(left.package.data+right.package.data)
 return Step(Rule('binary-release-join',(left.package,right.package),output,name),(left,right))
expected=join(join(leaves[0],leaves[1],'join01'),join(leaves[2],leaves[3],'join23'),'join0123')
new_input=map_seeds(unit,expected)
counts={'legacy_schedules':0,'new_schedules':0};legacy_lengths=set();new_lengths=set()
def explore_old(net,n=0):
 active=net.enabled()
 if not active:
  assert net.observe_barrier()==((),True)
  assert sorted(k for k,_ in net.nodes.values())==['BARRIER','READY']
  counts['legacy_schedules']+=1;legacy_lengths.add(n);return
 assert not net.observe_barrier()[1]
 for pair in active:
  child=deepcopy(net);child.step(pair);explore_old(child,n+1)
def explore_new(net,n=0):
 active=net.active()
 if not active:
  assert net.readback()==expected
  counts['new_schedules']+=1;new_lengths.add(n);return
 for pair in active:
  child=deepcopy(net);child.rewrite(pair);explore_new(child,n+1)
explore_old(old_fixture());explore_new(Net(new_input))
assert legacy_lengths=={6} and new_lengths=={7}
try:join(leaves[0],leaves[0],'duplicated')
except ValueError:pass
else:raise AssertionError('adapter must reject duplicate ownership')
# Missing evidence is not synthesized: the translator requires four admissions.
def translate(admissions):
 if len(admissions)!=4:raise ValueError('four READY witnesses required')
 if [x.package.data for x in admissions]!=[(str(i),) for i in range(4)]:raise ValueError('wrong release boundary')
 return join(join(admissions[0],admissions[1],'join01'),join(admissions[2],admissions[3],'join23'),'join0123')
assert translate(leaves)==expected
for missing in range(4):
 try:translate(leaves[:missing]+leaves[missing+1:])
 except ValueError:pass
 else:raise AssertionError('missing release accepted')
report={'passed':True,**counts,'legacy_rewrites_per_schedule':6,'new_rewrites_per_schedule':7,'legacy_suffix_agent_kinds':['READY','JOIN','HOLD','BARRIER'],'new_agent_signatures':['flatten/1','seed/0','seed/1','step/1','step/2'],'new_domain_rule_instances':3,'new_domain_rule_schemas':1,'comparison':'Same completed release boundary for a fixture already possessing four READY admissions; new history additionally retains their individual witnesses and join tree. Not bisimulation of intermediate readiness or translation of upstream DONE/cleanup ownership.','conclusion':'Domain JOIN/HOLD execution is represented as witnessed binary-rule data, but total primitive count and rewrite count do not improve on this tiny suffix. Uniformity benefit remains a cross-domain hypothesis.','source_sha256':{str(p.relative_to(root.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (legacy/'four_cell_completion_barrier_net.py',Path(__file__),root/'local_net.py',root/'reference.py')}}
(root/'results/legacy-join-fixture.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
