"""WP364: exact invariant-positive-metric attack on exchange normalization."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    scale, A, D = sp.symbols("s A D", positive=True)
    B = sp.symbols("B", real=True)
    exchange = sp.Matrix([[0, scale], [1 / scale, 0]])
    gram = sp.Matrix([[A, B], [B, D]])
    residual = sp.simplify(exchange.T * gram * exchange - gram)
    invariant_D = A * scale**2
    invariant_gram = gram.subs(D, invariant_D)
    invariant_determinant = sp.factor(invariant_gram.det())

    hostile_exchange = exchange.subs(scale, 2)
    hostile_gram = sp.diag(1, 4)
    determinant_one_gram = sp.diag(1 / scale, scale)

    equal_norm_residual = sp.factor((invariant_D - A))
    equal_norm_roots = sp.solve(equal_norm_residual, scale)
    positive_equal_norm_roots = [root for root in equal_norm_roots if root.is_positive]

    checks = {
        "isometry_residual_has_declared_form": residual == sp.Matrix([
            [-A + D / scale**2, 0], [0, A * scale**2 - D]
        ]),
        "general_invariant_metric_has_D_equal_A_s_squared": (
            sp.simplify(residual.subs(D, invariant_D)) == sp.zeros(2)
        ),
        "invariant_metric_determinant_retains_open_positive_domain": sp.expand(invariant_determinant - (A**2 * scale**2 - B**2)) == 0,
        "hostile_scale_two_metric_is_positive": hostile_gram[0, 0] > 0 and hostile_gram.det() > 0,
        "hostile_scale_two_metric_is_invariant": hostile_exchange.T * hostile_gram * hostile_exchange == hostile_gram,
        "determinant_one_family_is_invariant": sp.simplify(exchange.T * determinant_one_gram * exchange - determinant_one_gram) == sp.zeros(2),
        "determinant_one_family_has_unit_determinant": determinant_one_gram.det() == 1,
        "equal_port_norms_force_unit_positive_scale": positive_equal_norm_roots == [sp.Integer(1)],
        "deliberate_euclidean_claim_fails_for_scale_two": hostile_exchange.T * sp.eye(2) * hostile_exchange != sp.eye(2),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP364",
        "admitted_state_domain": "positive scaled exchanges P_s and arbitrary symmetric positive-definite two-port Gram metrics G",
        "faithful_quotient_coordinate": "the relational two-port state together with its Gram metric; full physical16 remains projected to J^2",
        "source_authorized_probe_family": "exchange involution and Gram-isometry tests, with equal port norm treated as a separate proposed source condition",
        "contextual_partition": "for every s>0 there is a family D=A*s^2 and |B|<A*s of invariant positive metrics; s is the port norm ratio rather than a selected constant",
        "classification": "positive pairing rigidifies scale relative to its norm data but does not numerically select unit scale; equal-norm source structure is additionally required",
        "general_residual": str(residual),
        "invariant_metric": str(invariant_gram),
        "invariant_determinant": str(invariant_determinant),
        "scale_from_norm_ratio": "sqrt(D/A)",
        "hostile_pair": {"s": 2, "G": [[1, 0], [0, 4]], "determinant": 4},
        "smallest_exact_falsifier": "P_2 preserves the positive metric diag(1,4), so existence of an invariant positive pairing does not imply s=1",
        "remaining_physical_instrument_gate": "derive equal flavor/source port norms in a common source representation and realize their Gram pairing experimentally; post-readout orthonormalization is only presentation rigidification",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp364_positive_pairing_scale_kernel.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
