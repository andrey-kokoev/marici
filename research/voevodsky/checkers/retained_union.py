"""Two-input local OR zipper; union_from moves donor support, leaving it empty."""
from retained_set import RetainedSet

class UnionSet(RetainedSet):
 def union_from(self,other):
  assert isinstance(other,UnionSet) and other is not self
  active={'COPY','QB','QS','QR','E','AB','AS','AR','UL','U0','U1'}
  for net in (self,other):
   assert not any(net.kind(n) in active for n in net.types)
   net.audit();net.retained()
  # Move the actual donor chain, alpha-renaming to receiver-fresh names.
  old_head=other.wires['RET.p'];nodes=[];p=old_head
  while True:
   n,_=p.split('.');nodes.append(n)
   if other.kind(n)=='N':break
   p=other.wires[n+'.a']
  mapping={n:self.fresh(other.kind(n)) for n in nodes}
  internal=[(p,q) for p,q in other.wires.items() if p.split('.')[0] in mapping and q.split('.')[0] in mapping and p<q]
  def rename(p):
   n,port=p.split('.');return mapping[n]+'.'+port
  for n in nodes:self.add(mapping[n],other.types[n])
  for p,q in internal:self.link(rename(p),rename(q))
  for n in nodes:
   for port in other.types[n]:
    p=n+'.'+port
    if p in other.wires:
     q=other.wires.pop(p);del other.wires[q]
   del other.types[n]
  other.link('RET.p',other.chain(()));other.audit()
  left=self.wires.pop('RET.p');del self.wires[left]
  u=self.fresh('UL');self.add(u,('p','a','r'))
  for p,q in [(u+'.p',left),(u+'.a',rename(old_head)),(u+'.r','RET.p')]:self.link(p,q)
  self.audit()
 def enabled(self):
  return super().enabled()+[n for n in self.types if self.kind(n) in ('UL','U0','U1') and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0]) in ('B0','B1','N')]
 def step(self,n):
  k=self.kind(n)
  if k not in ('UL','U0','U1'):return super().step(n)
  assert n in self.enabled()
  d=self.wires[n+'.p'].split('.')[0];h=self.kind(d)
  if k=='UL':
   if h=='N':new=[];edges=[(n+'.a',n+'.r')]
   else:
    u=self.fresh('U1' if h=='B1' else 'U0');new=[(u,('p','a','r'))]
    edges=[(n+'.a',u+'.p'),(d+'.a',u+'.a'),(n+'.r',u+'.r')]
  else:
   b=self.fresh('B1' if k=='U1' or h=='B1' else 'B0');new=[(b,('p','a'))];edges=[(n+'.r',b+'.p')]
   if h=='N':edges.append((b+'.a',n+'.a'))
   else:
    u=self.fresh('UL');new.append((u,('p','a','r')))
    edges.extend([(b+'.a',u+'.r'),(n+'.a',u+'.p'),(d+'.a',u+'.a')])
  self.replace((n,d),edges,new)
 def run(self,priority=('UL','U0','U1','AB','AS','AR','COPY','QB','QS','QR','E')):
  while self.enabled():self.step(min(self.enabled(),key=lambda n:priority.index(self.kind(n))))
  assert not any(self.kind(n) in priority for n in self.types)
  self.retained()
