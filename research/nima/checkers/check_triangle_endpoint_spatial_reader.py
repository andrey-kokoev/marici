"""Covariant spatial reading of actual cross-composition endpoint counts.

Uses the existing tetrahedral point realization. It does not identify counts
with mass, endpoints with particle positions, or construction order with time.
"""
from contextlib import redirect_stdout
from itertools import permutations
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S
from check_twelve_triangle_positive_geometry import POINTS

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
with redirect_stdout(io.StringIO()):
    previous=runpy.run_path(str(HERE/'check_triangle_successor_rung_reader.py'))
composition=previous['composition']
X=S.Matrix.hstack(*(S.Matrix(POINTS[v]) for v in 'ABCD'))
left=S.Matrix(composition['target_read'](composition['products']['LR']))
right=S.Matrix(composition['target_read'](composition['products']['RL']))
checks=[]
def check(name,condition):
    if not condition:raise AssertionError(name)
    checks.append(name)


check('existing-tetrahedral-Gram',X.T*X==4*S.eye(4)-S.ones(4))
check('common-mode-annihilated',X*S.ones(4,1)==S.zeros(3,1))
check('contrast-isometry-up-to-known-factor',X*X.T==4*S.eye(3))
centroid=lambda counts:X*counts/sum(counts)
qL,qR=centroid(left),centroid(right)
check('left-endpoint-centroid',qL==S.Matrix([0,0,1]))
check('right-endpoint-centroid',qR==S.Matrix([0,0,-1]))
check('equal-count-midpoint',centroid(left+right)==S.zeros(3,1))
check('nonzero-separation',(qL-qR).dot(qL-qR)==4)

# All 24 relabellings act orthogonally in the supplied tetrahedral geometry.
# Transport the reader and labels together; no fixed camera axis is chosen.
for perm in permutations(range(4)):
    P=S.Matrix(4,4,lambda i,j:int(i==perm[j]))
    O=X*P*X.T/4
    check('orthogonal-frame/'+str(perm),O.T*O==S.eye(3))
    check('endpoint-covariance/'+str(perm),O*X==X*P)
    check('centroid-covariance/'+str(perm),centroid(P*left)==O*qL)

# Classify all linear maps from endpoint counts to this standard spatial
# representation commuting with the entire label action (three generators).
unknowns=S.symbols('a0:12')
A=S.Matrix(3,4,unknowns)
equations=[]
for k in range(3):
    perm=list(range(4));perm[k],perm[k+1]=perm[k+1],perm[k]
    P=S.Matrix(4,4,lambda i,j:int(i==perm[j]))
    O=X*P*X.T/4
    equations+=list(A*P-O*A)
solution=next(iter(S.linsolve(equations,unknowns)))
family=S.Matrix(3,4,solution)
free=set().union(*(v.free_symbols for v in family))
check('one-free-spatial-scale',len(free)==1)
scale=family[0,0]
check('all-equivariant-linear-readers-are-scaled-X',family==scale*X)

# Genuine seed automorphism swaps the original triangle roles and is a
# PROPER spatial rotation here, not electric charge conjugation.
perm=(1,0,3,2)
P=S.Matrix(4,4,lambda i,j:int(i==perm[j]))
O=X*P*X.T/4
check('seed-role-exchange',P*left==right)
check('role-exchange-is-proper-rotation',O.det()==1 and O==S.diag(1,-1,-1))
check('direction-reversed-by-rotation',O*qL==qR)

# Composition changes occurrence multiplicities; its centroid changes are
# not automatically a mass-conserving mechanical trajectory.
L_targets=S.Matrix([sum(composition['registry'][label][1]==v
                         for label in composition['components']['L']) for v in 'ABCD'])
check('construction-is-not-fixed-particle-count',sum(L_targets)==3 and sum(left)==2)

result={
    'schema':'marici.nima.triangle-endpoint-spatial-reader.v1','status':'pass','checks':checks,
    'representation':'existing regular tetrahedron on A,B,C,D',
    'readout':'normalized endpoint-count first moment X*c/sum(c); requires nonzero total count',
    'cross_centroids':{'LR':[str(v) for v in qL],'RL':[str(v) for v in qR]},
    'uniqueness':'all equivariant LINEAR first-moment maps into the declared standard spatial representation are scalar multiples of X; nonlinear readers are not classified',
    'scale':'undetermined physical length unit; fixture coordinates only',
    'charge_warning':'LR/RL are related by a proper spatial rotation in this realization. Their signed vector component is not by itself a rotation-invariant electric charge.',
    'dynamics_warning':'3 primitive records become 2 cross words; no conserved particle mass, velocity, momentum or elapsed time follows from centroid changes',
    'rung_boundary':'this is an explicit finer reader of retained endpoint information, not the old aggregate J4 or a selected physical observer',
    'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
}
(ROOT/'results/triangle-endpoint-spatial-reader.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} exact spatial-reader checks; prior native/rung bridge rerun')
print('Cross-channel centroids are (0,0,+1) and (0,0,-1) in the existing tetrahedral chart.')
print('Equivariant linear spatial reader unique up to scale; role reversal is a proper rotation, not a derived charge flip.')
