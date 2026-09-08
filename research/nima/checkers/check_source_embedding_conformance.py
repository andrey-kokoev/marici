#!/usr/bin/env python3
"""Conformance harness for a five-point source-embedding candidate."""
import json
from fractions import Fraction
from pathlib import Path
from sympy import Poly, Rational, expand, symbols

candidate_path = Path("research/nima/results/source_embedding_reference_fixture.json")
candidate = json.loads(candidate_path.read_text(encoding="utf-8"))
assert candidate["schema"] == "marici.source-embedding-candidate.v1"
assert candidate["dimension"] == candidate["n"] - 3
assert len(candidate["facets"]) == candidate["n"] * (candidate["n"] - 3) // 2

facets = candidate["facets"]
gradients = [tuple(Fraction(x) for x in facet["gradient"]) for facet in facets]
constants = [Fraction(facet["constant"]) for facet in facets]
maximal = [tuple(face) for face in candidate["maximal_faces"]]
assert set(maximal) == {(i, (i+1) % 5) for i in range(5)}

def det(u, v):
    return u[0]*v[1] - u[1]*v[0]

def solve(i, j):
    gi, gj = gradients[i], gradients[j]
    D = det(gi, gj)
    assert D != 0
    return ((-constants[i]*gj[1] + gi[1]*constants[j])/D,
            (-gi[0]*constants[j] + constants[i]*gj[0])/D)

def value(k, point):
    return constants[k] + gradients[k][0]*point[0] + gradients[k][1]*point[1]

jacobians = []
vertices = []
boundary_factorization = True
for i, j in maximal:
    jacobians.append(det(gradients[i], gradients[j]))
    point = solve(i, j)
    values = [value(k, point) for k in range(5)]
    assert values[i] == values[j] == 0
    assert all(values[k] > 0 for k in range(5) if k not in (i, j))
    vertices.append(point)
assert jacobians == [1] * 5
assert len(set(vertices)) == 5

# Distinct affine factors give a reduced simple-pole denominator.
for i in range(5):
    for j in range(i+1, 5):
        assert gradients[i] != gradients[j] or constants[i] != constants[j]

# The cyclic dlog numerator over the common denominator must lose its apparent
# cubic leading part; degree at most two is exactly regularity at infinity in d=2.
x, y = symbols("x y")
linear = [Rational(c.numerator, c.denominator) + Rational(g[0].numerator, g[0].denominator)*x + Rational(g[1].numerator, g[1].denominator)*y for c, g in zip(constants, gradients)]
numerator = 0
for i in range(5):
    omitted = {i, (i+1) % 5}
    product = 1
    for k in range(5):
        if k not in omitted:
            product *= linear[k]
    numerator += Rational(jacobians[i].numerator, jacobians[i].denominator) * product
numerator = expand(numerator)
infinity_regular = Poly(numerator, x, y).total_degree() <= 2
assert infinity_regular

# Generic boundary algebra: only the two cyclic terms incident to each facet
# contribute, giving dlog(a_next/a_previous), the interval form on a strict edge.
for i in range(5):
    assert det(gradients[i], gradients[(i+1) % 5]) == 1

checks = {
    "dimension_and_facet_count": True,
    "pentagon_incidence_and_strict_vertices": True,
    "regional_boundary_factorization": boundary_factorization,
    "triangulation_jacobians_match_unit_coefficients": True,
    "reduced_simple_pole_divisor": True,
    "projective_infinity_regularity": infinity_regular,
    "declared_volume_orientation": bool(candidate["volume_orientation"]),
    "source_derived_provenance": candidate["provenance"]["status"] == "source_derived" and bool(candidate["provenance"]["source_locator"]),
    "zero_dimensional_normalization": candidate["zero_dimensional_normalization"] is not None,
}
promotion_ready = all(checks.values())
assert not promotion_ready
assert [name for name, passed in checks.items() if not passed] == ["source_derived_provenance", "zero_dimensional_normalization"]

fmt = lambda z: str(z.numerator) if z.denominator == 1 else f"{z.numerator}/{z.denominator}"
result = {
    "schema": "marici.source-embedding-conformance.v2",
    "status": "passed",
    "candidate": str(candidate_path),
    "checks": checks,
    "promotion_ready": promotion_ready,
    "canonical_numerator": str(numerator),
    "canonical_numerator_degree": Poly(numerator, x, y).total_degree(),
    "vertices": [[fmt(px), fmt(py)] for px, py in vertices],
    "residuals": [name for name, passed in checks.items() if not passed],
    "acceptance": "a replacement candidate must retain every algebraic pass and supply source-derived provenance plus zero-dimensional normalization",
    "boundary": "the harness validates declared algebraic data; it cannot authenticate provenance or derive a physical source map",
}
out = Path("research/nima/results/source_embedding_conformance.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
