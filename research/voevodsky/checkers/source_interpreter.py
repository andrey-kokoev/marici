"""Direct finite-word semantics; no graph, rule manifest, or reducer imports."""
from program_inputs import word,program

def interpret(bits,instructions):
 w=list(word(bits));observations=[]
 def member(i):return i<len(w) and w[i]==1
 def add(i):
  if i>=len(w):w.extend([0]*(i+1-len(w)))
  w[i]=1
 for op,a in program(instructions,{'member','add','union','ifadd','scan'}):
  if op=='member':observations.append(('boolean',member(a)))
  elif op=='add':add(a)
  elif op=='union':
   for i,b in enumerate(a):
    if i>=len(w):w.append(b)
    elif b:w[i]=1
  elif op=='ifadd':
   i,t,f=a;answer=member(i);observations.append(('boolean',answer));add(t if answer else f)
  else:
   cursor,fuel=a;outcome='EXHAUSTED'
   while fuel:
    fuel-=1
    if member(cursor):outcome='FOUND';break
    add(cursor);cursor+=1
   observations.append(('scan',outcome))
 return {'word':tuple(w),'observations':tuple(observations)}
