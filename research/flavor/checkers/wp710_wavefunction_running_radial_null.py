"""Exact no-go for displacing WP708 rays by field normalization alone."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
ln, lm, lx, lc = sp.symbols(
    "lambda_n lambda_m lambda_x lambda_c", nonzero=True, real=True
)
sn, sm = sp.symbols("s_n s_m", positive=True)
gn, gm = sp.symbols("gamma_n gamma_m", real=True)

transformed = {
    ln: sn**4*ln,
    lm: sm**4*lm,
    lx: sn**2*sm**2*lx,
    lc: sn**2*sm**2*lc,
}
radial_ratio = sp.factor(ln*lm/lx**2)
correlation_ratio = sp.factor(lc/lx)
radial_margin = sp.factor(4*radial_ratio-1)

N = 2*gn
M = 2*gm
X = 2*(gn+gm)
C = 2*(gn+gm)

checks = {
    "radial_ratio_exactly_invariant": sp.simplify(radial_ratio.subs(transformed)-radial_ratio) == 0,
    "correlation_ratio_exactly_invariant": sp.simplify(correlation_ratio.subs(transformed)-correlation_ratio) == 0,
    "radial_margin_exactly_invariant": sp.simplify(radial_margin.subs(transformed)-radial_margin) == 0,
    "wp709_response_combination_vanishes": sp.simplify(N+M-X) == 0,
    "correlation_and_mixed_leg_weights_match": C == X,
    "unequal_anomalous_dimensions_still_cancel": sp.simplify((N+M-X).subs({gn: 2, gm: -3})) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP710",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "arbitrary positive independent normalizations of the two WP662 triplet fields and their induced anomalous-dimension beta terms",
    "faithful_coordinate": "radial ratio lambda_n lambda_m/lambda_x^2 and correlation ratio lambda_c/lambda_x",
    "source_authorized_operation": "field normalization and external-leg anomalous-dimension transport",
    "contextual_partition": "normalization shears individual coupling coordinates but leaves both faithful projective ratios exactly fixed",
    "classification": "presentation transport/rigidifier only; neither selector nor instrument, and exactly null under the WP709 radial acceptance functional",
    "smallest_exact_falsifier": "N+M-X=0 for arbitrary gamma_n and gamma_m, equivalently exact invariance of the radial margin",
    "remaining_gate": "derive genuine vertex corrections with positive self-versus-mixed combination from one frozen completed source",
}
(ROOT / "results" / "wp710_wavefunction_running_radial_null.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
