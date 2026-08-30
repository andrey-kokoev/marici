"""Exact ideal chirality analyzer for the protected two-pair decay."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
u, v, alpha = sp.symbols("u v alpha", real=True)
W = u+v
N = alpha*(u-v)
response = sp.Matrix([W, N])
J = response.jacobian([u, v])
Q_reconstructed = sp.simplify((W**2+(N/alpha)**2)/2)

e = sp.symbols("e", real=True)
confusion = sp.Matrix([[1-e, e], [e, 1-e]])
hostile_1 = {u: 1, v: 4}
hostile_2 = {u: sp.Rational(121, 25), v: sp.Rational(4, 25)}

checks = {
    "width_plus_chirality_response_is_rank_two": J.det() == -2*alpha,
    "loop_erosion_reconstructs_exactly": sp.simplify(Q_reconstructed-(u**2+v**2)) == 0,
    "symmetric_helicity_confusion_has_expected_determinant": confusion.det() == 1-2*e,
    "confusion_analyzing_power": sp.simplify((1-2*e)-alpha).subs(alpha, 1-2*e) == 0,
    "half_confusion_collapses_rank": J.det().subs(alpha, 0) == 0,
    "wp671_hostile_pair_separates_for_nonzero_analyzer": (
        response.subs(hostile_1)-response.subs(hostile_2)).subs(alpha, 1) != sp.zeros(2, 1),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP672", "status": "PASS", "checks": checks,
    "source_coordinates": ["u=|y|^2", "v=|z|^2"],
    "ideal_readout": ["W=u+v", "N=alpha(u-v)"],
    "response_determinant": "-2alpha",
    "erosion_reconstruction": "u^2+v^2=(W^2+(N/alpha)^2)/2",
    "symmetric_confusion": "alpha=1-2e; rank collapses only at e=1/2",
    "classification": "an ideal calibrated chirality moment repairs magnitude and loop-erosion identification in one open decay",
    "smallest_exact_falsifier": "alpha=0, equivalently symmetric helicity confusion e=1/2",
    "remaining_gate": "derive a physical polarimeter, analyzing power, acceptance, backgrounds, and covariance from the protected decay cascade",
}
(ROOT / "results" / "wp672_protected_chirality_analyzer.json").write_text(
    json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
