"""Independent exact verification of shared-source/per-run information costs.
No producer, clipping implementation, or optimizer is imported.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,gzip,hashlib
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
r=json.loads(gzip.decompress((R/'saturated-tail-refinement-storage.json.gz').read_bytes()));cp=R/'saturated-tail-refinement-storage-contract.json';contract=load(cp)
for p,h in r['bindings'].items():assert sha(Path(p))==h
assert sha(cp)==r['contract_sha256']
source=load(R/'two-moment-tail-complexity.json')
for p,h in source['bindings'].items():assert sha(Path(p))==h
counts={'states':0,'query_checks':0,'separating_pairs':0}
for packet,spec in zip(r['families'],contract['finite_replays']):
 m=packet['m'];H=packet['H'];assert (m,H)==(spec['m'],spec['H'])
 owning=next(f for f in source['families'] if f['m']==m)
 caps=list(map(Q,owning['caps']));slopes=list(map(Q,owning['slopes']));base=[(tuple(map(Q,f['normal'])),Q(f['upper'])) for f in owning['facets']]
 original={tuple(map(Q,z)) for f in owning['facets'] for z in f['edge_endpoints']}
 optimizer=(sum(caps),dot(caps,slopes));assert optimizer==tuple(map(Q,packet['optimizer']))
 assert all(v>0 for v in slopes) and Q(packet['minimum'])==-optimizer[1]>Q(packet['threshold'])==-2*optimizer[1]
 library=packet['library'];assert len(library)==H and len({tuple(f['probe']) for f in library})==H
 cuts=[]
 for f in library:
  probe=tuple(map(Q,f['probe']));lift=list(map(Q,f['probe_source_lift']));n=tuple(map(Q,f['normal']));b=Q(f['upper'])
  assert probe in original and probe!=optimizer
  assert all(0<=t<=cap for t,cap in zip(lift,caps)) and (sum(lift),dot(lift,slopes))==probe
  incident=[a for a,v in base if dot(a,probe)==v];assert len(incident)==2
  assert n==tuple(sum(a[j] for a in incident) for j in (0,1))
  peak=dot(n,probe);other=max(dot(n,p) for p in original if p!=probe)
  assert peak>other and b==(peak+other)/2 and peak-b==Q(f['farkas_gap'])>0
  assert all(dot(n,p)<b for p in original if p!=probe)
  cuts.append((n,b))
 # All possible residual vertices are pair intersections of shared base/cut
 # lines. Mark which cuts a pair needs and which cuts its point violates.
 allrows=base+cuts;arrangement=[]
 for i,j in combinations(range(len(allrows)),2):
  (a,b),(c,d)=allrows[i],allrows[j];det=a[0]*c[1]-a[1]*c[0]
  if not det:continue
  point=((b*c[1]-a[1]*d)/det,(a[0]*d-b*c[0])/det)
  if not all(dot(n,point)<=v for n,v in base):continue
  required=sum(1<<(k-len(base)) for k in (i,j) if k>=len(base))
  violated=sum(1<<k for k,(n,v) in enumerate(cuts) if dot(n,point)>v)
  arrangement.append((point,required,violated))
 states=packet['states'];assert [s['mask'] for s in states]==list(range(2**H))
 for state in states:
  mask=state['mask'];expected={p for p,needed,bad in arrangement if needed&mask==needed and not bad&mask}
  points=set()
  for v in state['polygon']:
   point=tuple(map(Q,v['observable']));lift=list(map(Q,v['source_lift']))
   assert len(lift)==m and all(0<=x<=cap for x,cap in zip(lift,caps))
   assert (sum(lift),dot(lift,slopes))==point
   assert all(dot(n,point)<=b for j,(n,b) in enumerate(cuts) if mask>>j&1)
   points.add(point)
  assert points==expected and optimizer in points and max(p[1] for p in points)==optimizer[1]
  for j,f in enumerate(library):
   probe=tuple(map(Q,f['probe']));feasible=not bool(mask>>j&1)
   assert feasible==state['answers'][j]
   if feasible:assert all(dot(n,probe)<=b for k,(n,b) in enumerate(cuts) if mask>>k&1)
   else:
    n,b=cuts[j]
    # Exact Farkas contradiction: cut plus positive multiples of the
    # appropriate point-equality directions has zero lhs and negative rhs.
    lhs=list(n);rhs=b
    for k,a in enumerate(n):
     sign=-1 if a>0 else 1;mult=abs(a)
     lhs[k]+=mult*sign;rhs+=mult*sign*probe[k]
    assert lhs==[0,0] and rhs==-Q(f['farkas_gap'])<0
   counts['query_checks']+=1
  counts['states']+=1
 assert len({tuple(s['answers']) for s in states})==2**H
 for a,b in combinations(range(2**H),2):
  diff=a^b;j=(diff&-diff).bit_length()-1
  assert states[a]['answers'][j]!=states[b]['answers'][j];counts['separating_pairs']+=1
 budget=packet['budget'];assert budget['required_bits']==H==budget['sufficient_bits'] and budget['offered']==H-1
 assert 2**H>2**budget['offered'] and budget['status']=='REFUSE_BUDGET'
 a,b=budget['collision_masks'];j=budget['separating_probe'];assert a==0 and b==1<<(H-1) and j==H-1
 assert a%(2**(H-1))==b%(2**(H-1)) and states[a]['answers'][j]!=states[b]['answers'][j]
 # Shared source and observable-only rows give saturation algebraically:
 # C_J=P intersect L^-1(intersection H_j). Exact polygon equality above
 # proves P intersect L^-1(Q_J)=C_J, not merely vertex-lift existence.
assert counts==r['counts']
print('PASS:',counts,'; exact saturated images, common optimizer/certificate, primal/Farkas probes, H-bit sufficiency and budget obstruction')
