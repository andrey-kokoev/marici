"""Reconstruct live provenance without consulting tags or constructor history."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
from typed_net_invariant import validate

def reconstruct(net):
 copies=[n for n in net.types if n.split('_')[0]=='COPY']
 assert len(copies)<=1
 originals=set()
 if copies:
  node=net.wires[copies[0]+'.p'].split('.')[0]
  while True:
   assert node not in originals
   originals.add(node)
   kind=node.split('_')[0]
   if kind=='N':break
   assert kind in ('B0','B1')
   node=net.wires[node+'.a'].split('.')[0]
 return {n:('ORIGINAL' if n in originals else 'COPIED') for n in net.types if n.split('_')[0] in ('B0','B1','K','N')}

if __name__=='__main__':
 with redirect_stdout(StringIO()):
  from check_tagged_individual_redex_schedules import replay,fixtures
  from check_reachable_family_diamonds import canonical
 states=edges=0
 for bits,indices in fixtures:
  pending=[()];seen=set()
  while pending:
   prefix=pending.pop();net,choices=replay(bits,indices,prefix)
   assert validate(net) is None
   assert reconstruct(net)==net.tags
   key=canonical(net)
   if key in seen:continue
   seen.add(key)
   for choice in choices:
    child,_=replay(bits,indices,prefix+(choice,))
    assert validate(child) is None and reconstruct(child)==child.tags
    pending.append(prefix+(choice,));edges+=1
  states+=len(seen)
 report={'passed':True,'states':states,'transitions':edges,'finding':'Live ORIGINAL/COPIED labels reconstruct from COPY source chain without tags or origin history.','scope':'Four fixtures; conditional structural lemma in companion note, not a certification of existing canonical serialization.'}
 out=Path(__file__).resolve().parents[1]/'results/structural-tag-reconstruction.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
