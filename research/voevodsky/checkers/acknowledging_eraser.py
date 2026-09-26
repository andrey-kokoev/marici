"""Isolated linear garbage acknowledgment; not yet a whole-operation barrier."""
from retained_membership import RetainedMembership

class AcknowledgingEraser(RetainedMembership):
 def __init__(self,kinds):
  kinds=tuple(kinds);assert all(k in ('B0','B1','K') for k in kinds)
  self.types={};self.wires={};self.serial=0;self.steps=0
  self.add('ACK',('p',));e=self.fresh('EA');self.add(e,('p','r'))
  self.link(e+'.p',self.chain(kinds));self.link(e+'.r','ACK.p');self.audit()
 def enabled(self):
  return [n for n in self.types if self.kind(n)=='EA' and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0]) in ('B0','B1','K','N')]
 def step(self,n):
  assert n in self.enabled()
  d=self.wires[n+'.p'].split('.')[0]
  if self.kind(d)=='N':
   done=self.fresh('DONE');self.replace((n,d),[(n+'.r',done+'.p')],[(done,('p',))])
  else:
   e=self.fresh('EA');self.replace((n,d),[(n+'.r',e+'.r'),(d+'.a',e+'.p')],[(e,('p','r'))])
 def acknowledged(self):return self.kind(self.wires['ACK.p'].split('.')[0])=='DONE'
