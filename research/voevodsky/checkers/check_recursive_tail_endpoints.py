"""Audit B/K auxiliary successors and finite tail endpoint kinds."""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_tagged_individual_redex_schedules import replay,fixtures
 from check_reachable_family_diamonds import canonical
 from check_phase_auxiliary_tail_types import valid as phase_valid

def role(name):
 if name.startswith(('Q1','Q2')):return 'Q_'+name[2:].split('_')[0]
 return name.split('_')[0]
def valid(net):
 if not phase_valid(net):return False
 for name in net.types:
  tag=role(name)
  if tag not in ('B0','B1','K'):continue
  peer=net.wires[name+'.a'];p,port=peer.split('.');r=role(p)
  if tag=='K':
   if (r,port) not in {('K','p'),('N','p')}:return False
  elif (r,port) not in {('B0','p'),('B1','p'),('N','p'),('COPY','a'),('COPY','b')}:return False
  seen=set();cursor=name
  while role(cursor) in ('B0','B1','K'):
   if cursor in seen:return False
   seen.add(cursor)
   cursor=net.wires[cursor+'.a'].split('.')[0]
  if role(cursor) not in ('N','COPY'):return False
  if tag=='K' and role(cursor)!='N':return False
 return True

states=arcs=0;endpoints={}
for bits,indices in fixtures:
 pending=[()];seen=set()
 while pending:
  prefix=pending.pop();net,choices=replay(bits,indices,prefix)
  state=canonical(net)
  if state in seen:continue
  seen.add(state)
  assert valid(net),(bits,indices,prefix,[(x,net.wires[x+'.a']) for x in net.types if role(x) in ('B0','B1','K') and not valid(net)])
  for name in net.types:
   if role(name) in ('B0','B1','K'):
    pair=(role(name),role(net.wires[name+'.a'].split('.')[0]),net.wires[name+'.a'].split('.')[1])
    endpoints[str(pair)]=endpoints.get(str(pair),0)+1
  for choice in choices:
   child,_=replay(bits,indices,prefix+(choice,))
   assert valid(child)
   pending.append(prefix+(choice,));arcs+=1
 states+=len(seen)
report={'passed':True,'states':states,'transitions':arcs,'observed_endpoint_kinds':endpoints,'scope':'Local auxiliary-successor closure on four tiny inputs all redex choices. Endpoint typing is necessary but does not establish global component reachability or uniqueness.'}
out=Path(__file__).resolve().parents[1]/'results/recursive-tail-endpoints.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
