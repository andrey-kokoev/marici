import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
q = [Fraction(x,23) for x in (6,8,1,4,2,2)]
u = [Fraction(1,6)] * 6
matchings = [
    ((0,2),(1,4),(3,5)), ((0,2),(1,5),(3,4)),
    ((0,4),(1,2),(3,5)), ((0,4),(1,5),(2,3)),
    ((0,5),(1,2),(3,4)), ((0,5),(1,4),(2,3)),
]

def matvec(A,x):
    return [sum(A[i][j]*x[j] for j in range(6)) for i in range(6)]

def matching_matrix(pairs):
    A=[[Fraction(0)]*6 for _ in range(6)]
    for i,j in pairs:
        a=(u[0]-q[j])/(q[i]-q[j])
        A[i][i]=a; A[i][j]=1-a
        A[j][j]=1-a; A[j][i]=a
    return A

matching_maps=[matching_matrix(pairs) for pairs in matchings]
for A in matching_maps:
    assert all(sum(row)==1 for row in A)
    assert matvec(A,q)==u
    assert [sum(A[i][j] for i in range(6)) for j in range(6)] != [Fraction(1)]*6

# Any modulus P=|S|^2 of a unitary S is doubly stochastic. Hence the six
# matching maps cannot arise as S-matrix moduli.
doubly_stochastic_matches=0
intersection_count=sum(
    all(sum(A[i][j] for i in range(6)) == 1 for j in range(6))
    for A in matching_maps
)
assert intersection_count == doubly_stochastic_matches == 0

# Fixed-q doubly stochastic maps form a nonempty 20-dimensional affine family
# before positivity: 11 independent row/column constraints and five further
# independent target constraints. J6/6 is a positive interior member.
J=[[Fraction(1,6)]*6 for _ in range(6)]
assert all(sum(row)==1 for row in J)
assert all(sum(J[i][j] for i in range(6))==1 for j in range(6))
assert matvec(J,q)==u
fixed_q_doubly_stochastic_affine_dimension=36-11-5
assert fixed_q_doubly_stochastic_affine_dimension==20

result={
    "schema":"marici.flavor.wp1151.v1",
    "status":"PASS",
    "question":"Do fixed-q unitary S-matrix transition maps intersect the rank-three matching polytope?",
    "dpc":{
        "conjecture":"A fixed-q nonuniversal S-matrix can realize one of the rank-three matching maps.",
        "rivals":["row-stochastic matching","doubly stochastic S-matrix modulus","fixed-q intersection","disjoint algebraic classes"],
        "risky_consequences":["Pq=u","row sums one","column sums one from unitarity","six matching maps included if intersection exists"],
        "falsification_attempt":"Every matching map fails double stochasticity; the fixed-q doubly stochastic family is nonempty and 20-dimensional, so the classes are disjoint.",
        "residual":"A nonunitary production kernel could realize a matching, or a doubly stochastic support gate may select another map.",
        "disposition":"reject fixed-q S-matrix realization of rank-three matchings"
    },
    "matching_maps":6,
    "matching_maps_row_stochastic":True,
    "matching_maps_hit_target":True,
    "matching_maps_doubly_stochastic":doubly_stochastic_matches,
    "smatrix_matching_intersection":intersection_count,
    "fixed_q_doubly_stochastic_affine_dimension":fixed_q_doubly_stochastic_affine_dimension,
    "uniform_member":"J6/6",
    "classification":"classification no-go: fixed-q S-matrix moduli and rank-three matching maps are disjoint",
    "remaining_gate":"classify support constraints inside the fixed-q doubly stochastic polytope",
    "hostile_gate":"do not omit column normalization when calling a map an S-matrix modulus",
    "claim_boundary":"the disjointness theorem is algebraic; physical production authority remains absent",
    "disposition":"fixed-q S-matrix leaf resolved; doubly stochastic support rival selected"
}

(ROOT/"results"/"wp1151_fixed_q_smatrix_disjointness.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1151 PASS:",intersection_count,fixed_q_doubly_stochastic_affine_dimension)
