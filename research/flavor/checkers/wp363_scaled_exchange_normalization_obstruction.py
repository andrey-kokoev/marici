"""WP363: exact scaled-exchange attack on the WP362 unit Ward normalization."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    alpha, scale = sp.symbols("alpha s", positive=True)
    K = sp.Matrix([[1, -alpha], [-alpha, alpha**2]])
    exchange = sp.Matrix([[0, scale], [1 / scale, 0]])
    ward_residual = sp.simplify(exchange.T * K * exchange - K)
    involution_residual = sp.simplify(exchange**2 - sp.eye(2))
    euclidean_pairing_residual = sp.simplify(exchange.T * exchange - sp.eye(2))

    alpha_roots = sp.solve(ward_residual[0, 0], alpha)
    positive_alpha_roots = [root for root in alpha_roots if root.is_positive]
    scale_roots = sp.solve(euclidean_pairing_residual[0, 0], scale)
    positive_scale_roots = [root for root in scale_roots if root.is_positive]

    checks = {
        "scaled_exchange_is_involutive_for_all_positive_scales": involution_residual == sp.zeros(2),
        "ward_residual_has_declared_diagonal_form": ward_residual == sp.Matrix([
            [alpha**2 / scale**2 - 1, 0], [0, scale**2 - alpha**2]
        ]),
        "ward_invariance_fixes_alpha_to_scale": positive_alpha_roots == [scale],
        "scale_two_is_involutive": exchange.subs(scale, 2) ** 2 == sp.eye(2),
        "scale_two_selects_alpha_two": ward_residual.subs({scale: 2, alpha: 2}) == sp.zeros(2),
        "scale_two_rejects_alpha_one": ward_residual.subs({scale: 2, alpha: 1}) != sp.zeros(2),
        "euclidean_pairing_fixes_unit_positive_scale": positive_scale_roots == [sp.Integer(1)],
        "unit_scale_preserves_euclidean_pairing": euclidean_pairing_residual.subs(scale, 1) == sp.zeros(2),
        "deliberate_nonunit_pairing_residual_is_detected": euclidean_pairing_residual.subs(scale, 2) != sp.zeros(2),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP363",
        "admitted_state_domain": "positive scaled involutions P_s on the relational ports (J^2,Q/M2), with no common port metric assumed initially",
        "faithful_quotient_coordinate": "the relational two-port experiment modulo its scale-dependent stabilizer groupoid; full physical16 remains downstream and nonfaithfully projected to J^2",
        "source_authorized_probe_family": "scaled exchange Ward tests; a Euclidean two-port Gram pairing is tested separately as additional source structure",
        "contextual_partition": "each positive scale s defines an involutive exchange and fixes alpha=s; only an independently authorized common positive pairing selects s=1",
        "classification": "exchange rigidifier of alpha relative to port calibration, not an absolute numerical selector; unit selection is conditional on a new source-defined pairing",
        "scaled_exchange": str(exchange),
        "involution_residual": str(involution_residual),
        "ward_residual": str(ward_residual),
        "positive_alpha_solution": [str(root) for root in positive_alpha_roots],
        "euclidean_pairing_residual": str(euclidean_pairing_residual),
        "positive_pairing_scale_solution": [str(root) for root in positive_scale_roots],
        "smallest_exact_falsifier": "P_2^2=I but Ward invariance selects alpha=2, so involutive exchange alone does not imply unit normalization",
        "remaining_physical_instrument_gate": "derive a common positive Gram metric for the two ports before readout, or treat measured detector scale s as calibration and withdraw numerical-selector authority",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp363_scaled_exchange_normalization_obstruction.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
