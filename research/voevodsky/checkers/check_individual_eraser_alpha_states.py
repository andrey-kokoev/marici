"""Search individual enabled ERASE choices, quotienting by rooted alpha graph."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_copy_two_queries_interleavings import ScheduledTwin
 from check_reachable_family_diamonds import canonical

class Branch(Exception):
 def __init__(self,choices):self.choices=choices

def replay(bits,indices,prefix):
 net=ScheduledTwin(bits,*indices)
 def policy(history,options):
  erasers=[name for name in net.types if name.startswith('E_') and net.wires[name+'.p'].split('.')[0].startswith(('N_','B0_','B1_','K_'))]
  choices=tuple((rank,name) for rank in dict.fromkeys(options) for name in (erasers if rank==3 else (None,)))
  if len(history)==len(prefix):raise Branch(choices)
  rank,name=prefix[len(history)]
  assert (rank,name) in choices
  net.preferred_redex_name=name
  return (rank,)+tuple(x for x in range(4) if x!=rank)
 try:net.run_order(policy)
 except Branch as branch:return net,branch.choices
 return net,()

results=[]
for n in range(3):
 for bits in product((0,1),repeat=n):
  for i,j in product(range(n+2),repeat=2):
   prefixes=[()];seen=set();terminal=0;arcs=0
   while prefixes:
    prefix=prefixes.pop()
    net,choices=replay(bits,(i,j),prefix)
    state=canonical(net)
    if state in seen:continue
    seen.add(state);net.audit()
    if not choices:
     assert len(net.types)==4
     answer=tuple(net.wires['OUT'+str(k)+'.p'].startswith('TRUE_') for k in (1,2))
     assert answer==(i<n and bool(bits[i]),j<n and bool(bits[j]))
     terminal+=1
    for choice in choices:
     child,_=replay(bits,(i,j),prefix+(choice,))
     assert canonical(child)!=state
     prefixes.append(prefix+(choice,));arcs+=1
    assert len(seen)<10000
   assert terminal==1
   results.append({'bits':bits,'indices':(i,j),'states':len(seen),'edges':arcs})
report={'passed':True,'fixtures':len(results),'states_total':sum(x['states'] for x in results),'edges_total':sum(x['edges'] for x in results),'largest':max(results,key=lambda x:x['states']),'search':'all enabled family choices AND all individually enabled eraser choices, alpha quotient','result':'one correct terminal alpha-class per n<=2 support and both indices 0..n+1','limit':'Finite exhaustive small inputs only; no arbitrary-n inductive invariant or confluence proof.'}
out=Path(__file__).resolve().parents[1]/'results/individual-eraser-alpha-states.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
