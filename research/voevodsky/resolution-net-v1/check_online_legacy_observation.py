"""Finite tau-saturated release comparison; not strong bisimulation."""
from pathlib import Path
from copy import deepcopy
from collections import deque
import sys,json,hashlib
from reference import Package,Admission,Rule
from pending import Hole,Branch
from open_net import OpenNet
from open_observer import observe
root=Path(__file__).parent;legacy=root.parent/'checkers';sys.path.insert(0,str(legacy))
from four_cell_completion_barrier_net import BarrierNet

p=Package('release');u=Rule('join',(p,p),p,'structural-join')
context=Branch(u,(Branch(u,(Hole('0',p),Hole('1',p))),Branch(u,(Hole('2',p),Hole('3',p)))))
def legacy_initial():
 n=BarrierNet();slots={str(i):n.add('NEXT',str(i)) for i in range(4)};lower=[]
 for i in (0,2):
  j=n.add('JOIN');n.link((j,'p'),(slots[str(i)],'p'));n.link((j,'a'),(slots[str(i+1)],'p'));lower.append(j)
 top=n.add('JOIN');end=n.add('BARRIER');n.link((top,'p'),(lower[0],'o'));n.link((top,'a'),(lower[1],'o'));n.link((top,'o'),(end,'p'));n.validate();return n,slots,end

def legacy_shape(n,end):
 def visit(node):
  kind,label=n.nodes[node]
  if kind in ('READY','NEXT'):return kind,label
  if kind=='JOIN':return kind,visit(n.wires[node,'p'][0]),visit(n.wires[node,'a'][0])
  if kind=='HOLD':return kind,visit(n.wires[node,'p'][0])
  raise ValueError(kind)
 return visit(n.wires[end,'p'][0])

summaries=[];systems=[]
for name in ('legacy','resolution'):
 if name=='legacy':initial,slots,end=legacy_initial()
 else:initial=OpenNet(context)
 def shape(n):return legacy_shape(n,end) if name=='legacy' else observe(n)['shape']
 def ready(n):return n.observe_barrier()[1] if name=='legacy' else n.released()
 def active(n):return n.enabled() if name=='legacy' else n.active()
 def advance(n,event):
  kind,value=event
  if kind=='tau':
   if name=='legacy':n.step(value)
   else:n.rewrite(value)
  elif name=='legacy':
   node=slots[value]
   if n.nodes[node]!=('NEXT',value):raise ValueError('arrival must consume waiting boundary')
   n.nodes[node]=('READY',value);n.validate()
  else:n.arrive(value,'ticket-'+value,Admission(p,'READY-'+value))
 first=(shape(initial),());nodes=[(initial,())];index={first:0};edges={};queue=deque([0]);observations={}
 while queue:
  k=queue.popleft();n,arrived=nodes[k];observations[k]=ready(n)
  if ready(n) and len(arrived)!=4:raise RuntimeError('release before all arrivals')
  events=[('tau',x) for x in active(n)]+[('arrival',str(i)) for i in range(4) if str(i) not in arrived]
  edges[k]=[]
  for event in events:
   child=deepcopy(n);advance(child,event)
   following=arrived if event[0]=='tau' else tuple(sorted((*arrived,event[1])))
   key=(shape(child),following)
   if key not in index:index[key]=len(nodes);nodes.append((child,following));queue.append(index[key])
   edges[k].append(('tau' if event[0]=='tau' else event[1],index[key]))
 memo={}
 def saturation(k):
  if k in memo:return memo[k]
  following=[j for label,j in edges[k] if label=='tau']
  answer=set().union(*(saturation(j) for j in following)) if following else {k}
  memo[k]=answer;return answer
 macro=set();terminal_checks=0
 for k,(_,arrived) in enumerate(nodes):
  terminals=saturation(k)
  for j in terminals:
   if observations[j]!=(len(arrived)==4):raise RuntimeError('saturated readiness mismatch')
   terminal_checks+=1
   available={label for label,_ in edges[j] if label!='tau'}
   if available!={str(i) for i in range(4)}-set(arrived):raise RuntimeError('arrival alphabet mismatch')
   for label,target in edges[j]:
    if label=='tau':continue
    for final in saturation(target):macro.add((arrived,label,nodes[final][1],observations[final]))
 systems.append(macro)
 summaries.append({'system':name,'reachable_projected_states':len(nodes),'transitions':sum(map(len,edges.values())),'saturation_checks':terminal_checks,'arrival_macro_edges':len(macro)})
if systems[0]!=systems[1] or len(systems[0])!=32:raise RuntimeError('macro transition systems differ')
# Explicit strong-timing counterexample: normalize v1 before all inputs,
# then supply the final input. Legacy still needs a READY/HOLD interaction.
v1=OpenNet(context)
while v1.active():v1.rewrite(v1.active()[0])
old,slots,end=legacy_initial()
for i in range(4):
 if i==3:
  while old.enabled():old.step(old.enabled()[0])
 v1.arrive(str(i),'t'+str(i),Admission(p,'e'+str(i)));old.nodes[slots[str(i)]]=('READY',str(i));old.validate()
if not v1.released() or old.observe_barrier()[1]:raise RuntimeError('expected immediate timing distinction absent')
report={'passed':True,'systems':summaries,'tau_saturated_macro_systems_equal':True,'macro_edges':32,'strong_immediate_readiness_equal':False,'scope':'Four-input join fixture with NEXT nodes used only as external arrival placeholders. Actual legacy JOIN/HOLD reductions unchanged. Receipt order is projected out, arrival labels retained. Finite quiescent/tau-saturated release equivalence, NOT general weak bisimulation, strong timing, linear token consumption or upstream cleanup equivalence.','source_sha256':{str(path.relative_to(root.parent)):hashlib.sha256(path.read_bytes()).hexdigest() for path in (Path(__file__),legacy/'four_cell_completion_barrier_net.py',root/'open_net.py',root/'open_observer.py')}}
(root/'results/online-legacy-observation.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
