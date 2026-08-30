"""WP372: exact rank certificate for a two-point threshold scan with nuisance."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    L, omega, step, coupling = sp.symbols("L Omega d c", positive=True)
    nuisance = sp.symbols("delta", real=True)
    gamma = sp.symbols("gamma", positive=True)

    def threshold(mass2):
        denominator = mass2**2 + omega**2
        return sp.Matrix([
            -coupling * mass2 / denominator,
            -coupling * omega / denominator,
        ])

    differential = sp.Matrix([1, -1])
    stacked_record = (
        threshold(L).col_join(threshold(L + step))
        + nuisance * differential.col_join(differential)
    )
    stacked_jacobian = stacked_record.jacobian([L, omega, nuisance])
    certified_minor = sp.factor(stacked_jacobian[[0, 1, 2], :].det())
    denominator = (L**2 + omega**2)**2 * ((L + step)**2 + omega**2)**2
    positive_polynomial = (
        2 * L**3 + 2 * L**2 * omega + 5 * L**2 * step
        + 2 * L * omega**2 + 2 * L * omega * step + 4 * L * step**2
        + 2 * omega**3 + 3 * omega**2 * step + step**3
    )
    expected_minor = -coupling**2 * step * positive_polynomial / denominator

    confusion = sp.Matrix([
        [(1 + gamma) / 2, (1 - gamma) / 2],
        [(1 - gamma) / 2, (1 + gamma) / 2],
    ])
    block_confusion = sp.diag(1, 1, 1, 1)
    block_confusion[:2, :2] = confusion
    block_confusion[2:, 2:] = confusion
    transformed_signal_rank = int((block_confusion * stacked_jacobian).rank())
    collapsed_rank = int(stacked_jacobian.subs(step, 0).rank())

    polynomial_terms = sp.Add.make_args(sp.expand(positive_polynomial))
    checks = {
        "certified_minor_has_declared_factorization": sp.simplify(certified_minor - expected_minor) == 0,
        "positive_polynomial_has_nine_positive_monomials": len(polynomial_terms) == 9 and all(
            term.as_coeff_Mul()[0] > 0 for term in polynomial_terms
        ),
        "stacked_jacobian_has_rank_three": int(stacked_jacobian.rank()) == 3,
        "positive_contrast_detector_preserves_rank": transformed_signal_rank == 3,
        "block_detector_determinant_is_gamma_squared": block_confusion.det() == gamma**2,
        "collapsed_scan_kills_certified_minor": certified_minor.subs(step, 0) == 0,
        "collapsed_scan_retains_only_rank_two": collapsed_rank == 2,
        "shared_nuisance_column_is_declared_differential_pair": stacked_jacobian[:, 2] == differential.col_join(differential),
        "deliberate_repeated_setting_fails_full_rank": collapsed_rank < 3,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP372",
        "admitted_state_domain": "two predeclared mediator mass-squared settings L and L+d with L,Omega,d,c>0, one fixed differential background shared across settings, and calibrated detector contrast gamma>0",
        "faithful_quotient_coordinate": "local threshold pole coordinates (L,Omega) plus the shared background nuisance delta; full physical16 remains downstream and projected",
        "source_authorized_probe_family": "two finite-width dispersive/absorptive records at source-controlled distinct mass settings with one shared nuisance",
        "contextual_partition": "the two-point stack separates all local (L,Omega,delta) perturbations; repeated identical settings retain the one-dimensional kernel",
        "classification": "source-supported rank-three threshold identification instrument; neither numerical selector nor physical16-faithful probe",
        "stacked_jacobian": str(stacked_jacobian),
        "certified_minor": str(certified_minor),
        "positive_polynomial": str(positive_polynomial),
        "full_rank": 3,
        "collapsed_scan_rank": collapsed_rank,
        "smallest_exact_falsifier": "d=0 collapses the two settings, makes the certified minor zero, and reduces the stacked rank from three to two",
        "remaining_physical_instrument_gate": "realize and calibrate two mediator pole-mass settings, validate one shared background across them, and freeze the scan before inspecting flavor outcomes",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp372_two_point_threshold_scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
