"""Structural recognition, not execution of the production compiler."""
from pure_replacement import validate,require
from program_inputs import word,program

def recognize(types,wires,bits,instructions,outputs,tags):
 bits=word(bits);ops=program(instructions,{'member','add','union','ifadd','scan'});validate(types,wires);used=set()
 def take(n,kind,ports):
  require(n not in used and n.split('_')[0]==kind and set(types[n])==set(ports.split()),'wrong/shared agent');used.add(n)
 def chain(port,kinds):
  p=wires[port]
  for kind in list(kinds)+['N']:
   n,label=p.split('.');require(label=='p','wrong chain orientation');take(n,kind,'p' if kind=='N' else 'p a')
   if kind!='N':p=wires[n+'.a']
 take('RET','RET','p');take('ACK','ACK','p')
 # Read instruction order backwards from the final continuation, not metadata.
 support='RET.p';ack='ACK.p';found=[]
 for op,arg in reversed(ops):
  g,port=wires[support].split('.');require(port=='r' and wires[ack]==g+'.c','split continuation')
  kind={'member':'GM','add':'GA','union':'GU','ifadd':'GC','scan':'GS'}[op]
  ports='p s r b c'+(' o' if op in ('member','ifadd','scan') else '')+(' t f' if op=='ifadd' else ' f' if op=='scan' else '')
  take(g,kind,ports)
  if op=='union':chain(g+'.b',('B1' if x else 'B0' for x in arg))
  else:
   index=arg[0] if op in ('scan','ifadd') else arg;chain(g+'.b',('K',)*index)
   if op=='scan':chain(g+'.f',('K',)*arg[1])
   elif op=='ifadd':chain(g+'.t',('K',)*arg[1]);chain(g+'.f',('K',)*arg[2])
  if op in ('member','ifadd','scan'):
   root,p=wires[g+'.o'].split('.');require(p=='p','bad observation orientation');take(root,'OUT','p');found.append((root,'scan' if op=='scan' else 'boolean'))
  support=g+'.s';ack=g+'.p'
 chain(support,('B1' if x else 'B0' for x in bits))
 done,p=wires[ack].split('.');require(p=='p','bad initial acknowledgment');take(done,'DONE','p')
 require(list(reversed(found))==list(zip(outputs,tags)) and len(outputs)==len(tags)==len(found),'observation declaration mismatch')
 require(used==set(types),'unaccounted initial nodes')
 return {'recognized':True,'instructions':len(ops),'observations':len(found),'scope':'structural declaration match; not authenticated construction history'}
