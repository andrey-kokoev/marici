import json
from pathlib import Path

import mpmath as mp
import sympy as sp


A = sp.Rational(3, 5)
B = sp.Rational(-12, 25)
C_selected = sp.Rational(4, 5)
D_selected = sp.Rational(9, 25)
C_complement = sp.Rational(0)
D_complement = sp.Rational(4, 5)
lam = sp.Rational(5, 3)
x = sp.Rational(-9, 20)
u = sp.Rational(1)
epsilon = sp.Rational(1, 5)

state_residual = sp.simplify((lam - A) * x - B * u)
selected = sp.simplify(C_selected * x + D_selected * u)
complement = sp.simplify(C_complement * x + D_complement * u)
canonical_incidence = sp.Rational(0)
hostile_incidence = sp.simplify(2 * epsilon / (1 + 2 * epsilon) * u)

mp.mp.dps = 60


def local(p, w):
    return mp.sinh(w * mp.log(p)) / (mp.sqrt(p) * w)


def theta_sum(w):
    return local(2, w) + local(3, w)


theta_root = mp.findroot(
    theta_sum,
    (mp.mpc("0.68", "7.43"), mp.mpc("0.70", "7.45")),
    tol=mp.mpf("1e-50"),
)
theta_locals = [local(2, theta_root), local(3, theta_root)]
theta_dagger_power = sum(abs(value) ** 2 for value in theta_locals)

classification = {
    "packet_zero": selected == 0 and complement == 0 and hostile_incidence == 0,
    "selected_transmission_zero": state_residual == 0 and selected == 0 and (x != 0 or u != 0) and complement != 0,
    "incidence_alias": selected == 0 and canonical_incidence != hostile_incidence,
    "normalization_erasure": False,
    "theta_off_seam_event_is_selected_transmission_zero": abs(theta_sum(theta_root)) < mp.mpf("1e-45") and theta_dagger_power > mp.mpf("1e-2"),
}

checks = {
    "rosenbrock_state_equation_holds": state_residual == 0,
    "selected_output_is_dark": selected == 0,
    "complementary_output_is_bright": complement == sp.Rational(4, 5),
    "fractional_incidence_output_is_two_sevenths": hostile_incidence == sp.Rational(2, 7),
    "canonical_fractional_incidence_is_zero": canonical_incidence == 0,
    "event_is_not_packet_zero": not classification["packet_zero"],
    "event_is_transmission_zero": classification["selected_transmission_zero"],
    "event_is_incidence_alias": classification["incidence_alias"],
    "theta_hostile_receives_same_transmission_class": classification["theta_off_seam_event_is_selected_transmission_zero"],
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "classification": classification,
    "exact_fixture": {
        "lambda": str(lam), "state": str(x), "input": str(u),
        "selected": str(selected), "complement": str(complement),
        "canonical_incidence": str(canonical_incidence),
        "hostile_incidence": str(hostile_incidence),
    },
    "theta_hostile": {
        "root_real": mp.nstr(mp.re(theta_root), 25),
        "root_imag": mp.nstr(mp.im(theta_root), 25),
        "dagger_power": mp.nstr(theta_dagger_power, 25),
    },
}
out = Path(__file__).resolve().parents[1] / "results" / "incidence_aware_rosenbrock_classifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
