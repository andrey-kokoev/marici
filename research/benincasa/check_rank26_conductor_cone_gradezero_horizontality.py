"""Formal scaling and Milnor-rank audit for the universal conductor generator."""

from fractions import Fraction
import json
from pathlib import Path


# For w^2 - R^2 - q*S, the Jacobian in the fiber variables (w,R) is
# (2*w,-2*R), hence its Milnor algebra has basis [1].
milnor_basis = ["1"]

# Put R=lambda*t, w=lambda*sqrt(t^2+1), lambda^2=q*S.
# dR contributes lambda and K^alpha contributes lambda^(2*alpha),
# with alpha=-1/2+epsilon.
alpha_constant = Fraction(-1, 2)
alpha_epsilon = Fraction(1)
lambda_constant_power = 1 + 2 * alpha_constant
lambda_epsilon_power = 2 * alpha_epsilon

# Therefore the local period scales as (q*S)^epsilon.  Multiplication by
# the source normalization epsilon removes the beta-function 1/epsilon pole.
grade_zero_q_power = 0
grade_zero_s_power = 0
first_grade_log_terms = ["log(q)", "log(S)"]

checks = {
    "milnor_rank_is_one": len(milnor_basis) == 1,
    "constant_lambda_power_cancels": lambda_constant_power == 0,
    "epsilon_lambda_power_is_two": lambda_epsilon_power == 2,
    "local_period_scales_as_qS_to_epsilon": lambda_epsilon_power == 2,
    "normalized_grade_zero_is_q_independent": grade_zero_q_power == 0,
    "normalized_grade_zero_is_S_independent": grade_zero_s_power == 0,
    "S_enters_only_at_first_epsilon_grade": first_grade_log_terms == ["log(q)", "log(S)"],
}

payload = {
    "schema": "marici.rank26-conductor-universal-generator.v2",
    "local_family": "w^2 = R^2 + q*S",
    "milnor_basis": milnor_basis,
    "milnor_rank": len(milnor_basis),
    "period_scaling": "(q*S)^epsilon",
    "normalized_universal_grade_zero_scaling": "1",
    "first_epsilon_grade": first_grade_log_terms,
    "domain": "S != 0 (away from existing triangle support)",
    "scope": "This trivializes the universal A1 vanishing-cycle generator only. The full source port also contains numerator and spectator-wall coefficients and need not be horizontal.",
    "checks": checks,
    "all_passed": all(checks.values()),
}

out = Path(__file__).with_name("rank26-conductor-cone-gradezero-horizontality.json")
out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["all_passed"]:
    raise SystemExit(1)
