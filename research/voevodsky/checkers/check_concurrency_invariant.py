"""Check actual replacement interfaces whenever a redex has a competitor."""
from scanning_set_program import ScanningSetProgram
from itertools import combinations,product
from random import Random
from collections import Counter
from pathlib import Path
import json
allowed={tuple(sorted(p)) for p in [('COPY',q) for q in ('QB','QS','QR','EA')]+[(a,'EA') for a in ('ABc','ASc','ARc','JOIN')]}
pairs=Counter();concurrent=serial_splices=0
class Audited(ScanningSetProgram):
 def replace(self,names,edges,new):
  global concurrent,serial_splices
  competitors=[a for a in self.enabled() if a!=names[0]]
  old=set(names);boundary={n+'.'+p for n in names for p in self.types[n] if self.wires[n+'.'+p].split('.')[0] not in old}
  fresh={n+'.'+p for n,ps in new for p in ps}
  assert Counter(p for e in edges for p in e)==Counter(boundary|fresh)
  splices=[(a,b) for a,b in edges if a in boundary and b in boundary]
  if competitors:
   assert not splices,(names,splices)
   for a,b in edges:
    if a in boundary:assert b in fresh
    if b in boundary:assert a in fresh
   concurrent+=1
  elif splices:serial_splices+=1
  super().replace(names,edges,new)
rng=Random(115);runs=states=0
alphabet=[('scan',(0,3)),('ifadd',(1,0,3)),('member',1),('add',2),('union',()),('union',(1,0))]
for size in range(4):
 for ops in product(alphabet,repeat=size):
  for word in ((),(0,1),(1,0,1)):
   net=Audited(word,ops)
   while net.enabled():
    choices=net.enabled();assert len(choices)<=2
    for a,b in combinations(choices,2):
     pair=tuple(sorted((net.kind(a),net.kind(b))));assert pair in allowed; pairs[pair]+=1
     assert not {a,net.wires[a+'.p'].split('.')[0]}&{b,net.wires[b+'.p'].split('.')[0]}
    net.step(rng.choice(choices));states+=1
   assert net.observe()['complete'];runs+=1
assert set(pairs)==allowed,allowed-set(pairs)
assert serial_splices>0
report={'passed':True,'runs':runs,'rewrite_states':states,'concurrent_replacements_checked':concurrent,'serial_splice_replacements':serial_splices,'concurrent_families':{'/'.join(k):v for k,v in sorted(pairs.items())},'scope':'One seeded schedule per bounded mixed fixture; actual production templates checked before mutation; not exhaustive reachability.'}
p=Path(__file__).resolve().parents[1]/'results/concurrency-invariant.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
