"""Enumerate all observed rule cases and audit progress premises on each edge."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay
 from check_reachable_family_diamonds import canonical
 from check_rooted_component_coverage import rooted
 from check_recursive_tail_endpoints import valid as tails
 from check_original_chain_all_tiny_schedules import originals,owns
 from check_copy_frontier_branch_anchors import anchored

cases={};states=arcs=0
for n in range(3):
 for bits in product((0,1),repeat=n):
  for indices in product(range(n+3),repeat=2):
   initial,_=replay(bits,indices,());origin=originals(initial)
   pending=[()];seen=set()
   while pending:
    prefix=pending.pop();net,choices=replay(bits,indices,prefix)
    key=canonical(net)
    if key in seen:continue
    seen.add(key)
    assert rooted(net) and tails(net) and owns(net,origin) and anchored(net)
    for rank,eraser in choices:
     if rank==0:agent=next(name for name in net.types if name.startswith('COPY'))
     elif rank in (1,2):agent=next(name for name in net.types if name.startswith('Q'+str(rank)))
     else:agent=eraser
     other=net.wires[agent+'.p'].split('.')[0]
     family='COPY' if rank==0 else ('E' if rank==3 else 'Q_'+agent[2:].split('_')[0])
     head=other.split('_')[0]
     pair=(family,head);cases[pair]=cases.get(pair,0)+1
     child,_=replay(bits,indices,prefix+((rank,eraser),))
     assert rooted(child) and tails(child) and owns(child,origin) and anchored(child),(pair,bits,indices,prefix)
     arcs+=1;pending.append(prefix+((rank,eraser),))
   states+=len(seen)
expected={(f,h) for f,heads in {'COPY':('B0','B1','N'),'Q_B':('K','N'),'Q_S':('B0','B1','N'),'Q_R':('B0','B1','N'),'E':('B0','B1','K','N')}.items() for h in heads}
assert set(cases)==expected,(set(cases)^expected)
report={'passed':True,'states':states,'transitions':arcs,'rule_cases':{str(k):v for k,v in sorted(cases.items())},'finding':'All 15 rule pairs occur; before/after root coverage, phase/finite-tail typing, original suffix ownership, and independent COPY branch anchors hold on all tiny reachable edges.','scope':'Finite instantiated-edge ledger, not universal rule-template preservation over arbitrary typed boundary contexts.'}
out=Path(__file__).resolve().parents[1]/'results/progress-premise-rule-ledger.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
