"""WP280: exact signed-Jarlskog orientation repair and kernel audit."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    signed_j = sp.symbols("signed_j", real=True)
    rotation_generator = sp.Matrix([[0, 1], [-1, 0]])
    drift = signed_j * rotation_generator
    reflection = sp.diag(1, -1)

    transformed_drift = sp.simplify((-signed_j) * reflection * rotation_generator * reflection.inv())
    covariance_residual = sp.simplify(transformed_drift - drift)

    sensor = sp.Matrix([[1, 0]])
    actuator = sp.Matrix([1, 0])
    observability = sensor.col_join(sensor * drift)
    controllability = actuator.row_join(drift * actuator)
    observation_gram = sp.simplify(observability.T * observability)
    control_gram = sp.simplify(controllability * controllability.T)

    observability_at_zero = observability.subs(signed_j, 0)
    controllability_at_zero = controllability.subs(signed_j, 0)
    hostile_speeds = [drift.subs(signed_j, value) for value in (1, 2)]

    checks = {
        "pseudoscalar_drift_covariant_under_reflection": covariance_residual == sp.zeros(2),
        "observability_determinant_is_signed_j": observability.det() == signed_j,
        "controllability_determinant_is_minus_signed_j": controllability.det() == -signed_j,
        "observation_gram_determinant_is_j_squared": observation_gram.det() == signed_j**2,
        "control_gram_determinant_is_j_squared": control_gram.det() == signed_j**2,
        "tower_determinants_are_nonzero_polynomials": observability.det() != 0 and controllability.det() != 0,
        "cp_conserving_locus_reopens_both_kernels": observability_at_zero.rank() == 1 and controllability_at_zero.rank() == 1,
        "different_nonzero_j_values_change_drift_speed": hostile_speeds[1] == 2 * hostile_speeds[0],
        "descent_does_not_fix_clock_normalization": hostile_speeds[0] != hostile_speeds[1],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP280",
        "theorem_domain": "nondegenerate physical16 deviation slice carrying the signed Jarlskog pseudoscalar J",
        "candidate_drift": "A=J*[[0,1],[-1,0]]",
        "reflection_rule": "J -> -J and orientation generator -> -orientation generator",
        "observability_tower": [[str(value) for value in observability.row(i)] for i in range(2)],
        "controllability_tower": [[str(value) for value in controllability.row(i)] for i in range(2)],
        "observation_gram_determinant": str(observation_gram.det()),
        "control_gram_determinant": str(control_gram.det()),
        "cp_conserving_ranks": {"observability": int(observability_at_zero.rank()), "controllability": int(controllability_at_zero.rank())},
        "contextual_partition": "for J nonzero the dynamic towers separate and reach the two-dimensional slice; at J=0 both collapse to rank one, with conditioning controlled by |J|",
        "classification": "signed J repairs orientation descent and gives generic formal dynamic closure, but using a measured physical16 coordinate as a drift coefficient is a self-reading law, not yet a source-generated selector or instrument",
        "first_nonfaithful_arrow": "quotient-available signed J readout -> dynamical coefficient that physically drives flavor",
        "smallest_exact_falsifier": "J=0 makes both tower determinants vanish; J=1 and J=2 both descend but generate different drift speeds",
        "remaining_physical_instrument_gate": "derive a CP-odd dynamical field or source coupling whose vacuum value produces the orientation and clock normalization, then establish behavior near J=0, noise margin, sensor, actuator, and stabilization",
        "scope_limit": "the packet proves covariance and generic rank only; it does not authorize feedback from a measured J value into Standard Model Yukawa parameters",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp280_jarlskog_oriented_drift.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
