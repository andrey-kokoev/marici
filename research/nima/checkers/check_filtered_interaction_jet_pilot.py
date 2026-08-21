"""Exact jet pilot for probing depth and composable coherence residues."""

import json
from pathlib import Path
import sympy as sp


d = 2
x = sp.symbols("x")


def trunc(poly, degree):
    poly = sp.Poly(sp.expand(poly), x)
    return sp.expand(sum(coeff*x**k for (k,), coeff in poly.terms()
                         if k <= degree))


# Truncation naturality for generic finite polynomials.
a = sp.symbols("a0:6")
b = sp.symbols("b0:6")
f = sum(a[i]*x**i for i in range(6))
g = sum(b[i]*x**i for i in range(6))
naturality = sp.expand(trunc(f*g, d) - trunc(trunc(f, d)*trunc(g, d), d))
assert naturality == 0


def star(u, v):
    """Multiplication in k[x]/(x^(d+1)), coefficient vectors 0..d."""
    return [sp.expand(sum(u[i]*v[k-i] for i in range(k+1))) for k in range(d+1)]


def B(u, v):
    """First omitted coefficient, degree d+1."""
    return sp.expand(sum(u[i]*v[d+1-i] for i in range(1, d+1)))


u = list(sp.symbols("u0:3"))
v = list(sp.symbols("v0:3"))
w = list(sp.symbols("w0:3"))

# Hochschild cocycle for the square-zero next-grade extension.  The degree-3
# line is acted on only by constant coefficients modulo x^4.
cocycle = sp.expand(
    u[0]*B(v, w)
    - B(star(u, v), w)
    + B(u, star(v, w))
    - B(u, v)*w[0]
)
assert cocycle == 0


def lifted_mul(U, V):
    base_u, r_u = U
    base_v, r_v = V
    return (star(base_u, base_v),
            sp.expand(base_u[0]*r_v + r_u*base_v[0] + B(base_u, base_v)))


ru, rv, rw = sp.symbols("ru rv rw")
left = lifted_mul(lifted_mul((u, ru), (v, rv)), (w, rw))
right = lifted_mul((u, ru), lifted_mul((v, rv), (w, rw)))
assert all(sp.expand(p-q) == 0 for p, q in zip(left[0], right[0]))
assert sp.expand(left[1]-right[1]) == 0

# Catch-up is not canonical: two depth-1 jets have identical truncation but
# distinct depth-2 extensions, and an interaction exposes the difference.
f_shallow_1 = 1
f_shallow_2 = 1 + x**2
assert trunc(f_shallow_1, 1) == trunc(f_shallow_2, 1)
catchup_difference = sp.expand(trunc(f_shallow_2*g, 2) - trunc(f_shallow_1*g, 2))
assert catchup_difference != 0

result = {
    "status": "PASS",
    "depth": d,
    "truncation_naturality_residual": str(naturality),
    "next_grade_residue": "B(u,v)=u1*v2+u2*v1",
    "hochschild_cocycle_residual": str(cocycle),
    "lifted_associator_base": [str(sp.expand(p-q)) for p, q in zip(left[0], right[0])],
    "lifted_associator_residue": str(sp.expand(left[1]-right[1])),
    "noncanonical_catchup_difference": str(catchup_difference),
    "conclusion": (
        "Finite probing depth is modeled by jet truncation. The first omitted "
        "grade is a composable Hochschild cocycle that restores the next-depth "
        "extension. A shallower jet cannot catch up canonically without an "
        "independent extension law."
    ),
}
out = Path(__file__).parents[1] / "results" / "filtered_interaction_jet_pilot.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
