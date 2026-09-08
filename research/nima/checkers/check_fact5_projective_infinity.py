#!/usr/bin/env python3
"""Symbolic projective-infinity audit for cyclic affine dlog forms."""
import json
from pathlib import Path
from sympy import factor, fraction, simplify, symbols

w = symbols("w")
p = symbols("p0:5")
q = symbols("q0:5")
linear = [p[i] + q[i]*w for i in range(5)]
jacobian = [p[i]*q[(i+1)%5] - q[i]*p[(i+1)%5] for i in range(5)]
infinity_residue = simplify(sum(jacobian[i]/(linear[i]*linear[(i+1)%5]) for i in range(5)))
assert infinity_residue == 0

# Each summand is a telescoping logarithmic derivative.
telescoping_terms = [simplify(q[(i+1)%5]/linear[(i+1)%5] - q[i]/linear[i]) for i in range(5)]
assert all(simplify(jacobian[i]/(linear[i]*linear[(i+1)%5]) - telescoping_terms[i]) == 0 for i in range(5))
assert simplify(sum(telescoping_terms)) == 0

# Deliberate failure: an open chain lacks the closing cancellation.
open_chain = simplify(sum(jacobian[i]/(linear[i]*linear[(i+1)%5]) for i in range(4)))
open_num, open_den = fraction(open_chain)
assert factor(open_num) != 0

# Exact common-Jacobian family members also have zero residue, although the
# generic identity does not require equal Jacobians.
samples = [(0, 0), (symbols("r")/4, symbols("r")/3)]
result = {
    "schema": "marici.fact5-projective-infinity.v1",
    "status": "passed",
    "strength": "symbolic identity for every cyclic five-tuple of affine facet gradients; no positivity or common-Jacobian hypothesis required",
    "projective_chart": "x=1/z, y=w/z, so dx wedge dy=-z^-3 dz wedge dw",
    "candidate_infinity_residue": "sum det(v_i,v_{i+1})/(l_i(w) l_{i+1}(w))",
    "infinity_residue": "0",
    "mechanism": "term i equals d/dw log(l_{i+1}/l_i), hence the cyclic sum telescopes",
    "deliberate_failure": {
        "operation": "remove the closing fifth cyclic term",
        "residual_numerator": str(factor(open_num)),
        "residual_nonzero": True,
    },
    "boundary": "absence of a pole along the infinity divisor is generic cyclic algebra and does not select a positive geometry, affine fan, support constants, or physical source",
}
out = Path("research/nima/results/fact5_projective_infinity.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
