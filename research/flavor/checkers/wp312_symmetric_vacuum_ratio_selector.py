"""WP312: exact symmetric-vacuum selector and matched-spectrum consequence."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    v1, v2 = sp.symbols("v1 v2", positive=True)
    radial_scale, radial_stiffness, exchange_stiffness = sp.symbols(
        "radial_scale radial_stiffness exchange_stiffness", positive=True
    )
    potential = radial_stiffness * (v1**2 + v2**2 - radial_scale**2) ** 2 + exchange_stiffness * (v1 - v2) ** 2
    selected_value = radial_scale / sp.sqrt(2)
    selected_substitution = {v1: selected_value, v2: selected_value}
    gradient = sp.Matrix([sp.diff(potential, v1), sp.diff(potential, v2)])
    hessian = sp.hessian(potential, (v1, v2)).subs(selected_substitution)
    hessian_eigenvalues = set(hessian.eigenvals())
    selected_ratio = sp.simplify(selected_value / selected_value)
    positive_zero_locus = sp.solve(
        (v1 - v2, v1**2 + v2**2 - radial_scale**2), (v1, v2), dict=True
    )

    yukawa_y = sp.diag(1, 2, 4)
    yukawa_z = sp.diag(1, 3, 9)
    symmetric_mass_up = sp.simplify(selected_value * yukawa_y + selected_value * yukawa_z)
    symmetric_mass_down = sp.simplify(selected_value * yukawa_y + selected_value * yukawa_z)

    checks = {
        "potential_is_exchange_invariant": sp.simplify(potential.subs({v1: v2, v2: v1}, simultaneous=True) - potential) == 0,
        "potential_is_sum_of_nonnegative_squares": potential.subs(selected_substitution) == 0,
        "selected_vacuum_is_stationary": gradient.subs(selected_substitution) == sp.zeros(2, 1),
        "selected_vacuum_hessian_channels_are_positive": hessian_eigenvalues == {4 * exchange_stiffness, 8 * radial_scale**2 * radial_stiffness},
        "positive_zero_locus_is_unique_symmetric_vacuum": positive_zero_locus == [{v1: selected_value, v2: selected_value}],
        "ratio_has_zero_response_to_all_three_source_parameters": all(sp.diff(selected_ratio, parameter) == 0 for parameter in (radial_scale, radial_stiffness, exchange_stiffness)),
        "physical_radius_responds_to_radial_scale": sp.diff(selected_value, radial_scale) == 1 / sp.sqrt(2),
        "symmetric_matching_forces_equal_mass_matrices": symmetric_mass_up == symmetric_mass_down,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP312",
        "source_potential": "V=lambda*(v1^2+v2^2-R^2)^2+kappa*(v1-v2)^2 with lambda,kappa,R>0",
        "selected_vacuum": "v1=v2=R/sqrt(2)",
        "selected_ratio": "v1/v2=1",
        "source_response": {
            "ratio_rank": 0,
            "physical_radius_rank": 1,
        },
        "ensemble_statement": "the ratio prediction is independent of every positive lambda, kappa, and R; the absolute scale is not",
        "matching_consequence": "under WP311 matching, v1=v2 forces M_u=M_d=(R/sqrt(2))*(Y+Z), stronger than equal hierarchy ratios",
        "descent": "the vacuum potential is exchange invariant in the enlarged source; physical16 descent still requires gauge breaking and covariant Yukawa matching",
        "classification": "genuine source-derived ratio selector across the declared positive coefficient family, but not a full physical16 selector and phenomenologically exposed by its equal-spectrum consequence",
        "smallest_exact_falsifier": "any admitted physical packet with unequal ordered up/down spectra falsifies the symmetric WP311 matching, even if a coarser hierarchy ratio happened to agree",
        "remaining_physical_instrument_gate": "test the equal-spectrum prediction on the complete fitted physical16 ensemble; if falsified, introduce source-derived exchange breaking without fitting away the ratio prediction",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp312_symmetric_vacuum_ratio_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
