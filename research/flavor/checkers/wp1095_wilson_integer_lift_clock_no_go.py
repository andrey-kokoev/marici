import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# A Wilson phase measures an exponent modulo 1, not its integer lift.
theta0 = Fraction(1, 3)
theta1 = theta0 + 1
theta2 = theta0 + 2
assert theta0 % 1 == theta1 % 1 == theta2 % 1 == Fraction(1, 3)

# The corresponding clock orbits differ.
def clock(n):
    return 6 * n * n
assert clock(0) == 0
assert clock(1) == 6
assert clock(2) == 24
assert len({clock(0), clock(1), clock(2)}) == 3

# The quadratic clock also cannot determine the sign convention sigma from B/A.
assert clock(-1) == clock(1)

supply = {
    "wilson_phase_available_conditionally": True,
    "phase_defined_modulo_one": True,
    "integer_lift_selected": False,
    "clock_orbit_selected": False,
    "sigma_selected_by_quadratic_clock": False,
}
assert list(supply.values()).count(False) == 3

result = {
    "schema": "marici.flavor.wp1095.v1",
    "status": "PASS",
    "question": "Can a conditional Wilson phase select the integer clock lift n or sigma?",
    "phase_lifts": [str(theta0), str(theta1), str(theta2)],
    "common_phase_mod_one": str(theta0 % 1),
    "clock_values_for_n_0_1_2": [str(clock(0)), str(clock(1)), str(clock(2))],
    "sign_witness": {"n": 1, "minus_n": -1, "clock_equal": True},
    "current_source_supply": supply,
    "classification": "negative gate: Wilson phase sees the exponent modulo one, not the integer clock lift",
    "remaining_gate": "source packet selecting the integer flux lift n, unit orbit B/A=6n^2, and sign convention sigma",
    "hostile_gate": "do not infer n from a Wilson phase modulo one or infer sigma from the quadratic value 6n^2",
    "claim_boundary": "the conditional Wilson constructor may fix a phase class, but not its integral representative or clock orientation",
    "disposition": "Wilson integer-lift clock loophole closed",
}

(ROOT / "results" / "wp1095_wilson_integer_lift_clock_no_go.json").write_text(json.dumps(result, indent=2) + "\n")
print("WP1095 PASS:", theta0 % 1, clock(0), clock(1), clock(2), clock(-1) == clock(1))
