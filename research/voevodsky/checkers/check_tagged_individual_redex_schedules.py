"""Check runtime type propagation over every small individual-redex choice."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_runtime_original_copy_tags import Tagged
 from check_reachable_family_diamonds import canonical

class Branch(Exception):
 def __init__(self,choices):self.choices=choices

def replay(bits,indices,prefix):
 net=Tagged(bits,*indices)
 def policy(history,options):
  erasers=[name for name in net.types if name.startswith('E_') and net.wires[name+'.p'].split('.')[0].startswith(('N_','B0_','B1_','K_'))]
  choices=tuple((rank,name) for rank in dict.fromkeys(options) for name in (erasers if rank==3 else (None,)))
  if len(history)==len(prefix):raise Branch(choices)
  rank,name=prefix[len(history)];assert (rank,name) in choices
  net.preferred_redex_name=name
  return (rank,)+tuple(x for x in range(4) if x!=rank)
 try:net.run_order(policy)
 except Branch as branch:return net,branch.choices
 return net,()

fixtures=(((),(0,0)),((1,),(0,1)),((1,0),(1,0)),((0,1),(2,2)))
states=arcs=checks=0
for bits,indices in fixtures:
 queue=[()];seen=set()
 while queue:
  prefix=queue.pop();net,choices=replay(bits,indices,prefix)
  key=canonical(net)
  if key in seen:continue
  seen.add(key);net.validate_tags();checks+=net.tag_checks
  for choice in choices:
   child,_=replay(bits,indices,prefix+(choice,))
   child.validate_tags()
   queue.append(prefix+(choice,));arcs+=1
 states+=len(seen)
# Non-head original-tail forgery must fail before any rewrite.
forged=Tagged((0,1),0,0);tail=forged.origin[1]
forged.tags[tail]='COPIED'
try:forged.validate_tags()
except AssertionError:pass
else:raise AssertionError('forged original tail accepted')
report={'passed':True,'fixtures':len(fixtures),'alpha_states':states,'transitions':arcs,'replay_tag_checks':checks,'nonhead_original_tail_forgery':'rejected','scope':'Four tiny fixtures under all individually enabled redex choices, not arbitrary-n grammar proof.'}
out=Path(__file__).resolve().parents[1]/'results/tagged-individual-redex-schedules.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
