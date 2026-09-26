from scanning_set_program import ScanningSetProgram
from certified_replacement import checked_replace
from rule_templates import check_template,TEMPLATES
from pathlib import Path
import json
base=Path(__file__).resolve().parents[1];table=json.loads((base/'results/combined-signature.json').read_text());seen=set()
class Checked(ScanningSetProgram):
 def replace(self,names,edges,new):
  seen.add(check_template(self.types,names,edges,new,before=self.before))
  expected=checked_replace(self.types,self.wires,names,edges,new,before=self.before,after=self.serial,signature=table['signature'],allowed=table['allowed_pairs'])
  super().replace(names,edges,new);assert expected==(self.types,self.wires)
for k,heads in table['allowed_pairs'].items():
 for h in heads:
  net=Checked.__new__(Checked);net.types={};net.wires={};net.serial=0;net.steps=0;net.releases=[]
  a=net.fresh(k);b=net.fresh(h)
  for n,kind in [(a,k),(b,h)]:net.add(n,tuple(table['signature'][kind]))
  net.link(a+'.p',b+'.p')
  for n in (a,b):
   for p in net.types[n]:
    if p=='p':continue
    root=net.fresh('OUT');net.add(root,('p',));net.link(n+'.'+p,root+'.p')
  net.before=net.serial;net.step(a)
assert seen==set(TEMPLATES) and len(seen)==57
report={'passed':True,'templates':len(seen),'layers':['exact slot template','typed allocation witness','pure replacement differential'],'scope':'All57 typed pair fixtures with passive boundary leaves; hand transcription, not independent external review or arbitrary contextual proof.'}
(base/'results/full-certificates.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
