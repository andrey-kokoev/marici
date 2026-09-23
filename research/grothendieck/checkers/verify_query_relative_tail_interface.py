"""Independent exact source-enumeration replay of the query-relative packet.
No import of the producer, hull/clipping implementation, or an LP optimizer.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,hashlib
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(m):
 a,b,c=m;return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def source_vertices(A,b):
 vertices=set()
 for ids in combinations(range(len(b)),3):
  rows=[A[i] for i in ids];rhs=[b[i] for i in ids];d=det(rows)
  if not d:continue
  x=tuple(det([[rhs[i] if j==k else rows[i][j] for j in range(3)] for i in range(3)])/d for k in range(3))
  if all(dot(row,x)<=v for row,v in zip(A,b)):vertices.add(x)
 return vertices
r=load(R/'query-relative-tail-interface.json');cp=R/'query-relative-tail-interface-contract.json';contract=load(cp)
for p,h in r['bindings'].items():assert sha(Path(p))==h
assert sha(cp)==r['contract_sha256']
s=load(R/'ternary-tail-budget-dpc.json');assert sha(R/'ternary-tail-budget-dpc.json')==contract['source_sha256']
for p,h in s['bindings'].items():assert sha(Path(p))==h
caps=list(map(Q,s['atom_capacity_upper']));budgets=list(map(Q,s['prefix_budget_upper']));c=[Q(z['lower']) for z in s['weights']]
A=[];b=[]
for i in range(3):A.append([Q(-int(i==j)) for j in range(3)]);b.append(Q(0))
for i in range(3):A.append([Q(int(i==j)) for j in range(3)]);b.append(caps[i])
for i in range(3):A.append([Q(int(j<=i)) for j in range(3)]);b.append(budgets[i])
assert A==[list(map(Q,row)) for row in r['source_constraints']['A']] and b==list(map(Q,r['source_constraints']['b']))
assert c==list(map(Q,r['objective_coefficients']))
def image(x):return sum(x),dot(c,x)
def in_hull(z,points):
 if z in points:return True
 for p,q in combinations(points,2):
  diff=(q[0]-p[0],q[1]-p[1]);j=next((j for j in (0,1) if diff[j]),None)
  if j is not None:
   t=(z[j]-p[j])/diff[j]
   if 0<=t<=1 and all(z[k]==p[k]+t*diff[k] for k in (0,1)):return True
 for p,q,t in combinations(points,3):
  a=q[0]-p[0];bb=t[0]-p[0];cc=q[1]-p[1];d=t[1]-p[1];delta=a*d-bb*cc
  if not delta:continue
  u=((z[0]-p[0])*d-bb*(z[1]-p[1]))/delta;v=(a*(z[1]-p[1])-cc*(z[0]-p[0]))/delta
  if u>=0 and v>=0 and u+v<=1:return True
 return False
def verify_image(packet,AA,bb):
 points=[]
 for vertex in packet:
  z=tuple(map(Q,vertex['observable']));x=tuple(map(Q,vertex['source_lift']))
  assert all(dot(row,x)<=v for row,v in zip(AA,bb)) and image(x)==z;points.append(z)
 vertices=source_vertices(AA,bb)
 # Source is bounded by unchanged atom caps; every nonempty source polytope
 # has vertices. Convexity makes these two containments a complete proof.
 assert bool(points)==bool(vertices)
 assert all(in_hull(image(x),points) for x in vertices)
 return points
initial=verify_image(r['initial_polygon'],A,b)
facets=[(tuple(map(Q,row['coefficients'])),Q(row['upper'])) for row in r['facets']]
assert len(initial)==len(facets)>=3
for i,((n,d),raw) in enumerate(zip(facets,r['facet_omission_witnesses'])):
 assert n!=(0,0)
 assert dot(n,initial[i])==d==dot(n,initial[(i+1)%len(initial)])
 assert all(dot(n,z)<d for j,z in enumerate(initial) if j not in (i,(i+1)%len(initial)))
 witness=tuple(map(Q,raw));assert dot(n,witness)>d
 assert all(dot(nn,witness)<=dd for j,(nn,dd) in enumerate(facets) if j!=i)
# Every projected trace is checked against the full retained source rows.
for name,trace in r['traces'].items():
 AA=list(A);bb=list(b)
 for step in trace:
  n=list(map(Q,step['frame']['coefficients']));d=Q(step['frame']['upper']);AA.append([n[0]+n[1]*v for v in c]);bb.append(d)
  verify_image(step['polygon'],AA,bb)
 assert bool(trace[-1]['polygon'])==(name=='compatible-refinement')
trace=r['traces']['separately-feasible-inconsistent-chain']
for step in trace:
 n=list(map(Q,step['frame']['coefficients']));d=Q(step['frame']['upper'])
 assert source_vertices(A+[[n[0]+n[1]*v for v in c]],b+[d])
fake=tuple(map(Q,r['rectangle_false_point']))
assert all(min(z[j] for z in initial)<=fake[j]<=max(z[j] for z in initial) for j in (0,1)) and not in_hull(fake,initial)
p=tuple(map(Q,r['out_of_language_collision']['left']));q=tuple(map(Q,r['out_of_language_collision']['right']))
assert image(p)==image(q) and (p[0]<=1000)!=(q[0]<=1000)
assert all(dot(row,x)<=v for x in (p,q) for row,v in zip(A,b))
budget=r['budget_control'];assert budget['necessary_initial_facets']==len(facets)==budget['sufficient_initial_facets']>budget['refuse_budget']
# Corrupted source lift must be rejected even if its observable looks legal.
bad=[dict(v) for v in r['initial_polygon']];bad[0]=dict(bad[0],source_lift=['-1','0','0'])
try:verify_image(bad,A,b)
except AssertionError:pass
else:raise AssertionError('fabricated source lift accepted')
print('PASS: exact source-image equality, all persistent query updates, six irredundant facets, budget obstruction, separate-range failure, language-extension collision and corrupted-lift rejection')
