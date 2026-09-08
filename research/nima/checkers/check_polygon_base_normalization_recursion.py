#!/usr/bin/env python3
"""Exact exponent recursion for polygon canonical-form normalizations."""
import json
from pathlib import Path

stages = []
for n in range(3, 8):
    exponent = n - 2
    splits = []
    for p in range(3, n + 1):
        q = n + 2 - p
        if q < 3:
            continue
        left, right = p - 2, q - 2
        assert left + right == exponent
        splits.append({"p": p, "q": q, "left_exponent": left, "right_exponent": right})
    stages.append({"n": n, "normalization": f"s^{exponent}", "factorization_splits": splits})

# Triangle cuts force c_n=s*c_(n-1), so c_3=s uniquely determines every c_n.
for n in range(4, 8):
    assert (n - 2) == 1 + ((n - 1) - 2)

result = {
    "schema": "marici.polygon-base-normalization-recursion.v1",
    "status": "passed",
    "strength": "generic integer-exponent theorem; finite n=3..7 census checks split bookkeeping only",
    "theorem": "if c_3=s and every chord residue factorizes multiplicatively, then c_n=s^(n-2)",
    "proof": "a triangle cut gives c_n=c_3*c_(n-1); induction fixes c_n, and p+q=n+2 verifies every other split",
    "stages": stages,
    "orientation_consequence": "changing the oriented point normalization s to -s multiplies the n-point form by (-1)^(n-2)",
    "boundary": "recursion propagates but does not choose s; source orientation and normalization remain required",
}
out = Path("research/nima/results/polygon_base_normalization_recursion.json")
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(result, sort_keys=True))
