"""Interpret live queries by virtually completing COPY; assumes typed invariant."""
def support(net,port):
 bits=[];seen=set()
 while True:
  assert port not in seen;seen.add(port)
  name,p=port.split('.');kind=name.split('_')[0]
  if kind=='COPY':
   assert p in ('a','b');port=net.wires[name+'.p'];continue
  assert p=='p'
  if kind=='N':return tuple(bits)
  assert kind in ('B0','B1')
  bits.append(kind=='B1');port=net.wires[name+'.a']

def budget(net,port):
 k=0;seen=set()
 while True:
  assert port not in seen;seen.add(port)
  name,p=port.split('.');assert p=='p'
  kind=name.split('_')[0]
  if kind=='N':return k
  assert kind=='K';k+=1;port=net.wires[name+'.a']

def values(net):
 result=[]
 for channel in (1,2):
  name,p=net.wires['OUT'+str(channel)+'.p'].split('.')
  kind=name.split('_')[0]
  if kind in ('TRUE','FALSE'):
   assert p=='p';result.append(kind=='TRUE');continue
  assert name.startswith('Q'+str(channel)) and p=='r'
  phase=name[2:].split('_')[0]
  word=support(net,net.wires[name+('.a' if phase=='B' else '.p')])
  index=budget(net,net.wires[name+'.p']) if phase=='B' else (budget(net,net.wires[name+'.a'])+1 if phase=='S' else 0)
  assert phase in ('B','S','R')
  result.append(index<len(word) and word[index])
 return tuple(result)
