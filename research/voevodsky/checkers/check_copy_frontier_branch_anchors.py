"""Each COPY output-side component must have its own OUT or ERASE root."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay
 from check_reachable_family_diamonds import canonical

def anchored(net):
 copiers=[x for x in net.types if x.startswith('COPY')]
 if not copiers:return True
 assert len(copiers)==1
 copy=copiers[0]
 adj={x:set() for x in net.types if x!=copy}
 for p,q in net.wires.items():
  a=p.split('.')[0];b=q.split('.')[0]
  if copy in (a,b):continue
  adj[a].add(b);adj[b].add(a)
 sides=[]
 for port in ('a','b'):
  start=net.wires[copy+'.'+port].split('.')[0]
  seen=set();queue=[start]
  while queue:
   x=queue.pop()
   if x in seen:continue
   seen.add(x);queue.extend(adj[x]-seen)
  if not any(x in ('OUT1','OUT2') or x.startswith('E_') for x in seen):return False
  sides.append(seen)
 return sides[0].isdisjoint(sides[1])

# Rebuild the previous counterexample before its COPY--NIL rewrite.
from check_full_unary_query_port_graph import Net
pre=Net.__new__(Net);pre.types={};pre.wires={};pre.serial=0;pre.steps=0
for name,ps in (('COPY',('p','a','b')),('N_1',('p',)),('B0_1',('p','a')),('N_2',('p',)),('E_1',('p',)),('OUT1',('p',)),('OUT2',('p',)),('TRUE_1',('p',)),('FALSE_1',('p',))):pre.add(name,ps)
for a,b in (('COPY.p','N_1.p'),('COPY.a','B0_1.a'),('COPY.b','E_1.p'),('B0_1.p','N_2.p'),('OUT1.p','TRUE_1.p'),('OUT2.p','FALSE_1.p')):pre.link(a,b)
assert not anchored(pre)
fixtures=states=arcs=frontiers=0
for n in range(3):
 for bits in product((0,1),repeat=n):
  for indices in product(range(n+2),repeat=2):
   fixtures+=1;queue=[()];seen=set()
   while queue:
    prefix=queue.pop();net,choices=replay(bits,indices,prefix)
    key=canonical(net)
    if key in seen:continue
    seen.add(key);assert anchored(net),(bits,indices,prefix)
    frontiers+=any(x.startswith('COPY') for x in net.types)
    for c in choices:
     child,_=replay(bits,indices,prefix+(c,));assert anchored(child)
     queue.append(prefix+(c,));arcs+=1
   states+=len(seen)
report={'passed':True,'fixtures':fixtures,'alpha_states':states,'transitions':arcs,'live_copy_frontier_states':frontiers,'malformed_rooted_forest':'rejected by side-branch anchor','condition':'after cutting COPY, the a and b sides are disjoint and each contains OUT or ERASE','scope':'All small individual-redex choices n<=2, not symbolic preservation for arbitrary-n or all typed context graphs.'}
out=Path(__file__).resolve().parents[1]/'results/copy-frontier-branch-anchors.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
