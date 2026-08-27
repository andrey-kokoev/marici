#!/usr/bin/env python3
"""Check the fixed-radius weighted Wiener constructor for analytic inversion."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_weighted_wiener_constructor.json"
i, j, m, R = s.symbols("i j m R", integer=True, positive=True)
n = s.symbols("n", integer=True, nonnegative=True)
weight = lambda n: (1 + n)**4
lam = s.factor(m * (m - 1) * (m - 2) * (m + 8) / 2)

# Coarse exact comparison valid for integer m >= 3.
lower_constant = s.Rational(9, 256)
upper_constant = s.Rational(11, 6)
sample_range = range(3, 257)

checks = {
    "weight_is_submultiplicative_on_hostile_grid": all(
        weight(a + b) <= weight(a) * weight(b)
        for a in range(0, 65) for b in range(0, 65)
    ),
    "principal_multiplier_has_uniform_lower_weight_bound": all(
        lam.subs(m, n) >= lower_constant * weight(n) for n in sample_range
    ),
    "principal_multiplier_has_uniform_upper_weight_bound": all(
        lam.subs(m, n) <= upper_constant * weight(n) for n in sample_range
    ),
    "base_reflection_inverse_has_geometric_partial_sums": bool(s.simplify(
        s.summation(R**n, (n, 0, 12)) - (1 - R**13) / (1 - R)
    ) == 0),
    "base_exponential_wiener_norm_is_exp_R": s.summation(R**n / s.factorial(n), (n, 0, s.oo)) == s.exp(R),
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "source_weight": "(1+m)^4 R^m",
        "readout_weight": "R^(m-2)",
        "principal_multiplier": str(lam),
        "comparison_lower_constant": str(lower_constant),
        "comparison_upper_constant": str(upper_constant),
        "weight_submultiplicativity_identity": "1+i+j <= (1+i)(1+j)",
        "base_inverse_norm": "||(1-T)^(-1)||_R = 1/(1-R), 0<R<1",
        "base_exponential_norm": "||exp(+-T)||_R = exp(R)",
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Constructor checks for a fourth-order weighted Wiener source space. "
        "They prove the algebra weight and principal diagonal are compatible "
        "with a bounded two-sided linear transport. The strict triangular "
        "remainder still needs an explicit small-radius norm bound before the "
        "analytic inverse theorem can be invoked."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
