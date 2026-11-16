"""Interval-arithmetic certificate for 13-node 3D frames plus a 17-node 5D Ramsey extension.

The vertices have exact INTEGER coordinates. All 78 quaternion inner-product
signs are evaluated with outward-rounded intervals (mpmath.iv). Reversal of
individual frame lifts is fixed by demanding positive quaternion products
on consecutive edges of the specified single 13-cycle.

Run: python verify_ramsey35_integer_exact.py
"""
from itertools import combinations
from pathlib import Path
from mpmath import iv

iv.dps = 60
I = iv.mpf
P = [
    (  0,   0,   0),
    (-46,   5, -27),
    ( -9,  36, -29),
    (-35,  57, -70),
    (-31,  89, -33),
    (  5, 117, -51),
    (-27, 125, -11),
    ( -3, 115,  28),
    (-12, 156,  56),
    (-11, 109,  44),
    ( 27,  82,  55),
    (-14,  55,  70),
    (  2,  43,  25),
]
N = len(P)
assert N == 13 and len(set(P)) == N

def dot(u,v): return sum(a*b for a,b in zip(u,v))
def cross(u,v):
    return (u[1]*v[2]-u[2]*v[1],
            u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])
def norm(u): return iv.sqrt(dot(u,u))
def unit(u):
    mag=norm(u)
    assert mag > 0
    return tuple(a/mag for a in u)
def sign(x):
    if x > 0: return 1
    if x < 0: return -1
    raise AssertionError('Interval contains zero: %s' % x)

points=[tuple(I(c) for c in p) for p in P]
steps=[tuple(points[(i+1)%N][d]-points[i][d] for d in range(3)) for i in range(N)]
tangents=[unit(s) for s in steps]
binormals=[unit(cross(steps[(i-1)%N],steps[i])) for i in range(N)]
normal=[cross(w,t) for w,t in zip(binormals,tangents)]
frames=[[[tangents[i][row],normal[i][row],binormals[i][row]]
        for row in range(3)] for i in range(N)]

def quaternion_of_rotation(R):
    # Use the numerically largest quaternion component to choose a branch.
    tr=R[0][0]+R[1][1]+R[2][2]
    v=[tr, R[0][0]*2-tr, R[1][1]*2-tr, R[2][2]*2-tr]
    branch=max(range(4),key=lambda i:float(v[i].a))
    if branch == 0:
        s=2*iv.sqrt(1+tr)
        return (s/4,(R[2][1]-R[1][2])/s,(R[0][2]-R[2][0])/s,(R[1][0]-R[0][1])/s)
    if branch == 1:
        s=2*iv.sqrt(1+R[0][0]-R[1][1]-R[2][2])
        return ((R[2][1]-R[1][2])/s,s/4,(R[0][1]+R[1][0])/s,(R[0][2]+R[2][0])/s)
    if branch == 2:
        s=2*iv.sqrt(1+R[1][1]-R[0][0]-R[2][2])
        return ((R[0][2]-R[2][0])/s,(R[0][1]+R[1][0])/s,s/4,(R[1][2]+R[2][1])/s)
    s=2*iv.sqrt(1+R[2][2]-R[0][0]-R[1][1])
    return ((R[1][0]-R[0][1])/s,(R[0][2]+R[2][0])/s,(R[1][2]+R[2][1])/s,s/4)

q=[quaternion_of_rotation(F) for F in frames]
for i in range(1,N):
    if sign(dot(q[i-1],q[i]))<0:
        q[i]=tuple(-x for x in q[i])
assert sign(dot(q[N-1],q[0]))>0, 'The closed B traversal is not positive-liftable'

adj=[[False]*N for _ in range(N)]
minimum_gap=1.0
for i,j in combinations(range(N),2):
    dij=dot(q[i],q[j]); z=sign(dij)
    actual_A=(z<0)
    cyclic_dist=min(j-i,N-(j-i))
    expected_A=(cyclic_dist in (2,3))
    assert actual_A == expected_A, (i,j,z,cyclic_dist)
    adj[i][j]=adj[j][i]=actual_A
    minimum_gap=min(minimum_gap,abs(float(dij.a)),abs(float(dij.b)))

assert all(not all(adj[i][j] for i,j in combinations(S,2))
           for S in combinations(range(N),3)), 'A-triangle exists'
assert all(any(adj[i][j] for i,j in combinations(S,2))
           for S in combinations(range(N),5)), 'Independent five-set exists'
assert sum(adj[i][j] for i,j in combinations(range(N),2))==26
print('CERTIFIED: 13 integer-coordinate nodes, closed single B-cycle')
print('All 78 A/B assignments are strictly determined by 3D Frenet-frame spinor signs')
print('A-distance classes: {2,3} modulo 13; A-edges = 26')
print('A-triangles = 0; independent five-sets = 0')
print('Minimum certified absolute quaternion dot lower bound >',minimum_gap)

# Preserve the quaternion four-coordinate projection of all 13 original nodes.
# Give each a fifth coordinate exactly 61/100.
# The four new nodes have integer 5D coordinates / 1_000_000.
# The common scale of each new vector is immaterial to the inner-product signs.
epsilon=I(61)/100
Y=[tuple(q[i])+ (epsilon,) for i in range(13)]
NEW_INT=[
    (-511255, 372613, -324622,  230384, 664320),
    ( 569744, 490616, -308438, -413180, 410897),
    (-269717,-213302,  587795, -626489, 379161),
    ( 299013,-593714,  242105,  538146, 458126),
]
Y.extend(tuple(I(v)/I(1_000_000) for v in row) for row in NEW_INT)
assert len(Y)==17

# Exactly the A-neighbors expected from the 13+4 decomposition.
ATTACH=[{8,9},{6,11,12},{4,5,10},{1,2,7}]
C4={(13,15),(13,16),(14,15),(14,16)}

adj17=[[False]*17 for _ in range(17)]
minimum=1e6
for i,j in combinations(range(17),2):
    tij=dot(Y[i],Y[j])
    negative=sign(tij)<0
    if j<13:
        expected=min((j-i)%13,(i-j)%13) in (2,3)
    elif i<13:
        expected=i in ATTACH[j-13]
    else:
        expected=(i,j) in C4
    assert negative==expected, (i,j,negative,expected)
    adj17[i][j]=adj17[j][i]=negative
    minimum=min(minimum,abs(float(tij.a)),abs(float(tij.b)))

assert sum(adj17[i][j] for i,j in combinations(range(17),2))==41
assert all(not all(adj17[i][j] for i,j in combinations(S,2))
           for S in combinations(range(17),3)), 'A triangle'
assert all(any(adj17[i][j] for i,j in combinations(S,2))
           for S in combinations(range(17),6)), 'B independent 6'
print('CERTIFIED: full 17-node graph has 41 A-edges, no A triangles, no B six-sets')
print('CERTIFIED: the four new nodes induce C4 with A-edges:',sorted(C4))
print('CERTIFIED: new-to-old attachment sets:',[sorted(S) for S in ATTACH])
print('CERTIFIED: first 4 coordinates of original 13 nodes exactly preserve their 3D Frenet quaternions')
print('CERTIFIED: common fifth coordinate 61/100, four rational additional 5-vectors')
print('Minimum certified absolute dot-product lower bound >', minimum)
print('NOTE: These are 5D sign vectors. The 17-vector configuration has NOT been')
print('      realized as the Frenet frames of a single closed 17-node path in R3.')

# Single-cycle generators matching the nested A-subset/B-whole-set requirement.
# On old 13 nodes, a makes the step +2, which is always an A-connection.
A_CYCLE=[(2*i)%13 for i in range(13)]
# On all 17 nodes, b makes one B-cycle; it inserts each extra node
# into a different edge of the original B-cycle (0,1,...,12).
B_CYCLE=[0,13,1,2,14,3,4,5,6,15,7,8,16,9,10,11,12]
assert len(set(A_CYCLE))==13 and set(A_CYCLE)==set(range(13))
assert len(set(B_CYCLE))==17 and set(B_CYCLE)==set(range(17))
assert all(adj17[A_CYCLE[i]][A_CYCLE[(i+1)%13]]
           for i in range(13))
assert all(not adj17[B_CYCLE[i]][B_CYCLE[(i+1)%17]]
           for i in range(17))
print('CERTIFIED: one closed A-cycle on the original 13 nodes,')
print('           one closed B-cycle on all 17 nodes, A subset B.')
print('A-cycle:',A_CYCLE)
print('B-cycle:',B_CYCLE)
