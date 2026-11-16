"""Interval-arithmetic certificate of a 17-vertex R(3,6) witness from 3D Frenet geometry.

The graph is induced by the 3D closed polygon's discrete Frenet frames,
whose continuously selected unit quaternion lifts q_i yield A iff q_i.q_j < -3/8.
Run: python verify_ramsey36_frenet17_integer_exact.py
"""
from itertools import combinations
from pathlib import Path
from mpmath import iv

iv.dps=70
I=iv.mpf
P=[tuple(map(int,line.split(','))) for line in Path(__file__).with_name('ramsey36_frenet17_integer.csv').read_text().splitlines()[1:]]
ORDER=[0, 1, 8, 16, 13, 9, 15, 5, 14, 2, 11, 7, 6, 4, 10, 12, 3]
A_CYCLE_LABELS=[0,16,1,11,8,14,4,7,15,3,13,5,9]
N=len(P)
assert N==17 and len(set(P))==17

def dot(u,v):return sum(a*b for a,b in zip(u,v))
def cross(u,v):
 return (u[1]*v[2]-u[2]*v[1],u[2]*v[0]-u[0]*v[2],u[0]*v[1]-u[1]*v[0])
def norm(u):return iv.sqrt(dot(u,u))
def unit(u):
 mag=norm(u)
 assert mag>0
 return tuple(a/mag for a in u)
def sign(x):
 if x>0:return 1
 if x<0:return -1
 raise AssertionError('interval contains zero '+str(x))

points=[tuple(I(c) for c in p) for p in P]
steps=[tuple(points[(i+1)%N][d]-points[i][d] for d in range(3)) for i in range(N)]
tangents=[unit(s) for s in steps]
binormals=[unit(cross(steps[(i-1)%N],steps[i])) for i in range(N)]
normals=[cross(w,t) for w,t in zip(binormals,tangents)]
frames=[[[tangents[i][r],normals[i][r],binormals[i][r]] for r in range(3)] for i in range(N)]

def quaternion_of_rotation(R):
 tr=R[0][0]+R[1][1]+R[2][2]
 v=[tr,R[0][0]*2-tr,R[1][1]*2-tr,R[2][2]*2-tr]
 branch=max(range(4),key=lambda i:float(v[i].a))
 if branch==0:
  s=2*iv.sqrt(1+tr)
  return (s/4,(R[2][1]-R[1][2])/s,(R[0][2]-R[2][0])/s,(R[1][0]-R[0][1])/s)
 if branch==1:
  s=2*iv.sqrt(1+R[0][0]-R[1][1]-R[2][2])
  return ((R[2][1]-R[1][2])/s,s/4,(R[0][1]+R[1][0])/s,(R[0][2]+R[2][0])/s)
 if branch==2:
  s=2*iv.sqrt(1+R[1][1]-R[0][0]-R[2][2])
  return ((R[0][2]-R[2][0])/s,(R[0][1]+R[1][0])/s,s/4,(R[1][2]+R[2][1])/s)
 s=2*iv.sqrt(1+R[2][2]-R[0][0]-R[1][1])
 return ((R[1][0]-R[0][1])/s,(R[0][2]+R[2][0])/s,(R[1][2]+R[2][1])/s,s/4)

q=[quaternion_of_rotation(F) for F in frames]
for i in range(1,N):
 if sign(dot(q[i-1],q[i]))<0:q[i]=tuple(-x for x in q[i])
assert sign(dot(q[N-1],q[0]))==1,'B traversing holonomy is nontrivial'

# Graph induced by the 3D geometry
adj=[[False]*N for _ in range(N)]
min_margin=float('inf');min_bstep=float('inf')
for i,j in combinations(range(N),2):
 d=dot(q[i],q[j])
 margin=d+I(3)/8
 adj[i][j]=adj[j][i]=(sign(margin)<0)
 low= float(margin.a) if sign(margin)>0 else -float(margin.b)
 min_margin=min(min_margin,low)
for i in range(N):
 step=dot(q[i],q[(i+1)%N]);assert sign(step)>0
 min_bstep=min(min_bstep,float(step.a))

assert sum(adj[i][j] for i,j in combinations(range(N),2))==41
assert all(not all(adj[i][j] for i,j in combinations(s,2)) for s in combinations(range(N),3))
assert all(any(adj[i][j] for i,j in combinations(s,2)) for s in combinations(range(N),6))
orig_index={v:i for i,v in enumerate(ORDER)}
a_cycle=[orig_index[v] for v in A_CYCLE_LABELS]
assert len(a_cycle)==13 and len(set(a_cycle))==13
assert all(adj[a_cycle[i]][a_cycle[(i+1)%13]] for i in range(13))
assert all(not adj[i][(i+1)%N] for i in range(N))

# Compare against independently certified graph from the 17 input integer quaternions.
refv=[
 [579471,380654,395853,-602177],[837840,170865,382164,-350399],
 [-755823,429836,424061,-253267],[97196,20307,975408,-196773],
 [505262,-70207,-203519,-835680],[-58306,856670,-271175,434949],
 [-223856,504272,-767738,-325848],[-738905,477607,398979,258316],
 [478217,458709,-654513,364017],[-232223,-884587,-269678,-301417],
 [782674,-237491,515088,-256326],[-567591,-721727,337862,-206882],
 [553494,-48915,280449,782688],[-426123,-502006,-472864,-585499],
 [-423077,-43312,634776,645127],[357039,-141848,-718200,580165],
 [-528373,319067,-699911,359365]]
def ri(i,j):
 a=refv[ORDER[i]];b=refv[ORDER[j]]
 d=sum(x*y for x,y in zip(a,b));ss=(sum(x*x for x in a))*(sum(x*x for x in b))
 return d<0 and 64*d*d>9*ss
assert all(adj[i][j]==ri(i,j) for i,j in combinations(range(N),2))
print('CERTIFIED integer 3D 17-node closed Frenet path')
print('A edges=41, A triangles=0, B-independent 6-subsets=0')
print('B single cycle length=17, A single cycle length=13')
print('All B-step quaternion dots positive, minimum >',min_bstep)
print('Minimum margin from -3/8 >',min_margin)
print('All 136 A/B edges match independently certified 17-node graph')
print('B order (original labels)',ORDER)
print('A cycle indices in path order',a_cycle)
