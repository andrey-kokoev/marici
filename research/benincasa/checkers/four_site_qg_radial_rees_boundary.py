"""Type the physical d=3 radial boundary inside the q_G node smoothing."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-radial-rees-boundary.json"


def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])
            -m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])
            +m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))


def adj3(m):
    a,b,c=m[0]; d,e,f=m[1]; g,h,i=m[2]
    return [[e*i-f*h,c*h-b*i,b*f-c*e],
            [f*g-d*i,a*i-c*g,c*d-a*f],
            [d*h-e*g,b*g-a*h,a*e-b*d]]


def mv(m,v): return [sum(x*y for x,y in zip(row,v)) for row in m]
def dot(x,y): return sum(a*b for a,b in zip(x,y))


# Exact positive-definite witness for the Schur-complement identity.
g = [[Fraction(2),Fraction(1),Fraction(0)],
     [Fraction(1),Fraction(3),Fraction(1)],
     [Fraction(0),Fraction(1),Fraction(5)]]
h = adj3(g); determinant = det3(g)
n = [Fraction(1),Fraction(2),Fraction(-1)]
v = mv(g,n)                  # v_i = ell.p_i in the chosen Gram basis.
ell_squared = dot(n,v)
assert dot(v,mv(h,v)) == determinant * ell_squared

# Equivalently v^T adj(G) v = det(G) ell_parallel^2.  In physical d=3,
# ell=ell_parallel and the full block Gram/Cayley-Menger determinant is zero.
assert determinant * ell_squared - dot(v,mv(h,v)) == 0

packet = {
    "schema": "marici.benincasa.four_site_qg_radial_rees_boundary.v1",
    "full_gram_form": "K=det(G) ell^2-v^T adj(G) v",
    "radial_rees_equation": "omega^2=det(G)-vhat^T adj(G) vhat",
    "physical_dimension": 3,
    "external_span_rank": 3,
    "physical_schur_complement": "ell_perp^2=0",
    "physical_exceptional_condition": "omega=0",
    "real_vanishing_cycle": "S3 in the rank-one A1 smoothing",
    "literal_physical_boundary": "equatorial S2 at omega=0",
    "integral_activation": "not determined: the equator does not choose either hemisphere or an oriented S3 generator",
    "required_extra_datum": "a transverse/dimensional continuation or source gluing of the two omega sheets",
    "new_carrier_datum": False,
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps(packet))
