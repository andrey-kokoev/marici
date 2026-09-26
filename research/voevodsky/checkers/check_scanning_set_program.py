from scanning_set_program import ScanningSetProgram
from itertools import product
from random import Random
from pathlib import Path
import json
rng=Random(101);runs=steps=0
for program in (p for size in range(4) for p in product([('scan',(0,0)),('scan',(0,3)),('member',0),('add',1),('union',(0,1)),('ifadd',(1,0,2))],repeat=size)):
 for bits in ((),(0,),(1,)):
  w=list(bits);observations=[]
  for op,a in program:
   if op=='scan':
    c,f=a;tag='EXHAUSTED'
    for _ in range(f):
     if c<len(w) and w[c]:tag='FOUND';break
     w.extend([0]*max(0,c+1-len(w)));w[c]=1;c+=1
    observations.append(('scan',tag))
   elif op=='union':w=[int((i<len(w) and w[i]) or (i<len(a) and a[i])) for i in range(max(len(w),len(a)))]
   else:
    if op=='ifadd':
     i,t,f=a;b=i<len(w) and bool(w[i]);observations.append(('boolean',b));a=t if b else f
    if op=='member':observations.append(('boolean',a<len(w) and bool(w[a])))
    else:w.extend([0]*max(0,a+1-len(w)));w[a]=1
  net=ScanningSetProgram(bits,program);previous=net.observe()['observations']
  while net.enabled():
   view=net.observe();assert not view['complete'] and view['word'] is None
   for old,new in zip(previous,view['observations']):
    assert old[0]==new[0]
    if old[1] is not None:assert old==new
   previous=view['observations']
   for g in net.enabled():
    if net.kind(g) in net.gates_kinds:
     assert g==net.gates[len(net.releases)]
     assert not any(net.kind(n) in net.work for n in net.types)
   net.step(rng.choice(net.enabled()))
  assert net.observe()=={'observations':tuple(observations),'complete':True,'word':tuple(w)}
  assert net.releases==net.gates
  used=set()
  for root in ['RET','ACK']+net.outputs:
   todo=[root];part=set()
   while todo:
    x=todo.pop()
    if x in part:continue
    part.add(x);todo.extend(net.wires[x+'.'+p].split('.')[0] for p in net.types[x])
   assert not used&part and len(part)==(len(w)+2 if root=='RET' else 2);used|=part
  assert used==set(net.types)
  runs+=1;steps+=net.steps
report={'passed':True,'runs':runs,'rewrites':steps,'max_length':3,'seed':101,'scope':'Six instruction fixtures, three inputs, one seeded schedule; ordered typed snapshots, cleanup-gated releases and exact final component coverage.'}
p=Path(__file__).resolve().parents[1]/'results/scanning-set-program.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
