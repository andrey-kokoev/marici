"""Show exactly why changing renormalization scale is not a physical probe."""
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
a, b = sp.symbols("a b", real=True)
mu, mu0, Q, Q1, Q2 = sp.symbols("mu mu0 Q Q1 Q2", positive=True)

running = a + b * sp.log(mu / mu0)
form_factor = sp.expand_log(running + b * sp.log(Q / mu), force=True)
physical = sp.simplify(form_factor)
canonical = a + b * sp.log(Q / mu0)

same_q_mu0 = sp.simplify(form_factor.subs(mu, mu0))
same_q_2mu0 = sp.expand_log(form_factor.subs(mu, 2 * mu0), force=True)
pair = sp.Matrix([
    a + b * sp.log(Q1 / mu0),
    a + b * sp.log(Q2 / mu0),
])
jacobian = pair.jacobian([a, b])

checks = {
    "physical_form_factor_is_mu_independent": sp.simplify(sp.diff(physical, mu)) == 0,
    "running_and_explicit_log_cancel": sp.simplify(physical - canonical) == 0,
    "two_mu_choices_same_record_at_fixed_Q": sp.simplify(same_q_mu0 - same_q_2mu0) == 0,
    "two_physical_momenta_have_affine_rank": sp.simplify(jacobian.det() - sp.log(Q2 / Q1)) == 0,
    "momentum_difference_removes_boundary": sp.simplify(pair[1] - pair[0] - b * sp.log(Q2 / Q1)) == 0,
    "coincident_momenta_collapse_rank": sp.simplify(jacobian.det().subs(Q2, Q1)) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP690",
    "status": "PASS",
    "checks": checks,
    "domain": "one-loop affine portal form factor with positive mu, mu0, Q and source-generated coefficient b",
    "typing_result": "renormalization-scale variation at fixed physical momentum is a coordinate change, not a complementary physical context",
    "correction": "WP689 remains an affine comparison theorem only when its two contexts are independently executable physical contexts such as distinct momenta",
    "physical_repair": "F(Q2)-F(Q1)=b log(Q2/Q1), independent of the boundary value a",
    "classification": "renormalization-scale rigidification is neither a selector nor an instrument; distinct physical-momentum response could be a complementary probe",
    "smallest_exact_falsifier": "at fixed Q, any claimed two-scale response difference is zero after running and the explicit logarithm are combined",
    "remaining_gate": "derive the finite-Q same-channel form factor and calibrate two distinct physical-momentum measurements with uncertainties and support",
}
(ROOT / "results" / "wp690_renormalization_scale_noninstrument.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
