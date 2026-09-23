"""Shared-model versus run-specific storage on saturated owning tail faces."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,gzip,subprocess,sys
import query_relative_tail_geometry as g
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
cp=R/'saturated-tail-refinement-storage-contract.json';contract=load(cp);ch=sha(cp)
subprocess.run([sys.executable,str(HERE/'verify_two_moment_tail_complexity.py')],check=True)
source_path=R/'two-moment-tail-complexity.json';source=load(source_path)
packets=[];counts={'states':0,'query_checks':0,'separating_pairs':0}
for spec in contract['finite_replays']:
 m=spec['m'];H=spec['H'];family=next(f for f in source['families'] if f['m']==m)
 caps=list(map(Q,family['caps']));slopes=list(map(Q,family['slopes']));facets=[(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in family['facets']]
 lifted=[]
 for f in family['facets']:
  for z,x in zip(f['edge_endpoints'],f['endpoint_lifts']):lifted.append((tuple(map(Q,z)),tuple(map(Q,x))))
 polygon=g.hull(lifted);optimizer=(sum(caps),dot(caps,slopes));assert optimizer in [z for z,x in polygon]
 assert H<=len(polygon)-1
 library=[]
 for z,lift in polygon:
  if z==optimizer:continue
  incident=[n for n,b in facets if dot(n,z)==b];assert len(incident)==2
  normal=tuple(sum(n[j] for n in incident) for j in (0,1));peak=dot(normal,z)
  other=max(dot(normal,p) for p,x in polygon if p!=z);assert peak>other
  bound=(peak+other)/2
  assert dot(normal,optimizer)<=bound
  assert all(dot(normal,p)<=bound for p,x in polygon if p!=z)
  library.append({'normal':list(map(str,normal)),'upper':str(bound),'probe':list(map(str,z)),'probe_source_lift':list(map(str,lift)),'farkas_gap':str(peak-bound)})
 library=library[:H]
 rows=[(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in library]
 states=[]
 for mask in range(2**H):
  current=polygon
  for i,(normal,bound) in enumerate(rows):
   if mask>>i&1:current=g.clip(current,normal,bound)
  assert optimizer in [z for z,x in current]
  assert max(z[1] for z,x in current)==optimizer[1]
  answers=[]
  for i,f in enumerate(library):
   z=tuple(map(Q,f['probe']));lift=list(map(Q,f['probe_source_lift']))
   feasible=all(dot(n,z)<=b for j,(n,b) in enumerate(rows) if mask>>j&1)
   assert feasible==(not bool(mask>>i&1));answers.append(feasible)
   if feasible:
    assert all(0<=v<=cap for v,cap in zip(lift,caps)) and (sum(lift),dot(slopes,lift))==z
   else:assert dot(rows[i][0],z)-rows[i][1]==Q(f['farkas_gap'])>0
  states.append({'mask':mask,'answers':answers,'polygon':[{'observable':list(map(str,z)),'source_lift':list(map(str,x))} for z,x in current]})
  counts['states']+=1;counts['query_checks']+=H
 assert len({tuple(s['answers']) for s in states})==2**H
 # XOR produces a named separating query for every distinct pair.
 for left in range(2**H):
  for right in range(left+1,2**H):
   i=((left^right)&-(left^right)).bit_length()-1
   assert states[left]['answers'][i]!=states[right]['answers'][i];counts['separating_pairs']+=1
 # One explicit budget refusal plus a sufficient mask code, not a claim that
 # the much larger exported audit polygons occupy H bits.
 packets.append({'m':m,'H':H,'library':library,'optimizer':list(map(str,optimizer)),'minimum':str(-optimizer[1]),'threshold':str(-2*optimizer[1]),'states':states,'budget':{'offered':H-1,'status':'REFUSE_BUDGET','required_bits':H,'sufficient_bits':H,'collision_masks':[0,1<<(H-1)],'separating_probe':H-1}})
assert sha(cp)==ch
out={'schema':'saturated-tail-refinement-storage-result.v1','status':'EXACT_REPRESENTATION_OR_STORAGE_OBSTRUCTION','contract_sha256':ch,'counts':counts,'families':packets,'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'query_relative_tail_geometry.py',cp,source_path)},'scope':'H-bit runtime mask plus shared source/library; exported polygons and source lifts are verification data, not a claim of H-bit total storage.'}
raw=(json.dumps(out,separators=(',',':'))+'\n').encode();(R/'saturated-tail-refinement-storage.json.gz').write_bytes(gzip.compress(raw,mtime=0))
print(json.dumps(counts,indent=2))
