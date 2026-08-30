"""WP316: exact nontrivial-flux selector on the exchange quotient."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def ratio(flux):
    return sp.simplify(sp.sqrt(flux**2 + 1) - flux)


def main():
    sectors = [-3, -2, -1, 1, 2, 3]
    energies = {flux: flux**2 for flux in sectors}
    minimum_energy = min(energies.values())
    minima = [flux for flux, energy in energies.items() if energy == minimum_energy]
    quotient_orbits = sorted({abs(flux) for flux in sectors})
    minimum_quotient_orbits = sorted({abs(flux) for flux in minima})
    ratio_pair = [ratio(flux) for flux in minima]

    checks = {
        "zero_flux_is_excluded_by_declared_topological_domain": 0 not in sectors,
        "quadratic_energy_selects_exactly_unit_flux_pair": minima == [-1, 1],
        "exchange_identifies_opposite_fluxes": minimum_quotient_orbits == [1],
        "quotient_minimum_is_singleton_orbit": len(minimum_quotient_orbits) == 1,
        "ordered_ratio_pair_is_reciprocal": sp.simplify(ratio_pair[0] * ratio_pair[1]) == 1,
        "negative_flux_ratio_is_one_plus_sqrt_two": ratio(-1) == 1 + sp.sqrt(2),
        "positive_flux_ratio_is_sqrt_two_minus_one": ratio(1) == -1 + sp.sqrt(2),
        "orientation_is_needed_for_ordered_ratio": ratio(-1) != ratio(1),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP316",
        "theorem_domain": "nontrivial integer flux sectors n in Z without zero, with exchange n~-n and parameter-free energy E=n^2",
        "literal_minima": minima,
        "exchange_quotient_minimum": "the singleton orbit |n|=1",
        "ordered_ratio_pair": [str(value) for value in ratio_pair],
        "unlabelled_prediction": "the reciprocal pair {1+sqrt(2), sqrt(2)-1} modulo up/down exchange",
        "descent": "E=n^2 descends under exchange and selects one orbit; an ordered ratio does not descend until an orientation or labelled port is added",
        "classification": "genuine parameter-free discrete selector on the nontrivial-flux exchange quotient; twofold ordered-ratio fiber before adding a relational orientation port",
        "smallest_exact_falsifier": "literal sectors n=-1 and n=1 have equal minimum energy but predict reciprocal ordered ratios",
        "reference_rule": "choosing a flux sign or naming the up sector reduces the groupoid to an oriented stabilizer and defines a new relational experiment",
        "remaining_physical_instrument_gate": "derive the exclusion of n=0 from source topology, show exchange is the admitted quotient upstream, and implement any required orientation port before matching the unit-flux orbit to physical16",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp316_nontrivial_flux_orbit_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
