"""Synthetic typed pairs audit the combined dispatch, not just reachable fixtures."""
from scanning_set_program import ScanningSetProgram
from collections import Counter
from itertools import product
from pathlib import Path
import json
spec={}
def declare(kinds,ports):
 for k in kinds.split():spec[k]=set(ports.split())
declare('RET ACK OUT N TRUE FALSE DONE TOKEN FOUND EXHAUSTED','p')
declare('K B0 B1','p a');declare('COPY','p a b');declare('QB QS ABc ASc ULc U0c U1c','p a r c')
declare('QR ARc','p r c');declare('EA','p r')
declare('GM','p s r b c o');declare('GA GU','p s r b c');declare('GC','p s r b c o t f');declare('GS','p s r b c o f')
declare('WAIT','p b s r t f o c');declare('PICK','p s r t f o c');declare('JOIN','p a c');declare('JOINR','p c')
declare('DC','p a b c');declare('PREP','p a b q i r c');declare('READY','p a b d q i r c')
declare('FUEL','p s u r o c');declare('START','p s q i u f r o c');declare('TEST','p b s i u f r o c');declare('CHOOSE','p s i u f r o c');declare('NEXT','p s u f r o c');declare('CLEAN','p u f o c');declare('DRAIN','p f o c');declare('FINISH','p o c');declare('SEAL','p c')
allowed={}
for kinds,heads in [('COPY','B0 B1 N'),('QB ABc DC FUEL','K N'),('QS QR ASc ARc ULc U0c U1c','B0 B1 N'),('EA','B0 B1 K N'),('GM GA GU GC GS WAIT JOIN JOINR PREP READY START TEST NEXT CLEAN DRAIN FINISH','DONE'),('PICK CHOOSE','TRUE FALSE'),('SEAL','TOKEN')]:
 for k in kinds.split():allowed[k]=set(heads.split())
rule_sizes={}
class Audited(ScanningSetProgram):
 def replace(self,names,edges,new):
  assert len(names)==2 and len(set(names))==2 and len(new)<=4
  rule_sizes[self.kind(names[0])+'--'+self.kind(names[1])]=len(new)
  old=set(names);boundary={n+'.'+p for n in names for p in self.types[n] if self.wires[n+'.'+p].split('.')[0] not in old}
  fresh={n+'.'+p for n,ps in new for p in ps}
  assert Counter(p for e in edges for p in e)==Counter(boundary|fresh)
  for n,ps in new:assert set(ps)==spec[self.kind(n)] and len(ps)==len(set(ps))
  super().replace(names,edges,new)
positive=negative=0
for k in allowed:
 for h in ('K','N','B0','B1','TRUE','FALSE','DONE','TOKEN'):
  net=Audited.__new__(Audited);net.types={};net.wires={};net.serial=1000;net.steps=0;net.releases=[]
  for name,kind in [('x',k),('y',h)]:net.add(kind+'_'+name,tuple(sorted(spec[kind])))
  a=k+'_x';b=h+'_y';net.link(a+'.p',b+'.p')
  for name in (a,b):
   for port in net.types[name]:
    if port=='p':continue
    root=net.fresh('OUT');net.add(root,('p',));net.link(name+'.'+port,root+'.p')
  net.audit();enabled=net.enabled()
  assert enabled==([a] if h in allowed[k] else []),(k,h,enabled)
  if enabled:net.step(a);assert net.steps==1;positive+=1
  else:negative+=1
# Adjacent placeholder replacement must preserve the continuation chain.
compiled=0
for ops in product(('ifadd','scan'),repeat=4):
 net=ScanningSetProgram((),[(op,(0,1,2) if op=='ifadd' else (0,2)) for op in ops])
 for i,g in enumerate(net.gates):
  assert net.kind(g)==('GC' if ops[i]=='ifadd' else 'GS')
  assert net.wires[g+'.r']==(net.gates[i+1]+'.s' if i+1<len(ops) else 'RET.p')
  assert net.wires[g+'.c']==(net.gates[i+1]+'.p' if i+1<len(ops) else 'ACK.p')
  assert net.wires[g+'.o']==net.outputs[i]+'.p'
 for name,ports in net.types.items():assert set(ports)==spec[net.kind(name)]
 compiled+=1
report={'passed':True,'signature':{k:sorted(v) for k,v in sorted(spec.items())},'allowed_pairs':{k:sorted(v) for k,v in sorted(allowed.items())},'max_created_agents':max(rule_sizes.values()),'rule_created_agents':rule_sizes,'positive_pairs':positive,'negative_pairs':negative,'adjacent_four_gate_compilations':compiled,'mro':[c.__name__ for c in ScanningSetProgram.__mro__],'scope':'One symbolic outside-leaf fixture per typed pair; checks production dispatch and new-port signature/linearity. Not semantic correctness of arbitrary contexts.'}
p=Path(__file__).resolve().parents[1]/'results/combined-signature.json';p.write_text(json.dumps(report,indent=2)+'\n');print({k:v for k,v in report.items() if k not in ('signature','allowed_pairs')})
