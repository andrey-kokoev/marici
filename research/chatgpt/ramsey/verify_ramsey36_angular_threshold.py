"""Exact integer certificate: 17 unit 4D vectors with one common positive angular threshold.
No numpy/scipy needed. Run: python verify_ramsey36_angular_threshold.py
"""
from itertools import combinations
from math import isqrt
V = [
    [579471, 380654, 395853, -602177],
    [837840, 170865, 382164, -350399],
    [-755823, 429836, 424061, -253267],
    [97196, 20307, 975408, -196773],
    [505262, -70207, -203519, -835680],
    [-58306, 856670, -271175, 434949],
    [-223856, 504272, -767738, -325848],
    [-738905, 477607, 398979, 258316],
    [478217, 458709, -654513, 364017],
    [-232223, -884587, -269678, -301417],
    [782674, -237491, 515088, -256326],
    [-567591, -721727, 337862, -206882],
    [553494, -48915, 280449, 782688],
    [-426123, -502006, -472864, -585499],
    [-423077, -43312, 634776, 645127],
    [357039, -141848, -718200, 580165],
    [-528373, 319067, -699911, 359365],
]
N=17
TH_NUM=3; TH_DEN=8
ACYCLE=[0,16,1,11,8,14,4,7,15,3,13,5,9]
BCYCLE=[9,11,13,16,15,8,6,5,7,2,14,12,1,0,10,3,4]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def squarednorm(v):return dot(v,v)
def atype(i,j):
    c=dot(V[i],V[j]); t=TH_NUM**2*squarednorm(V[i])*squarednorm(V[j]);v=c*c*TH_DEN**2
    if c>=0:return False
    assert v!=t,('degenerate at threshold',i,j)
    return v>t
assert len(V)==17 and all(len(q)==4 for q in V)
adj=[[False]*N for _ in range(N)]
for i,j in combinations(range(N),2): adj[i][j]=adj[j][i]=atype(i,j)
assert sum(adj[i][j] for i,j in combinations(range(N),2))==41
assert all(not all(adj[i][j] for i,j in combinations(S,2)) for S in combinations(range(N),3))
assert all(any(adj[i][j] for i,j in combinations(S,2)) for S in combinations(range(N),6))
assert len(set(ACYCLE))==13
assert len(set(BCYCLE))==N
assert all(adj[ACYCLE[i]][ACYCLE[(i+1)%13]] for i in range(13))
assert all(not adj[BCYCLE[i]][BCYCLE[(i+1)%N]] for i in range(N))
assert all(dot(V[BCYCLE[i]],V[BCYCLE[(i+1)%N]])>0 for i in range(N))
print('EXACT CERTIFIED: 17 nodes, 41 A-pairs; A-triangle-free, no independent 6')
print('EXACT CERTIFIED: single A-cycle of length 13 and B-cycle of length 17')
print('EXACT CERTIFIED: all 17 B-steps have POSITIVE quaternion inner products')
print('EXACT CERTIFIED: A iff normalized q_i dot q_j < -3/8')
print('A-cycle',ACYCLE)
print('B-cycle',BCYCLE)
