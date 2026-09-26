"""Local unary insertion on the retained membership interface; calls are host-wired."""
from retained_membership import RetainedMembership

class RetainedSet(RetainedMembership):
 def insert(self,index):
  assert isinstance(index,int) and index>=0
  assert not any(self.kind(n) in ('COPY','QB','QS','QR','E','AB','AS','AR') for n in self.types)
  self.retained()
  head=self.wires.pop('RET.p');del self.wires[head]
  a=self.fresh('AB');self.add(a,('p','a','r'))
  budget=self.chain(('K',)*index)
  self.link(a+'.p',budget);self.link(a+'.a',head);self.link(a+'.r','RET.p');self.audit()
 def enabled(self):
  allowed={'AB':{'K','N'},'AS':{'B0','B1','N'},'AR':{'B0','B1','N'}}
  return super().enabled()+[n for n in self.types if self.kind(n) in allowed and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0]) in allowed[self.kind(n)]]
 def step(self,n):
  k=self.kind(n)
  if k not in ('AB','AS','AR'):return super().step(n)
  assert n in self.enabled()
  d=self.wires[n+'.p'].split('.')[0];h=self.kind(d)
  def node(kind,ports):return self.fresh(kind),ports
  if k=='AB':
   a=node('AR' if h=='N' else 'AS',('p','r') if h=='N' else ('p','a','r'))
   new=[a];edges=[(n+'.a',a[0]+'.p'),(n+'.r',a[0]+'.r')]
   if h=='K':edges.append((d+'.a',a[0]+'.a'))
  elif k=='AS':
   b=node('B0' if h=='N' else h,('p','a'));a=node('AB',('p','a','r'));new=[b,a]
   edges=[(n+'.r',b[0]+'.p'),(b[0]+'.a',a[0]+'.r'),(n+'.a',a[0]+'.p')]
   if h=='N':
    tail=node('N',('p',));new.append(tail);edges.append((tail[0]+'.p',a[0]+'.a'))
   else:edges.append((d+'.a',a[0]+'.a'))
  else:
   b=node('B1',('p','a'));new=[b];edges=[(n+'.r',b[0]+'.p')]
   if h=='N':
    tail=node('N',('p',));new.append(tail);edges.append((b[0]+'.a',tail[0]+'.p'))
   else:edges.append((b[0]+'.a',d+'.a'))
  self.replace((n,d),edges,new)
 def run(self,priority=('AB','AS','AR','COPY','QB','QS','QR','E')):
  while self.enabled():self.step(min(self.enabled(),key=lambda n:priority.index(self.kind(n))))
  assert not any(self.kind(n) in ('AB','AS','AR','COPY','QB','QS','QR','E') for n in self.types)
  self.retained()
