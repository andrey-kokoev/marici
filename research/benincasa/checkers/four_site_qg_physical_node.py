"""Exact local type of the q_G quartic double solid at physical infinity."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-physical-node.json"


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def transpose(m): return [list(x) for x in zip(*m)]
def matmul(a,b): return [[sum(x*y for x,y in zip(row,col)) for col in transpose(b)] for row in a]


# Projective chart y4=1 and local coordinates ui=yi-1.  For
# Delta=(y2^2-y1^2,y3^2-y2^2,y4^2-y3^2), this is dDelta/du at u=0.
j = [[-2, 2, 0], [0, -2, 2], [0, 0, -2]]
assert det3(j) == -8

# Verify det(J^T H J)=det(J)^2 det(H) on a generic exact witness.
h = [[Fraction(2), Fraction(1), Fraction(0)],
     [Fraction(1), Fraction(3), Fraction(1)],
     [Fraction(0), Fraction(1), Fraction(5)]]
restricted = matmul(matmul(transpose(j), h), j)
assert det3(restricted) == det3(j)**2 * det3(h)
assert det3(h) != 0

# For a 3x3 Gram matrix G, det(adj G)=det(G)^2.  Since
# B2=-1/4 u^T J^T adj(G) J u, Hess(B2)=-1/2 J^T adj(G) J.
hessian_scalar = Fraction(-1, 2)**3 * det3(j)**2
assert hessian_scalar == -8

packet = {
    "schema": "marici.benincasa.four_site_qg_physical_node.v1",
    "projective_chart": "y4=1; ui=yi-1 for i=1,2,3",
    "difference_jacobian": j,
    "difference_jacobian_determinant": det3(j),
    "branch_quadratic_part": "B2=-1/4 u^T J^T adj(G) J u",
    "branch_hessian_determinant": "-8 det(G)^2",
    "genericity_condition": "det(G) != 0",
    "branch_singularity": "ordinary double point in the P3 branch surface",
    "double_cover_local_form": "W^2=u1^2+u2^2+u3^2 after etale/Morse coordinates",
    "hypersurface_complex_dimension": 3,
    "milnor_number": 1,
    "vanishing_cycle": "rank-one H3 (topological S3)",
    "local_monodromy_on_vanishing_line": "+1",
    "picard_lefschetz_warning": "the vanishing line is fixed, while the ambient H3 local system may carry a nontrivial transvection extension",
    "deeper_support": "det(G)=0",
    "new_carrier_datum": False,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
