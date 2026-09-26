"""Graph-level two-step diamond for distinct query active pairs after copying."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json,re
with redirect_stdout(StringIO()):
 from check_copy_two_queries_interleavings import ScheduledTwin

class Snapshot(Exception):pass

def kind(name):return re.sub(r'_\d+$','',name)
def canonical(net):
 # Traverse rooted port graph from OUT1/OUT2; allocate alpha names on visit.
 mapping={};todo=['OUT1','OUT2'];order=[]
 for name in todo:
  if name in mapping:continue
  mapping[name]=len(mapping);order.append(name)
  for port in sorted(net.types[name]):
   neighbor=net.wires[f'{name}.{port}'].split('.')[0]
   if neighbor not in mapping and neighbor not in todo:todo.append(neighbor)
 assert len(mapping)==len(net.types)
 return tuple((kind(name),tuple((p,mapping[net.wires[f'{name}.{p}'].split('.')[0]],net.wires[f'{name}.{p}'].split('.')[1]) for p in sorted(net.types[name]))) for name in order)

def after_two(bits,first,second):
 net=ScheduledTwin(bits,0,0)
 def policy(history,options):
  if 0 in options:return (0,1,2,3)
  taken=[x for x in history if x in (1,2)]
  if len(taken)==2:raise Snapshot()
  desired=first if not taken else second
  assert desired in options
  return (desired,)+tuple(x for x in range(4) if x!=desired)
 try:net.run_order(policy)
 except Snapshot:pass
 else:raise AssertionError('snapshot not reached')
 net.audit()
 return canonical(net)

cases=0
for bits in ((),(0,),(1,),(0,1),(1,0),(1,1)):
 left=after_two(bits,1,2);right=after_two(bits,2,1)
 assert left==right,(bits,left,right)
 cases+=1
report={'passed':True,'fixtures':cases,'diamond':'one Q1 and one Q2 active-pair rewrite commute modulo fresh-agent alpha names after COPY normalizes','canonicalization':'rooted OUT1/OUT2 port-graph traversal preserving agent kind, port names and peer ports','scope':'One local disjoint-query critical pair per fixture at indices (0,0); not all redex pairs or global confluence.'}
out=Path(__file__).resolve().parents[1]/'results/disjoint-query-redex-diamond.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
