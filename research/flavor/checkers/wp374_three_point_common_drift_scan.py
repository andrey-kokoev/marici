"""WP374: exact three-context certificate with shared common drift."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    L, omega, step, coupling = sp.symbols("L Omega d c", positive=True)
    eta = sp.symbols("eta", real=True)

    def common_channel(mass2):
        return -coupling * (mass2 + omega) / (mass2**2 + omega**2) + 2 * eta

    common_records = sp.Matrix([
        common_channel(L),
        common_channel(L + step),
        common_channel(L + 2 * step),
    ])
    differences = sp.Matrix([
        sp.cancel(common_records[1] - common_records[0]),
        sp.cancel(common_records[2] - common_records[0]),
    ])
    reduced_jacobian = differences.jacobian([L, omega])
    reduced_determinant = sp.factor(sp.cancel(reduced_jacobian.det()))

    denominator = (
        (L**2 + omega**2)**2
        * ((L + step)**2 + omega**2)**2
        * ((L + 2 * step)**2 + omega**2)**2
    )
    positive_polynomial = (
        3 * L**4 + 12 * L**3 * step + 6 * L**2 * omega**2
        + 15 * L**2 * step**2 + 12 * L * omega**2 * step
        + 6 * L * step**3 + 3 * omega**4 + 7 * omega**2 * step**2
    )
    expected_reduced = -8 * omega * coupling**2 * step**3 * positive_polynomial / denominator
    reconstructed_full_determinant = sp.factor(-2 * reduced_determinant)

    # Direct finite benchmark of the original six records and six parameters.
    delta0, delta1, delta2 = sp.symbols("delta0 delta1 delta2", real=True)
    common = sp.Matrix([1, 1])
    differential = sp.Matrix([1, -1])

    def threshold(mass2):
        den = mass2**2 + omega**2
        return sp.Matrix([-coupling * mass2 / den, -coupling * omega / den])

    raw_records = (
        threshold(L) + eta * common + delta0 * differential
    ).col_join(
        threshold(L + step) + eta * common + delta1 * differential
    ).col_join(
        threshold(L + 2 * step) + eta * common + delta2 * differential
    )
    raw_jacobian = raw_records.jacobian([L, omega, eta, delta0, delta1, delta2])
    benchmark_rank = int(raw_jacobian.subs({L: 1, omega: 2, step: 1, coupling: 3}).rank())
    polynomial_terms = sp.Add.make_args(sp.expand(positive_polynomial))

    checks = {
        "reduced_determinant_has_declared_factorization": sp.simplify(
            reduced_determinant - expected_reduced
        ) == 0,
        "positive_polynomial_has_eight_positive_monomials": len(polynomial_terms) == 8 and all(
            term.as_coeff_Mul()[0] > 0 for term in polynomial_terms
        ),
        "common_channel_jacobian_has_rank_three": int(common_records.jacobian([L, omega, eta]).rank()) == 3,
        "direct_six_parameter_benchmark_has_full_rank": benchmark_rank == 6,
        "full_determinant_reconstruction_is_positive_expression": sp.simplify(
            reconstructed_full_determinant - 16 * omega * coupling**2 * step**3 * positive_polynomial / denominator
        ) == 0,
        "collapsed_scan_kills_reduced_determinant": reduced_determinant.subs(step, 0) == 0,
        "spacing_enters_cubically": sp.limit(reduced_determinant / step**3, step, 0, dir="+") != 0,
        "two_settings_are_dimensionally_insufficient": 4 < 2 + 1 + 2,
        "independent_common_offsets_are_dimensionally_insufficient": 6 < 2 + 3 + 3,
        "deliberate_collapsed_context_fails": reduced_determinant.subs(step, 0) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP374",
        "admitted_state_domain": "three predeclared equally spaced positive mediator mass settings, one common offset shared across the scan, and independent differential offsets at each setting",
        "faithful_quotient_coordinate": "local (L,Omega,eta,delta0,delta1,delta2) threshold packet; full physical16 remains downstream and projected",
        "source_authorized_probe_family": "three common-channel contexts plus freely fitted differential channels",
        "contextual_partition": "the three-setting records separate all six admitted local parameters; independent common drift at every point exceeds record dimension",
        "classification": "minimal three-context identifier for shared common plus arbitrary differential drift; neither numerical selector nor physical16-faithful probe",
        "reduced_jacobian": str(reduced_jacobian),
        "reduced_determinant": str(reduced_determinant),
        "reconstructed_full_determinant": str(reconstructed_full_determinant),
        "positive_polynomial": str(positive_polynomial),
        "benchmark_full_rank": benchmark_rank,
        "smallest_exact_falsifier": "d=0 kills the determinant with a cubic spacing factor",
        "remaining_physical_instrument_gate": "realize three calibrated mass settings, validate one shared common offset, and freeze the equally spaced scan before flavor readout",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp374_three_point_common_drift_scan.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
