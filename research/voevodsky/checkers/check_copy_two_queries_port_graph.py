"""One wired finite-signature copier feeding two destructive membership queries."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_fixed_signature_membership_net import Membership

class Twin(Membership):
 def __init__(self,bits,i,j):
  self.types={};self.wires={};self.serial=0;self.steps=0
  self.add('OUT1',('p',));self.add('OUT2',('p',))
  head=self.bits(bits)
  self.add('COPY',('p','a','b'));self.link('COPY.p',head)
  for label,index,out,port in (('Q1',i,'OUT1','a'),('Q2',j,'OUT2','b')):
   budget=self.chain('K',index)
   self.add(label+'B',('p','a','r'))
   self.link(label+'B.p',budget);self.link(label+'B.r',out+'.p')
   self.link(label+'B.a','COPY.'+port)
  self.audit()
 def run(self):
  while True:
   copiers=[x for x in self.types if x.startswith('COPY')]
   if not copiers:break
   q=copiers[0];other=self.wires[q+'.p'].split('.')[0]
   if other.startswith('N_'):
    l=self.fresh('N');r=self.fresh('N')
    self.replace((q,other),[(q+'.a',l+'.p'),(q+'.b',r+'.p')],[(l,('p',)),(r,('p',))])
   else:
    assert other.startswith(('B0_','B1_'))
    kind=other.split('_')[0]
    l=self.fresh(kind);r=self.fresh(kind);nxt=self.fresh('COPY')
    self.replace((q,other),[(q+'.a',l+'.p'),(q+'.b',r+'.p'),(l+'.a',nxt+'.a'),(r+'.a',nxt+'.b'),(other+'.a',nxt+'.p')],[(l,('p','a')),(r,('p','a')),(nxt,('p','a','b'))])
  # Each Q instance is a disjoint connected component after copying.
  # Rename Q1B/Q2B to Q_B in one component at a time is unnecessary:
  # run the same local phase rules with a query-specific name prefix.
  while True:
   qs=[x for x in self.types if x.startswith(('Q1','Q2'))]
   es=[x for x in self.types if x.startswith('E_')]
   if not qs and not es:break
   q=(qs or es)[0];other=self.wires[q+'.p'].split('.')[0]
   if q.startswith('E_'):
    if other.startswith('N_'):self.replace((q,other),[],[])
    else:
     assert other.startswith(('B0_','B1_','K_'))
     e=self.fresh('E');self.replace((q,other),[(other+'.a',e+'.p')],[(e,('p',))])
    continue
   prefix=q[:2];phase=q[2:].split('_')[0]
   if phase=='B':
    if other.startswith('N_'):
     new=self.fresh(prefix+'R');self.replace((q,other),[(q+'.a',new+'.p'),(q+'.r',new+'.r')],[(new,('p','r'))])
    else:
     assert other.startswith('K_')
     new=self.fresh(prefix+'S');self.replace((q,other),[(q+'.a',new+'.p'),(other+'.a',new+'.a'),(q+'.r',new+'.r')],[(new,('p','a','r'))])
   elif phase=='S':
    if other.startswith('N_'):
     out=self.fresh('FALSE');e=self.fresh('E')
     self.replace((q,other),[(q+'.r',out+'.p'),(q+'.a',e+'.p')],[(out,('p',)),(e,('p',))])
    else:
     assert other.startswith(('B0_','B1_'))
     new=self.fresh(prefix+'B');self.replace((q,other),[(q+'.a',new+'.p'),(other+'.a',new+'.a'),(q+'.r',new+'.r')],[(new,('p','a','r'))])
   else:
    assert phase=='R'
    if other.startswith('N_'):
     out=self.fresh('FALSE');self.replace((q,other),[(q+'.r',out+'.p')],[(out,('p',))])
    else:
     assert other.startswith(('B0_','B1_'))
     out=self.fresh('TRUE' if other.startswith('B1_') else 'FALSE');e=self.fresh('E')
     self.replace((q,other),[(q+'.r',out+'.p'),(other+'.a',e+'.p')],[(out,('p',)),(e,('p',))])
  self.audit()
  assert len(self.types)==4
  return tuple(self.wires['OUT'+str(i)+'.p'].startswith('TRUE_') for i in (1,2)),self.steps

cases=0;maximum=0
for n in range(6):
 for bits in product((0,1),repeat=n):
  for i in range(n+2):
   for j in range(n+2):
    answers,steps=Twin(bits,i,j).run()
    assert answers==(i<n and bits[i]==1,j<n and bits[j]==1)
    cases+=1;maximum=max(maximum,steps)
report={'passed':True,'cases':cases,'max_rewrites':maximum,'normal_form':'two BOOL--OUT components, no shared support','linearity':'one symmetric wire per live port checked after every COPY, QUERY and ERASE rewrite','finite_agent_kinds':'B0 B1 K N COPY Q_B Q_S Q_R E BOOL OUT (indexed instance IDs not agent kinds)','qualification':'Deterministic copier-first schedule only; generic confluence, insertion/union and further reuse not proven.'}
out=Path(__file__).resolve().parents[1]/'results/copy-two-queries-port-graph.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
