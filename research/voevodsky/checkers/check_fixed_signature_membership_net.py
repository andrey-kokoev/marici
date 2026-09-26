"""Executable finite-signature, destructive indexed-membership port net.

Support: ordered B0/B1 chain; index: unary K chain. The only agent
kinds are B0,B1,K,N,Q_B,Q_SKIP,Q_READ,E,TRUE,FALSE,OUT. No label is
stored in an agent kind or payload. Every rewrite checks wire linearity.
"""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_full_unary_query_port_graph import Net

class Membership(Net):
 def __init__(self,bits,index):
  self.types={};self.wires={};self.serial=0;self.steps=0
  self.add('OUT',('p',))
  support=self.bits(bits);budget=self.chain('K',index)
  self.add('Q_B',('p','a','r'))
  self.link('Q_B.p',budget);self.link('Q_B.a',support);self.link('Q_B.r','OUT.p');self.audit()
 def bits(self,values):
  tail=self.fresh('N');self.add(tail,('p',));head=f'{tail}.p'
  for bit in reversed(values):
   assert bit in (0,1)
   name=self.fresh('B1' if bit else 'B0');self.add(name,('p','a'))
   self.link(f'{name}.a',head);head=f'{name}.p'
  return head
 def finish(self,q,other,answer,extra_tail=None):
  out=self.fresh('TRUE' if answer else 'FALSE')
  erase=self.fresh('E')
  connections=[(f'{q}.r',f'{out}.p'),(f'{q}.a',f'{erase}.p')]
  agents=[(out,('p',)),(erase,('p',))]
  if extra_tail is not None:
   e2=self.fresh('E');connections.append((f'{other}.a',f'{e2}.p'));agents.append((e2,('p',)))
  self.replace((q,other),connections,agents)
 def normalize(self):
  while True:
   queries=[n for n in self.types if n.startswith('Q_')]
   erasers=[n for n in self.types if n.startswith('E_')]
   if not queries and not erasers:break
   name=(queries or erasers)[0];other=self.wires[f'{name}.p'].split('.')[0]
   if name.startswith('Q_'):
    if name=='Q_B' or name.startswith('Q_B_'):
     if other.startswith('N_'):
      nxt=self.fresh('Q_READ')
      self.replace((name,other),[(f'{name}.a',f'{nxt}.p'),(f'{name}.r',f'{nxt}.r')],[(nxt,('p','r'))])
     else:
      assert other.startswith('K_')
      nxt=self.fresh('Q_SKIP')
      self.replace((name,other),[(f'{name}.a',f'{nxt}.p'),(f'{other}.a',f'{nxt}.a'),(f'{name}.r',f'{nxt}.r')],[(nxt,('p','a','r'))])
    elif name=='Q_SKIP' or name.startswith('Q_SKIP_'):
     if other.startswith('N_'):self.finish(name,other,False)
     else:
      assert other.startswith(('B0_','B1_'))
      nxt=self.fresh('Q_B')
      self.replace((name,other),[(f'{name}.a',f'{nxt}.p'),(f'{other}.a',f'{nxt}.a'),(f'{name}.r',f'{nxt}.r')],[(nxt,('p','a','r'))])
    else:
     assert name.startswith('Q_READ_')
     if other.startswith('N_'):
      out=self.fresh('FALSE')
      self.replace((name,other),[(f'{name}.r',f'{out}.p')],[(out,('p',))])
     else:
      assert other.startswith(('B0_','B1_'))
      out=self.fresh('TRUE' if other.startswith('B1_') else 'FALSE')
      erase=self.fresh('E')
      self.replace((name,other),[(f'{name}.r',f'{out}.p'),(f'{other}.a',f'{erase}.p')],[(out,('p',)),(erase,('p',))])
   else:
    assert name.startswith('E_')
    if other.startswith('N_'):self.replace((name,other),[],[])
    else:
     assert other.startswith(('B0_','B1_','K_'))
     nxt=self.fresh('E')
     self.replace((name,other),[(f'{other}.a',f'{nxt}.p')],[(nxt,('p',))])
  self.audit()
  outputs=[n for n in self.types if n.startswith(('TRUE_','FALSE_'))]
  assert len(outputs)==1 and len(self.types)==2 and self.wires[f'{outputs[0]}.p']=='OUT.p'
  return outputs[0].startswith('TRUE_'),self.steps

cases=0;peak=0
for n in range(9):
 for bits in product((0,1),repeat=n):
  for index in range(n+2):
   answer,steps=Membership(bits,index).normalize()
   assert answer==(index<n and bits[index]==1)
   cases+=1;peak=max(peak,steps)
report={'passed':True,'cases':cases,'max_rewrites':peak,'finite_agent_kinds':['B0','B1','K','N','Q_B','Q_SKIP','Q_READ','E','TRUE','FALSE','OUT'],'result':'read support membership at unary index; out-of-range false','invariant':'every live port exactly one symmetric wire after each principal-pair rewrite; BOOL--OUT sole normal form','contract':'destructive support and query, fixed agent alphabet; n encoded by network size','not_proven':'union insertion, reusable probes, arbitrary scheduling confluence, Nima correspondence'}
out=Path(__file__).resolve().parents[1]/'results/fixed-signature-membership-net.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
