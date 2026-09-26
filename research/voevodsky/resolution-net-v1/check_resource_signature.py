from pathlib import Path
from itertools import permutations
import json,hashlib
from reference import Rule,Step,map_seeds,unit
from local_net import Net
from resource_signature import seed,consume,join,validate_history,World
s=seed(('a','b','c'),'initial');histories=[]
for order in permutations(('a','b','c')):
 h=s
 for token in order:h=consume(h,token);validate_history(h)
 histories.append(h)
 net=Net(map_seeds(unit,h))
 while net.active():net.rewrite(net.active()[0])
 if net.readback()!=h:raise RuntimeError('resource history lost')
if len(set(histories))!=6 or len({h.package for h in histories})!=1:raise RuntimeError('history/endpoint distinction lost')
a=seed(('a',),'a-origin');b=seed(('b',),'b-origin');spent=consume(a,'a')
rejected=0
for action in (lambda:consume(spent,'a'),lambda:consume(a,'unknown'),lambda:join(a,a),lambda:join(spent,spent),lambda:join(spent,a)):
 try:action()
 except ValueError:rejected+=1
 else:raise RuntimeError('invalid resource use allowed')
valid=join(consume(a,'a'),consume(b,'b'));validate_history(valid)
# Generic endpoint typing alone accepts an invented revival rule. Resource
# signature admission must reject it: uniform syntax is not arbitrary authority.
forged=Step(Rule('revive',(spent.package,),a.package,'invented'),(spent,))
try:validate_history(forged)
except ValueError:rejected+=1
else:raise RuntimeError('forged transition accepted')
# Alternate histories from the same initial world remain admissible.
left=consume(a,'a');right=consume(a,'a')
validate_history(left);validate_history(right)
root=Path(__file__).parent
report={'passed':True,'resource_orders':6,'same_endpoint_distinct_histories':True,'negative_controls':rejected,'disjoint_join_valid':True,'alternate_forks_individually_valid':True,'internal_net_changes':0,'scope':'Finite domain-signature checks plus unchanged local flattening. Footprint separation prevents overlapping branches within one accepted derivation, not competing global commits. String witnesses are not authenticated authority.','source_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ('resource_signature.py','check_resource_signature.py','local_net.py')}}
(root/'results/resource-signature.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
