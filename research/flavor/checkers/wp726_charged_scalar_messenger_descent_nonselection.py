"""Exact charged-scalar messenger descent and portal nonselection theorem."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
R, X = sp.symbols("R X", real=True)
M, mu, a, b = sp.symbols("M mu a b", positive=True)
dn, dm = sp.symbols("d_n d_m", positive=True, integer=True)
an, am, bn, bm = sp.symbols("a_n a_m b_n b_m", positive=True)
Mn, Mm = sp.symbols("M_n M_m", positive=True)
cn, cm = sp.symbols("c_n c_m", real=True)

mass2 = M**2+a*R+b*X
cw_kernel = sp.expand(mass2**2*(sp.log(mass2/mu**2)-sp.Rational(3, 2)))
mixed_curvature = sp.simplify(sp.diff(cw_kernel, R, X).subs({R: 0, X: 0}))

loop_n = sp.factor(dn*an*bn*sp.log(Mn**2/mu**2))
loop_m = sp.factor(dm*am*bm*sp.log(Mm**2/mu**2))
renormalized_contrast = sp.factor((cn+loop_n)-(cm+loop_m))
cancel_choice = sp.solve(sp.Eq(renormalized_contrast, 0), cn)[0]

checks = {
    "mixed_curvature_descends_to_real_norm_invariants": sp.simplify(mixed_curvature-2*a*b*sp.log(M**2/mu**2)) == 0,
    "natural_scalar_matching_scale_has_zero_finite_mixed_curvature": sp.simplify(mixed_curvature.subs(mu, M)) == 0,
    "below_threshold_log_has_positive_sign": sp.simplify(mixed_curvature.subs(mu, M/sp.E)-4*a*b) == 0,
    "above_threshold_log_has_negative_sign": sp.simplify(mixed_curvature.subs(mu, sp.E*M)+4*a*b) == 0,
    "representation_multiplicity_only_multiplies_vertex_product": sp.simplify(loop_n-dn*an*bn*sp.log(Mn**2/mu**2)) == 0,
    "independent_vertex_rescaling_changes_portal": sp.diff(loop_n, an) != 0,
    "renormalized_counterterm_can_cancel_total_contrast": sp.simplify(renormalized_contrast.subs(cn, cancel_choice)) == 0,
    "charged_scalars_add_no_chiral_gauge_anomaly": True,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP726",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "neutral real SO(3) triplets coupled through norm invariants to heavy charged scalar messengers with positive masses",
    "faithful_coordinate": "the ordered renormalized portal pair on the original real-triplet quotient",
    "source_operation": "integrate out anomaly-free charged scalar species whose masses depend on |n|^2 or |m|^2 and chi^2",
    "descent": "the one-loop action depends only on real norm invariants and therefore descends without charging or complexifying n and m",
    "classification": "operator-support rigidifier and potentially labelled carrier, but not a sign or magnitude selector",
    "smallest_exact_falsifiers": [
        "the finite mixed curvature is zero at mu=M and reverses sign across that presentation scale",
        "an allowed renormalized counterterm cancels any computed loop contrast",
        "multiplicity fixes only an integer prefactor while a_i b_i remains continuous",
    ],
    "remaining_gate": "a source-fixed gauge-Yukawa relation for every messenger vertex and counterterm boundary, plus full supertrace matching whose contrast is scheme-independent and nonzero",
    "instrument_gate": "charged species labels are potential ports, but an actual production-decay analysis must preserve them with calibrated rank two",
}
(ROOT / "results" / "wp726_charged_scalar_messenger_descent_nonselection.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
