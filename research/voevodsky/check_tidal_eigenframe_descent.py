"""Exact tidal eigenframe/overlap controls; no causal Einstein solver.
Universal topological and degeneration arguments are in the companion note.
"""
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

ROOT=Path(__file__).resolve().parents[2]
receipt=ROOT/'research/nima/results/machian-newtonian-localization.json'
old=json.loads(receipt.read_text(encoding='utf-8'))
D=tuple(tuple(F(x) for x in row) for row in old['jet_a']['hessian'])
I=tuple(tuple(F(i==j) for j in range(3)) for i in range(3))
Z=tuple(tuple(F(0) for j in range(3)) for i in range(3))
def tr(a):return tuple(zip(*a))
def mm(a,b):return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def add(a,b):return tuple(tuple(a[i][j]+b[i][j] for j in range(3)) for i in range(3))
def sc(c,a):return tuple(tuple(c*x for x in row) for row in a)
def conj(r,a):return mm(mm(r,a),tr(r))
def diag(v):return tuple(tuple(F(v[i]) if i==j else F(0) for j in range(3)) for i in range(3))
def rz(c,s):return ((c,-s,F(0)),(s,c,F(0)),(F(0),F(0),F(1)))
def rx(c,s):return ((F(1),F(0),F(0)),(F(0),c,-s),(F(0),s,c))
def determinant(a):return sum((-1)**sum(p[i]>p[j] for i in range(3) for j in range(i+1,3))*a[0][p[0]]*a[1][p[1]]*a[2][p[2]] for p in permutations(range(3)))
def projectors(e,lam):
    out=[]
    for i in range(3):
        p=I
        for j in range(3):
            if i!=j:p=mm(p,sc(1/(lam[i]-lam[j]),add(e,sc(-lam[j],I))))
        out.append(p)
    return out
lam=tuple(D[i][i] for i in range(3))
R=rz(F(3,5),F(4,5));S=rx(F(5,13),F(12,13))
Ps=projectors(D,lam);E=conj(R,D);Pr=projectors(E,lam)
checks={
 'fixture_simple_spectrum':len(set(lam))==3,
 'rational_frames_are_oriented_orthogonal':all(mm(tr(r),r)==I and determinant(r)==1 for r in (R,S)),
 'projectors_resolve_identity':add(add(Ps[0],Ps[1]),Ps[2])==I,
 'projector_orthogonality':all(mm(Pr[i],Pr[j])==(Pr[i] if i==j else Z) for i in range(3) for j in range(3)),
 'spectral_reconstruction':add(add(sc(lam[0],Pr[0]),sc(lam[1],Pr[1])),sc(lam[2],Pr[2]))==E,
 'projector_rotation_naturality':all(Pr[i]==conj(R,Ps[i]) for i in range(3)),
}
V4=[diag(s) for s in product((-1,1),repeat=3) if s[0]*s[1]*s[2]==1]
checks['four_generic_sign_choices']=len(V4)==4 and all(conj(mm(R,s),D)==E for s in V4)
checks['signs_invisible_to_projectors']=all(conj(mm(R,s),Ps[i])==Pr[i] for s in V4 for i in range(3))
# Chart frames map local vector coordinates to one declared shared Euclidean space.
frames=(I,R,mm(R,S))
trans=lambda i,j:mm(tr(frames[i]),frames[j]) # j-local -> i-local
local=[conj(tr(r),D) for r in frames]
checks['overlap_tensor_compatibility']=all(conj(trans(i,j),local[j])==local[i] for i in range(3) for j in range(3))
checks['actual_frame_triple_cocycle']=mm(trans(0,1),trans(1,2))==trans(0,2)
# Pairwise valid stabilizer maps are not automatically a coherent cocycle.
h=diag((-1,-1,1))
checks['hostile_all_pairs_preserve_tidal_data']=conj(h,D)==D and conj(I,D)==D
checks['hostile_triple_rejected']=mm(I,I)!=h
# Spectral loop Rz(theta)D Rz(theta)^T, theta from 0 to pi.
checks['loop_returns_same_tensor']=conj(h,D)==D
checks['loop_frame_does_not_return']=h!=I
checks['loop_midpoint_not_constant_tensor']=conj(rz(F(0),F(1)),D)!=D
# Double-eigenvalue limit: frames rotated within yz-plane give distinct splits.
A=diag((-2,1,1));U=rx(F(3,5),F(4,5))
checks['axial_limit_rotation_invariant']=conj(U,A)==A
checks['axial_split_not_uniquely_extendible']=conj(U,Ps[1])!=Ps[1]
checks['axial_cluster_projector_invariant']=conj(U,add(Ps[1],Ps[2]))==add(Ps[1],Ps[2])
for eps in (F(1,2),F(1,10),F(1,100)):
    vals=(F(-2),1-eps,1+eps);a=diag(vals);b=conj(U,a)
    checks['split_projectors_at_epsilon_'+str(eps)]=projectors(a,vals)[1]==Ps[1] and projectors(b,vals)[1]==conj(U,Ps[1])
checks['axial_disconnected_stabilizer_present']=conj(diag((-1,1,-1)),A)==A
checks['flat_all_test_rotations_preserved']=all(conj(r,Z)==Z for r in (R,S,U,h))
paths=[Path(__file__),receipt,ROOT/'research/nima/checkers/check_machian_local_tidal_frame.py',ROOT/'research/aspect/a-berry-eigenline-falsifies-frozen-v10.md']
packet=dict(passed=all(checks.values()),checks=checks,fixture_eigenvalues=list(map(str,lam)),
 scope='Finite exact frame and projector tests. Loop no-section theorem and all-epsilon degeneration proof are written mathematics; no causal gluing or physical holonomy claim.',
 source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
Path(__file__).with_name('tidal-eigenframe-descent.json').write_text(json.dumps(packet,indent=2)+'\n',encoding='utf-8')
print(json.dumps(packet,indent=2))
raise SystemExit(0 if packet['passed'] else 1)
