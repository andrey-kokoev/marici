"""Gauge invariance of the discrete witness-loop defect.

Fix endpoint tags; internal tags form four-point filling fibers over each of
six coordinate orders. Reparameterizations are arbitrary permutations of each
fiber; edge maps transform coherently by endpoint conjugation.
"""
from itertools import permutations, product
from pathlib import Path
import subprocess
import sys
import hashlib
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
prior=Path(__file__).with_name('check_repeated_diamond_coherence.py')
subprocess.run([sys.executable,str(prior)],check=True,capture_output=True,text=True)
prior_result=OUT/'repeated-diamond-coherence.json'
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n')
contract={'prior_sha256':hashlib.sha256(prior_result.read_bytes()).hexdigest(),
 'source':'The previously frozen twisted tag transport; three distinct coordinate operations; fixed outer tags.',
 'identity':'Discrete identity on the four internal tag assignments.',
 'admitted_coordinate_changes':'Arbitrary bijections independently at the six ordering fibers, with every edge transported by its endpoints.',
 'prediction':'Loop defect changes only by conjugation; its cycle type prevents removing it by such coordinate changes.',
 'scope':'This tests reparameterization, not replacement of edge maps or newly added higher source identifications.'}
cp=OUT/'braid-defect-coordinate-invariance-contract.json';save(cp,contract)
points=list(product((0,1),repeat=2));orders=list(permutations(range(3)));gauges=list(permutations(range(4)))
identity=tuple(range(4))
def then(f,g):return tuple(g[f[i]] for i in range(4))
def inv(f):return tuple(f.index(i) for i in range(4))
def edge(outer,i):
 out=[]
 for a,b in points:
  tags=[outer,a,b,0]
  tags[i+1]^=tags[i]
  out.append(points.index(tuple(tags[1:3])))
 return tuple(out)
def next_order(order,i):
 o=list(order);o[i],o[i+1]=o[i+1],o[i];return tuple(o)
def path_map(start,word,outer,G):
 order=start;result=identity
 for i in word:
  nxt=next_order(order,i)
  transported=then(then(inv(G[order]),edge(outer,i)),G[nxt])
  result=then(result,transported);order=nxt
 return order,result

def cycles(f):
 seen=set();out=[]
 for i in range(4):
  if i in seen:continue
  cyc=[];j=i
  while j not in seen:seen.add(j);cyc.append(j);j=f[j]
  out.append(cyc)
 return out
reports=[];checks=0
for outer in (0,1):
 start=(0,1,2);G0={o:identity for o in orders}
 end,L=path_map(start,(0,1,0),outer,G0)
 end2,R=path_map(start,(1,0,1),outer,G0);assert end==end2
 omega=then(L,inv(R));assert omega!=identity
 # Exhaust all changes at start/end and all independent changes at either
 # route's two internal vertices. General cancellation is also checked locally.
 for g in gauges:
  conjugated=then(then(inv(g),omega),g)
  assert conjugated!=identity
  assert sorted(map(len,cycles(conjugated)))==sorted(map(len,cycles(omega)))
  checks+=1
 for g0,gm,g1 in product(gauges,repeat=3):
  f,h=edge(outer,0),edge(outer,1)
  ef=then(then(inv(g0),f),gm);eh=then(then(inv(gm),h),g1)
  assert then(ef,eh)==then(then(inv(g0),then(f,h)),g1)
  checks+=1
 # Explicit nontrivial gauges at ALL six ordering spaces; endpoint calculation
 # plus the exhaustive local cancellation identity establishes arbitrary paths.
 for shift in range(24):
  G={o:gauges[(shift+7*i)%24] for i,o in enumerate(orders)}
  _,Lg=path_map(start,(0,1,0),outer,G)
  _,Rg=path_map(start,(1,0,1),outer,G)
  assert then(Lg,inv(Rg))==then(then(inv(G[start]),omega),G[start])
  checks+=1
 # Order and fixed points are discrete conjugacy invariants.
 power=identity;order=0
 while True:
  power=then(power,omega);order+=1
  if power==identity:break
  assert order<=24
 reports.append({'initial_outer_tag':outer,'points':points,'L':L,'R':R,'omega':omega,
                 'cycles':cycles(omega),'fixed_points':[points[i] for i in range(4) if omega[i]==i],
                 'defect_order':order})
# Uniform witness equality induced by an equivalence relation on tag pairs.
# To trivialize BOTH defects requires identifying every point in their joint orbit.
parent=list(range(4))
def root(i):
 while parent[i]!=i:i=parent[i]
 return i
for report in reports:
 for i,j in enumerate(report['omega']):parent[root(i)]=root(j)
groups={}
for i in range(4):groups.setdefault(root(i),[]).append(points[i])
assert len(groups)==1
report={'passed':True,'contract_sha256':hashlib.sha256(cp.read_bytes()).hexdigest(),
 'defects':reports,'coordinate_and_cancellation_checks':checks,
 'all_start_fiber_gauges_exhausted':24,
 'theorem':'Coherent vertex reparameterization sends Omega to g_start Omega g_start^-1. Nonidentity and cycle type persist under every such reparameterization.',
 'uniform_quotient_to_kill_both_defects':list(groups.values()),
 'higher_witness_status':'No homotopy to identity exists in the frozen discrete witness types. Adding identifications changes their source identity structure.',
 'scope':'Obstruction intrinsic to the fixed transport up to coordinate change, not intrinsic to the underlying product source under arbitrary replacement of diamond maps. A tag-preserving replacement was already coherent.'}
save(OUT/'braid-defect-coordinate-invariance.json',report)
print(json.dumps(report,indent=2))
