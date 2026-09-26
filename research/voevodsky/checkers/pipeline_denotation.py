"""Read-only live observation interpreter; does not reduce or consult program input."""
from functools import lru_cache

def observe(net):
 visiting=set()
 def add(s,i):
  s=list(s)+[0]*max(0,i+1-len(s));s[i]=1;return tuple(s)
 def union(s,t):return tuple(int((i<len(s) and s[i]) or (i<len(t) and t[i])) for i in range(max(len(s),len(t))))
 def peer(n,p):return net.wires[n+'.'+p]
 def budget(p):
  seen=set();k=0
  while True:
   assert p not in seen;seen.add(p)
   n,port=p.split('.');assert port=='p'
   kind=net.kind(n)
   if kind=='N':return k
   assert kind=='K';k+=1;p=peer(n,'a')
 @lru_cache(None)
 def word(p):
  assert p not in visiting,('cyclic denotation',p)
  visiting.add(p)
  n,port=p.split('.');kind=net.kind(n)
  if port=='p':
   if kind=='N':result=()
   else:
    assert kind in ('B0','B1');result=(int(kind=='B1'),)+word(peer(n,'a'))
  elif kind=='COPY':
   assert port in ('a','b');result=word(peer(n,'p'))
  else:
   assert port=='r'
   if kind=='AB':result=add(word(peer(n,'a')),budget(peer(n,'p')))
   elif kind=='AS':result=add(word(peer(n,'p')),budget(peer(n,'a'))+1)
   elif kind=='AR':result=add(word(peer(n,'p')),0)
   elif kind=='UL':result=union(word(peer(n,'p')),word(peer(n,'a')))
   else:
    assert kind in ('U0','U1');result=union((int(kind=='U1'),)+word(peer(n,'a')),word(peer(n,'p')))
  visiting.remove(p);return result
 answers=[]
 for out in net.outputs:
  n,p=peer(out,'p').split('.');kind=net.kind(n)
  if kind in ('TRUE','FALSE'):
   assert p=='p';answers.append(kind=='TRUE');continue
  assert p=='r' and kind in ('QB','QS','QR')
  s=word(peer(n,'a' if kind=='QB' else 'p'))
  i=budget(peer(n,'p')) if kind=='QB' else budget(peer(n,'a'))+1 if kind=='QS' else 0
  answers.append(i<len(s) and bool(s[i]))
 return word(peer('RET','p')),tuple(answers)
