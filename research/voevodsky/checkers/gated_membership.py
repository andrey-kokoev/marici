"""Two membership calls separated by a local cleanup-DONE gate."""
from acknowledged_membership import AcknowledgedMembership

class GatedMembership(AcknowledgedMembership):
 def __init__(self,bits,i,j):
  super().__init__(bits,i);self.first_out=self.out
  g=self.fresh('GATE');o=self.fresh('OUT');self.second_out=o
  self.add(g,('p','s','r','b','o','c'));self.add(o,('p',))
  head=self.wires.pop('RET.p');del self.wires[head]
  ack=self.wires.pop('ACK.p');del self.wires[ack]
  for p,q in [(g+'.s',head),(g+'.r','RET.p'),(g+'.p',ack),(g+'.c','ACK.p'),(g+'.o',o+'.p'),(g+'.b',self.chain(('K',)*j))]:self.link(p,q)
  self.audit();self.gate_firings=0
 def enabled(self):
  return super().enabled()+[n for n in self.types if self.kind(n)=='GATE' and self.kind(self.wires[n+'.p'].split('.')[0])=='DONE' and self.wires[n+'.p'].endswith('.p')]
 def step(self,n):
  if self.kind(n)!='GATE':return super().step(n)
  assert n in self.enabled()
  d=self.wires[n+'.p'].split('.')[0]
  c=self.fresh('COPY');q=self.fresh('QB')
  self.replace((n,d),[(n+'.s',c+'.p'),(n+'.r',c+'.a'),(c+'.b',q+'.a'),(n+'.b',q+'.p'),(n+'.o',q+'.r'),(n+'.c',q+'.c')],[(c,('p','a','b')),(q,('p','a','r','c'))])
  self.gate_firings+=1
