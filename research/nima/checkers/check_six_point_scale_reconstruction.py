#!/usr/bin/env python3
"""Exact left-inverse reconstruction of six-point positive facet scales."""
import importlib.util
import json
from pathlib import Path
from sympy import Matrix

helper_path=Path(__file__).with_name("check_generic_polygon_face_product.py")
spec=importlib.util.spec_from_file_location("polygon_faces",helper_path)
poly=importlib.util.module_from_spec(spec)
spec.loader.exec_module(poly)

n=6
channels=tuple(sorted(poly.diagonals(n)))
triangulations=sorted((tuple(sorted(t)) for t in poly.dissections_on(channels) if len(t)==n-3),key=repr)
A=Matrix([[int(c in t) for c in channels] for t in triangulations])
assert A.shape==(14,9) and A.rank()==9
L=(A.T*A).inv()*A.T
assert L.shape==(9,14)
assert L*A==Matrix.eye(9)

# Each row reconstructs log(lambda_c) from log(w_T). Verify on independent
# prime valuations, which avoids numerical logarithms and fractional powers.
primes=[2,3,5,7,11,13,17,19,23]
weight_values=[]
for row in A.tolist():
    value=1
    for incidence,prime in zip(row,primes):
        if incidence:
            value*=prime
    weight_values.append(value)
for channel_index in range(9):
    valuation=A[:,channel_index]
    reconstructed=L*valuation
    expected=Matrix([int(i==channel_index) for i in range(9)])
    assert reconstructed==expected

result={
    "schema":"marici.six-point-scale-reconstruction.v1",
    "status":"passed",
    "strength":"exact rational left inverse for the declared six-point incidence ordering; positive factorable weights give unique positive scales",
    "channels":[list(c) for c in channels],
    "left_inverse_rows":[[str(value) for value in L.row(i)] for i in range(9)],
    "identity_check":"L*A=I_9",
    "factorable_prime_scales":primes,
    "generated_triangulation_weights":weight_values,
    "reconstruction":"lambda_c=product_T w_T^(L_cT), using the unique positive real roots",
    "boundary":"nonpositive or complex weights require separate sign and branch data; reconstructed scales do not supply source provenance",
}
out=Path("research/nima/results/six_point_scale_reconstruction.json")
out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n",encoding="utf-8")
print(json.dumps(result,sort_keys=True))
