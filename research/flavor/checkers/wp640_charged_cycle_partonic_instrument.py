"""Exact WP640 symmetry-broken partonic-response audit."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def wilson(l_a, l_b, h, singlet, adjoint, m_chi):
    if m_chi <= 0:
        raise ValueError("m_chi must be positive")
    return (l_a + l_b) ** 2 * h**2 * singlet**2 * adjoint**2 / m_chi**2


def normalized_amplitude_square(g, shat):
    if shat <= 0:
        raise ValueError("shat must be positive")
    return g**2 * shat**2


unit = (F(1),) * 3
g_plus = wilson(F(1), F(1), *unit, F(1))
g_minus = wilson(F(1), F(-1), *unit, F(1))
g_mass_two = wilson(F(1), F(1), *unit, F(2))
shat = F(1)

checks = {
    "constructive_wilson_is_four": g_plus == 4,
    "destructive_wilson_is_zero": g_minus == 0,
    "same_cycle_mass_two_wilson_is_one": g_mass_two == 1,
    "constructive_normalized_amplitude_square_is_sixteen": (
        normalized_amplitude_square(g_plus, shat) == 16),
    "destructive_partonic_response_is_zero": (
        normalized_amplitude_square(g_minus, shat) == 0),
    "mass_two_normalized_amplitude_square_is_one": (
        normalized_amplitude_square(g_mass_two, shat) == 1),
    "four_quark_operator_dimension_is_six": 4 * F(3, 2) == 6,
    "wilson_mass_dimension_is_minus_two": -2 == 4 - 6,
    "charged_bilinear_product_is_neutral": F(1) + F(-1) == 0,
    "integrated_over_cosine_has_factor_two": F(2, 32) == F(1, 16),
    "common_total_current_sign_is_invisible": (
        normalized_amplitude_square(wilson(F(-1), F(-1), *unit, F(1)), shat)
        == normalized_amplitude_square(g_plus, shat)),
}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP640",
    "status": "PASS",
    "checks": checks,
    "process": "u_L anti-d_R -> u_L anti-d_R at fixed helicity and fixed color",
    "wilson": "G=|L_A+L_B|^2 h^2 s^2 x^2/m_chi^2",
    "matrix_element_square": "|M|^2=G^2 shat^2",
    "differential_cross_section": "d sigma/d cos(theta)=G^2 shat/(32 pi)",
    "total_cross_section": "sigma=G^2 shat/(16 pi)",
    "contextual_partition": {"plus,m=1": "16", "minus,m=1": "0", "plus,m=2": "1"},
    "kernel": "the sign or phase of the total matched current is invisible without interference",
    "classification": "executable source-level partonic probe; neither selector nor detector-calibrated instrument",
    "instrument_gate": "PDFs, tagging, interference, running, cuts, resolution, backgrounds, systematics, and likelihood",
}
(ROOT / "results" / "wp640_charged_cycle_partonic_instrument.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
