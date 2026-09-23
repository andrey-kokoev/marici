"""Independent rational replay of the source diamond and restricted images."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,hashlib
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def det(a):
 x,y,z=a;return x[0]*(y[1]*z[2]-y[2]*z[1])-x[1]*(y[0]*z[2]-y[2]*z[0])+x[2]*(y[0]*z[1]-y[1]*z[0])
def vertices(A,b):
 out=set()
 for ids in combinations(range(len(b)),3):
  mat=[A[i] for i in ids];rhs=[b[i] for i in ids];d=det(mat)
  if not d:continue
  p=tuple(det([[rhs[i] if j==k else mat[i][j] for j in range(3)] for i in range(3)])/d for k in range(3))
  if all(dot(row,p)<=v for row,v in zip(A,b)):out.add(p)
 return out
def inside(p,pts):
 if p in pts:return True
 for a,b in combinations(pts,2):
  diff=tuple(y-x for x,y in zip(a,b));j=next((j for j in (0,1) if diff[j]),None)
  if j is not None:
   t=(p[j]-a[j])/diff[j]
   if 0<=t<=1 and all(p[k]==a[k]+t*diff[k] for k in (0,1)):return True
 for a,b,c in combinations(pts,3):
  u=(b[0]-a[0],b[1]-a[1]);v=(c[0]-a[0],c[1]-a[1]);z=(p[0]-a[0],p[1]-a[1]);d=u[0]*v[1]-u[1]*v[0]
  if d:
   s=(z[0]*v[1]-z[1]*v[0])/d;t=(u[0]*z[1]-u[1]*z[0])/d
   if s>=0 and t>=0 and s+t<=1:return True
 return False
r=load(R/'analytical-saturation-diamond.json')
for p,h in r['bindings'].items():assert sha(Path(p))==h
assert r['contract_sha256']==sha(R/'analytical-saturation-diamond-contract.json')
own=load(R/'query-relative-tail-interface.json')
for p,h in own['bindings'].items():assert sha(Path(p))==h
A=[list(map(Q,row)) for row in own['source_constraints']['A']];b=list(map(Q,own['source_constraints']['b']));c=list(map(Q,own['objective_coefficients']))
def obs(x):return sum(x),dot(c,x)
diamond=r['diamond'];p,q,t=[tuple(map(Q,diamond[k])) for k in ('start','S_middle','end')]
assert all(dot(row,x)<=v for x in (p,q,t) for row,v in zip(A,b))
assert obs(p)[0]==obs(q)[0] and obs(q)[1]==obs(t)[1]
missing=tuple(map(Q,diamond['missing_reverse_observable']));assert missing==(obs(t)[0],obs(p)[1])
coef=[v-min(c) for v in c];assert all(v>=0 for v in coef) and coef==list(map(Q,diamond['nonnegative_source_row']['coefficients']))
assert missing[1]-min(c)*missing[0]==Q(diamond['nonnegative_source_row']['candidate_value'])<0
for row in r['rectangle_corners']:
 x=tuple(map(Q,row['source_lift']));assert all(dot(a,x)<=d for a,d in zip(A,b)) and obs(x)==tuple(map(Q,row['observable']))
for case in r['cases']:
 AA=list(A);bb=list(b)
 for frame in case['frames']:
  n=list(map(Q,frame['normal']));d=Q(frame['upper']);AA.append([n[0]+n[1]*v for v in c]);bb.append(d)
 pts=[]
 for row in case['image']:
  x=tuple(map(Q,row['source_lift']));z=tuple(map(Q,row['observable']));assert obs(x)==z
  assert all(dot(a,x)<=d for a,d in zip(AA,bb));pts.append(z)
 vs=vertices(AA,bb);assert vs and all(inside(obs(x),pts) for x in vs)
 # Boundedness and source lifts give the reverse image inclusion by convexity.
 dim=0 if len(set(pts))==1 else 1
 if any((v[0]-u[0])*(w[1]-u[1])!=(v[1]-u[1])*(w[0]-u[0]) for u,v,w in combinations(pts,3)):dim=2
 rectangle={(s,f) for s in (min(p[0] for p in pts),max(p[0] for p in pts)) for f in (min(p[1] for p in pts),max(p[1] for p in pts))}
 isrect=rectangle.issubset(set(pts));assert case['affine_dimension']==dim and case['rectangular']==isrect
 assert case['commutes']==(dim<2 or isrect)
 if case['name']=='S<=B3/2':assert all(dot(row,x)<=v for x in (p,q,t) for row,v in zip(AA,bb))
assert [case['commutes'] for case in r['cases']]==[False,False,True,True]
print('PASS: source-backed noncommuting diamond, impossible reverse filling, exact restricted images, line/rectangle repairs and persistent upper-bound obstruction')
