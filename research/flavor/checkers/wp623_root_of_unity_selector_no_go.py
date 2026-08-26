"""Exact WP623 rational root-of-unity selector obstruction."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

target_r = sp.Rational(3, 5)
target_x = 2 * target_r
allowed_rational_cosines = {
    sp.Integer(-1),
    sp.Rational(-1, 2),
    sp.Integer(0),
    sp.Rational(1, 2),
    sp.Integer(1),
}

# If theta/pi is rational, zeta=exp(i theta) is a root of unity. Therefore
# x=zeta+zeta^-1=2 cos(theta) is an algebraic integer. A rational algebraic
# integer is an integer, and |x|<=2 leaves only -2,-1,0,1,2.
allowed_x = {2 * value for value in allowed_rational_cosines}
target_numerator, target_denominator = sp.fraction(target_x)

# Exact finite witnesses for each allowed rational cosine.
witnesses = {
    sp.Integer(1): (sp.Integer(1), sp.Integer(0)),
    sp.Rational(1, 2): (sp.Integer(6), sp.Integer(1)),
    sp.Integer(0): (sp.Integer(4), sp.Integer(1)),
    sp.Rational(-1, 2): (sp.Integer(3), sp.Integer(2)),
    sp.Integer(-1): (sp.Integer(2), sp.Integer(1)),
}
witness_checks = {
    str(value): sp.simplify(sp.cos(2 * sp.pi * k / n) - value) == 0
    for value, (n, k) in witnesses.items()
}

# Deliberate fitted-readout evasion. It reaches the target at the trivial
# root-of-unity vacuum but inserts the target as the readout coefficient.
a = sp.Integer(0)
b = target_r
fitted_readout = a + b * sp.cos(0)

checks = {
    "target_double_cosine_is_rational": target_x.is_Rational,
    "target_double_cosine_is_not_integer": target_denominator != 1,
    "root_of_unity_rational_values_are_exhausted": allowed_x == {-2, -1, 0, 1, 2},
    "target_is_excluded_from_single_clock_spectrum": target_r not in allowed_rational_cosines,
    "all_allowed_values_have_exact_clock_witnesses": all(witness_checks.values()),
    "nearest_allowed_positive_value_is_one_half": min(
        (abs(target_r - value), value) for value in allowed_rational_cosines
    )[1] == sp.Rational(1, 2),
    "nearest_exact_residual_is_one_tenth": min(
        abs(target_r - value) for value in allowed_rational_cosines
    ) == sp.Rational(1, 10),
    "integer_harmonic_does_not_change_algebraic_integer_gate": target_x not in allowed_x,
    "fitted_affine_readout_can_fake_target": fitted_readout == target_r,
    "fitted_evasion_contains_target_coefficient": b == target_r,
}

if not all(checks.values()):
    raise SystemExit(f"WP623 check failed: {checks}")
checks = {key: bool(value) for key, value in checks.items()}

result = {
    "work_package": "WP623",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "one compact phase theta with integer-harmonic potential and the fixed relational readout r=cos(theta)",
    "constructor": "U_n(theta)=Lambda^4(1-cos(n theta)); minima have theta=2 pi k/n",
    "exact_theorem": "if theta/pi and cos(theta) are rational, then cos(theta) is one of -1,-1/2,0,1/2,1",
    "target_obstruction": "r=3/5 gives 2r=6/5, a rational noninteger, so it cannot equal zeta+zeta^-1 for a root of unity zeta",
    "contextual_partition": ["r=-1", "r=-1/2", "r=0", "r=1/2", "r=1"],
    "classification": "source-derived discrete selector on the H-referenced relational family, but it excludes rather than selects the observed point",
    "smallest_exact_falsifier": "the nearest allowed positive value is r=1/2, leaving exact residual 1/10 from r=3/5",
    "deliberate_failure": "an affine readout r=(3/5) cos(theta) reaches the target at theta=0 only by inserting 3/5 into the instrument map",
    "descent": "the compact clock can descend in its own source groupoid, but its flavor readout uses the H reference and therefore defines a new relational experiment over the stabilizer groupoid",
    "physical_probe": "measure clock periodicity, harmonic number, winding or domain-wall sectors, and the calibrated map from clock phase to the WP618 root-vector mass ratio in one source lineage",
    "instrument_gate": "no admitted apparatus currently establishes that the flavor lens is the fixed cosine readout of a compact source clock",
    "remaining_source_gate": "a multi-clock or independently derived nonlinear map may evade the theorem, but must be frozen before comparison with r=3/5",
}

out = ROOT / "results" / "wp623_root_of_unity_selector_no_go.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
