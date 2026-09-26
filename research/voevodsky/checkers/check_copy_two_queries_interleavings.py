"""Exercise alternate enabled-redex schedules of the wired copy/query net."""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_copy_two_queries_port_graph import Twin

class ScheduledTwin(Twin):
 def run_order(self,order):
  history=[]
  while True:
   candidates=[]
   for name in self.types:
    if not name.startswith(('COPY','Q1','Q2','E_')):continue
    other=self.wires[name+'.p'].split('.')[0]
    if other.startswith('COPY'):continue # query faces COPY auxiliary, not an active pair
    if name.startswith('COPY') and not other.startswith(('B0_','B1_','N_')):continue
    if name.startswith(('Q1','Q2')) and not other.startswith(('K_','B0_','B1_','N_')):continue
    if name.startswith('E_') and not other.startswith(('K_','B0_','B1_','N_')):continue
    candidates.append((name,other))
   if not candidates:
    assert len(self.types)==4, ('deadlock',self.types)
    break
   kind_order={'COPY':0,'Q1':1,'Q2':2,'E_':3}
   def rank(item):
    name=item[0]
    return next(i for prefix,i in kind_order.items() if name.startswith(prefix))
   current_order=order(tuple(history),tuple(rank(item) for item in candidates)) if callable(order) else order
   preferred=getattr(self,'preferred_redex_name',None)
   candidates.sort(key=lambda item:(current_order.index(rank(item)),0 if item[0]==preferred else 1))
   name,other=candidates[0];history.append(rank((name,other)))
   if name.startswith('COPY'):
    if other.startswith('N_'):
     l=self.fresh('N');r=self.fresh('N')
     self.replace((name,other),[(name+'.a',l+'.p'),(name+'.b',r+'.p')],[(l,('p',)),(r,('p',))])
    else:
     kind=other.split('_')[0];l=self.fresh(kind);r=self.fresh(kind);nxt=self.fresh('COPY')
     self.replace((name,other),[(name+'.a',l+'.p'),(name+'.b',r+'.p'),(l+'.a',nxt+'.a'),(r+'.a',nxt+'.b'),(other+'.a',nxt+'.p')],[(l,('p','a')),(r,('p','a')),(nxt,('p','a','b'))])
   elif name.startswith('E_'):
    if other.startswith('N_'):self.replace((name,other),[],[])
    else:
     nxt=self.fresh('E');self.replace((name,other),[(other+'.a',nxt+'.p')],[(nxt,('p',))])
   else:
    prefix=name[:2];phase=name[2:].split('_')[0]
    if phase=='B':
     if other.startswith('N_'):
      nxt=self.fresh(prefix+'R');self.replace((name,other),[(name+'.a',nxt+'.p'),(name+'.r',nxt+'.r')],[(nxt,('p','r'))])
     else:
      assert other.startswith('K_')
      nxt=self.fresh(prefix+'S');self.replace((name,other),[(name+'.a',nxt+'.p'),(other+'.a',nxt+'.a'),(name+'.r',nxt+'.r')],[(nxt,('p','a','r'))])
    elif phase=='S':
     if other.startswith('N_'):
      out=self.fresh('FALSE');erase=self.fresh('E')
      self.replace((name,other),[(name+'.r',out+'.p'),(name+'.a',erase+'.p')],[(out,('p',)),(erase,('p',))])
     else:
      assert other.startswith(('B0_','B1_'))
      nxt=self.fresh(prefix+'B');self.replace((name,other),[(name+'.a',nxt+'.p'),(other+'.a',nxt+'.a'),(name+'.r',nxt+'.r')],[(nxt,('p','a','r'))])
    else:
     assert phase=='R'
     if other.startswith('N_'):
      out=self.fresh('FALSE');self.replace((name,other),[(name+'.r',out+'.p')],[(out,('p',))])
     else:
      assert other.startswith(('B0_','B1_'))
      out=self.fresh('TRUE' if other.startswith('B1_') else 'FALSE');erase=self.fresh('E')
      self.replace((name,other),[(name+'.r',out+'.p'),(other+'.a',erase+'.p')],[(out,('p',)),(erase,('p',))])
  self.audit()
  return tuple(self.wires['OUT'+str(i)+'.p'].startswith('TRUE_') for i in (1,2)),history

orders=((0,1,2,3),(1,2,0,3),(2,1,3,0),(3,2,1,0))
cases=0;actual_interleaved=0
for n in range(6):
 for bits in product((0,1),repeat=n):
  for i in range(n+2):
   for j in range(n+2):
    for order in orders:
     answers,history=ScheduledTwin(bits,i,j).run_order(order)
     assert answers==(i<n and bool(bits[i]),j<n and bool(bits[j]))
     if 0 in history and any(h in (1,2) for h in history[:history.index(0)]):actual_interleaved+=1
     cases+=1
report={'passed':True,'cases':cases,'schedules':len(orders),'queries_before_first_copy':actual_interleaved,'blocked':'query principal temporarily meets COPY auxiliary; copier rewrite reconnects a bit principal and unblocks','invariant':'one symmetric wire per live port after every rewrite; two BOOL--OUT normal form','limit':'Four deterministic priority schedules on bounded nets; not exhaustive arbitrary-schedule confluence.'}
out=Path(__file__).resolve().parents[1]/'results/copy-two-queries-interleavings.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
