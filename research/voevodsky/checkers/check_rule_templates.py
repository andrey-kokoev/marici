from rule_templates import check_template,TEMPLATES
from scanning_set_program import ScanningSetProgram
from itertools import product
from pathlib import Path
import json
seen=set();checks=0;swaps=0
class Checked(ScanningSetProgram):
 def step(self,n):self.before_step=self.serial;return super().step(n)
 def replace(self,names,edges,new):
  global checks,swaps
  key='--'.join(self.kind(n) for n in names)
  if key in TEMPLATES:
   seen.add(check_template(self.types,names,edges,new,before=self.before_step));checks+=1
   if key=='GS--DONE':
    def swap(p):return names[0]+'.b' if p==names[0]+'.f' else names[0]+'.f' if p==names[0]+'.b' else p
    wrong=[(swap(a),swap(b)) for a,b in edges]
    try:check_template(self.types,names,wrong,new,before=self.before_step)
    except ValueError:swaps+=1
    else:raise AssertionError('linear role swap admitted')
  super().replace(names,edges,new)
for bits in ((),(0,),(1,)):
 for ops in product([('scan',(0,1)),('ifadd',(0,0,1)),('member',0),('add',1),('union',())],repeat=2):
  net=Checked(bits,ops)
  while net.enabled():net.step(net.enabled()[0])
assert seen<=set(TEMPLATES) and swaps>0
try:check_template({},('UNKNOWN_1','N_2'),[],[],before=2)
except ValueError:pass
else:raise AssertionError('uncovered rule accepted')
report={'passed':True,'covered_templates':len(seen),'total_runtime_templates':57,'matched_certificates':checks,'linear_role_swaps_rejected':swaps,'scope':'Mixed-program coverage subset of full hand-declared manifest; unknown rules fail closed. Not independent review.'}
p=Path(__file__).resolve().parents[1]/'results/rule-templates.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
