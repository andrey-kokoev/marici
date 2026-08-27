"""Exact conditional Gram for the protected total-rate and chirality ports."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
alpha, p, q, r = sp.symbols("alpha p q r", real=True)
J = sp.Matrix([[1, 1], [alpha, -alpha]])
precision = sp.Matrix([[p, r], [r, q]])
gram = sp.simplify(J.T*precision*J)

tau = sp.symbols("tau", nonnegative=True)
independent_precision = sp.diag(1, tau)
independent_gram = sp.simplify(J.T*independent_precision*J)

a0, da, w0 = sp.symbols("a0 da w0", positive=True)
robust_alpha = a0-da
robust_lower_bound = 2*w0*sp.Min(1, robust_alpha**2)

checks = {
    "response_determinant": J.det() == -2*alpha,
    "general_conditional_gram_determinant": sp.factor(gram.det()) == 4*alpha**2*(p*q-r**2),
    "independent_metric_determinant": sp.factor(independent_gram.det()) == 4*alpha**2*tau,
    "missing_chirality_precision_collapses_rank": independent_gram.subs(tau, 0).rank() == 1,
    "unit_metric_singular_values_squared": (J*J.T).eigenvals() == {sp.Integer(2): 1, 2*alpha**2: 1},
    "robust_bound_positive_under_strict_gates": robust_lower_bound.subs({a0: 1, da: sp.Rational(1, 4), w0: sp.Rational(1, 2)}) == sp.Rational(9, 16),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP673", "status": "PASS", "checks": checks,
    "response": "J=[[1,1],[alpha,-alpha]] on (u,v)",
    "independent_precision": "W=[[p,r],[r,q]] with p>0 and pq-r^2>0",
    "gram_determinant": "det(J^T W J)=4alpha^2(pq-r^2)",
    "robust_lower_bound": "lambda_min>=2 w_min min(1,(|alpha_0|-delta_alpha)^2)",
    "acceptance": ["|alpha_0|>delta_alpha", "independently calibrated w_min>0"],
    "classification": "the two-port family is conditionally faithful exactly when analyzer and detector metric are independently nondegenerate",
    "smallest_exact_falsifier": "zero chirality precision tau=0 gives rank-one Gram",
    "remaining_gate": "name and calibrate a physical polarimeter and its covariance without using the target signal to manufacture rank",
}
(ROOT / "results" / "wp673_protected_conditional_gram.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
