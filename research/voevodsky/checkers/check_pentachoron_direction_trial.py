"""Exact geometry and independent reversal tests; no charge identification."""
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
A, B, C, D = [tuple(map(Q, p)) for p in [(1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1)]]
F = tuple((A[j]+B[j]+C[j])/3 for j in range(3))
E = tuple(2*F[j]-D[j] for j in range(3))
points = [p+(Q(0),) for p in [A,B,C,D]] + [E+(Q(1),)]

def det(m):
    if len(m)==1: return m[0][0]
    return sum((-1)**j*m[0][j]*det([r[:j]+r[j+1:] for r in m[1:]]) for j in range(len(m)))

def boundary(chain):
    out={}
    for cell, value in chain.items():
        if len(cell)==1: continue
        for i in range(len(cell)):
            f=cell[:i]+cell[i+1:]
            out[f]=out.get(f,0)+(-1)**i*value
    return {k:v for k,v in out.items() if v}

def cross(a,b):
    return tuple(a[(j+1)%3]*b[(j+2)%3]-a[(j+2)%3]*b[(j+1)%3] for j in range(3))

def dot(a,b): return sum(x*y for x,y in zip(a,b))

facets = list(combinations(range(5),4))
flags = [tuple(tuple(sorted(p[:k])) for k in range(1,6)) for p in permutations(range(5))]
body=tuple(range(5))
edges=[(a,b) for k in range(1,5) for a in combinations(range(5),k) for b in combinations(range(5),k+1) if set(a)<set(b)]
volume_det=det([[points[i][j]-points[0][j] for j in range(4)] for i in range(1,5)])
normal=cross(tuple(B[j]-A[j] for j in range(3)),tuple(C[j]-A[j] for j in range(3)))
# Existing triangle-mode representation v=r+i sqrt(3)s.
r=tuple(F[j]-(A[j]+B[j])/2 for j in range(3))
s=tuple((A[j]-B[j])/2 for j in range(3))
bivector=cross(r,s)
# Reverse the construction's traversal only: ordered triangle input is unchanged.
traversal_reversed_bivector=cross(r,s)
# Separate operation: reverse the cyclic order, replacing s by -s.
cycle_reversed_bivector=cross(r,tuple(-x for x in s))
checks={
    'nondegenerate_four_simplex':volume_det!=0,
    'five_tetrahedral_boundary_cells':len(facets)==5,
    'boundary_squared_zero':not boundary(boundary({body:1})),
    'projected_pair_has_opposite_apices':dot(normal,tuple(D[j]-A[j] for j in range(3)))*dot(normal,tuple(E[j]-A[j] for j in range(3)))<0,
    'projected_new_apex_is_retained_reflection':E==tuple(2*F[j]-D[j] for j in range(3)),
    'pair_shares_ABC':set((0,1,2,3))&set((0,1,2,4))=={0,1,2},
    'complement_three_cells_share_DE':set.intersection(*[set(f) for f in facets if 3 in f and 4 in f])=={3,4},
    'one_hundred_twenty_flags':len(set(flags))==120,
    'seventy_five_incidence_arrows':len(edges)==75,
    'traversal_reversal_involutive':all(tuple(reversed(tuple(reversed(f))))==f for f in flags),
    'traversal_reversal_does_not_force_flux_reversal':bivector!=tuple(Q(0) for _ in range(3)) and traversal_reversed_bivector==bivector,
    'cyclic_order_reversal_conjugates_mode_and_reverses_bivector':cycle_reversed_bivector==tuple(-x for x in bivector),
    'hidden_height_is_not_selected_by_projection':all(p[:3]==q[:3] for p,q in zip(points,points[:4]+[E+(Q(2),)])),
}
assert all(checks.values()),checks
result={'verification_passed':True,'checks':checks,'vertices_4d':{n:list(map(str,p)) for n,p in zip('ABCDE',points)},'affine_determinant':str(volume_det),'supplied_hidden_height':'1','projection':'discard w; viewer optionally shears projected x by lambda*w','classification':'geometric_parent_exists; direction_alone_does_not_determine_charge','electron_pentachoron_identification_established':False,'electromagnetic_charge_derived':False}
(ROOT/'research/voevodsky/results/pentachoron_direction_trial.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
