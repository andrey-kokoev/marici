"""Exact signed boson-versus-Dirac vertex contrast at the WP708 ray."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
gn, gm = sp.symbols("g_n g_m", real=True)
kappa = sp.symbols("kappa", positive=True)
Fn, Fm = sp.symbols("F_n F_m", nonnegative=True)

N_b = kappa*gn**2
M_b = kappa*gm**2
X_b = 2*kappa*gn*gm
C_b = sp.Integer(0)
bosonic_contrast = sp.factor(N_b+M_b-X_b)
total_contrast = sp.factor(bosonic_contrast-8*(Fn+Fm))
wp709_displacement = sp.factor(total_contrast/28)

checks = {
    "bosonic_channel_is_positive_gram_contrast": bosonic_contrast == kappa*(gm-gn)**2,
    "exchange_symmetric_boson_is_null": bosonic_contrast.subs(gm, gn) == 0,
    "asymmetric_unit_witness_opens_without_fermions": wp709_displacement.subs({kappa: 1, gn: 1, gm: 0, Fn: 0, Fm: 0}) == sp.Rational(1, 28),
    "complete_signed_combination": sp.simplify(total_contrast-(kappa*(gm-gn)**2-8*Fm-8*Fn)) == 0,
    "symmetric_boson_cannot_beat_one_fermion_chain": wp709_displacement.subs({kappa: 1, gn: 1, gm: 1, Fn: 1, Fm: 0}) == -sp.Rational(2, 7),
    "strict_repair_witness": wp709_displacement.subs({kappa: 9, gn: 1, gm: 0, Fn: 1, Fm: 0}) == sp.Rational(1, 28),
    "correlation_beta_is_not_directly_generated": C_b == 0,
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP712",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "conditional extension by one heavy real boson with mass squared M^2+g_n|n|^2+g_m|m|^2, combined with WP711 disjoint Dirac strengths",
    "faithful_coordinate": "signed WP709 vertex contrast kappa(g_n-g_m)^2-8(F_n+F_m)",
    "candidate_source_operation": "positive bosonic one-loop supertrace in the independently derived quartic counterterm channel",
    "contextual_partition": "the response sees the squared bosonic coupling contrast and total fermion strength, not their signs, allocations, or unique UV constructor",
    "classification": "conditional stability-opening existence constructor; neither numerical selector nor physical instrument until the boson and channel are source-authorized",
    "smallest_exact_falsifier": "g_n=g_m with F_n+F_m>0 makes the complete contrast strictly negative",
    "remaining_gate": "freeze the boson action and normalization independently, derive the counterterm and thresholds, prove the displaced transverse basin, and attach a calibrated portal readout",
}
(ROOT / "results" / "wp712_bosonic_vertex_contrast_gate.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
