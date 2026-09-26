"""Search for stuck nonterminal states under the directed typed-root conditions."""
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

def enabled(net):
 found=[]
 for name in net.types:
  if not name.startswith(('COPY','Q1','Q2','E_')):continue
  peer=net.wires[name+'.p'];other=peer.split('.')[0]
  if peer.split('.')[1]!='p':continue
  if name.startswith('COPY') and other.startswith(('B0_','B1_','N_')):found.append(name)
  elif name.startswith(('Q1','Q2')):
   phase=name[2:].split('_')[0]
   types={'B':('K_','N_'),'S':('B0_','B1_','N_'),'R':('B0_','B1_','N_')}
   if other.startswith(types[phase]):found.append(name)
  elif name.startswith('E_') and other.startswith(('B0_','B1_','K_','N_')):found.append(name)
 return found

states=arcs=waiting_only=0;terminal=0
for n in range(3):
 for bits in product((0,1),repeat=n):
  for indices in product(range(n+2),repeat=2):
   queue=[()];seen=set()
   while queue:
    prefix=queue.pop();net,choices=replay(bits,indices,prefix)
    key=canonical(net)
    if key in seen:continue
    seen.add(key)
    assert rooted(net) and tails(net)
    active=enabled(net)
    if not active:
     assert len(net.types)==4 and all(net.wires['OUT'+str(i)+'.p'].startswith(('TRUE_','FALSE_')) for i in (1,2)),(bits,indices,prefix)
     terminal+=1
    else:
     assert choices
     if all(net.wires[name+'.p'].split('.')[0].startswith('COPY') for name in net.types if name.startswith(('Q1','Q2','E_'))):waiting_only+=1
    for c in choices:
     child,_=replay(bits,indices,prefix+(c,));assert rooted(child) and tails(child)
     arcs+=1;queue.append(prefix+(c,))
   states+=len(seen)
report={'passed':True,'alpha_states':states,'transitions':arcs,'terminal_classes_counted_per_input':terminal,'all_query_eraser_principals_waiting_states':waiting_only,'finding':'in every reachable checked state with no typed active pair both outputs are BOOL and only four agents remain','scope':'All individual redex schedules n<=2, not a proof that local typing and rooting alone force arbitrary-n progress.'}
out=Path(__file__).resolve().parents[1]/'results/rooted-nonterminal-progress.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
