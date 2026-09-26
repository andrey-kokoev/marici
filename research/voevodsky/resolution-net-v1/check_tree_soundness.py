"""Finite executable checks of the structural soundness argument."""
from pathlib import Path
from copy import deepcopy
from dataclasses import replace
import hashlib,json
from reference import Package, Admission, Rule, Step, unit, flatten
from local_net import Net
from tree_audit import audit,outer_size
p=Package('P');s=unit(Admission(p,'seed'));u=Rule('u',(p,),p,'u');v=Rule('v',(p,p),p,'v')
fixtures=[unit(s),Step(u,(unit(s),)),Step(v,(unit(s),unit(s))),Step(v,(Step(u,(unit(s),)),Step(u,(unit(s),)))),Step(v,(unit(Step(u,(s,))),unit(Step(v,(s,s)))))]
states=steps=diamonds=leaves=0
for h in fixtures:
 expected=flatten(h)
 def visit(net):
  global states,steps,diamonds,leaves
  value,cost,syntax=audit(net);states+=1;assert value==expected
  pairs=net.active()
  assert (cost==0)==(len(pairs)==0)
  for index,first in enumerate(pairs):
   for second in pairs[index+1:]:
    left=deepcopy(net);left.rewrite(first);assert second in left.active();left.rewrite(second)
    right=deepcopy(net);right.rewrite(second);assert first in right.active();right.rewrite(first)
    assert audit(left)==audit(right);diamonds+=1
  if not pairs:
   assert net.readback()==expected;leaves+=1
  for pair in pairs:
   child=deepcopy(net);child.rewrite(pair)
   assert audit(child)[1]==cost-1;steps+=1;visit(child)
 net=Net(h);assert audit(net)[1]==outer_size(h);visit(net)
# Payload mutations must now fail integrated typed admission.
mutations=[]
net=Net(Step(u,(unit(s),)));f,d=net.active()[0]
for node,changes in ((f,{'level':0}),(d,{'level':8}),(d,{'kind':'unknown'}),(d,{'payload':Rule('wrong',(Package('Q'),),p,'bad')})):
 bad=deepcopy(net);bad.agents[node]=replace(bad.agents[node],**changes);mutations.append(bad)
rejected=0
for bad in mutations:
 try:audit(bad)
 except (ValueError,TypeError):rejected+=1
 else:raise AssertionError('malformed typed net accepted')
root=Path(__file__).parent
report={'passed':True,'states':states,'single_step_checks':steps,'local_diamonds':diamonds,'terminal_paths':leaves,'typed_mutations_rejected':rejected,'source_sha256':{n:hashlib.sha256((root/n).read_bytes()).hexdigest() for n in ('reference.py','local_net.py','tree_audit.py','check_tree_soundness.py')},'scope':'Finite checks of pending-work decrease, semantic simulation, identifier-independent local diamonds, and separate typed admission. General tree-class argument is in tree-soundness.md; not machine-checked universal proof or shared-net semantics.'}
(root/'results/tree-soundness.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
