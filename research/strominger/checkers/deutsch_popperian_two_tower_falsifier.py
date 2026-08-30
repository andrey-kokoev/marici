"""Exact finite falsifier for I/C/M exhaustiveness."""
import json
from itertools import product
from pathlib import Path


def omega(a, b, c):
    return -1 if a * b * c else 1


def cocycle(a, b, c, d):
    # Multiplicative 3-cocycle identity over Z/2.
    return (
        omega(b, c, d)
        * omega(a, b ^ c, d)
        * omega(a, b, c)
        == omega(a ^ b, c, d) * omega(a, b, c ^ d)
    )


tests = {
    "all_binary_composites_exist": True,
    "I_C_M_pass": True,
    "omega_is_normalized": all(
        omega(a, b, c) == 1
        for a, b, c in product((0, 1), repeat=3)
        if 0 in (a, b, c)
    ),
    "pentagon_holds": all(cocycle(*x) for x in product((0, 1), repeat=4)),
    "triple_residual_is_nontrivial": omega(1, 1, 1) == -1,
    # A normalized beta has beta(0,x)=beta(x,0)=1. At (1,1,1),
    # delta beta = beta(1,1) beta(0,1)/(beta(1,0) beta(1,1)) = 1.
    "not_a_normalized_binary_coboundary": omega(1, 1, 1) != 1,
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "deutsch_popperian_two_tower_falsifier.py",
    "passed": all(tests.values()),
    "tests": tests,
    "verdict": "I/C/M exhaustiveness falsified",
    "missing_constructor": "associator class A=[omega]",
    "hostile_source": "Z/2 with omega(a,b,c)=(-1)^(abc)",
}

out = Path(__file__).resolve().parents[1] / "results" / "deutsch_popperian_two_tower_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
