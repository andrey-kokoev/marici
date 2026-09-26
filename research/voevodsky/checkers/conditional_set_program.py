"""Finite mixed programs with ifadd(i,t,f), compiled before any reduction."""
from strict_set_program import StrictSetProgram
from conditional_insertion import ConditionalInsertion
from program_inputs import word, program as normalize_program

class ConditionalSetProgram(ConditionalInsertion):
 gates_kinds=StrictSetProgram.gates_kinds|{'GC'}
 work=StrictSetProgram.work|{'WAIT','PICK','JOIN','JOINR'}
 def __init__(self,bits,program):
  bits=word(bits);program=normalize_program(program,{'member','add','union','ifadd'});base=[];branches={}
  for index,(op,arg) in enumerate(program):
   if op=='ifadd':
    arg=tuple(arg);assert len(arg)==3 and all(type(x) is int and x>=0 for x in arg)
    branches[index]=arg;base.append(('member',arg[0]))
   else:base.append((op,arg))
  StrictSetProgram.__init__(self,bits,base)
  # Replace each placeholder GM before execution, preserving its outside peers.
  for index,(i,t,f) in branches.items():
   old=self.gates[index];g=self.fresh('GC');ports=self.types[old]
   self.add(g,ports+('t','f'))
   for p in ports:
    peer=self.wires.pop(old+'.'+p);del self.wires[peer];self.link(g+'.'+p,peer)
   del self.types[old]
   self.link(g+'.t',self.chain(('K',)*t));self.link(g+'.f',self.chain(('K',)*f));self.gates[index]=g
  self.audit()
 def observe(self):
  """Read-only snapshot for valid constructed nets; readiness is not completion.

  None is pending, False is a published negative result. The support word is
  exposed only at final ACK. This does not validate arbitrary imported nets.
  """
  values=[]
  for out in self.outputs:
   peer=self.wires[out+'.p'];kind=self.kind(peer.split('.')[0])
   values.append(kind=='TRUE' if peer.endswith('.p') and kind in ('TRUE','FALSE') else None)
  peer=self.wires['ACK.p']
  complete=peer.endswith('.p') and self.kind(peer.split('.')[0])=='DONE'
  return {'snapshots':tuple(values),'complete':complete,'word':self.retained() if complete else None}
 def enabled(self):
  return super().enabled()+[n for n in self.types if self.kind(n)=='GC' and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0])=='DONE']
 def step(self,n):
  if self.kind(n)!='GC':return super().step(n)
  assert n in self.enabled()
  d=self.wires[n+'.p'].split('.')[0]
  c=self.fresh('COPY');q=self.fresh('QB');w=self.fresh('WAIT')
  new=[(c,('p','a','b')),(q,('p','a','r','c')),(w,('p','b','s','r','t','f','o','c'))]
  edges=[(n+'.s',c+'.p'),(c+'.a',w+'.s'),(c+'.b',q+'.a'),(n+'.b',q+'.p'),(q+'.r',w+'.b'),(q+'.c',w+'.p')]+[(n+'.'+p,w+'.'+p) for p in ('r','t','f','o','c')]
  self.replace((n,d),edges,new);self.releases.append(n)
