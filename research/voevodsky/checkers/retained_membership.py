"""Fixed-signature retained membership. start() is caller-side interface plugging.

No input word is saved for reuse: subsequent calls consume the actual RET chain.
"""
class RetainedMembership:
 def __init__(self,bits):
  self.types={};self.wires={};self.serial=0;self.steps=0
  self.add('RET',('p',));self.link('RET.p',self.chain(tuple('B1' if b else 'B0' for b in bits)))
  self.audit()
 def add(self,n,ports):
  assert n not in self.types;self.types[n]=tuple(ports)
 def fresh(self,k):
  self.serial+=1;return k+'_'+str(self.serial)
 def link(self,p,q):
  assert p!=q and p not in self.wires and q not in self.wires
  self.wires[p]=q;self.wires[q]=p
 def audit(self):
  assert set(self.wires)=={n+'.'+p for n,ps in self.types.items() for p in ps}
  assert all(p!=q and self.wires.get(q)==p for p,q in self.wires.items())
 def chain(self,kinds):
  n=self.fresh('N');self.add(n,('p',));tail=n+'.p'
  for k in reversed(kinds):
   n=self.fresh(k);self.add(n,('p','a'));self.link(n+'.a',tail);tail=n+'.p'
  return tail
 @staticmethod
 def kind(n):return n.split('_')[0]
 def enabled(self):
  allowed={'COPY':{'B0','B1','N'},'QB':{'K','N'},'QS':{'B0','B1','N'},'QR':{'B0','B1','N'},'E':{'B0','B1','K','N'}}
  return [n for n in self.types if self.kind(n) in allowed and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0]) in allowed[self.kind(n)]]
 def retained(self):
  p=self.wires['RET.p'];out=[];seen=set()
  while True:
   n,port=p.split('.');assert port=='p' and n not in seen;seen.add(n)
   k=self.kind(n)
   if k=='N':return tuple(out)
   assert k in ('B0','B1');out.append(int(k=='B1'));p=self.wires[n+'.a']
 def start(self,index):
  assert isinstance(index,int) and index>=0
  assert not any(self.kind(n) in ('COPY','QB','QS','QR','E') for n in self.types)
  self.retained() # require a completed chain, not a pending frontier
  head=self.wires.pop('RET.p');del self.wires[head]
  c=self.fresh('COPY');q=self.fresh('QB');o=self.fresh('OUT')
  self.add(c,('p','a','b'));self.add(q,('p','a','r'));self.add(o,('p',))
  budget=self.chain(('K',)*index)
  for a,b in [(c+'.p',head),(c+'.a','RET.p'),(c+'.b',q+'.a'),(q+'.p',budget),(q+'.r',o+'.p')]:self.link(a,b)
  self.audit();return o
 def answer(self,out):
  k=self.kind(self.wires[out+'.p'].split('.')[0]);assert k in ('TRUE','FALSE');return k=='TRUE'
 def replace(self,names,edges,new):
  exposed={}
  for n in names:
   for p in self.types[n]:
    x=n+'.'+p
    if x not in self.wires:continue
    y=self.wires.pop(x);del self.wires[y]
    if y.split('.')[0] not in names:exposed[x]=y
   del self.types[n]
  for n,ps in new:self.add(n,ps)
  for a,b in edges:self.link(exposed.get(a,a),exposed.get(b,b))
  self.steps+=1;self.audit()
 def step(self,n):
  assert n in self.enabled()
  d=self.wires[n+'.p'].split('.')[0];k=self.kind(n);h=self.kind(d)
  def node(kind,ports):return (self.fresh(kind),ports)
  if k=='COPY':
   if h=='N':
    l=node('N',('p',));r=node('N',('p',));new=[l,r];edges=[(n+'.a',l[0]+'.p'),(n+'.b',r[0]+'.p')]
   else:
    l=node(h,('p','a'));r=node(h,('p','a'));c=node('COPY',('p','a','b'));new=[l,r,c]
    edges=[(n+'.a',l[0]+'.p'),(n+'.b',r[0]+'.p'),(l[0]+'.a',c[0]+'.a'),(r[0]+'.a',c[0]+'.b'),(d+'.a',c[0]+'.p')]
  elif k=='E':
   if h=='N':new=[];edges=[]
   else:
    e=node('E',('p',));new=[e];edges=[(d+'.a',e[0]+'.p')]
  elif k=='QB':
   q=node('QR' if h=='N' else 'QS',('p','r') if h=='N' else ('p','a','r'));new=[q]
   edges=[(n+'.a',q[0]+'.p'),(n+'.r',q[0]+'.r')]
   if h!='N':edges.append((d+'.a',q[0]+'.a'))
  elif k=='QS' and h!='N':
   q=node('QB',('p','a','r'));new=[q];edges=[(n+'.a',q[0]+'.p'),(d+'.a',q[0]+'.a'),(n+'.r',q[0]+'.r')]
  else:
   b=node('TRUE' if k=='QR' and h=='B1' else 'FALSE',('p',));new=[b];edges=[(n+'.r',b[0]+'.p')]
   if k=='QS' or h!='N':
    e=node('E',('p',));new.append(e);edges.append((n+'.a' if k=='QS' else d+'.a',e[0]+'.p'))
  self.replace((n,d),edges,new)
 def run(self,priority=('COPY','QB','QS','QR','E')):
  while self.enabled():self.step(min(self.enabled(),key=lambda n:priority.index(self.kind(n))))
  assert not any(self.kind(n) in ('COPY','QB','QS','QR','E') for n in self.types)
  self.retained()
