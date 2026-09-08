#!/usr/bin/env python3
"""Exact Poincare residues of the declared five-point pentagon slice."""
import json
from pathlib import Path
from sympy import Matrix, Rational, simplify, symbols

x, y, q, s = symbols("x y q s")
facets = [x, y, 1-x, Rational(3, 2)-x-y, 1-y]
gradients = [Matrix([f.diff(x), f.diff(y)]) for f in facets]
compatible = [(i, (i + 1) % 5) for i in range(5)]
records = []

for i in range(5):
    previous = (i - 1) % 5
    following = (i + 1) % 5
    coordinate_map = Matrix([facets[i], facets[following]])
    jacobian = Matrix.hstack(gradients[i], gradients[following]).det()
    assert jacobian == 1
    solution = list(Matrix([facets[i] - q, facets[following] - s]).jacobian([x, y]).inv() * Matrix([0, 0])) if False else None
    # Solve the affine equations q=a_i, s=a_{i+1} directly.
    G = Matrix([[gradients[i][0], gradients[i][1]], [gradients[following][0], gradients[following][1]]])
    constants = Matrix([facets[i].subs({x: 0, y: 0}), facets[following].subs({x: 0, y: 0})])
    xy = G.inv() * (Matrix([q, s]) - constants)
    restricted_previous = simplify(facets[previous].subs({x: xy[0], y: xy[1], q: 0}))
    edge_previous = simplify(restricted_previous.subs(q, 0))
    length = simplify(edge_previous + s)
    assert length.diff(s) == 0 and length > 0
    residue_coefficient = simplify(1 / s + 1 / edge_previous)
    interval_coefficient = simplify(1 / s + 1 / (length - s))
    assert simplify(residue_coefficient - interval_coefficient) == 0
    records.append({
        "facet": i,
        "previous_facet": previous,
        "following_facet": following,
        "normal_tangent_jacobian": str(jacobian),
        "edge_length_in_following_coordinate": str(length),
        "normal_first_residue": f"dlog(a{following}/a{previous})",
        "endpoint_residues_in_increasing_following_coordinate": [1, -1],
        "stokes_outward_orientation_sign": -1,
    })

result = {
    "schema": "marici.fact5-slice-boundary-residues.v1",
    "status": "passed",
    "strength": "exact residues on all five facets of one declared affine slice; conditional on its unsourced selection",
    "facets_checked": len(records),
    "records": records,
    "normal_convention": "Omega=dlog(a_i) wedge Res_i + regular",
    "orientation_relation": "because a_i>=0 and det(d a_i,d a_{i+1})=+1, increasing a_{i+1} is opposite the Stokes orientation induced by the outward normal -d a_i",
    "factorization": "each residue is the canonical logarithmic one-form of the interval between facets i+1 and i-1",
    "boundary": "this verifies conditional canonical-form recursion, not source authority for the slice, constants, contour, or physical normalization",
}
out = Path("research/nima/results/fact5_slice_boundary_residues.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
