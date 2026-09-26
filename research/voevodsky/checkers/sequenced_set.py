"""Compile straight-line set programs once; execution is only local rewrites.

No completion barrier: edges enforce prefix-demand dataflow sequencing.
Union operands are literal words compiled into independent linear inputs.
"""
from retained_union import UnionSet

class SequencedSet(UnionSet):
 def __init__(self,bits,program):
  bits=tuple(bits);program=list(program)
  assert all(b in (0,1) for b in bits)
  normalized=[]
  for op,arg in program:
   assert op in ('add','member','union')
   if op=='union':
    arg=tuple(arg);assert all(b in (0,1) for b in arg)
   else:assert isinstance(arg,int) and arg>=0
   normalized.append((op,arg))
  super().__init__(bits)
  source=self.wires.pop('RET.p');del self.wires[source]
  self.outputs=[]
  # Immutable tuple of compiler declarations, used only by proof diagnostics.
  self.stage_ops=tuple(op for op,arg in normalized)
  # Stage metadata is diagnostic only; never used to enable or dispatch rules.
  self.stage={n:-1 for n in self.types};self.current_stage=-1;self.history=[]
  for stage,(op,arg) in enumerate(normalized):
   before=set(self.types)
   if op=='add':
    a=self.fresh('AB');self.add(a,('p','a','r'))
    self.link(a+'.p',self.chain(('K',)*arg));self.link(a+'.a',source);source=a+'.r'
   elif op=='member':
    c=self.fresh('COPY');q=self.fresh('QB');o=self.fresh('OUT')
    self.add(c,('p','a','b'));self.add(q,('p','a','r'));self.add(o,('p',))
    self.link(c+'.p',source);self.link(c+'.b',q+'.a')
    self.link(q+'.p',self.chain(('K',)*arg));self.link(q+'.r',o+'.p')
    self.outputs.append(o);source=c+'.a'
   else:
    u=self.fresh('UL');self.add(u,('p','a','r'))
    self.link(u+'.p',source);self.link(u+'.a',self.chain(tuple('B1' if b else 'B0' for b in arg)));source=u+'.r'
   for n in set(self.types)-before:self.stage[n]=stage
  self.link('RET.p',source);self.audit()
 def step(self,n):
  self.current_stage=self.stage[n];self.history.append(self.current_stage)
  super().step(n)
 def replace(self,names,edges,new):
  super().replace(names,edges,new)
  for n,ps in new:self.stage[n]=self.current_stage
  for n in names:self.stage.pop(n,None)
 def execute(self,order='forward',limit=100000):
  while self.enabled():
   assert self.steps<limit,'test resource guard, not a normalization proof'
   choices=self.enabled()
   # Order can stress late or early stages; no stage-readiness condition.
   n=max(choices,key=lambda n:self.stage[n]) if order=='reverse' else min(choices,key=lambda n:self.stage[n])
   self.step(n)
  active={'COPY','QB','QS','QR','E','AB','AS','AR','UL','U0','U1'}
  assert not any(self.kind(n) in active for n in self.types),'stuck program'
  return self.retained(),tuple(self.answer(o) for o in self.outputs)
