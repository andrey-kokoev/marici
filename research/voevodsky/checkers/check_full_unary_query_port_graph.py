"""Small fully wired linear unary threshold net, including terminal erasure."""
from pathlib import Path
import json

class Net:
 def __init__(self,c,k):
  self.types={};self.wires={};self.serial=0;self.steps=0
  self.add('OUT',('p',))
  count=self.chain('U',c);budget=self.chain('K',k)
  self.add('Q_B',('p','a','r'))
  self.link('Q_B.p',budget);self.link('Q_B.a',count);self.link('Q_B.r','OUT.p')
  self.audit()
 def add(self,name,ports):
  assert name not in self.types;self.types[name]=tuple(ports)
 def fresh(self,prefix):
  self.serial+=1;return f'{prefix}_{self.serial}'
 def link(self,x,y):
  assert x not in self.wires and y not in self.wires and x!=y
  self.wires[x]=y;self.wires[y]=x
 def chain(self,typ,n):
  tail=self.fresh('N');self.add(tail,('p',));head=f'{tail}.p'
  for _ in range(n):
   name=self.fresh(typ);self.add(name,('p','a'));self.link(f'{name}.a',head);head=f'{name}.p'
  return head
 def audit(self):
  ports={f'{name}.{p}' for name,ps in self.types.items() for p in ps}
  assert set(self.wires)==ports
  assert all(self.wires.get(v)==u for u,v in self.wires.items())
 def active(self):
  for name,ps in list(self.types.items()):
   if 'p' not in ps or name=='OUT':continue
   other=self.wires[f'{name}.p'].split('.')[0]
   if name.startswith(('Q_B','Q_C','E_')) or name in ('Q_B','Q_C'):
    if other in self.types:return name,other
  raise AssertionError('no active pair before termination')
 def replace(self,names,connections,new_agents):
  exposed={}
  for name in names:
   for p in self.types[name]:
    port=f'{name}.{p}'
    if port not in self.wires:continue # internal active-pair wire already removed
    neighbor=self.wires.pop(port)
    self.wires.pop(neighbor)
    if neighbor.split('.')[0] not in names:exposed[port]=neighbor
   del self.types[name]
  for name,ps in new_agents:self.add(name,ps)
  for a,b in connections:self.link(exposed.get(a,a),exposed.get(b,b))
  self.steps+=1;self.audit()
 def normalize(self):
  while True:
   erasers=[name for name in self.types if name.startswith('E_')]
   queries=[name for name in self.types if name.startswith('Q_') or name in ('Q_B','Q_C')]
   if not queries and not erasers:break
   name=(queries or erasers)[0];other=self.wires[f'{name}.p'].split('.')[0]
   kind=self.types[other]
   if name.startswith('Q_') or name in ('Q_B','Q_C'):
    phase=name.split('_')[1] if name not in ('Q_B','Q_C') else name[-1]
    if other.startswith('N_'):
     boolname=self.fresh('TRUE' if phase=='B' else 'FALSE')
     erase=self.fresh('E')
     self.replace((name,other),[(f'{name}.r',f'{boolname}.p'),(f'{name}.a',f'{erase}.p')],[(boolname,('p',)),(erase,('p',))])
    else:
     assert (phase=='B' and other.startswith('K_')) or (phase=='C' and other.startswith('U_'))
     nxt=self.fresh('Q_C' if phase=='B' else 'Q_B')
     self.replace((name,other),[(f'{name}.a',f'{nxt}.p'),(f'{other}.a',f'{nxt}.a'),(f'{name}.r',f'{nxt}.r')],[(nxt,('p','a','r'))])
   else:
    assert name.startswith('E_')
    if other.startswith('N_'):self.replace((name,other),[],[])
    else:
     assert other.startswith(('U_','K_'))
     nxt=self.fresh('E')
     self.replace((name,other),[(f'{other}.a',f'{nxt}.p')],[(nxt,('p',))])
  self.audit()
  outputs=[n for n in self.types if n.startswith(('TRUE_','FALSE_'))]
  assert len(outputs)==1 and len(self.types)==2 and self.wires[f'{outputs[0]}.p']=='OUT.p'
  return outputs[0].startswith('TRUE_'),self.steps

cases=0;max_steps=0
for c in range(17):
 for k in range(17):
  result,steps=Net(c,k).normalize()
  assert result==(c>=k)
  cases+=1;max_steps=max(max_steps,steps)
report={'passed':True,'cases':cases,'max_steps':max_steps,'invariant':'every live agent port has exactly one symmetric wire after every rewrite','normal_form':'one BOOL--OUT wire; all count/budget/eraser/query agents consumed','rules':'Q_B/Q_C with K/U/NIL, ERASE with K/U/NIL','scope':'Small bounded executable port graph, destructive query only; generic confluence and Nima E/E_B translation unproved.'}
out=Path(__file__).resolve().parents[1]/'results/full-unary-query-port-graph.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
