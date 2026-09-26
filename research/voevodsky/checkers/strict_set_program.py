"""Compile once: all mixed operations released only by local DONE gates."""
from acknowledged_membership import AcknowledgedMembership
from retained_membership import RetainedMembership
from program_inputs import word, program as normalize_program

class StrictSetProgram(AcknowledgedMembership):
 gates_kinds={'GM','GA','GU'}
 work={'COPY','QB','QS','QR','EA','ABc','ASc','ARc','ULc','U0c','U1c'}
 def __init__(self,bits,program):
  bits=word(bits)
  normalized=normalize_program(program,{'member','add','union'})
  RetainedMembership.__init__(self,bits)
  self.add('ACK',('p',));d=self.fresh('DONE');self.add(d,('p',));self.link('ACK.p',d+'.p')
  self.outputs=[];self.gates=[];self.releases=[]
  for op,arg in normalized:
   k={'member':'GM','add':'GA','union':'GU'}[op];g=self.fresh(k)
   self.add(g,('p','s','r','b','c','o') if op=='member' else ('p','s','r','b','c'))
   support=self.wires.pop('RET.p');del self.wires[support]
   ack=self.wires.pop('ACK.p');del self.wires[ack]
   operand=self.chain(tuple('B1' if b else 'B0' for b in arg) if op=='union' else ('K',)*arg)
   for p,q in [(g+'.s',support),(g+'.r','RET.p'),(g+'.p',ack),(g+'.c','ACK.p'),(g+'.b',operand)]:self.link(p,q)
   if op=='member':
    o=self.fresh('OUT');self.add(o,('p',));self.link(g+'.o',o+'.p');self.outputs.append(o)
   self.gates.append(g)
  self.audit()
 def enabled(self):
  allowed={'GM':{'DONE'},'GA':{'DONE'},'GU':{'DONE'},'ABc':{'K','N'},'ASc':{'B0','B1','N'},'ARc':{'B0','B1','N'},'ULc':{'B0','B1','N'},'U0c':{'B0','B1','N'},'U1c':{'B0','B1','N'}}
  return super().enabled()+[n for n in self.types if self.kind(n) in allowed and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0]) in allowed[self.kind(n)]]
 def step(self,n):
  k=self.kind(n)
  if k not in self.gates_kinds|{'ABc','ASc','ARc','ULc','U0c','U1c'}:return super().step(n)
  assert n in self.enabled()
  d=self.wires[n+'.p'].split('.')[0];h=self.kind(d)
  def node(kind,ports):return self.fresh(kind),ports
  def done(new,edges):
   a=node('DONE',('p',));new.append(a);edges.append((n+'.c',a[0]+'.p'))
  if k in self.gates_kinds:
   self.releases.append(n) # diagnostics, not readiness logic
   if k=='GM':
    c=node('COPY',('p','a','b'));q=node('QB',('p','a','r','c'));new=[c,q]
    edges=[(n+'.s',c[0]+'.p'),(n+'.r',c[0]+'.a'),(c[0]+'.b',q[0]+'.a'),(n+'.b',q[0]+'.p'),(n+'.o',q[0]+'.r'),(n+'.c',q[0]+'.c')]
   else:
    q=node('ABc' if k=='GA' else 'ULc',('p','a','r','c'));new=[q]
    edges=[(n+'.s',q[0]+('.a' if k=='GA' else '.p')),(n+'.b',q[0]+('.p' if k=='GA' else '.a')),(n+'.r',q[0]+'.r'),(n+'.c',q[0]+'.c')]
  elif k=='ABc':
   q=node('ARc' if h=='N' else 'ASc',('p','r','c') if h=='N' else ('p','a','r','c'));new=[q]
   edges=[(n+'.a',q[0]+'.p'),(n+'.r',q[0]+'.r'),(n+'.c',q[0]+'.c')]
   if h=='K':edges.append((d+'.a',q[0]+'.a'))
  elif k=='ASc':
   b=node('B0' if h=='N' else h,('p','a'));q=node('ABc',('p','a','r','c'));new=[b,q]
   edges=[(n+'.r',b[0]+'.p'),(b[0]+'.a',q[0]+'.r'),(n+'.a',q[0]+'.p'),(n+'.c',q[0]+'.c')]
   if h=='N':
    tail=node('N',('p',));new.append(tail);edges.append((tail[0]+'.p',q[0]+'.a'))
   else:edges.append((d+'.a',q[0]+'.a'))
  elif k=='ARc':
   b=node('B1',('p','a'));new=[b];edges=[(n+'.r',b[0]+'.p')]
   if h=='N':
    tail=node('N',('p',));new.append(tail);edges.append((b[0]+'.a',tail[0]+'.p'))
   else:edges.append((b[0]+'.a',d+'.a'))
   done(new,edges)
  elif k=='ULc':
   if h=='N':new=[];edges=[(n+'.a',n+'.r')];done(new,edges)
   else:
    q=node('U1c' if h=='B1' else 'U0c',('p','a','r','c'));new=[q]
    edges=[(n+'.a',q[0]+'.p'),(d+'.a',q[0]+'.a'),(n+'.r',q[0]+'.r'),(n+'.c',q[0]+'.c')]
  else:
   b=node('B1' if k=='U1c' or h=='B1' else 'B0',('p','a'));new=[b];edges=[(n+'.r',b[0]+'.p')]
   if h=='N':edges.append((b[0]+'.a',n+'.a'));done(new,edges)
   else:
    q=node('ULc',('p','a','r','c'));new.append(q)
    edges.extend([(b[0]+'.a',q[0]+'.r'),(n+'.a',q[0]+'.p'),(d+'.a',q[0]+'.a'),(n+'.c',q[0]+'.c')])
  self.replace((n,d),edges,new)
