"""Probe an inductive candidate: every connected agent-component is a tree."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_individual_eraser_alpha_states import replay
 from check_reachable_family_diamonds import canonical

def forest(net):
 adjacency={n:set() for n in net.types};edges=set()
 for port,peer in net.wires.items():
  a=port.split('.')[0];b=peer.split('.')[0]
  if a==b:return False
  adjacency[a].add(b);adjacency[b].add(a)
  edges.add(frozenset((a,b)))
 # Port incidence already checked by net.audit; no multiple interagent wires.
 if len(edges)*2!=sum(len(x) for x in adjacency.values()):return False
 unseen=set(adjacency)
 while unseen:
  root=next(iter(unseen));queue=[root];component=set()
  for name in queue:
   if name in component:continue
   component.add(name);queue.extend(adjacency[name]-component)
  unseen-=component
  if sum(len(adjacency[x]) for x in component)//2!=len(component)-1:return False
 return True

fixtures=(((),(0,0)),((1,),(0,1)),((1,0),(1,0)),((0,1),(2,2)))
counts=[]
for bits,indices in fixtures:
 pending=[()];seen=set();transitions=0
 while pending:
  prefix=pending.pop();net,choices=replay(bits,indices,prefix)
  state=canonical(net)
  if state in seen:continue
  seen.add(state);net.audit()
  assert forest(net),(bits,indices,prefix)
  # The only active-principal candidates in this prototype are typed
  # COPY, Q1, Q2 and E. Bool/OUT have no reduction rule.
  assert sum(x.startswith('COPY') for x in net.types)<=1
  assert sum(x.startswith('Q1') for x in net.types)<=1
  assert sum(x.startswith('Q2') for x in net.types)<=1
  for choice in choices:
   pending.append(prefix+(choice,));transitions+=1
 counts.append({'bits':bits,'indices':indices,'alpha_states':len(seen),'edges':transitions})
report={'passed':True,'fixtures':counts,'candidate_invariant':'agent-level graph is a forest; one COPY and at most one Q per output; linear ports','scope':'Checked reachable alpha states of four tiny inputs with individual eraser choices; preservation for arbitrary n and all well-typed forests not established.'}
out=Path(__file__).resolve().parents[1]/'results/reachable-net-forest-invariant.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
