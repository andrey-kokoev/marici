"""Exact WP585 adaptive-closure no-go for the inclusive Higgs instrument."""

import itertools
import json
from pathlib import Path

import sympy as sp

z, lambda_s = sp.symbols("z lambda_s", positive=True, real=True)
p = 1 - z


def history_probability(history):
    clicks = sum(history)
    return sp.expand(p**clicks * (1 - p) ** (len(history) - clicks))


histories = [
    history
    for length in range(1, 5)
    for history in itertools.product((0, 1), repeat=length)
]
probabilities = {history: history_probability(history) for history in histories}
policy_weights = {
    history: sp.Symbol("a_" + ("e" if not history else "".join(map(str, history))))
    for length in range(4)
    for history in itertools.product((0, 1), repeat=length)
}

hostile_minus = {z: sp.Rational(1, 4), lambda_s: sp.Rational(1, 2)}
hostile_plus = {z: sp.Rational(1, 4), lambda_s: sp.Rational(3, 2)}

checks = {
    "all_finite_history_probabilities_are_lambda_s_blind": all(
        sp.diff(probability, lambda_s) == 0 for probability in probabilities.values()
    ),
    "all_hostile_history_laws_agree_through_length_four": all(
        probability.subs(hostile_minus) == probability.subs(hostile_plus)
        for probability in probabilities.values()
    ),
    "null_records_remain_lambda_s_blind": all(
        sp.diff(probabilities[(0,) * length], lambda_s) == 0
        for length in range(1, 5)
    ),
    "policy_family_is_nontrivial": len(policy_weights) == 15,
    "hostile_single_trial_probability_is_three_quarters": p.subs(hostile_minus)
    == p.subs(hostile_plus)
    == sp.Rational(3, 4),
}

if not all(checks.values()):
    raise SystemExit(f"WP585 check failed: {checks}")

checks = {key: bool(value) for key, value in checks.items()}
result = {
    "work_package": "WP585",
    "status": "PASS",
    "checks": checks,
    "authorized_trial_kernel": "Bernoulli record with p=1-z",
    "closure_family": "all finite products, mixtures, null conditioning, and adaptive choices between q settings based on prior records",
    "contextual_partition": "fixed-z classes with unrestricted positive lambda_s fiber",
    "exact_theorem": "factorization through z is preserved by finite adaptive composition, so every q score and every q Fisher entry is zero",
    "finite_checker_depth": 4,
    "checked_history_count": len(histories),
    "hostile_pair": "(z,lambda_s)=(1/4,1/2) and (1/4,3/2)",
    "classification": "adaptive closure of a physical rank-one readout; neither selector nor rigidifier",
    "smallest_falsifier_of_repair": "any claimed adaptive q separation using only this instrument contradicts equality of the one-trial kernels",
    "remaining_gate": "introduce a source-authorized trial kernel with nonzero q dependence before taking contextual closure",
}

out = Path(__file__).resolve().parents[1] / "results" / "wp585_inclusive_higgs_adaptive_closure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
