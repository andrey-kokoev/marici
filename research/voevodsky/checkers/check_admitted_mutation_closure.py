"""Apply exactly one production-engine rewrite to each admitted mutation/redex."""
from contextlib import redirect_stdout
from io import StringIO
from copy import deepcopy
from itertools import combinations
from pathlib import Path
import json
from typed_net_invariant import validate
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay,fixtures
 from check_reachable_family_diamonds import canonical

class StopAfterStep(Exception):pass

def step(net,agent):
 child=deepcopy(net)
 rank=0 if agent.startswith('COPY') else (3 if agent.startswith('E_') else int(agent[1]))
 def policy(history,options):
  if history:raise StopAfterStep()
  assert rank in options
  child.preferred_redex_name=agent
  return (rank,)+tuple(i for i in range(4) if i!=rank)
 before=child.steps
 try:child.run_order(policy)
 except StopAfterStep:pass
 assert child.steps==before+1
 return child

admitted=edges=0;rules={}
for bits,indices in fixtures:
 pending=[()];seen=set()
 while pending:
  prefix=pending.pop();net,choices=replay(bits,indices,prefix)
  key=canonical(net)
  if key in seen:continue
  seen.add(key)
  wires=[(p,q) for p,q in net.wires.items() if p<q]
  for (a,b),(c,d) in combinations(wires,2):
   for x,y in ((c,d),(d,c)):
    altered=deepcopy(net)
    for p,q in ((a,x),(b,y)):altered.wires[p]=q;altered.wires[q]=p
    if validate(altered) is not None:continue
    admitted+=1
    for agent in altered.types:
     if not agent.startswith(('COPY','Q1','Q2','E_')):continue
     peer=altered.wires[agent+'.p'];other,port=peer.split('.')
     if port!='p':continue
     family='COPY' if agent.startswith('COPY') else ('E' if agent.startswith('E_') else 'Q_'+agent[2:].split('_')[0])
     rule=family+'--'+other.split('_')[0]
     child=step(altered,agent)
     assert validate(child) is None,(bits,indices,prefix,(a,b,c,d,x,y),rule,validate(child))
     rules[rule]=rules.get(rule,0)+1;edges+=1
  pending.extend(prefix+(choice,) for choice in choices)
report={'passed':True,'admitted_mutation_instances':admitted,'one_step_edges':edges,'rule_counts':rules,'scope':'One-step production-engine closure for admitted two-wire mutations of four tiny fixture state spaces, not exhaustive typed graphs or universal preservation. Mutations not deduplicated.'}
out=Path(__file__).resolve().parents[1]/'results/admitted-mutation-closure.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
