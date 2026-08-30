import json
import sympy as sp


z = sp.symbols("z")
I = sp.I
probes = [sp.Rational(0), sp.Rational(1), sp.Rational(2)]
jet_order = 2
w = sp.Rational(3, 5) + I * sp.Rational(4, 5)

# Include the completion endpoints and every signed real probe.  Since the
# polynomial is in z^2, one factor handles both signs.
nodes_squared = [sp.Rational(1, 4)] + [x**2 for x in probes]
V = sp.prod((z**2 - node) ** (jet_order + 1) for node in nodes_squared)
R = sp.simplify(-1 / V.subs(z, w))
w2 = sp.expand(w**2)
b = sp.simplify(sp.im(R) / sp.im(w2))
a = sp.simplify(sp.re(R) - b * sp.re(w2))
H = sp.expand(1 + V * (a + b * z**2))

checks = {
    "real_even": sp.expand(H.subs(z, -z) - H) == 0
    and all(c.is_real for c in sp.Poly(H, z).all_coeffs()),
    "endpoint_normalization_plus": sp.simplify(H.subs(z, sp.Rational(1, 2)) - 1) == 0,
    "endpoint_normalization_minus": sp.simplify(H.subs(z, -sp.Rational(1, 2)) - 1) == 0,
    "inserted_zero": sp.simplify(H.subs(z, w)) == 0,
    "quartet": all(
        sp.simplify(H.subs(z, root)) == 0
        for root in (w, -w, sp.conjugate(w), -sp.conjugate(w))
    ),
    "finite_jets_preserved": all(
        sp.simplify(sp.diff(H - 1, z, order).subs(z, sign * x)) == 0
        for x in probes
        for sign in (-1, 1)
        for order in range(jet_order + 1)
    ),
    "interpolation_nondegenerate": sp.im(w2) != 0,
}

result = {
    "schema": "marici.grothendieck.finite_jet_orbit_hostile_divisor.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "probes": [str(x) for x in probes],
    "jet_order": jet_order,
    "hostile_zero": str(w),
    "degree_H": int(sp.degree(H, z)),
    "coefficient_a": str(a),
    "coefficient_b": str(b),
    "general_gate": "Im(w^2)=2 alpha beta is nonzero for a genuine off-axis, off-seam quartet",
}

print(json.dumps(result, indent=2, sort_keys=True))
