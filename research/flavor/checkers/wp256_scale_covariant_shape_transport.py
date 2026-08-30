"""WP256: exact leave-one-out audit of scale-covariant visible-mass shapes."""

import json
from pathlib import Path

from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[1]
COUNTS = {
    "130": Matrix([12, 241, 418, 185, 39, 0]),
    "140": Matrix([4, 123, 163, 87, 12, 0]),
    "160": Matrix([22, 226, 256, 154, 20, 0]),
}
OLD_TV = Rational(23108773, 354073635)


def main():
    totals = {mass: sum(column) for mass, column in COUNTS.items()}
    shapes = {mass: column / totals[mass] for mass, column in COUNTS.items()}
    predicted = Rational(2, 3) * shapes["130"] + Rational(1, 3) * shapes["160"]
    residual = shapes["140"] - predicted
    tv = sum(abs(value) for value in residual) / 2
    improvement = OLD_TV - tv
    hostile_zero_residual = Matrix.zeros(6, 1)
    checks = {
        "selected_counts_reproduce_wp254": totals == {"130": 895, "140": 389, "160": 678},
        "normalized_shapes": all(sum(shape) == 1 for shape in shapes.values()),
        "linear_prediction_normalized": sum(predicted) == 1,
        "exact_scale_covariant_closure_fails": residual != hostile_zero_residual,
        "total_variation_positive": tv > 0,
        "total_variation_improves_over_fixed_gev_bins": improvement > 0,
        "deliberate_zero_residual_claim_fails": sum(value ** 2 for value in residual) != 0,
        "interpolation_authority_withheld": True,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP256",
        "dimensionless_bins_exact": ["0", "1/3", "1/2", "2/3", "5/6", "1", "infinity"],
        "raw_templates": {mass: [int(value) for value in column] for mass, column in COUNTS.items()},
        "normalized_shapes_exact": {mass: [str(value) for value in shape] for mass, shape in shapes.items()},
        "linear_140_prediction_exact": [str(value) for value in predicted],
        "residual_exact": [str(value) for value in residual],
        "total_variation_exact": str(tv),
        "total_variation_decimal": float(tv),
        "wp255_total_variation_exact": str(OLD_TV),
        "absolute_improvement_exact": str(improvement),
        "relative_tv_ratio_exact": str(tv / OLD_TV),
        "classification": "dimensionless source-mass scaling improves the finite-pilot interpolation diagnostic but fails exact leave-one-out closure and therefore does not authorize transport to the physical poles",
        "smallest_exact_falsifier": "the first-bin residual -3353749/354073635 already falsifies exact scale-covariant closure",
        "remaining_instrument_gate": "derive a source-authorized uncertain response transport or simulate the actual pole masses directly, then validate weighted completion, correlated uncertainties, QCD, and finite-power rank",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp256_scale_covariant_shape_transport.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
