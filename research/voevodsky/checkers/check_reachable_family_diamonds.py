"""Sample reachable two-family local diamonds on wired copier/query nets.

Different enabled families may act on disjoint active pairs. Check whether
both orderings remain enabled and have equal alpha-canonical successors.
"""
from contextlib import redirect_stdout
from io import StringIO
from itertools import combinations
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_copy_two_queries_interleavings import ScheduledTwin

class Stop(Exception):pass

def canonical(net):
 # OUT-rooted components followed by detached garbage components.
 def kind(name):return name.rsplit('_',1)[0] if name.rsplit('_',1)[-1].isdigit() else name
 roots=['OUT1','OUT2']
 mapping={};order=[]
 while len(mapping)<len(net.types):
  if not roots:
   roots=[min((x for x in net.types if x not in mapping),key=lambda x:(kind(x),x))]
  root=roots.pop(0)
  if root in mapping:continue
  queue=[root]
  for name in queue:
   if name in mapping:continue
   mapping[name]=len(mapping);order.append(name)
   for port in sorted(net.types[name]):
    neighbor=net.wires[f'{name}.{port}'].split('.')[0]
    if neighbor not in mapping and neighbor not in queue:queue.append(neighbor)
 return tuple((kind(name),tuple((p,mapping[net.wires[f'{name}.{p}'].split('.')[0]],net.wires[f'{name}.{p}'].split('.')[1]) for p in sorted(net.types[name]))) for name in order)

def snapshot(bits,indices,prefix,follow=()):
 net=ScheduledTwin(bits,*indices);choices=[]
 def policy(history,options):
  k=len(history)
  if k==len(prefix)+len(follow):
   choices.extend(dict.fromkeys(options))
   raise Stop()
  chosen=(prefix+follow)[k]
  if chosen not in options:raise ValueError('redex no longer enabled')
  return (chosen,)+tuple(x for x in range(4) if x!=chosen)
 try:net.run_order(policy)
 except Stop:pass
 else:
  # already normal: canonical net still available
  pass
 return net,tuple(choices)

fixtures=(((),(0,0)),((1,),(0,0)),((1,0),(0,1)),((0,1),(1,0)))
checked=0;by_pair={};skipped=0
for bits,indices in fixtures:
 prefixes={()}
 for static in ((0,1,2,3),(1,2,0,3),(2,1,3,0),(3,2,1,0)):
  _,history=ScheduledTwin(bits,*indices).run_order(static)
  prefixes.update(tuple(history[:k]) for k in range(len(history)+1))
 for prefix in prefixes:
  net,options=snapshot(bits,indices,prefix)
  for a,b in combinations(options,2):
   try:
    left,_=snapshot(bits,indices,prefix,(a,b))
    right,_=snapshot(bits,indices,prefix,(b,a))
   except ValueError:
    skipped+=1;continue
   assert canonical(left)==canonical(right),(bits,indices,prefix,a,b)
   key=f'{min(a,b)}-{max(a,b)}';by_pair[key]=by_pair.get(key,0)+1
   checked+=1
report={'passed':True,'tested_two_step_diamonds':checked,'families':'0 COPY, 1 Q1, 2 Q2, 3 ERASE','by_family_pair':by_pair,'second_not_enabled':skipped,'scope':'Reachable prefixes from four static schedules on four fixtures; same-family eraser alternatives and arbitrary contexts untested.'}
out=Path(__file__).resolve().parents[1]/'results/reachable-family-diamonds.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
