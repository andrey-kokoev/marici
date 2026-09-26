"""Runtime fuel-bounded scanner. No instruction unrolling or host cursor state."""
from strict_set_program import StrictSetProgram
from retained_membership import RetainedMembership
from triple_cursor import TripleCursor
from acknowledged_unary_copy import AcknowledgedUnaryCopy
from program_inputs import word, natural

class FuelScanner(StrictSetProgram):
 def __init__(self,bits,cursor,fuel):
  bits=word(bits);cursor=natural(cursor);fuel=natural(fuel)
  RetainedMembership.__init__(self,bits)
  self.add('ACK',('p',));self.add('OUTCOME',('p',))
  s=self.wires.pop('RET.p');del self.wires[s]
  g=self.fresh('FUEL');self.add(g,('p','s','u','r','o','c'))
  for p,q in [('p',self.chain(('K',)*fuel)),('s',s),('u',self.chain(('K',)*cursor)),('r','RET.p'),('o','OUTCOME.p'),('c','ACK.p')]:self.link(g+'.'+p,q)
  self.audit()
 def observe(self):
  """Pending-aware terminal outcome; support is public only at final ACK."""
  peer=self.wires['OUTCOME.p'];kind=self.kind(peer.split('.')[0])
  outcome=kind if peer.endswith('.p') and kind in ('FOUND','EXHAUSTED') else None
  peer=self.wires['ACK.p'];complete=peer.endswith('.p') and self.kind(peer.split('.')[0])=='DONE'
  return {'outcome':outcome,'complete':complete,'word':self.retained() if complete else None}
 def enabled(self):
  allowed={'DC':{'K','N'},'PREP':{'DONE'},'READY':{'DONE'},'FUEL':{'K','N'},'START':{'DONE'},'TEST':{'DONE'},'CHOOSE':{'TRUE','FALSE'},'NEXT':{'DONE'},'CLEAN':{'DONE'},'FINISH':{'DONE'},'DRAIN':{'DONE'},'SEAL':{'TOKEN'}}
  return super().enabled()+[n for n in self.types if self.kind(n) in allowed and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0]) in allowed[self.kind(n)]]
 def step(self,n):
  k=self.kind(n)
  if k=='DC':return AcknowledgedUnaryCopy.step(self,n)
  if k in ('PREP','READY'):return TripleCursor.step(self,n)
  if k not in ('FUEL','START','TEST','CHOOSE','NEXT','CLEAN','FINISH','DRAIN','SEAL'):return super().step(n)
  assert n in self.enabled();d=self.wires[n+'.p'].split('.')[0];h=self.kind(d)
  new=[];edges=[]
  def node(kind,ports):
   x=self.fresh(kind);new.append((x,tuple(ports.split())));return x
  def forward(x,ports):edges.extend((n+'.'+p,x+'.'+p) for p in ports.split())
  if k=='FUEL' and h=='K':
   dc=node('DC','p a b c');prep=node('PREP','p a b q i r c');g=node('START','p s q i u f r o c')
   edges.extend([(n+'.u',dc+'.p'),(dc+'.a',prep+'.a'),(dc+'.b',prep+'.b'),(dc+'.c',prep+'.p'),(prep+'.q',g+'.q'),(prep+'.i',g+'.i'),(prep+'.r',g+'.u'),(prep+'.c',g+'.p'),(d+'.a',g+'.f')]);forward(g,'s r o c')
  elif k=='FUEL':
   # Outcome is early; final ACK waits for cursor cleanup.
   e=node('EA','p r');g=node('FINISH','p o c');v=node('EXHAUSTED','p')
   edges.extend([(n+'.u',e+'.p'),(e+'.r',g+'.p'),(n+'.s',n+'.r'),(n+'.o',v+'.p'),(n+'.c',g+'.c')])
   # FINISH needs an output slot to consume: carry a private token instead.
   token=node('TOKEN','p');edges.append((token+'.p',g+'.o'))
  elif k=='START':
   cp=node('COPY','p a b');q=node('QB','p a r c');g=node('TEST','p b s i u f r o c')
   edges.extend([(n+'.s',cp+'.p'),(cp+'.a',g+'.s'),(cp+'.b',q+'.a'),(n+'.q',q+'.p'),(q+'.r',g+'.b'),(q+'.c',g+'.p')]);forward(g,'i u f r o c')
  elif k=='TEST':
   g=node('CHOOSE','p s i u f r o c');edges.append((n+'.b',g+'.p'));forward(g,'s i u f r o c')
  elif k=='CHOOSE' and h=='FALSE':
   a=node('ABc','p a r c');g=node('NEXT','p s u f r o c')
   edges.extend([(n+'.i',a+'.p'),(n+'.s',a+'.a'),(a+'.r',g+'.s'),(a+'.c',g+'.p')]);forward(g,'u f r o c')
  elif k=='NEXT':
   g=node('FUEL','p s u r o c');cell=node('K','p a')
   edges.extend([(n+'.f',g+'.p'),(n+'.u',cell+'.a'),(cell+'.p',g+'.u')]);forward(g,'s r o c')
  elif k=='CHOOSE':
   # Serial cleanup of insertion budget, retained cursor, then residual fuel.
   e=node('EA','p r');g=node('CLEAN','p u f o c');v=node('FOUND','p')
   edges.extend([(n+'.i',e+'.p'),(e+'.r',g+'.p'),(n+'.s',n+'.r'),(n+'.o',v+'.p')]);forward(g,'u f c')
   token=node('TOKEN','p');edges.append((token+'.p',g+'.o'))
  elif k=='CLEAN':
   e=node('EA','p r');g=node('DRAIN','p f o c')
   edges.extend([(n+'.u',e+'.p'),(e+'.r',g+'.p')]);forward(g,'f o c')
  elif k=='DRAIN':
   e=node('EA','p r');g=node('FINISH','p o c')
   edges.extend([(n+'.f',e+'.p'),(e+'.r',g+'.p')]);forward(g,'o c')
  elif k=='SEAL':
   g=node('DONE','p');edges.append((n+'.c',g+'.p'))
  else:
   # Final acknowledgment; remove private token via a separate principal rule.
   g=node('SEAL','p c');edges.extend([(n+'.o',g+'.p'),(n+'.c',g+'.c')])
  self.replace((n,d),edges,new)
