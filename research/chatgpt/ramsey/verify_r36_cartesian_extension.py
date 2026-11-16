"""Interval-arithmetic certificate for a 13-node R(3,5) Frenet-frame construction.

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


# =============================================================
# Certified extension obstruction and graph catalogue comparison
# =============================================================
import networkx as nx

CIRCUITS=[
    (0,1,2,4,6), (3,5,7,8,9), (1,3,10,11,12),
    (0,2,8,10,11), (4,6,7,9,10), (0,2,3,5,12),
    (1,7,9,11,12), (1,3,4,6,8), (4,6,8,10,11),
    (0,2,8,10,12), (0,2,5,9,11), (0,2,4,6,9)
]
from itertools import permutations
allperms=list(permutations(range(4)))
def permsign(p):
    return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1
signedperms=[(p,permsign(p)) for p in allperms]
def det4(rows):
    return sum(sgn*rows[0][p[0]]*rows[1][p[1]]*rows[2][p[2]]*rows[3][p[3]]
        for p,sgn in signedperms)
for C in CIRCUITS:
    coeff=[]
    for skip in range(5):
        sub=[C[i] for i in range(5) if i!=skip]
        mat=[[q[i][r] for i in sub] for r in range(4)]
        coeff.append((-1)**skip*det4(mat))
    assert len({sign(c) for c in coeff})==1, C
for deleted in combinations(range(13),3):
    assert any(set(C).isdisjoint(deleted) for C in CIRCUITS)
print('CERTIFIED: each possible 10 of 13 quaternion points contains the origin')
print('in its convex hull (witnessed by one of 12 positive 5-point circuits).')
print('THEREFORE: no new quaternion can have <4 negative dot products with the 13.')

# Seven non-isomorphic R(3,6,17) critical graphs in graph6 encoding
GRAPH6 = ['P??GaOo`XMGsIcT?pSLaGuA?', 'P?C?I_h`SDEQQcLAh`dU?tG?', 'P@oGQA?`ACcdCtDYC]Ah?goC', 'PG?OSAKccKGiGwJSI[@oWUA_', 'PGD?OkeO_WAEGQobP_s`cgU?', 'Ps`A?WIDGeCdGsQEKK?oLL_O', 'Ps`A?_KChFCiBoQSKCOoXL_O']
H=nx.Graph();H.add_nodes_from(range(13))
H.add_edges_from((i,j) for i in range(13) for j in range(i+1,13)
            if min((j-i)%13,(i-j)%13) in (2,3))
assert H.number_of_edges()==26
A=list(nx.algorithms.isomorphism.GraphMatcher(H,H).isomorphisms_iter())
assert len(A)==52
from collections import Counter
counts=[];orbit_patterns=Counter()
for index,s in enumerate(GRAPH6,1):
    G=nx.from_graph6_bytes(s.encode())
    assert G.number_of_nodes()==17
    assert all(not all(G.has_edge(i,j) for i,j in combinations(T,2))
               for T in combinations(G.nodes(),3))
    assert all(any(G.has_edge(i,j) for i,j in combinations(T,2))
               for T in combinations(G.nodes(),6))
    embeddings=0
    for map17to13 in nx.algorithms.isomorphism.GraphMatcher(G,H).subgraph_isomorphisms_iter():
        embeddings+=1
        new=set(G.nodes())-set(map17to13)
        induced=G.subgraph(new)
        assert induced.number_of_edges()==4
        assert all(d==2 for _,d in induced.degree()) # exactly C4
        assert all(len(set(G.neighbors(u)) & set(map17to13)) in (2,3) for u in new)
        for u in new:
            nbr=tuple(sorted(map17to13[v] for v in map17to13 if G.has_edge(u,v)))
            rep=min(tuple(sorted(a[v] for v in nbr)) for a in A)
            orbit_patterns[rep]+=1
    counts.append(embeddings//52)
print('CERTIFIED: number of distinct induced 13-node copies across 7 graphs:',counts)
assert sum(counts)==14
print('CERTIFIED: each remaining 4-node induced graph is C4 = K2 Cartesian K2.')
assert set(orbit_patterns)=={(0,1),(0,1,5)}
print('CERTIFIED: only two possible A-attachment types, up to 13-node symmetry:',orbit_patterns)
print('GEOMETRIC CONTRADICTION: each new C4 node has 2 internal A-neighbors,')
print('and needs <=3 A-neighbors among the original 13 (total max degree 5),')
print('but the fixed 13-node Frenet realization forces >=4 old A-neighbors.')
print('NOTE: does NOT rule out deforming the original 13-node frames.')
