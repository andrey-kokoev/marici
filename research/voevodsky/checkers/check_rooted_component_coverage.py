"""Every live component must be rooted in an output or active eraser."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay,fixtures
 from check_reachable_family_diamonds import canonical
 from check_recursive_tail_endpoints import valid as tails
 from check_full_unary_query_port_graph import Net

def components(net):
 adj={name:set() for name in net.types}
 for p,q in net.wires.items():
  a=p.split('.')[0];b=q.split('.')[0];adj[a].add(b);adj[b].add(a)
 unseen=set(adj);groups=[]
 while unseen:
  queue=[next(iter(unseen))];group=set()
  for node in queue:
   if node in group:continue
   group.add(node);queue.extend(adj[node]-group)
  unseen-=group;groups.append(group)
 return groups

def rooted(net):
 groups=components(net)
 if not all(any(x in ('OUT1','OUT2') or x.startswith('E_') for x in group) for group in groups):return False
 for i in (1,2):
  head=net.wires['OUT'+str(i)+'.p'].split('.')[0]
  if not (head.startswith(('Q'+str(i),'TRUE_','FALSE_'))):return False
 return True

states=arcs=detached=0
for bits,indices in fixtures:
 queue=[()];seen=set()
 while queue:
  prefix=queue.pop();net,choices=replay(bits,indices,prefix)
  key=canonical(net)
  if key in seen:continue
  seen.add(key);assert tails(net) and rooted(net),(bits,indices,prefix)
  detached+=sum(1 for g in components(net) if not any(x in ('OUT1','OUT2') for x in g))
  for choice in choices:
   child,_=replay(bits,indices,prefix+(choice,));assert rooted(child)
   queue.append(prefix+(choice,));arcs+=1
 states+=len(seen)
# Locally typed tail with no OUT, E, Q or COPY root is a stuck component.
mal=Net.__new__(Net);mal.types={};mal.wires={};mal.serial=0;mal.steps=0
for name,ports in (('B0_1',('p','a')),('N_1',('p',)),('N_2',('p',))):mal.add(name,ports)
mal.link('B0_1.a','N_1.p');mal.link('B0_1.p','N_2.p');mal.audit()
assert not all(any(x in ('OUT1','OUT2') or x.startswith('E_') for x in g) for g in components(mal))
report={'passed':True,'states':states,'transitions':arcs,'detached_component_instances':detached,'malformed_fully_wired_bit_tail':'rejected: no OUT or E root','scope':'Root coverage on four tiny reachable inputs; root membership alone is insufficient for an arbitrary-n no-stuck theorem.'}
out=Path(__file__).resolve().parents[1]/'results/rooted-component-coverage.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
