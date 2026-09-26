"""No replacement bypass: exact templates + typed allocation + pure evaluation."""
from scanning_set_program import ScanningSetProgram
from certified_replacement import checked_replace
from rule_templates import check_template
from itertools import product
from random import Random
from collections import Counter
from copy import deepcopy
from pathlib import Path
import json
base=Path(__file__).resolve().parents[1];table=json.loads((base/'results/combined-signature.json').read_text());counts=Counter();splices=0
class Checked(ScanningSetProgram):
 def step(self,n):
  self.pre_serial=self.serial
  return super().step(n)
 def replace(self,names,edges,new):
  global splices
  snapshot=deepcopy((self.types,self.wires))
  key=check_template(self.types,names,edges,new,before=self.pre_serial)
  expected=checked_replace(self.types,self.wires,names,edges,new,before=self.pre_serial,after=self.serial,signature=table['signature'],allowed=table['allowed_pairs'],protected=['RET','ACK']+self.outputs)
  assert snapshot==(self.types,self.wires)
  old=set(names);splices+=any(a.split('.')[0] in old and b.split('.')[0] in old for a,b in edges)
  super().replace(names,edges,new);assert expected==(self.types,self.wires);counts[key]+=1
rng=Random(121);runs=steps=0
alphabet=[('scan',(0,2)),('ifadd',(1,0,2)),('member',1),('add',2),('union',()),('union',(1,0))]
for length in range(4):
 for ops in product(alphabet,repeat=length):
  for bits in ((),(0,1),(1,0)):
   net=Checked(bits,ops)
   while net.enabled():net.step(rng.choice(net.enabled()))
   assert net.observe()['complete'];runs+=1;steps+=net.steps
assert sum(counts.values())==steps
report={'passed':True,'programs':runs,'checked_replacements':steps,'skipped_replacements':0,'distinct_templates':len(counts),'splice_replacements':splices,'rule_counts':dict(sorted(counts.items())),'scope':'Full layered checks on every replacement in bounded seeded mixed executions; initial compiler and manifest correctness still trusted premises.'}
(base/'results/whole-run-certificates.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='rule_counts'}))
