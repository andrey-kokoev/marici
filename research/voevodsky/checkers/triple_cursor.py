"""Two locally gated unary copies; three outputs published only at final latch."""
from acknowledged_unary_copy import AcknowledgedUnaryCopy

class TripleCursor(AcknowledgedUnaryCopy):
 def __init__(self,length,cyclic=False):
  assert type(length) is int and length>=0
  self.types={};self.wires={};self.serial=0;self.steps=0
  if cyclic:
   self.add('BOUND',('a','b','c','d'));self.roots=tuple('BOUND.'+p for p in ('a','b','c','d'))
  else:
   for r in ('QUERY','INSERT','CURSOR','ACK'):self.add(r,('p',))
   self.roots=tuple(r+'.p' for r in ('QUERY','INSERT','CURSOR','ACK'))
  d=self.fresh('DC');g=self.fresh('PREP')
  self.add(d,('p','a','b','c'));self.add(g,('p','a','b','q','i','r','c'))
  self.link(d+'.p',self.chain(('K',)*length))
  for a,b in [(d+'.a',g+'.a'),(d+'.b',g+'.b'),(d+'.c',g+'.p')]:self.link(a,b)
  for p,root in zip(('q','i','r','c'),self.roots):self.link(g+'.'+p,root)
  self.audit()
 def enabled(self):
  return super().enabled()+[n for n in self.types if self.kind(n) in ('PREP','READY') and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0])=='DONE']
 def step(self,n):
  k=self.kind(n)
  if k=='DC':return super().step(n)
  assert n in self.enabled();done=self.wires[n+'.p'].split('.')[0]
  if k=='PREP':
   d=self.fresh('DC');g=self.fresh('READY')
   new=[(d,('p','a','b','c')),(g,('p','a','b','d','q','i','r','c'))]
   edges=[(n+'.b',d+'.p'),(n+'.a',g+'.a'),(d+'.a',g+'.b'),(d+'.b',g+'.d'),(d+'.c',g+'.p')]+[(n+'.'+p,g+'.'+p) for p in ('q','i','r','c')]
  else:
   d=self.fresh('DONE');new=[(d,('p',))]
   edges=[(n+'.a',n+'.q'),(n+'.b',n+'.i'),(n+'.d',n+'.r'),(n+'.c',d+'.p')]
  self.replace((n,done),edges,new)
