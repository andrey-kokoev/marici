"""WP373: exact two-context robustness to independent differential drift."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    L, omega, step, coupling = sp.symbols("L Omega d c", positive=True)
    delta0, delta1, eta0, eta1 = sp.symbols("delta0 delta1 eta0 eta1", real=True)
    gamma = sp.symbols("gamma", real=True)

    def threshold(mass2):
        denominator = mass2**2 + omega**2
        return sp.Matrix([
            -coupling * mass2 / denominator,
            -coupling * omega / denominator,
        ])

    common = sp.Matrix([1, 1])
    differential = sp.Matrix([1, -1])
    record0 = threshold(L) + delta0 * differential
    record1 = threshold(L + step) + delta1 * differential
    stacked = record0.col_join(record1)
    drift_jacobian = stacked.jacobian([L, omega, delta0, delta1])
    drift_determinant = sp.factor(drift_jacobian.det())
    expected_determinant = (
        4 * omega * coupling**2 * step * (L**2 + L * step + omega**2)
        / ((L**2 + omega**2)**2 * ((L + step)**2 + omega**2)**2)
    )

    confusion = sp.Matrix([
        [(1 + gamma) / 2, (1 - gamma) / 2],
        [(1 - gamma) / 2, (1 + gamma) / 2],
    ])
    confused0 = confusion * threshold(L) + delta0 * differential
    confused1 = confusion * threshold(L + step) + delta1 * differential
    confused_jacobian = confused0.col_join(confused1).jacobian([L, omega, delta0, delta1])
    confused_determinant = sp.factor(confused_jacobian.det())

    arbitrary_background_stack = (
        threshold(L) + delta0 * differential + eta0 * common
    ).col_join(
        threshold(L + step) + delta1 * differential + eta1 * common
    )
    arbitrary_background_jacobian = arbitrary_background_stack.jacobian(
        [L, omega, delta0, delta1, eta0, eta1]
    )
    arbitrary_rank = int(arbitrary_background_jacobian.rank())

    checks = {
        "independent_differential_drift_determinant_exact": sp.simplify(
            drift_determinant - expected_determinant
        ) == 0,
        "independent_differential_drift_has_full_rank": int(drift_jacobian.rank()) == 4,
        "detector_confusion_leaves_determinant_unchanged": sp.simplify(
            confused_determinant - drift_determinant
        ) == 0,
        "zero_contrast_still_has_rank_four_across_contexts": int(confused_jacobian.subs(gamma, 0).rank()) == 4,
        "collapsed_scan_kills_determinant": drift_determinant.subs(step, 0) == 0,
        "arbitrary_two_component_drift_saturates_record_rank": arbitrary_rank == 4,
        "arbitrary_two_component_drift_leaves_kernel_two": 6 - arbitrary_rank == 2,
        "deliberate_full_background_identification_fails": arbitrary_rank < 6,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP373",
        "admitted_state_domain": "two distinct positive mass settings with independent post-detector differential backgrounds; detector contrast may include zero for the cross-context rank theorem",
        "faithful_quotient_coordinate": "local pole coordinates (L,Omega) together with two differential nuisances; individual threshold-channel pairs are not reconstructed at zero contrast",
        "source_authorized_probe_family": "two source-controlled common-channel contexts with independent differential offsets",
        "contextual_partition": "distinct contexts separate (L,Omega,delta0,delta1); adding independent common offsets at both settings creates a two-dimensional kernel",
        "classification": "cross-context pole identifier robust to differential drift and even complete channel confusion; neither threshold-channel reconstruction nor flavor selection",
        "drift_jacobian_determinant": str(drift_determinant),
        "confused_jacobian_determinant": str(confused_determinant),
        "arbitrary_background_rank": arbitrary_rank,
        "arbitrary_background_kernel_dimension": 6 - arbitrary_rank,
        "smallest_exact_falsifier": "d=0 kills the scan determinant; allowing independent common and differential offsets at both points leaves a two-dimensional kernel",
        "remaining_physical_instrument_gate": "calibrate or constrain common-mode drift across the two predeclared mass settings and validate that the pole model is shared across contexts",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp373_two_point_background_drift_robustness.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
