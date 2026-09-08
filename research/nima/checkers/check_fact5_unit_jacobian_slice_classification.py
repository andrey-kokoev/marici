#!/usr/bin/env python3
"""Symbolic classification of common-Jacobian cyclic five-facet gradients."""
import json
from pathlib import Path
from sympy import Matrix, simplify, symbols

a, b = symbols("a b")
u = (1 - b) / (a * b - 1)
v = (1 - a) / (a * b - 1)
gradients = [Matrix([1, 0]), Matrix([0, 1]), Matrix([-1, a]), Matrix([u, v]), Matrix([b, -1])]
determinants = [simplify(Matrix.hstack(gradients[i], gradients[(i + 1) % 5]).det()) for i in range(5)]
assert determinants == [1, 1, 1, 1, 1]

# The reference slice is the a=b=0 member.
reference = [tuple(vector.subs({a: 0, b: 0})) for vector in gradients]
assert reference == [(1, 0), (0, 1), (-1, 0), (-1, -1), (0, -1)]

# Finite exact samples establish that common Jacobian does not select one fan.
samples = []
for av, bv in [(-2, -1), (-1, 0), (0, 0), (0, 2), (2, 0), (2, 2)]:
    if av * bv == 1:
        continue
    specialized = [tuple(simplify(x.subs({a: av, b: bv})) for x in vector) for vector in gradients]
    specialized_dets = [Matrix.hstack(Matrix(specialized[i]), Matrix(specialized[(i + 1) % 5])).det() for i in range(5)]
    assert specialized_dets == [1] * 5
    samples.append({"a": av, "b": bv, "gradients": [list(map(str, vector)) for vector in specialized]})
assert len({repr(sample["gradients"]) for sample in samples}) == len(samples)

# Exceptional locus: ab=1 is inconsistent unless a=b=1; at a=b=1 the two
# equations for the fourth gradient coincide and leave u+v=-1.
result = {
    "schema": "marici.fact5-unit-jacobian-slice-classification.v1",
    "status": "passed",
    "strength": "symbolic affine-gradient classification up to a chosen GL2 frame; boundedness and source selection are separate",
    "normalization": "use GL2 to set v0=(1,0), v1=(0,1) and common Jacobian J=1",
    "generic_family": {
        "parameters": ["a", "b"],
        "condition": "a*b != 1",
        "gradients": ["(1,0)", "(0,1)", "(-1,a)", "((1-b)/(ab-1),(1-a)/(ab-1))", "(b,-1)"],
        "cyclic_determinants": list(map(str, determinants)),
    },
    "exceptional_locus": "a*b=1 is inconsistent except a=b=1, where u+v=-1 and the fan is degenerate",
    "distinct_exact_samples": samples,
    "reference_member": "a=b=0",
    "boundary": "equal Jacobians fix form coefficients only; support constants, bounded positive region, ABHY/source authority, and physical normalization remain unsupplied",
}
out = Path("research/nima/results/fact5_unit_jacobian_slice_classification.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
