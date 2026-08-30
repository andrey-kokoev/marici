import json
from pathlib import Path

import sympy as sp


lam = sp.symbols("lambda", positive=True)
Delta = sp.Integer(2)
g0 = 1 / sp.sqrt(2)
gD0 = 1 / sp.sqrt(2)
T = sp.diag(lam, 1 / lam)
S = sp.Matrix([[0, 1], [1, 0]])
pair = sp.Matrix([g0, gD0])
deformed = sp.simplify(T * pair)

product_error = sp.simplify(Delta * deformed[0] * deformed[1] - 1)
exchange_commutator = sp.simplify(T * S - S * T)
commutator_norm_squared = sp.simplify(sp.trace(exchange_commutator.T * exchange_commutator))
log_asymmetry = sp.simplify(sp.log(deformed[0] / deformed[1]))

at_two = {lam: 2}

checks = {
    "self_dual_pair_is_primitive": sp.simplify(Delta * g0 * gD0) == 1,
    "reciprocal_threshold_preserves_product": product_error == 0,
    "exchange_commutator_formula": sp.simplify(
        commutator_norm_squared - 2 * (lam - 1 / lam) ** 2
    ) == 0,
    "positive_exchange_intertwining_selects_identity_threshold": sp.solve(
        sp.Eq(lam - 1 / lam, 0), lam
    ) == [1],
    "lambda_two_product_monitor_is_dark": product_error.subs(at_two) == 0,
    "lambda_two_exchange_defect_is_nine_halves": commutator_norm_squared.subs(at_two) == sp.Rational(9, 2),
    "lambda_two_log_asymmetry_is_log_four": sp.simplify(log_asymmetry.subs(at_two) - sp.log(4)) == 0,
    "lambda_two_moves_away_from_self_dual_pair": deformed.subs(at_two) != pair,
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "primitive_pair": [str(g0), str(gD0)],
    "lambda_two_pair": [str(sp.simplify(v.subs(at_two))) for v in deformed],
    "lambda_two_product_error": str(product_error.subs(at_two)),
    "lambda_two_exchange_defect": str(commutator_norm_squared.subs(at_two)),
    "lambda_two_log_asymmetry": str(log_asymmetry.subs(at_two)),
    "classification": {
        "product_preserved": True,
        "exchange_intertwined": False,
        "optical_emulator_action": "authorized",
        "physical_dual_source_action": "missing",
    },
}
out = Path(__file__).resolve().parents[1] / "results" / "primitive_product_dual_return_gain.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
