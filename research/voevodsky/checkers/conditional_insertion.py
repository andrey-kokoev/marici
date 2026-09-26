"""A completed query selects one insertion; final DONE includes rejected cleanup."""
from strict_set_program import StrictSetProgram
from acknowledged_membership import AcknowledgedMembership

class ConditionalInsertion(StrictSetProgram):
 def __init__(self,bits,index,true_index,false_index):
  assert all(type(i) is int and i>=0 for i in (index,true_index,false_index))
  AcknowledgedMembership.__init__(self,bits,index)
  g=self.fresh('WAIT');self.add(g,('p','b','s','r','t','f','o','c'))
  for root,port in [('ACK','p'),('RET','s'),(self.out,'b')]:
   peer=self.wires.pop(root+'.p');del self.wires[peer];self.link(g+'.'+port,peer)
  for p,q in [('r','RET.p'),('c','ACK.p'),('o',self.out+'.p'),('t',self.chain(('K',)*true_index)),('f',self.chain(('K',)*false_index))]:self.link(g+'.'+p,q)
  self.audit()
 def enabled(self):
  allowed={'WAIT':{'DONE'},'PICK':{'TRUE','FALSE'},'JOIN':{'DONE'},'JOINR':{'DONE'}}
  return super().enabled()+[n for n in self.types if self.kind(n) in allowed and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0]) in allowed[self.kind(n)]]
 def step(self,n):
  k=self.kind(n)
  if k not in ('WAIT','PICK','JOIN','JOINR'):return super().step(n)
  assert n in self.enabled()
  d=self.wires[n+'.p'].split('.')[0];h=self.kind(d)
  if k=='WAIT':
   q=self.fresh('PICK');new=[(q,('p','s','r','t','f','o','c'))]
   edges=[(n+'.b',q+'.p')]+[(n+'.'+p,q+'.'+p) for p in ('s','r','t','f','o','c')]
  elif k=='PICK':
   a=self.fresh('ABc');e=self.fresh('EA');j=self.fresh('JOIN');v=self.fresh(h)
   new=[(a,('p','a','r','c')),(e,('p','r')),(j,('p','a','c')),(v,('p',))]
   selected,rejected=('t','f') if h=='TRUE' else ('f','t')
   edges=[(n+'.'+selected,a+'.p'),(n+'.s',a+'.a'),(n+'.r',a+'.r'),(a+'.c',j+'.p'),(n+'.'+rejected,e+'.p'),(e+'.r',j+'.a'),(n+'.c',j+'.c'),(n+'.o',v+'.p')]
  elif k=='JOIN':
   j=self.fresh('JOINR');new=[(j,('p','c'))];edges=[(n+'.a',j+'.p'),(n+'.c',j+'.c')]
  else:
   j=self.fresh('DONE');new=[(j,('p',))];edges=[(n+'.c',j+'.p')]
  self.replace((n,d),edges,new)
