from copy import deepcopy
from pathlib import Path
import json,hashlib
from reference import Package,Admission,Rule,Step,unit,map_seeds
from local_net import Net
from port_refinement import reify,diagram
p=Package('P');s=unit(Admission(p,'proof'));u=Rule('u',(p,),p,'u');v=Rule('v',(p,p),p,'v')
a=Step(u,(s,));b=Step(v,(s,a))
fixtures=[unit(s),unit(a),unit(b),map_seeds(unit,b),Step(v,(Step(u,(unit(a),)),Step(u,(unit(b),)))),unit(unit(b))]
counts={'states':0,'steps':0,'F-seed':0,'F-unary':0,'F-binary':0,'compression_cases':0,'contextual_steps':0}
for history in fixtures:
 def explore(net):
  counts['states']+=1;term,paths=reify(net)
  if set(paths)!={pair[0] for pair in net.active()}:raise RuntimeError('active/pending correspondence failed')
  for pair in net.active():
   after=deepcopy(net);after.rewrite(pair);certificate=diagram(net,pair,after)
   counts['steps']+=1;counts[certificate['rule']]+=1
   counts['compression_cases']+=certificate['pure_compression_required'];counts['contextual_steps']+=bool(certificate['context_path'])
   explore(after)
 explore(Net(history))
# A type-correct wrong witness change is invisible to endpoint-only checking.
before=Net(unit(a));pair=before.active()[0];after=deepcopy(before);after.rewrite(pair)
from dataclasses import replace
for node,agent in after.agents.items():
 if agent.kind=='step':
  bad_rule=Rule(agent.payload.name,agent.payload.inputs,agent.payload.output,'wrong witness')
  after.agents[node]=replace(agent,payload=bad_rule);break
after.validate()
try:diagram(before,pair,after)
except ValueError:pass
else:raise RuntimeError('witness corruption escaped refinement check')
if not counts['compression_cases'] or not counts['contextual_steps']:raise RuntimeError('missing coverage')
root=Path(__file__).parent
report={'passed':True,**counts,'wrong_witness_mutation_rejected':True,'scope':'Executable one-step diagrams for reachable closed tree fixtures: reify(actual wire step)=compact(abstract contextual step). Pure compression explicit. Not a universal formal proof of Python implementation.','source_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ('port_refinement.py','check_port_refinement.py','local_net.py','admission.py','reference.py')}}
(root/'results/port-refinement.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
