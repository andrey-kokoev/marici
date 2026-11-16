"""Self-contained certificate for nested closed cycles and a nonuniform rotor field.

This is a construction of one (3,6)-Ramsey witness, NOT a formula for R(n,m).
A contains 13 nodes with a closed A-edge traversal; B contains all 17 nodes
with a closed B-edge traversal. All nodes carry quaternions and Hopf-projected
positions in R^3. A edge iff quaternion inner product < -1/2.
"""
from itertools import combinations
from math import sqrt
import numpy as np

V = np.array([
    [-493067,-32030,866007,-76752],
    [69223,-278520,511931,-809667],
    [505843,548009,551010,-374430],
    [426929,399069,-330195,741247],
    [-533358,729800,-400809,149243],
    [-385271,62017,-892348,-226793],
    [641523,418078,-322636,-556386],
    [520018,2615,816183,251833],
    [365212,-791716,-460272,167198],
    [-786791,-61869,162630,592186],
    [-421470,-514168,-573733,478356],
    [64076,44612,373680,924266],
    [-204254,896273,388055,66240],
    [-721940,332549,-79915,-601520],
    [43700,-364690,-470574,-802279],
    [734867,-588584,309400,-133459],
    [-301103,-944666,116497,-58061],
], dtype=np.int64)
N = 17
norm2 = [sum(int(t)**2 for t in v) for v in V]
edge = np.zeros((N,N), dtype=bool)
for i,j in combinations(range(N), 2):
    dij = sum(int(a)*int(b) for a,b in zip(V[i],V[j]))
    edge[i,j] = edge[j,i] = (dij < 0 and 4*dij*dij > norm2[i]*norm2[j])
assert int(np.triu(edge,1).sum()) == 41
assert not any(all(edge[i,j] for i,j in combinations(s,2)) for s in combinations(range(N),3))
assert not any(not any(edge[i,j] for i,j in combinations(s,2)) for s in combinations(range(N),6))

A_cycle = [0,3,1,10,2,8,13,11,6,16,4,7,5]
B_cycle = [0,16,15,14,13,12,11,10,9,5,8,3,4,6,2,7,1]
assert len(A_cycle)==len(set(A_cycle))==13
assert sorted(B_cycle)==list(range(N))
assert all(edge[A_cycle[i],A_cycle[(i+1)%13]] for i in range(13))
assert all(not edge[B_cycle[i],B_cycle[(i+1)%N]] for i in range(N))

Q=V/np.linalg.norm(V,axis=1)[:,None]
G=Q@Q.T
margin = min(abs(G[i,j]+0.5) for i,j in combinations(range(N),2))
assert margin > 0.063
assert all(G[B_cycle[i],B_cycle[(i+1)%N]]>0 for i in range(N))

def conjugate(q): return np.array([q[0],-q[1],-q[2],-q[3]])
def product(p,q):
    a,b,c,d=p; e,f,g,h=q
    return np.array([a*e-b*f-c*g-d*h,
                     a*f+b*e+c*h-d*g,
                     a*g-b*h+c*e+d*f,
                     a*h+b*g-c*f+d*e])

# Hopf projection from spinors onto unit vectors in R^3.
E = np.array([0., 0., 0., 1.])
X=np.array([product(product(q,E),conjugate(q))[1:] for q in Q])
sep = min(np.linalg.norm(X[i]-X[j]) for i,j in combinations(range(N),2))
assert sep > 0.15 and np.allclose(np.linalg.norm(X,axis=1),1)

def verify_cycle(cycle, required_holonomy):
    total=np.array([1.,0.,0.,0.])
    direct=np.array([1.,0.,0.,0.])
    for i in range(len(cycle)):
        z,w=Q[cycle[i]],Q[cycle[(i+1)%len(cycle)]]
        U=product(w,conjugate(z))
        s=1 if np.dot(z,w)>0 else -1
        shortest=s*U
        total=product(shortest,total)
        direct=product(U,direct)
        assert np.linalg.norm(product(product(U,product(product(z,E),conjugate(z))),conjugate(U))[1:] - product(product(w,E),conjugate(w))[1:])<1e-12
    assert np.linalg.norm(direct-np.array([1.,0.,0.,0.]))<1e-12
    assert np.linalg.norm(total-np.array([required_holonomy,0.,0.,0.]))<1e-12
    assert np.linalg.norm(sum((X[cycle[(i+1)%len(cycle)]]-X[cycle[i]] for i in range(len(cycle))), np.zeros(3)))<1e-12
    return total

verify_cycle(A_cycle, -1)
verify_cycle(B_cycle, +1)

# Exact Cartesian/additive decomposition of the same quaternion data.
u,v=Q[:,:2],Q[:,2:]
x=u+v
h=(u-v)/2
assert np.allclose(Q@Q.T,0.5*x@x.T+2*h@h.T,atol=1e-12)
assert min(np.linalg.norm(x[i]-x[j]) for i,j in combinations(range(N),2))>0.06
assert np.linalg.norm(sum((x[B_cycle[(i+1)%N]]-x[B_cycle[i]] for i in range(N)), np.zeros(2)))<1e-12

# Cyclic-equivalence defect in THIS chosen B traversal.
runs=[]
for d in range(1,(N-1)//2+1):
    bits=np.array([int(edge[B_cycle[i],B_cycle[(i+d)%N]]) for i in range(N)])
    runs.append(int(np.sum(bits != np.roll(bits,1))//2))
delta=2*sum(runs)
assert runs==[0,2,3,3,6,5,5,4] and delta==56

eta=np.rad2deg(np.arctan2(np.linalg.norm(v,axis=1),np.linalg.norm(u,axis=1)))
print('17 nodes; 41 A connections; no A triangle; no B independent 6-set')
print('A: 13-cycle; B: 17-cycle; both close in SO(3) and in 3D position')
print('spin holonomy of shortest relative rotations: A = -1, B = +1')
print('Hopf-projected min node separation:',round(sep,9))
print('Threshold margin:',round(margin,9))
print('Cartesian/additive identity: exact to rounding tolerance')
print('internal mixing angles (degrees) range:',round(min(eta),3), round(max(eta),3))
print('B-cycle distance-class runs:',runs)
print('B-cycle cyclic-equivalence defect:',delta)
