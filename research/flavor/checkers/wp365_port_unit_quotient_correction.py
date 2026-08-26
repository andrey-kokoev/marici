"""WP365: exact quotient audit under independent relational-port unit changes."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    a, b, scale, alpha = sp.symbols("a b s alpha", positive=True)
    A, D = sp.symbols("A D", positive=True)
    S = sp.diag(a, b)
    exchange = sp.Matrix([[0, scale], [1 / scale, 0]])
    K = sp.Matrix([[1, -alpha], [-alpha, alpha**2]])
    gram = sp.diag(A, D)

    transformed_exchange = sp.simplify(S * exchange * S.inv())
    transformed_scale = a * scale / b
    transformed_alpha = a * alpha / b
    transformed_K = sp.simplify(S.inv().T * K * S.inv())
    canonical_transformed_K = sp.Matrix([
        [1, -transformed_alpha],
        [-transformed_alpha, transformed_alpha**2],
    ]) / a**2
    transformed_gram = sp.simplify(S.inv().T * gram * S.inv())
    transformed_norm_ratio = sp.simplify(
        sp.sqrt(transformed_gram[1, 1] / transformed_gram[0, 0])
    )

    unit_exchange = exchange.subs(scale, 1)
    unit_K = K.subs(alpha, 1)
    unit_gram = sp.eye(2)
    hostile_units = {a: 2, b: 1}

    checks = {
        "exchange_conjugates_to_scaled_exchange": transformed_exchange == sp.Matrix([
            [0, transformed_scale], [1 / transformed_scale, 0]
        ]),
        "portal_quadratic_form_transforms_covariantly": transformed_K == canonical_transformed_K,
        "alpha_over_scale_is_unit_invariant": sp.simplify(transformed_alpha / transformed_scale - alpha / scale) == 0,
        "gram_transforms_covariantly": transformed_gram == sp.diag(A / a**2, D / b**2),
        "metric_norm_ratio_scales_like_exchange": transformed_norm_ratio == a * sp.sqrt(D / A) / b,
        "ward_relation_is_preserved": sp.simplify(
            (transformed_alpha - transformed_scale).subs(alpha, scale)
        ) == 0,
        "hostile_unit_change_moves_unit_exchange_to_scale_two": (
            (S * unit_exchange * S.inv()).subs(hostile_units) == sp.Matrix([[0, 2], [sp.Rational(1, 2), 0]])
        ),
        "hostile_unit_change_moves_alpha_one_to_two": transformed_alpha.subs({**hostile_units, alpha: 1}) == 2,
        "hostile_unit_change_moves_euclidean_metric": (
            (S.inv().T * unit_gram * S.inv()).subs(hostile_units) == sp.diag(sp.Rational(1, 4), 1)
        ),
        "deliberate_absolute_unit_claim_fails_descent": transformed_scale.subs({**hostile_units, scale: 1}) != 1,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP365",
        "admitted_state_domain": "positive independent unit changes x'=a*x and y'=b*y on the relational ports x=J^2 and y=Q/M2",
        "faithful_quotient_coordinate": "the port-unit quotient coordinate alpha/s together with covariant metric data; full physical16 remains nonfaithfully projected to J^2",
        "source_authorized_probe_family": "scaled exchange, portal quadratic form, and Gram pairing transported covariantly under independent port-unit changes",
        "contextual_partition": "presentations related by positive diagonal unit changes are equivalent; s, alpha, and equal-coordinate-norm statements vary, while alpha/s is invariant",
        "classification": "relational Ward selector of alpha/s=1 and presentation rigidifier after a unit choice; not an absolute numerical selector",
        "unit_change": str(S),
        "transformed_exchange": str(transformed_exchange),
        "transformed_alpha": str(transformed_alpha),
        "invariant_ratio": str(sp.simplify(transformed_alpha / transformed_scale)),
        "transformed_gram": str(transformed_gram),
        "hostile_pair": {
            "original": {"s": 1, "alpha": 1, "G": [[1, 0], [0, 1]]},
            "reparameterized": {"a": 2, "b": 1, "s": 2, "alpha": 2, "G": [["1/4", 0], [0, 1]]},
            "common_invariant": "alpha/s=1",
        },
        "smallest_exact_falsifier": "the (a,b)=(2,1) unit change maps the equivalent unit presentation from (s,alpha)=(1,1) to (2,2)",
        "remaining_physical_instrument_gate": "derive and realize a common-unit calibration map before flavor readout; otherwise only alpha/s=1 has quotient authority",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp365_port_unit_quotient_correction.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
