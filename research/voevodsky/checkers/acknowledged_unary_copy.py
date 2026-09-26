"""Linear unary duplication with local NIL-triggered completion."""
from retained_membership import RetainedMembership

class AcknowledgedUnaryCopy(RetainedMembership):
 def __init__(self,length,cyclic=False):
  assert type(length) is int and length>=0
  self.types={};self.wires={};self.serial=0;self.steps=0
  if cyclic:
   self.add('BOUND',('a','b','c'));self.roots=('BOUND.a','BOUND.b','BOUND.c')
  else:
   for root in ('LEFT','RIGHT','ACK'):self.add(root,('p',))
   self.roots=('LEFT.p','RIGHT.p','ACK.p')
  d=self.fresh('DC');self.add(d,('p','a','b','c'));self.link(d+'.p',self.chain(('K',)*length))
  for p,root in zip(('a','b','c'),self.roots):self.link(d+'.'+p,root)
  self.audit()
 def enabled(self):
  return [n for n in self.types if self.kind(n)=='DC' and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0]) in ('K','N')]
 def step(self,n):
  assert n in self.enabled();d=self.wires[n+'.p'].split('.')[0];h=self.kind(d)
  x=self.fresh(h);y=self.fresh(h);ports=('p','a') if h=='K' else ('p',)
  new=[(x,ports),(y,ports)];edges=[(n+'.a',x+'.p'),(n+'.b',y+'.p')]
  if h=='K':
   q=self.fresh('DC');new.append((q,('p','a','b','c')))
   edges.extend([(d+'.a',q+'.p'),(x+'.a',q+'.a'),(y+'.a',q+'.b'),(n+'.c',q+'.c')])
  else:
   q=self.fresh('DONE');new.append((q,('p',)));edges.append((n+'.c',q+'.p'))
  self.replace((n,d),edges,new)
