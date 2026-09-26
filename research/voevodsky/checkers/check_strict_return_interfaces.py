"""Audit actual replacement arguments before mutation, including return routing."""
from strict_set_program import StrictSetProgram
from collections import Counter
from itertools import product
from pathlib import Path
import json
cases=Counter()
class Audited(StrictSetProgram):
 def replace(self,names,edges,new):
  old=set(names);boundary={n+'.'+p for n in names for p in self.types[n] if self.wires[n+'.'+p].split('.')[0] not in old}
  fresh={n+'.'+p for n,ports in new for p in ports}
  assert len({n for n,ps in new})==len(new)
  assert not ({n for n,ps in new}&set(self.types))
  assert Counter(p for edge in edges for p in edge)==Counter(boundary|fresh)
  n,d=names;k=self.kind(n);h=self.kind(d);rule=k+'--'+h
  cases[rule]+=1
  return_port=n+('.r' if k=='EA' else '.c')
  if k!='COPY':
   targets=[b if a==return_port else a for a,b in edges if return_port in (a,b)]
   assert len(targets)==1,(rule,'return multiplicity')
   target=targets[0];agent,port=target.split('.')
   nk=self.kind(agent)
   terminal=(k=='EA' and h=='N') or (k=='QR' and h=='N') or k=='ARc' or (k in ('ULc','U0c','U1c') and h=='N')
   if terminal:assert nk=='DONE' and port=='p',rule
   elif k in ('QS','QR') and not (k=='QS' and h!='N'):
    assert nk=='EA' and port=='r',rule
   elif k=='EA':assert nk=='EA' and port=='r'
   else:assert port=='c' and agent in {x for x,ps in new},rule
  super().replace(names,edges,new)

runs=0
for n in range(3):
 for w in product((0,1),repeat=n):
  for i in range(4):
   for operand in ((),(0,),(1,),(0,1),(1,0,1)):
    program=[('member',i),('add',i),('union',operand),('member',3)]
    net=Audited(w,program)
    while net.enabled():net.step(net.enabled()[0])
    assert net.acknowledged();runs+=1
required={k+'--'+h for k,heads in {'GM':['DONE'],'GA':['DONE'],'GU':['DONE'],'ABc':['K','N'],'ASc':['B0','B1','N'],'ARc':['B0','B1','N'],'ULc':['B0','B1','N'],'U0c':['B0','B1','N'],'U1c':['B0','B1','N']}.items() for h in heads}
missing=required-set(cases)
# Single operations ensure short inputs do not get lengthened before union.
for w in ((),(0,),(1,),(0,1),(1,0)):
 for v in ((),(0,),(1,),(0,1),(1,0)):
  net=Audited(w,[('union',v)])
  while net.enabled():net.step(net.enabled()[0])
  runs+=1
assert required<=set(cases),required-set(cases)
report={'passed':True,'runs':runs,'replacement_checks':sum(cases.values()),'rule_counts':dict(sorted(cases.items())),'required_gate_update_union_cases':len(required),'scope':'Concrete production-call interface audit; all 20 gate/update/union typed cases covered. Not symbolic verification for arbitrary input or full postcondition proof.'}
out=Path(__file__).resolve().parents[1]/'results/strict-return-interfaces.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
