"""Degree and canonical-class audit of the four-site one-loop infinity boundary."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-infinity-boundary-not-k3.json"

def add(p, q):
    out = dict(p)
    for monomial, coefficient in q.items():
        out[monomial] = out.get(monomial, Fraction(0)) + coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def scale(p, scalar):
    return {m: scalar * a for m, a in p.items() if scalar * a}


def mul(p, q):
    out = {}
    for m, a in p.items():
        for n, b in q.items():
            exponent = tuple(x + y for x, y in zip(m, n))
            out[exponent] = out.get(exponent, Fraction(0)) + a * b
    return {m: a for m, a in out.items() if a}


def power(p, exponent):
    out = {(0,) * len(next(iter(p))): Fraction(1)}
    for _ in range(exponent):
        out = mul(out, p)
    return out


def variable(index, nvars):
    exponent = [0] * nvars
    exponent[index] = 1
    return {tuple(exponent): Fraction(1)}


def constant(value, nvars):
    return {(0,) * nvars: Fraction(value)}


def degree(p):
    return max(sum(m) for m in p)


def compose(p, images):
    out = {}
    nvars = len(next(iter(images[0])))
    for monomial, coefficient in p.items():
        term = constant(coefficient, nvars)
        for exponent, image in zip(monomial, images):
            term = mul(term, power(image, exponent))
        out = add(out, term)
    return out


y = [variable(i, 4) for i in range(4)]
z1, z2, z3, z4 = [power(item, 2) for item in y]
one4 = constant(1, 4)

# A generic-degree witness may use an orthonormal external Gram frame.
# The block Gram determinant is det(G_ext)*(l^2-v^T G_ext^-1 v).
v = [
    scale(add(add(z2, scale(z1, -1)), scale(one4, -1)), Fraction(1, 2)),
    scale(add(add(z3, scale(z2, -1)), scale(one4, -1)), Fraction(1, 2)),
    scale(add(add(z4, scale(z3, -1)), scale(one4, -1)), Fraction(1, 2)),
]
baikov = z1
for component in v:
    baikov = add(baikov, scale(mul(component, component), -1))
assert degree(baikov) == 4

# A marked cosmological denominator is linear in edge variables.  Eliminating
# y4 by q=0 cannot increase the degree and the generic quartic survives.
y1n, y2n, y3n, cn = [variable(i, 4) for i in range(4)]
y4_image = scale(add(add(add(cn, y1n), y2n), y3n), -1)
residue_polynomial = compose(baikov, [y1n, y2n, y3n, y4_image])
residue_degree = degree(residue_polynomial)
assert residue_degree == 4

# Double cover pi:X->P2 branched in 2d=4 has
# K_X=pi*(K_P2+dH)=pi*((-3+2)H)=-pi*H and (-K_X)^2=2.
base_dimension = 2
branch_degree = 4
half_branch_degree = branch_degree // 2
canonical_coefficient = -(base_dimension + 1) + half_branch_degree
anticanonical_square = 2
assert canonical_coefficient == -1

packet = {
    "schema": "marici.benincasa.four_site_infinity_boundary_not_k3.v1",
    "source_structure": "one-loop Baikov/Cayley-Menger Gram determinant is quadratic in squared edge variables",
    "degree_in_edge_variables": 4,
    "degree_after_linear_marked_cut_residue": residue_degree,
    "infinity_base": "P^2",
    "branch_degree": branch_degree,
    "canonical_class": "K_X=-pi^*H",
    "anticanonical_square": anticanonical_square,
    "generic_surface_type": "degree-two del Pezzo",
    "is_k3": False,
    "scope": "pure Cayley-Menger infinity boundary only; marked relative divisors and the full period system are not classified",
    "new_carrier_datum": False,
}

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps(packet))
