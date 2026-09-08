#!/usr/bin/env python3
"""Exact affine-coordinate and facet-rescaling invariance of the pentagon form."""
import json
from pathlib import Path
from sympy import Matrix, Rational, simplify, symbols

x, y, X, Y = symbols("x y X Y")
old_coordinates = Matrix([x, y])
new_coordinates = Matrix([X, Y])
M = Matrix([[2, 1], [1, 2]])
t = Matrix([Rational(1, 3), Rational(-2, 5)])
assert M.det() == 3
inverse_map = M.inv() * (new_coordinates - t)
old_facets = [x, y, 1-x, Rational(3, 2)-x-y, 1-y]
lambdas = [2, 3, 5, 7, 11]
transformed = [simplify(scale * facet.subs({x: inverse_map[0], y: inverse_map[1]})) for scale, facet in zip(lambdas, old_facets)]

def cyclic_form_coefficient(facets, coordinates):
    gradients = [Matrix([facet.diff(coordinates[0]), facet.diff(coordinates[1])]) for facet in facets]
    total = 0
    jacobians = []
    for i in range(5):
        j = (i+1) % 5
        determinant = Matrix.hstack(gradients[i], gradients[j]).det()
        jacobians.append(simplify(determinant))
        total += determinant/(facets[i]*facets[j])
    return simplify(total), jacobians

old_coefficient, old_jacobians = cyclic_form_coefficient(old_facets, old_coordinates)
new_coefficient, new_jacobians = cyclic_form_coefficient(transformed, new_coordinates)
expected = simplify(old_coefficient.subs({x: inverse_map[0], y: inverse_map[1]}) / M.det())
assert simplify(new_coefficient - expected) == 0
for i in range(5):
    expected_jacobian = Rational(lambdas[i] * lambdas[(i+1) % 5], M.det()) * old_jacobians[i]
    assert simplify(new_jacobians[i] - expected_jacobian) == 0

# Positive facet rescaling and invertible affine transport preserve the region
# and its labelled incidence; the ambient volume changes by det(M).
result = {
    "schema": "marici.source-embedding-gauge-invariance.v1",
    "status": "passed",
    "strength": "symbolic exact test of one nontrivial GL(2) affine change and five independent positive facet rescalings, backed by the generic dlog invariance argument",
    "coordinate_matrix": [[str(value) for value in M.row(i)] for i in range(2)],
    "coordinate_determinant": str(M.det()),
    "translation": list(map(str, t)),
    "facet_rescalings": lambdas,
    "transformed_cyclic_jacobians": list(map(str, new_jacobians)),
    "form_transport": "f_new(X,Y)=f_old(M^-1((X,Y)-t))/det(M)",
    "accepted_equivalence": "invertible affine coordinate transport plus positive labelled facet rescaling, with volume and orientation determinant recorded",
    "boundary": "gauge equivalence compares supplied embeddings; it neither supplies source provenance nor permits unlabelled or orientation-erasing identification",
}
out = Path("research/nima/results/source_embedding_gauge_invariance.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
