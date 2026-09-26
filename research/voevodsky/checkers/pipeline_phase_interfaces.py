"""Necessary phase/causality clauses; not a complete reachable-state grammar."""
controls={'COPY','QB','QS','QR','E','AB','AS','AR','UL','U0','U1'}
producers={('COPY','a'),('COPY','b'),('AB','r'),('AS','r'),('AR','r'),('UL','r'),('U0','r'),('U1','r')}

def validate(net):
 net.audit()
 def endpoint(n,port,types,wait=False,own=False):
  other,p=net.wires[n+'.'+port].split('.')
  k=net.kind(other);s=net.stage[n];t=net.stage[other]
  assert t<=s,(n,port,other,'backwards stage')
  if p=='p':
   assert k in types,(n,port,other,'wrong data type')
   if own:assert t==s
  else:
   assert wait and (k,p) in producers,(n,port,other,p,'invalid wait')
   if t==s:assert net.kind(n) in ('QB','QS','QR','E') and k=='COPY'
  if net.kind(n)=='COPY':assert t<s
 for n in net.types:
  k=net.kind(n)
  if k not in controls:continue
  if k in ('QB','AB'):endpoint(n,'p',{'K','N'},own=True)
  elif k in ('U0','U1'):endpoint(n,'p',{'B0','B1','N'},own=True)
  elif k=='E':endpoint(n,'p',{'B0','B1','K','N'},True)
  else:endpoint(n,'p',{'B0','B1','N'},True)
  if k in ('QB','AB','U0','U1'):endpoint(n,'a',{'B0','B1','N'},True)
  elif k in ('QS','AS'):endpoint(n,'a',{'K','N'},own=True)
  elif k=='UL':endpoint(n,'a',{'B0','B1','N'},own=True)
 # Conditional minimal-rank progress witness.
 live=[n for n in net.types if net.kind(n) in controls]
 if live:
  least=min(live,key=lambda n:(net.stage[n],0 if net.kind(n)=='COPY' else 1))
  assert least in net.enabled(),('minimal consumer blocked',least)
 return True
