"""Bounded raw-state exploration: no alpha/forest quotient of cyclic graphs."""
from scanning_set_program import ScanningSetProgram
from copy import deepcopy
from pathlib import Path
import json

def freeze(x):
 if isinstance(x,dict):return tuple(sorted((k,freeze(v)) for k,v in x.items()))
 if isinstance(x,(tuple,list)):return tuple(map(freeze,x))
 return x

def explore(bits,program,expected,cap=20000):
 pending=[ScanningSetProgram(bits,program)];seen=set();edges=branches=terminals=0;outcomes=set();lengths=set();complete=True
 publication_steps=[set() for _ in pending[0].outputs]
 while pending:
  net=pending.pop();key=freeze(net.__dict__)
  if key in seen:continue
  if len(seen)>=cap:complete=False;break
  seen.add(key);choices=net.enabled();view=net.observe()
  assert view['complete']==(not choices)
  if not view['complete']:assert view['word'] is None
  values=[value for tag,value in view['observations']]
  if None in values:assert all(value is None for value in values[values.index(None):])
  if not choices:
   assert view==expected,(bits,program,view)
   assert net.releases==net.gates
   outcomes.add(freeze(view));lengths.add(net.steps);terminals+=1
   continue
  assert not view['complete']
  branches+=len(choices)>1
  for a in choices:
   child=deepcopy(net);child.step(a);after=child.observe()
   for slot,(old,new) in enumerate(zip(view['observations'],after['observations'])):
    assert old[0]==new[0]
    if old[1] is not None:
     assert old==new
     root=net.outputs[slot];assert net.wires[root+'.p']==child.wires[root+'.p']
    elif new[1] is not None:publication_steps[slot].add(child.steps)
   pending.append(child);edges+=1
 return {'bits':bits,'program':program,'complete':complete,'state_cap':cap,'states':len(seen),'edges':edges,'branching_states':branches,'terminal_named_states':terminals,'distinct_terminal_observations':len(outcomes),'terminal_rewrite_counts':sorted(lengths),'publication_steps':[sorted(s) for s in publication_steps]}
fixtures=[
 ((1,0),[('member',0)],(1,0),(('boolean',True),)),
 ((),[('scan',(0,1))],(1,),(('scan','EXHAUSTED'),)),
 ((1,),[('scan',(0,2))],(1,),(('scan','FOUND'),)),
 ((0,),[('scan',(0,1)),('ifadd',(0,0,1))],(1,),(('scan','EXHAUSTED'),('boolean',True))),
 ((),[('ifadd',(0,0,1)),('scan',(0,1))],(1,1),(('boolean',False),('scan','EXHAUSTED'))),
]
results=[]
for bits,program,word,observations in fixtures:
 results.append(explore(bits,program,{'observations':observations,'complete':True,'word':word}))
# Check incompleteness signaling deliberately, not as a successful proof.
truncated=explore((),[('scan',(0,1))],{},cap=1)
assert not truncated['complete']
report={'passed':all(r['complete'] and r['distinct_terminal_observations']==1 for r in results),'fixtures':results,'cap_signal_checked':True,'scope':'Full reachable raw named state graphs for completed fixtures only; includes allocator, step counter and metadata. Not general confluence or independent rule implementation.'}
p=Path(__file__).resolve().parents[1]/'results/all-schedules.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report));assert report['passed']
