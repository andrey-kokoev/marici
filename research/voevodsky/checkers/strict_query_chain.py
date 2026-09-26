"""Compile a finite query sequence with local strict DONE gates."""
from gated_membership import GatedMembership
from acknowledged_membership import AcknowledgedMembership
from retained_membership import RetainedMembership

class StrictQueryChain(GatedMembership):
 def __init__(self,bits,indices):
  bits=tuple(bits);indices=tuple(indices)
  assert all(b in (0,1) for b in bits)
  assert all(type(i) is int and i>=0 for i in indices)
  self.gates=[];self.outputs=[];self.gate_firings=0
  if not indices:
   RetainedMembership.__init__(self,bits)
   self.add('ACK',('p',));d=self.fresh('DONE');self.add(d,('p',));self.link('ACK.p',d+'.p');self.audit();return
  AcknowledgedMembership.__init__(self,bits,indices[0]);self.outputs.append(self.out)
  for index in indices[1:]:
   g=self.fresh('GATE');o=self.fresh('OUT')
   self.add(g,('p','s','r','b','o','c'));self.add(o,('p',))
   head=self.wires.pop('RET.p');del self.wires[head]
   ack=self.wires.pop('ACK.p');del self.wires[ack]
   for p,q in [(g+'.s',head),(g+'.r','RET.p'),(g+'.p',ack),(g+'.c','ACK.p'),(g+'.o',o+'.p'),(g+'.b',self.chain(('K',)*index))]:self.link(p,q)
   self.gates.append(g);self.outputs.append(o)
  self.audit()
