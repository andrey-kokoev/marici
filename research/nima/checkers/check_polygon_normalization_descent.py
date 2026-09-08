#!/usr/bin/env python3
"""Exact gcd gate for descent from polygon normalizations to the point scalar."""
import json
from math import gcd
from pathlib import Path

cases = [
    {"sizes": [4], "exponents": [2], "gcd": 2, "unit_ambiguity": "s^2=1"},
    {"sizes": [5], "exponents": [3], "gcd": 3, "unit_ambiguity": "s^3=1"},
    {"sizes": [4, 5], "exponents": [2, 3], "gcd": 1, "unit_ambiguity": "s=1"},
    {"sizes": [5, 7], "exponents": [3, 5], "gcd": 1, "unit_ambiguity": "s=1"},
    {"sizes": [4, 6], "exponents": [2, 4], "gcd": 2, "unit_ambiguity": "s^2=1"},
]
for case in cases:
    exponents = [n-2 for n in case["sizes"]]
    assert exponents == case["exponents"]
    divisor = 0
    for exponent in exponents:
        divisor = gcd(divisor, exponent)
    assert divisor == case["gcd"]

# Adjacent sizes have coprime exponents and unit normalizations force s=1
# without extracting roots: s^(k+1)/s^k=s.
for n in range(4, 7):
    assert gcd(n-2, n-1) == 1

result = {
    "schema": "marici.polygon-normalization-descent.v1",
    "status": "passed",
    "strength": "generic exponent-gcd theorem with exact representative cases; source normalization premises remain external",
    "theorem": "unit normalizations at sizes S constrain the base scalar by s^g=1, where g=gcd{n-2:n in S}",
    "adjacent_size_corollary": "unit normalization at any adjacent sizes n,n+1 forces s=1 in every field because s^(n-1)/s^(n-2)=s",
    "single_size_boundary": "one even exponent leaves at least a sign ambiguity; one odd exponent can retain non-real roots unless the coefficient field and orientation line are restricted",
    "cases": cases,
    "boundary": "a presented unit coefficient is not a source normalization until the source-to-volume comparison is supplied",
}
out = Path("research/nima/results/polygon_normalization_descent.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
