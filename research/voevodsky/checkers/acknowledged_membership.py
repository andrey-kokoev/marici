"""Single retained query with a linear cleanup return; not a continuation gate."""
from retained_membership import RetainedMembership

class AcknowledgedMembership(RetainedMembership):
 def __init__(self,bits,index):
  super().__init__(bits);self.out=self.start(index)
  q=next(n for n in self.types if self.kind(n)=='QB')
  self.types[q]=self.types[q]+('c',)
  self.add('ACK',('p',));self.link(q+'.c','ACK.p');self.audit()
 def enabled(self):
  return super().enabled()+[n for n in self.types if self.kind(n)=='EA' and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0]) in ('B0','B1','K','N')]
 def step(self,n):
  k=self.kind(n)
  if k=='COPY':return super().step(n)
  assert n in self.enabled()
  d=self.wires[n+'.p'].split('.')[0];h=self.kind(d)
  def node(kind,ports):return self.fresh(kind),ports
  if k=='EA':
   x=node('DONE' if h=='N' else 'EA',('p',) if h=='N' else ('p','r'));new=[x]
   edges=[(n+'.r',x[0]+('.p' if h=='N' else '.r'))]
   if h!='N':edges.append((d+'.a',x[0]+'.p'))
  elif k=='QB':
   q=node('QR' if h=='N' else 'QS',('p','r','c') if h=='N' else ('p','a','r','c'));new=[q]
   edges=[(n+'.a',q[0]+'.p'),(n+'.r',q[0]+'.r'),(n+'.c',q[0]+'.c')]
   if h!='N':edges.append((d+'.a',q[0]+'.a'))
  elif k=='QS' and h!='N':
   q=node('QB',('p','a','r','c'));new=[q]
   edges=[(n+'.a',q[0]+'.p'),(d+'.a',q[0]+'.a'),(n+'.r',q[0]+'.r'),(n+'.c',q[0]+'.c')]
  else:
   assert k in ('QS','QR')
   b=node('TRUE' if k=='QR' and h=='B1' else 'FALSE',('p',));new=[b];edges=[(n+'.r',b[0]+'.p')]
   if k=='QS' or h!='N':
    e=node('EA',('p','r'));new.append(e)
    edges.extend([(n+'.a' if k=='QS' else d+'.a',e[0]+'.p'),(n+'.c',e[0]+'.r')])
   else:
    done=node('DONE',('p',));new.append(done);edges.append((n+'.c',done[0]+'.p'))
  self.replace((n,d),edges,new)
 def acknowledged(self):return self.kind(self.wires['ACK.p'].split('.')[0])=='DONE'
