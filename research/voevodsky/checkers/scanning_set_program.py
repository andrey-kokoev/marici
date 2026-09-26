"""Mixed finite programs with runtime scan and typed observation slots."""
from conditional_set_program import ConditionalSetProgram
from fuel_scanner import FuelScanner
from program_inputs import word, program as normalize_program

class ScanningSetProgram(ConditionalSetProgram,FuelScanner):
 gates_kinds=ConditionalSetProgram.gates_kinds|{'GS'}
 work=ConditionalSetProgram.work|{'DC','PREP','READY','FUEL','START','TEST','CHOOSE','NEXT','CLEAN','DRAIN','FINISH','SEAL'}
 def __init__(self,bits,program):
  bits=word(bits);program=normalize_program(program,{'member','add','union','ifadd','scan'})
  base=[];scans={};self.output_types=[]
  for index,(op,arg) in enumerate(program):
   if op=='scan':
    arg=tuple(arg);assert len(arg)==2 and all(type(x) is int and x>=0 for x in arg)
    scans[index]=arg;base.append(('member',arg[0]));self.output_types.append('scan')
   else:
    base.append((op,arg))
    if op in ('member','ifadd'):self.output_types.append('boolean')
  ConditionalSetProgram.__init__(self,bits,base)
  for index,(cursor,fuel) in scans.items():
   old=self.gates[index];g=self.fresh('GS');ports=self.types[old];self.add(g,ports+('f',))
   for p in ports:
    peer=self.wires.pop(old+'.'+p);del self.wires[peer];self.link(g+'.'+p,peer)
   del self.types[old];self.link(g+'.f',self.chain(('K',)*fuel));self.gates[index]=g
  self.audit()
 def enabled(self):
  return super().enabled()+[n for n in self.types if self.kind(n)=='GS' and self.wires[n+'.p'].endswith('.p') and self.kind(self.wires[n+'.p'].split('.')[0])=='DONE']
 def step(self,n):
  if self.kind(n)!='GS':return super().step(n)
  assert n in self.enabled();d=self.wires[n+'.p'].split('.')[0];g=self.fresh('FUEL')
  edges=[(n+'.f',g+'.p'),(n+'.b',g+'.u')]+[(n+'.'+p,g+'.'+p) for p in ('s','r','o','c')]
  self.replace((n,d),edges,[(g,('p','s','u','r','o','c'))]);self.releases.append(n)
 def observe(self):
  slots=[]
  for root,tag in zip(self.outputs,self.output_types):
   peer=self.wires[root+'.p'];kind=self.kind(peer.split('.')[0]);value=None
   if peer.endswith('.p'):
    if tag=='boolean' and kind in ('TRUE','FALSE'):value=kind=='TRUE'
    elif tag=='scan' and kind in ('FOUND','EXHAUSTED'):value=kind
   slots.append((tag,value))
  peer=self.wires['ACK.p'];complete=peer.endswith('.p') and self.kind(peer.split('.')[0])=='DONE'
  return {'observations':tuple(slots),'complete':complete,'word':self.retained() if complete else None}
