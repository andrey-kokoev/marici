from sequenced_set import SequencedSet
from itertools import product
from copy import deepcopy
from forest_canonical import canonical
from pathlib import Path
import json

def oracle(w,program):
 w=list(w);answers=[]
 for op,arg in program:
  if op=='add':
   w.extend([0]*max(0,arg+1-len(w)));w[arg]=1
  elif op=='member':answers.append(arg<len(w) and bool(w[arg]))
  else:w=[int((i<len(w) and w[i]) or (i<len(arg) and arg[i])) for i in range(max(len(w),len(arg)))]
 return tuple(w),tuple(answers)

runs=overlaps=0
for n in range(4):
 for w in product((0,1),repeat=n):
  for i,j in product(range(n+3),repeat=2):
   program=[('member',j),('add',i),('member',j),('union',(0,1,0)),('add',j),('member',i)]
   for order in ('forward','reverse'):
    net=SequencedSet(w,program);assert net.execute(order)==oracle(w,program)
    overlaps+=any(a>b for a,b in zip(net.history,net.history[1:]));runs+=1
# Exact exploration includes all individual eraser choices and multiple copies.
fixtures=[((),[('add',1),('member',1)]),((1,),[('member',0),('add',0),('member',0)]),((0,),[('union',(1,0)),('member',0)]),((),[('union',()),('add',0)])]
states=edges=0
for w,p in fixtures:
 pending=[SequencedSet(w,p)];seen=set();ends=set()
 while pending:
  net=pending.pop();key=canonical(net)
  if key in seen:continue
  seen.add(key);choices=net.enabled()
  if not choices:
   assert net.execute()==oracle(w,p);ends.add(key)
  for n in choices:
   child=deepcopy(net);child.step(n);pending.append(child);edges+=1
 assert len(ends)==1;states+=len(seen)
report={'passed':True,'six_operation_runs':runs,'runs_with_late_then_early_rewrites':overlaps,'exhaustive_fixtures':len(fixtures),'exact_states':states,'edges':edges,'scope':'Prewired straight-line dataflow sequencing; no host calls between operations. No completion barriers, dynamic branches, or arbitrary-program confluence theorem.'}
out=Path(__file__).resolve().parents[1]/'results/sequenced-set.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
