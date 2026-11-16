#!/usr/bin/env python3
"""Conditional geometry -> native seed transport audit.

All 12 A4-orbit comparison faces are ADDITIONAL assumptions. This script
proves matrix identities, finite edge-weight classification, a framed lift,
reflection covariance, and the failure of a naive Z4->Z2 Ramsey coloring.
"""
import json
from collections import Counter
from itertools import product
from pathlib import Path
import sympy as S

V='ABCD'
swap=dict(zip(V,'BADC'))
G=dict(zip(V,'BCAD')) # ABC cycle
H=dict(zip(V,'DACB')) # ADB cycle
ident={v:v for v in V}
def compose(p,q):return {v:p[q[v]] for v in V}
group={tuple(ident.values()):ident}; stack=[ident]
while stack:
    p=stack.pop()
    for generator in (G,H):
        q=compose(p,generator); key=tuple(q[v] for v in V)
        if key not in group:group[key]=q;stack.append(q)
assert len(group)==12
triples={tuple(p[v] for v in 'ABC') for p in group.values()}
assert len(triples)==12
assert ('A','B','C') in triples and ('A','D','B') in triples

J=S.Matrix([[-1,0,0],[0,0,1],[0,-1,0]])
R=-S.eye(3)
C=S.diag(-1,-1,1)
assert J**4==S.eye(3) and J**2==S.diag(1,-1,-1)
assert R*J*R==J and C*J*C==J.inv()
assert sum((J**i for i in range(4)),S.zeros(3))==S.zeros(3)
assert (S.eye(3)-J).det()!=0

pairs={
 'a':('AB','BA'), 'b':('AD','BC'), 'c':('CA','DB'),
 'd':('AC','BD'), 'e':('CB','DA'), 'f':('CD','DC')}
def labels(n,a,b):
    z={'a':a,'b':b,'c':a-b,'d':a+b,'e':2*a-b,'f':-a}
    return {e:z[k]%n for k,pair in pairs.items() for e in pair}
def flat(w,n):
    return all((w[u+v]+w[v+z]-w[u+z])%n==0 for u,v,z in triples)

all_solutions=[]
for a,b in product(range(4),repeat=2):
    w=labels(4,a,b)
    assert flat(w,4)
    assert all(w[e]==w[swap[e[0]]+swap[e[1]]] for e in w)
    # The homomorphic binary projection has one value on each opposite-edge matching.
    parity={''.join(sorted(e)):w[e]%2 for e in w}
    assert len(parity)==6
    matchings=[('AB','CD'),('AC','BD'),('AD','BC')]
    assert all(parity[x]==parity[y] for x,y in matchings)
    colors=tuple(parity[x] for x,y in matchings)
    assert sum(colors) in (0,2)
    # Extension requires both color graphs to be spanning paths.
    def degs(bit):
        return [sum(parity[''.join(sorted((v,u)))]==bit for u in V if u!=v) for v in V]
    assert not (degs(0)==[1,1,2,2] and degs(1)==[1,1,2,2])
    all_solutions.append({'a':a,'b':b,'matching_colors':colors,'seam':(2*a)%4})
assert len(all_solutions)==16
assert Counter(tuple(s['matching_colors']) for s in all_solutions)==Counter({(0,0,0):4,(0,1,1):4,(1,0,1):4,(1,1,0):4})

# Gauge shifts lambda_A=lambda_B and lambda_C=lambda_D vary b freely,
# leaving a untouched. Thus 4 reflection-compatible gauge classes.
gauge_classes={a:{tuple(sorted(labels(4,a,b).items())) for b in range(4)} for a in range(4)}
assert all(len(v)==4 for v in gauge_classes.values())
assert len({x['seam'] for x in all_solutions if x['a']%2})==1

# Geometry of the four marks and four-phase port copies.
marks={
 'A':S.Matrix([10,0,0]), 'B':S.Matrix([-10,0,0]),
 'C':S.Matrix([0,10,0]), 'D':S.Matrix([0,-10,0])}
assert all(R*marks[v]==marks[swap[v]] for v in V)
assert len({tuple(marks[v]) for v in V})==4
phase0=S.Matrix([0,1,0])
ring=[J**k*phase0 for k in range(4)]
assert len({tuple(x) for x in ring})==4
assert R*phase0==ring[2]

a,b=1,3
w=labels(4,a,b)

def affine(edge,position):
    u,v=edge
    return marks[v]+J**w[edge]*(position-marks[u])
# All original 6 edges and their promoted counterparts are pointed and reversible.
for e in w:
    u,v=e
    assert affine(e,marks[u])==marks[v]
    for k in range(4):
        assert affine(e,marks[u]+ring[k])==marks[v]+ring[(k+w[e])%4]
        # Reflection covariance, using source's point-reflection linear map -I.
        p=marks[u]+ring[k]
        se=swap[u]+swap[v]
        assert R*affine(e,p)==affine(se,R*p)
for u,v,z in triples:
    for k in range(4):
        p=marks[u]+ring[k]
        assert affine(v+z,affine(u+v,p))==affine(u+z,p)

p0=['CA','AD']
p1=['CA','AB','BA','AD']
seam=['AB','BA']
def run(word,p):
    for e in word:p=affine(e,p)
    return p
assert run(p0,marks['C'])==run(p1,marks['C'])==marks['D']
assert run(p0,marks['C']+ring[0])!=run(p1,marks['C']+ring[0])
assert all(run(seam,marks['A']+ring[k])==marks['A']+ring[(k+2)%4] for k in range(4))
assert run(seam,marks['A'])==marks['A']
assert all((2*w[e])%4 in (0,2) for e in w)

# No single common-centered J^w_e action can carry all 4 distinct marks
# in a connected native seed when w_AB=w_BA=a odd.
# AB then BA would imply J^(2a)*mA=mA, so J^2*mA=mA.
# J^2-fixed locus is the x-axis: all reachable marks are in a 2-orbit.
assert (J**2-S.eye(3)).nullspace()==[S.Matrix([1,0,0])]
# The genuinely observable ring is NOT fixed by J^2.
assert J**2*phase0!=phase0

# An inverting reflection on the phase fiber, with s^2=id, necessarily has
# lambda_A=lambda_B and w_BA=-w_AB at the reciprocal seam. Our a odd forbids it.
assert (w['AB']+w['BA'])%4==2
assert (w['AB']+(-w['AB']))%4==0

report={
 'status':'all_exact_checks_pass',
 'matrix_J': [list(map(int,J.row(i))) for i in range(3)],
 'J_order':4, 'J_square': [[int(J[i,j]) for j in range(3)] for i in range(3)] if False else [list(map(int,(J**2).row(i))) for i in range(3)],
 'first_clone_linear_reflection':'commutes with J',
 'central_clone_linear_reflection':'inverts J',
 'chiral_face_count':len(triples),
 'reflection_fixed_cocycle_solutions_Z4':len(all_solutions),
 'nonzero_seam_solutions':sum(x['seam']!=0 for x in all_solutions),
 'reflection_compatible_gauge_classes':4,
 'seam_nonzero_gauge_classes':[1,3],
 'binary_matching_patterns':{''.join(map(str,k)):v for k,v in Counter(tuple(s['matching_colors']) for s in all_solutions).items()},
 'binary_extendable_K4':0,
 'sample_edge_phases':w,
 'sample_p0_phase':sum(w[x] for x in p0)%4,
 'sample_p1_phase':sum(w[x] for x in p1)%4,
 'sample_seam_phase':sum(w[x] for x in seam)%4,
 'geometric_framed_lift':'4 distinct base centers, 5-point fibers, full reflection covariance',
 'scope':'Geometric point-mark frames and chiral 2-cells are independently chosen; no native source adapter established.'
}
output=Path('/mnt/data/marici_geometric_phase_bridge_audit_results.json')
output.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
