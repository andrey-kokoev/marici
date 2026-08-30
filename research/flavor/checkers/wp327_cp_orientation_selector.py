"""WP327: exact selector audit for the conjugate CP branches of WP326."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    c = sp.symbols("c", real=True)
    c0, epsilon = sp.symbols("c0 epsilon", real=True, positive=True)
    symmetric_potential = sp.expand((c**2 - c0**2) ** 2)
    curvature_plus = sp.simplify(sp.diff(symmetric_potential, c, 2).subs(c, c0))
    curvature_minus = sp.simplify(sp.diff(symmetric_potential, c, 2).subs(c, -c0))
    branch_energies_symmetric = {
        "minus": sp.simplify(symmetric_potential.subs(c, -c0)),
        "plus": sp.simplify(symmetric_potential.subs(c, c0)),
    }
    biased_potential = symmetric_potential - epsilon * c
    branch_energies_biased = {
        "minus": sp.simplify(biased_potential.subs(c, -c0)),
        "plus": sp.simplify(biased_potential.subs(c, c0)),
    }
    splitting = sp.simplify(branch_energies_biased["minus"] - branch_energies_biased["plus"])
    checks = {
        "cp_even_potential_is_even": sp.simplify(symmetric_potential.subs(c, -c) - symmetric_potential) == 0,
        "cp_even_source_has_two_zero_energy_minima": branch_energies_symmetric == {"minus": 0, "plus": 0},
        "both_cp_branches_are_locally_stable": curvature_plus == 8 * c0**2 and curvature_minus == 8 * c0**2,
        "cp_even_source_does_not_select_sign": branch_energies_symmetric["minus"] == branch_energies_symmetric["plus"],
        "positive_odd_bias_selects_positive_branch": sp.simplify(branch_energies_biased["minus"] - branch_energies_biased["plus"]) > 0,
        "branch_splitting_is_linear_in_bias": splitting == 2 * c0 * epsilon,
        "reversing_bias_reverses_selected_sign": sp.simplify(biased_potential.subs({c: -c0, epsilon: -epsilon}) - biased_potential.subs({c: c0, epsilon: -epsilon})) < 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP327",
        "admitted_state_domain": "the two complex-conjugate CP branches of WP326 represented by a real CP-odd coordinate c with target magnitude c0>0",
        "faithful_quotient_coordinate": "CP-odd orientation c together with CP-even spectral data on physical16",
        "source_operation": "CP-even spontaneous potential V0=(c^2-c0^2)^2, optionally augmented by the CP-odd bias -epsilon c",
        "symmetric_branch_energies": {key: str(value) for key, value in branch_energies_symmetric.items()},
        "biased_branch_energies": {key: str(value) for key, value in branch_energies_biased.items()},
        "exact_energy_splitting": str(splitting),
        "contextual_partition": "CP-even probes collapse the two branches into one class; a CP-sensitive probe separates them, but the CP-even source assigns equal energy",
        "classification": "the CP-even source selects a two-point conjugate vacuum fiber but not its orientation; an odd bias selects a sign while carrying new source authority",
        "smallest_exact_falsifier": "c=+c0 and c=-c0 have identical CP-even potential and curvature but opposite CP orientation",
        "remaining_physical_instrument_gate": "derive a nonzero CP-odd bias or a cosmological domain-preparation law independently of flavor data, and calibrate a CP-sensitive instrument; observing one domain does not prove unique source selection",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp327_cp_orientation_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
