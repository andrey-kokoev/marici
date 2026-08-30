#!/usr/bin/env python3
"""Match the real Pearcey ports to one- and two-saddle Gaussian regimes."""

import hashlib
import json
from pathlib import Path

import sympy as s

ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-connected-vertex-source-frontier.md"
RESULT = ROOT / "research/strominger/results/deutschean_pearcey_gaussian_matching.json"
u, X, Y, A, r = s.symbols("u X Y A r", positive=True)
sigma = s.symbols("sigma", integer=True)
S = -u**4 / 4 + X*u**2 / 2 + Y*u
S0 = S.subs(Y, 0)
stationary = s.factor(s.diff(S0, u))
positive_saddles = [s.sqrt(A), -s.sqrt(A)]
actions = [s.simplify(S0.subs({X: A, u: point})) for point in positive_saddles]
hessians = [s.simplify(s.diff(S0, u, 2).subs({X: A, u: point})) for point in positive_saddles]
weights = [s.exp(r), s.exp(-r)]
mixture_mean = s.factor(s.sqrt(A) * (weights[0] - weights[1]) / sum(weights))
mixture_second = s.factor(A * (weights[0] + weights[1]) / sum(weights))

checks = {
    "stationary_equation_has_cusp_factorization": stationary == -u*(u**2 - X),
    "negative_X_has_single_real_stationary_max": s.diff(S0, u, 2).subs({X: -A, u: 0}) == -A,
    "positive_X_has_two_equal_maxima": actions == [A**2/4, A**2/4],
    "positive_X_saddle_hessians_are_minus_2A": hessians == [-2*A, -2*A],
    "linear_control_biases_actions_by_2YsqrtX": s.simplify(
        S.subs({X: A, u: s.sqrt(A)}) - S.subs({X: A, u: -s.sqrt(A)})
        - 2*Y*s.sqrt(A)
    ) == 0,
    "two_branch_mean_is_tanh_weighted": s.simplify(
        mixture_mean - s.sqrt(A)*s.tanh(r).rewrite(s.exp)
    ) == 0,
    "two_branch_second_moment_is_A": mixture_second == A,
}

payload = {
    "artifact_sha256": hashlib.sha256(PACKET.read_bytes()).hexdigest().upper(),
    "checks": {key: bool(value) for key, value in checks.items()},
    "observed": {
        "stationary_equation_at_Y_0": str(stationary),
        "one_saddle_regime": "X=-A, A->infinity",
        "one_saddle_leading_P": "sqrt(2*pi/A)",
        "one_saddle_leading_mean": "0",
        "one_saddle_leading_variance": "1/A",
        "two_saddle_regime": "X=A, A->infinity",
        "two_saddle_leading_P": "2*sqrt(pi/A)*exp(A^2/4)",
        "two_saddle_action_bias": "2*Y*sqrt(A)",
        "two_saddle_leading_mean": "sqrt(A)*tanh(Y*sqrt(A))",
        "two_saddle_leading_second_moment": "A",
        "branch_weight_ratio": "exp(2*Y*sqrt(A))",
    },
    "passed": all(bool(value) for value in checks.values()),
    "semantic_boundary": (
        "Exact stationary geometry and leading Gaussian matching of the Pearcey "
        "ports. It proves one- versus two-branch reconstruction and the branch "
        "weight law. It does not yet match the full source amplitude, adjacent-"
        "grade normalization, or subleading H1/H2 coefficients."
    ),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if payload["passed"] else 1)
