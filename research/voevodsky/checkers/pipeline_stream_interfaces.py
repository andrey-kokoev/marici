"""Recursive consumer-tail ceilings, stopping at explicitly typed producers."""
from pipeline_phase_interfaces import validate as heads,controls,producers

def validate(net):
 heads(net)
 def walk(n,port,types,own=False,wait=False):
  cursor=net.wires[n+'.'+port];seen=set();s=net.stage[n]
  while True:
   assert cursor not in seen,('cycle',n,port);seen.add(cursor)
   other,p=cursor.split('.');k=net.kind(other);t=net.stage[other]
   assert t<=s,(n,port,other,'tail exceeds ceiling')
   if net.kind(n)=='COPY':assert t<s
   if p!='p':
    assert wait and (k,p) in producers
    if t==s:assert net.kind(n) in ('QB','QS','QR','E') and k=='COPY'
    return
   assert k in types,(n,port,other,'tail type')
   if own:assert t==s
   if k=='N':return
   cursor=net.wires[other+'.a']
 for n in net.types:
  k=net.kind(n)
  if k not in controls:continue
  if k in ('QB','AB'):walk(n,'p',{'K','N'},True)
  elif k in ('U0','U1'):walk(n,'p',{'B0','B1','N'},True)
  else:walk(n,'p',{'B0','B1','K','N'} if k=='E' else {'B0','B1','N'},wait=True)
  if k in ('QB','AB','U0','U1'):walk(n,'a',{'B0','B1','N'},wait=True)
  elif k in ('QS','AS'):walk(n,'a',{'K','N'},True)
  elif k=='UL':walk(n,'a',{'B0','B1','N'},True)
 return True
