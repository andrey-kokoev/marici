"""WP281: exact spontaneous-CP orientation-vacuum audit."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    field = sp.symbols("field", real=True)
    coupling, vev = sp.symbols("coupling vev", positive=True)
    potential = coupling * (field**2 - vev**2) ** 2 / 4
    derivative = sp.factor(sp.diff(potential, field))
    curvature = sp.factor(sp.diff(potential, field, 2))
    stationary_points = [sp.Integer(0), -vev, vev]
    stationary_residuals = [sp.simplify(derivative.subs(field, point)) for point in stationary_points]
    curvatures = [sp.simplify(curvature.subs(field, point)) for point in stationary_points]
    energies = [sp.simplify(potential.subs(field, point)) for point in stationary_points]

    rotation_generator = sp.Matrix([[0, 1], [-1, 0]])
    drifts = [sp.simplify(point * rotation_generator) for point in (-vev, vev)]
    sensor = sp.Matrix([[1, 0]])
    tower_determinants = [sp.factor(sensor.col_join(sensor * drift).det()) for drift in drifts]

    # A CP-odd linear bias is the smallest branch-lifting operator. Its values
    # on the unperturbed vacua differ by an exact amount, demonstrating the new
    # authority-bearing datum even though the true minima shift when bias != 0.
    bias = sp.symbols("bias", real=True)
    biased_potential = potential - bias * field
    bias_energy_split = sp.simplify(
        biased_potential.subs(field, vev) - biased_potential.subs(field, -vev)
    )

    checks = {
        "three_stationary_points_exact": all(residual == 0 for residual in stationary_residuals),
        "origin_is_unstable": curvatures[0] == -coupling * vev**2,
        "two_nonzero_vacua_are_stable": curvatures[1:] == [2 * coupling * vev**2, 2 * coupling * vev**2],
        "cp_conjugate_vacua_degenerate": energies[1] == energies[2] == 0,
        "vacuum_drifts_have_opposite_orientation": drifts[0] == -drifts[1],
        "both_nonzero_vacua_close_dynamic_rank": tower_determinants == [-vev, vev],
        "cp_even_action_does_not_select_sign": energies[1] - energies[2] == 0,
        "linear_cp_odd_bias_lifts_branch_degeneracy": bias_energy_split == -2 * bias * vev,
        "deliberate_unique_orientation_claim_fails": len({str(energy) + str(curvature_value) for energy, curvature_value in zip(energies[1:], curvatures[1:])}) == 1 and drifts[0] != drifts[1],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP281",
        "theorem_domain": "one real CP-odd dynamical field a with CP-even quartic source potential",
        "source_potential": "lambda*(a^2-v^2)^2/4",
        "stationary_points": [str(point) for point in stationary_points],
        "curvatures": [str(value) for value in curvatures],
        "energies": [str(value) for value in energies],
        "vacuum_drift_tower_determinants": [str(value) for value in tower_determinants],
        "cp_odd_bias_energy_split_on_unperturbed_vacua": str(bias_energy_split),
        "contextual_partition": "the CP-even source action selects the unordered pair of nonzero orientation vacua; signed readout separates the two branches but does not explain which one is prepared",
        "classification": "conditional source-generated orientation magnitude with two CP-conjugate branches; it repairs WP280's self-reading drift coefficient but is neither a unique signed selector nor a complete preparation instrument",
        "first_nonfaithful_arrow": "CP-symmetric vacuum pair -> uniquely prepared orientation branch",
        "smallest_exact_falsifier": "a=+v and a=-v have equal energy and curvature but generate opposite full-rank drift orientations",
        "remaining_physical_instrument_gate": "derive branch selection through a CP-odd bias, cosmological/domain history, boundary condition, or superselection mechanism, and derive v, kinetic normalization, coupling to flavor, noise, walls, and stabilization",
        "scope_limit": "the packet does not exclude spontaneous branch selection in a declared history; it denies a unique signed prediction from the CP-even local action alone",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp281_cp_odd_orientation_vacuum.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
