"""Declarative data/phase families, installed into the manifest without execution."""
def install(rule):
 for h in ('B0','B1','N'):
  if h=='N':rule('COPY--N',[('N','p'),('N','p')],'x.a--0.p x.b--1.p')
  else:rule('COPY--'+h,[(h,'p a'),(h,'p a'),('COPY','p a b')],'x.a--0.p x.b--1.p 0.a--2.a 1.a--2.b y.a--2.p')
 for h in ('K','B0','B1','N'):
  rule('EA--'+h,[('DONE','p')] if h=='N' else [('EA','p r')],'x.r--0.p' if h=='N' else 'x.r--0.r y.a--0.p')
 for h in ('K','N'):
  rule('QB--'+h,[('QR','p r c')] if h=='N' else [('QS','p a r c')],'x.a--0.p x.r--0.r x.c--0.c'+(' y.a--0.a' if h=='K' else ''))
 for h in ('B0','B1'):
  rule('QS--'+h,[('QB','p a r c')],'x.a--0.p y.a--0.a x.r--0.r x.c--0.c')
  rule('QR--'+h,[('TRUE' if h=='B1' else 'FALSE','p'),('EA','p r')],'x.r--0.p y.a--1.p x.c--1.r')
 rule('QS--N',[('FALSE','p'),('EA','p r')],'x.r--0.p x.a--1.p x.c--1.r')
 rule('QR--N',[('FALSE','p'),('DONE','p')],'x.r--0.p x.c--1.p')
 for h in ('K','N'):
  rule('ABc--'+h,[('ARc','p r c')] if h=='N' else [('ASc','p a r c')],'x.a--0.p x.r--0.r x.c--0.c'+(' y.a--0.a' if h=='K' else ''))
 for h in ('B0','B1','N'):
  nodes=[('B0' if h=='N' else h,'p a'),('ABc','p a r c')]
  edges='x.r--0.p 0.a--1.r x.a--1.p x.c--1.c '
  if h=='N':nodes.append(('N','p'));edges+='2.p--1.a'
  else:edges+='y.a--1.a'
  rule('ASc--'+h,nodes,edges)
  nodes=[('B1','p a')];edges='x.r--0.p '
  if h=='N':nodes.append(('N','p'));edges+='0.a--1.p ';slot=2
  else:edges+='0.a--y.a ';slot=1
  nodes.append(('DONE','p'));rule('ARc--'+h,nodes,edges+f'x.c--{slot}.p')
  if h=='N':rule('ULc--N',[('DONE','p')],'x.a--x.r x.c--0.p')
  else:rule('ULc--'+h,[('U1c' if h=='B1' else 'U0c','p a r c')],'x.a--0.p y.a--0.a x.r--0.r x.c--0.c')
  for k in ('U0c','U1c'):
   nodes=[('B1' if k=='U1c' or h=='B1' else 'B0','p a')]
   if h=='N':nodes.append(('DONE','p'));edges='x.r--0.p 0.a--x.a x.c--1.p'
   else:nodes.append(('ULc','p a r c'));edges='x.r--0.p 0.a--1.r x.a--1.p y.a--1.a x.c--1.c'
   rule(k+'--'+h,nodes,edges)
 rule('DC--K',[('K','p a'),('K','p a'),('DC','p a b c')],'x.a--0.p x.b--1.p y.a--2.p 0.a--2.a 1.a--2.b x.c--2.c')
 rule('DC--N',[('N','p'),('N','p'),('DONE','p')],'x.a--0.p x.b--1.p x.c--2.p')
 rule('PREP--DONE',[('DC','p a b c'),('READY','p a b d q i r c')],'x.b--0.p x.a--1.a 0.a--1.b 0.b--1.d 0.c--1.p x.q--1.q x.i--1.i x.r--1.r x.c--1.c')
 rule('READY--DONE',[('DONE','p')],'x.a--x.q x.b--x.i x.d--x.r x.c--0.p')
 rule('FUEL--K',[('DC','p a b c'),('PREP','p a b q i r c'),('START','p s q i u f r o c')],'x.u--0.p 0.a--1.a 0.b--1.b 0.c--1.p 1.q--2.q 1.i--2.i 1.r--2.u 1.c--2.p y.a--2.f x.s--2.s x.r--2.r x.o--2.o x.c--2.c')
 rule('FUEL--N',[('EA','p r'),('FINISH','p o c'),('EXHAUSTED','p'),('TOKEN','p')],'x.u--0.p 0.r--1.p x.s--x.r x.o--2.p x.c--1.c 3.p--1.o')
 rule('START--DONE',[('COPY','p a b'),('QB','p a r c'),('TEST','p b s i u f r o c')],'x.s--0.p 0.a--2.s 0.b--1.a x.q--1.p 1.r--2.b 1.c--2.p x.i--2.i x.u--2.u x.f--2.f x.r--2.r x.o--2.o x.c--2.c')
 rule('TEST--DONE',[('CHOOSE','p s i u f r o c')],'x.b--0.p x.s--0.s x.i--0.i x.u--0.u x.f--0.f x.r--0.r x.o--0.o x.c--0.c')
 rule('CHOOSE--FALSE',[('ABc','p a r c'),('NEXT','p s u f r o c')],'x.i--0.p x.s--0.a 0.r--1.s 0.c--1.p x.u--1.u x.f--1.f x.r--1.r x.o--1.o x.c--1.c')
 rule('NEXT--DONE',[('FUEL','p s u r o c'),('K','p a')],'x.f--0.p x.u--1.a 1.p--0.u x.s--0.s x.r--0.r x.o--0.o x.c--0.c')
 rule('CHOOSE--TRUE',[('EA','p r'),('CLEAN','p u f o c'),('FOUND','p'),('TOKEN','p')],'x.i--0.p 0.r--1.p x.s--x.r x.o--2.p x.u--1.u x.f--1.f x.c--1.c 3.p--1.o')
 rule('CLEAN--DONE',[('EA','p r'),('DRAIN','p f o c')],'x.u--0.p 0.r--1.p x.f--1.f x.o--1.o x.c--1.c')
 rule('DRAIN--DONE',[('EA','p r'),('FINISH','p o c')],'x.f--0.p 0.r--1.p x.o--1.o x.c--1.c')
 rule('FINISH--DONE',[('SEAL','p c')],'x.o--0.p x.c--0.c')
 rule('SEAL--TOKEN',[('DONE','p')],'x.c--0.p')
