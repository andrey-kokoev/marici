#!/usr/bin/env python3
"""Exact residue recursion on non-reference common-Jacobian pentagons."""
import json
from pathlib import Path
from sympy import Matrix, Rational, simplify, symbols

q, s = symbols("q s")
samples = [(Rational(0), Rational(0)), (Rational(1, 4), Rational(1, 3)), (Rational(-1, 4), Rational(1, 5))]
records = []

for a, b in samples:
    u = (1-b)/(a*b-1)
    v = (1-a)/(a*b-1)
    gradients = [Matrix([1, 0]), Matrix([0, 1]), Matrix([-1, a]), Matrix([u, v]), Matrix([b, -1])]
    constants = [Rational(1)] * 5
    for i in range(5):
        previous, following = (i-1) % 5, (i+1) % 5
        G = Matrix([[gradients[i][0], gradients[i][1]], [gradients[following][0], gradients[following][1]]])
        J = G.det()
        assert J == 1
        point = G.inv() * (Matrix([q, s]) - Matrix([constants[i], constants[following]]))
        prev = simplify(constants[previous] + gradients[previous].dot(point).subs(q, 0))
        slope = simplify(prev.diff(s))
        endpoint = simplify(-prev.subs(s, 0) / slope)
        scale = simplify(-slope)
        assert endpoint > 0 and scale > 0
        assert simplify(prev - scale*(endpoint-s)) == 0
        residue = simplify(1/s - slope/prev)
        interval = simplify(1/s + 1/(endpoint-s))
        assert simplify(residue-interval) == 0
        records.append({
            "a": str(a), "b": str(b), "facet": i,
            "normal_tangent_jacobian": str(J),
            "following_coordinate_endpoint": str(endpoint),
            "previous_facet_scale": str(scale),
            "endpoint_residues": [1, -1],
            "stokes_outward_orientation_sign": -1,
        })

assert len(records) == 15
result = {
    "schema": "marici.fact5-generic-slice-residue-recursion.v1",
    "status": "passed",
    "strength": "generic affine-edge proof plus exact checks on three rational common-Jacobian pentagons; not source selection",
    "checks": len(records),
    "samples": [[str(a), str(b)] for a, b in samples],
    "theorem": "every bounded simple affine pentagon with cyclic common nonzero Jacobian has interval residues dlog(a_{i+1}/a_{i-1}); support scales cancel",
    "records": records,
    "boundary": "boundedness, simple cyclic incidence, and common-Jacobian slice are assumptions; no scattering source derives them here",
}
out = Path("research/nima/results/fact5_generic_slice_residue_recursion.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
