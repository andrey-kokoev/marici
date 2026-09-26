"""Count port wires individually: parallel agent edges are cycles, not sets."""
import json
from pathlib import Path

def forest(net):
 net.audit()
 parent={n:n for n in net.types}
 def root(n):
  while parent[n]!=n:
   parent[n]=parent[parent[n]];n=parent[n]
  return n
 seen=set()
 for p,q in net.wires.items():
  edge=tuple(sorted((p,q)))
  if edge in seen:continue
  seen.add(edge)
  a=root(p.split('.')[0]);b=root(q.split('.')[0])
  if a==b:return False
  parent[a]=b
 return True

if __name__=='__main__':
 from contextlib import redirect_stdout
 from io import StringIO
 with redirect_stdout(StringIO()):
  from check_tagged_individual_redex_schedules import replay,fixtures
  from check_reachable_family_diamonds import canonical
  from check_full_unary_query_port_graph import Net
 def graph(agents,edges):
  net=Net.__new__(Net);net.types={};net.wires={}
  for n,ps in agents:net.add(n,ps)
  for a,b in edges:net.link(a,b)
  return net
 parallel=graph([('B0_1',('p','a')),('B1_2',('p','a'))],[('B0_1.p','B1_2.p'),('B0_1.a','B1_2.a')])
 loop=graph([('B0_1',('p','a'))],[('B0_1.p','B0_1.a')])
 tree=graph([('E_1',('p',)),('N_1',('p',))],[('E_1.p','N_1.p')])
 assert not forest(parallel) and not forest(loop) and forest(tree)
 states=edges=0
 for bits,indices in fixtures:
  pending=[()];seen=set()
  while pending:
   prefix=pending.pop();net,choices=replay(bits,indices,prefix)
   key=canonical(net)
   if key in seen:continue
   seen.add(key);assert forest(net)
   for choice in choices:
    child,_=replay(bits,indices,prefix+(choice,));assert forest(child)
    pending.append(prefix+(choice,));edges+=1
  states+=len(seen)
 report={'passed':True,'states':states,'transitions':edges,'negative_controls':['parallel port edges','agent self-loop'],'positive_control':'E--N tree','scope':'Correct multigraph acyclicity predicate; four tiny fixtures only, not unified invariant or universal preservation.'}
 out=Path(__file__).resolve().parents[1]/'results/port-multigraph-forest.json'
 out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
