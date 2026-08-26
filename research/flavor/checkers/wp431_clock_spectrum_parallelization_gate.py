"""Exact audit of whether an observed clock fixes the mediator spectrum."""

import json
from pathlib import Path

import sympy as sp


v, k, q, xi, omega = sp.symbols("v k q xi omega", positive=True, real=True)
mass = xi * v
residue = k * mass**2
width = q * mass
low_coefficient = sp.factor(residue / mass**2)
width_ratio = sp.factor(width / mass)
response = sp.factor(residue / (mass**2 - omega**2 - sp.I * mass * width))

benchmark = {v: 1, k: 1, q: sp.Rational(1, 10), omega: 1}
response_xi_1 = sp.simplify(response.subs(benchmark).subs(xi, 1))
response_xi_10 = sp.simplify(response.subs(benchmark).subs(xi, 10))

m0sq, kappa = sp.symbols("m0_squared kappa", real=True)
portal_ratio_squared = sp.factor(m0sq / v**2 + kappa)

checks = {
    "clock_normalized_family_preserves_low_coefficient": low_coefficient == k,
    "clock_normalized_family_preserves_dimensionless_width": width_ratio == q,
    "mediator_mass_depends_on_free_ratio": sp.diff(mass, xi) == v,
    "residue_and_width_depend_on_free_ratio": sp.diff(residue, xi) != 0 and sp.diff(width, xi) != 0,
    "hostile_pair_uses_same_clock_and_low_packet": mass.subs(benchmark).subs(xi, 1) == 1 and mass.subs(benchmark).subs(xi, 10) == 10,
    "hostile_pair_has_different_fixed_frequency_response": sp.simplify(response_xi_10 - response_xi_1) != 0,
    "portal_relation_retains_two_free_inputs": set(portal_ratio_squared.free_symbols) >= {m0sq, kappa},
    "setting_units_does_not_fix_ratio": xi in mass.free_symbols and v in mass.free_symbols,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP431",
    "title": "Clock-spectrum parallelization gate",
    "observed_clock": "electroweak scale v",
    "free_spectral_ratio": "xi = M/v",
    "common_low_energy_coefficient": str(low_coefficient),
    "common_dimensionless_width": str(width_ratio),
    "hostile_pair": {
        "xi_values": ["1", "10"],
        "response_xi_1": str(response_xi_1),
        "response_xi_10": str(response_xi_10),
    },
    "portal_ratio_squared": str(portal_ratio_squared),
    "classification": "an observed Standard Model clock does not fix the mediator spectrum without a source-derived mediator-to-clock relation",
    "smallest_exact_falsifier": "a source-derived equation fixing xi without an input adjusted to the flavor outcome",
    "remaining_gate": "derive or observe one absolute mediator invariant, then freeze the rest of the spectral packet independently",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).parents[1] / "results" / "wp431_clock_spectrum_parallelization_gate.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
