"""Check projection(step(G)) = step(projection(G)) before gate release."""
from gated_membership import GatedMembership
from acknowledged_membership import AcknowledgedMembership
from forest_canonical import canonical
from copy import deepcopy
from itertools import product
from pathlib import Path
import json

def project(net):
 g=next(n for n in net.types if net.kind(n)=='GATE')
 seeds=[net.wires[g+'.s'].split('.')[0],net.wires[g+'.p'].split('.')[0],net.first_out]
 keep=set();queue=list(seeds)
 while queue:
  n=queue.pop()
  if n==g or n in keep:continue
  keep.add(n);queue.extend(net.wires[n+'.'+p].split('.')[0] for p in net.types[n])
 result=AcknowledgedMembership.__new__(AcknowledgedMembership)
 result.types={n:net.types[n] for n in keep};result.wires={}
 result.serial=net.serial;result.steps=net.steps;result.out=net.first_out
 result.add('RET',('p',));result.add('ACK',('p',))
 for p,q in net.wires.items():
  if p.split('.')[0] in keep and q.split('.')[0] in keep:result.wires[p]=q
 result.link('RET.p',net.wires[g+'.s']);result.link('ACK.p',net.wires[g+'.p']);result.audit()
 return result

def raw(net):return tuple(sorted(net.types.items())),tuple(sorted(net.wires.items())),net.serial
fixtures=states=edges=ends=0
for n in range(3):
 for w in product((0,1),repeat=n):
  for i,j in product(range(n+2),repeat=2):
   pending=[GatedMembership(w,i,j)];seen=set();fixtures+=1
   while pending:
    net=pending.pop();sig=raw(net)
    if sig in seen:continue
    seen.add(sig);p=project(net)
    # Projection is a forest; the uncut graph need not be.
    canonical(p)
    enabled=[a for a in net.enabled() if net.kind(a)!='GATE']
    assert set(enabled)==set(p.enabled())
    if not enabled:
     assert p.acknowledged() and p.retained()==w
     assert p.answer(p.out)==(i<n and bool(w[i]));ends+=1
    for a in enabled:
     left=deepcopy(net);left.step(a);left=project(left)
     right=deepcopy(p);right.step(a)
     assert raw(left)==raw(right)
     pending_child=deepcopy(net);pending_child.step(a);pending.append(pending_child);edges+=1
   states+=len(seen)
report={'passed':True,'fixtures':fixtures,'raw_named_states':states,'commuting_projection_edges':edges,'ready_states':ends,'scope':'All pre-release choices for bounded two-call inputs, raw named-state search; no forest quotient applied to cyclic whole graph.'}
out=Path(__file__).resolve().parents[1]/'results/gate-projection.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
