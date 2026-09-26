"""Compare both orders by rule-local fresh allocation slots; cycles allowed."""
from scanning_set_program import ScanningSetProgram
from copy import deepcopy
from itertools import combinations
from pathlib import Path
import json
class Traced(ScanningSetProgram):
 def fresh(self,k):
  name=super().fresh(k)
  if hasattr(self,'created'):self.created.append(name)
  return name

def freeze(x):
 if isinstance(x,dict):return tuple(sorted((k,freeze(v)) for k,v in x.items()))
 if isinstance(x,(list,tuple)):return tuple(map(freeze,x))
 return x

def ordered(net,first,second):
 child=deepcopy(net);child.created=[];child.step(first);one=child.created[:]
 assert second in child.enabled(),'residual redex lost'
 child.created=[];child.step(second);two=child.created[:];del child.created
 return child,{first:one,second:two}

def diamond(net,a,b):
 pairs=[{x,net.wires[x+'.p'].split('.')[0]} for x in (a,b)]
 assert not pairs[0]&pairs[1]
 left,ls=ordered(net,a,b);right,rs=ordered(net,b,a)
 mapping={n:n for n in net.types if n in left.types}
 for redex in (a,b):
  assert len(ls[redex])==len(rs[redex])
  for x,y in zip(ls[redex],rs[redex]):
   assert net.kind(x)==net.kind(y);mapping[x]=y
 assert set(mapping)==set(left.types) and set(mapping.values())==set(right.types)
 def port(p):
  n,s=p.split('.');return mapping[n]+'.'+s
 assert {mapping[n]:ps for n,ps in left.types.items()}==right.types
 assert {port(p):port(q) for p,q in left.wires.items()}==right.wires
 assert left.serial==right.serial and left.steps==right.steps
 # Metadata references constructor names, fixed by this bijection.
 assert {k:v for k,v in left.__dict__.items() if k not in ('types','wires')}=={k:v for k,v in right.__dict__.items() if k not in ('types','wires')}
 assert left.observe()==right.observe()

fixtures=[((),[('scan',(0,1))]),((1,),[('scan',(0,2))]),((0,),[('scan',(0,1)),('ifadd',(0,0,1))]),((),[('ifadd',(0,0,1)),('scan',(0,1))])]
# QS can consume an already copied cell while COPY advances the remaining input.
fixtures.append(((0,1),[('member',1)]))
allowed_concurrency={tuple(sorted(p)) for p in [('COPY',q) for q in ('QB','QS','QR','EA')]+[(a,'EA') for a in ('ABc','ASc','ARc','JOIN')]}
states=diamonds=0;kinds=set()
for bits,program in fixtures:
 pending=[Traced(bits,program)];seen=set()
 while pending:
  net=pending.pop();key=freeze(net.__dict__)
  if key in seen:continue
  assert len(seen)<20000;seen.add(key)
  choices=net.enabled()
  for a,b in combinations(choices,2):
   pair=tuple(sorted((net.kind(a),net.kind(b))))
   assert pair in allowed_concurrency,pair
   diamond(net,a,b);diamonds+=1;kinds.add(pair)
  for a in choices:
   child=deepcopy(net);child.step(a);pending.append(child)
 states+=len(seen)
assert kinds==allowed_concurrency,allowed_concurrency-kinds
report={'passed':True,'states':states,'diamonds':diamonds,'concurrent_kind_pairs':sorted(kinds),'scope':'Every enabled pair in five complete bounded state graphs; all eight classified concurrent kind families witnessed; explicit rule-slot allocation bijections fix surviving agents, port labels and public roots. No forest quotient.'}
p=Path(__file__).resolve().parents[1]/'results/local-diamonds.json';p.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
