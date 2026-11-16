"""Exact integer certification of a 17-vertex (3,6)-Ramsey critical graph.

Take 17 4-dimensional integer vectors v_i. Normalize them to unit quaternions.
A iff <v_i,v_j>/||v_i||||v_j|| < -1/2.
No floating arithmetic is used in the graph verification.
"""
from itertools import combinations
from math import isqrt
from pathlib import Path

path=Path(__file__).with_name('ramsey36_natural_half_quaternions.csv')
V=[tuple(map(int,row.split(','))) for row in path.read_text().splitlines()[1:]]
N=len(V)
assert N==17 and all(len(x)==4 and x!=(0,0,0,0) for x in V)

def dot(x,y):return sum(a*b for a,b in zip(x,y))
ns=[dot(v,v) for v in V]
A=[[False]*N for _ in range(N)]
for i,j in combinations(range(N),2):
 d=dot(V[i],V[j]); ai=(d<0 and 4*d*d>ns[i]*ns[j]);A[i][j]=A[j][i]=ai
assert sum(A[i][j] for i,j in combinations(range(N),2))==41
assert not any(all(A[i][j] for i,j in combinations(t,2)) for t in combinations(range(N),3))
assert not any(not any(A[i][j] for i,j in combinations(s,2)) for s in combinations(range(N),6))

A_cycle=[0,3,1,10,2,8,13,11,6,16,4,7,5]
assert len(set(A_cycle))==13
assert all(A[A_cycle[i]][A_cycle[(i+1)%13]] for i in range(13))
B_cycle=[0,16,15,14,13,12,11,10,9,5,8,3,4,6,2,7,1]
assert sorted(B_cycle)==list(range(N))
assert all(not A[B_cycle[i]][B_cycle[(i+1)%17]] and dot(V[B_cycle[i]],V[B_cycle[(i+1)%17]])>0 for i in range(17))

from math import sqrt
pairdots=[dot(V[i],V[j])/sqrt(ns[i]*ns[j]) for i,j in combinations(range(N),2)]
pairs=list(combinations(range(N),2))
maxA=max(d for (i,j),d in zip(pairs,pairdots) if A[i][j]);minB=min(d for (i,j),d in zip(pairs,pairdots) if not A[i][j]);minbstep=min(dot(V[B_cycle[i]],V[B_cycle[(i+1)%17]])/sqrt(ns[B_cycle[i]]*ns[B_cycle[(i+1)%17]]) for i in range(17))
print('CERTIFIED: 17 nodes, 41 A edges, no A triangle, no B independent 6-set.')
print('Threshold -1/2: max A dot',maxA,'min B dot',minB)
print('B Hamiltonian cycle with strictly positive quaternion dots:',B_cycle)
print('minimum B step dot:',minbstep)
print('A 13-cycle:',A_cycle)
