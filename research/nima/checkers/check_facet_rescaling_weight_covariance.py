#!/usr/bin/env python3
"""Exact distinction between dlog gauge and unit-weight scalar normalization."""
import json
from pathlib import Path
from sympy import Matrix, Rational, simplify, symbols

x, y = symbols("x y")
facets = [x, y, 1-x, Rational(3,2)-x-y, 1-y]
scales = [2,3,5,7,11]
rescaled = [scales[i]*facets[i] for i in range(5)]

def det(u,v):
    return Matrix.hstack(u,v).det()
def gradients(forms):
    return [Matrix([f.diff(x),f.diff(y)]) for f in forms]
def scalar(forms, weights):
    return simplify(sum(weights[i]/(forms[i]*forms[(i+1)%5]) for i in range(5)))

old_gradients = gradients(facets)
new_gradients = gradients(rescaled)
old_jacobians = [det(old_gradients[i],old_gradients[(i+1)%5]) for i in range(5)]
new_jacobians = [det(new_gradients[i],new_gradients[(i+1)%5]) for i in range(5)]
assert old_jacobians == [1]*5
assert new_jacobians == [scales[i]*scales[(i+1)%5] for i in range(5)]

old_weighted = scalar(facets, old_jacobians)
new_weighted = scalar(rescaled, new_jacobians)
assert simplify(new_weighted-old_weighted) == 0
old_unit = scalar(facets, [1]*5)
new_unit = scalar(rescaled, [1]*5)
unit_residual = simplify(new_unit-old_unit)
assert unit_residual != 0

result = {
    "schema":"marici.facet-rescaling-weight-covariance.v1",
    "status":"passed",
    "strength":"exact five-point counterexample plus generic dlog scaling law",
    "facet_scales":scales,
    "rescaled_jacobian_weights":list(map(str,new_jacobians)),
    "weighted_form_invariant":True,
    "unit_weight_scalar_invariant":False,
    "unit_weight_residual":str(unit_residual),
    "correction":"positive facet rescaling is gauge for the logarithmic form only when triangulation weights transform by products of incident facet scales",
    "boundary":"a fixed unit-weight amplitude convention makes facet normalization source data rather than disposable gauge",
}
out=Path("research/nima/results/facet_rescaling_weight_covariance.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
