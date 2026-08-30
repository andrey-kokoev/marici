"""WP255: exact leave-one-out closure audit for linear mass transport."""

import json
from pathlib import Path

from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[1]
GRID = json.loads((ROOT / "data/cms-mu-tau-signal-grid/provenance.json").read_text())

def main():
    response = GRID["response"]
    counts = {m: Matrix(response[m]["raw_hist"]) for m in ["130", "140", "160"]}
    totals = {m: sum(counts[m]) for m in counts}
    shapes = {m: counts[m] / totals[m] for m in counts}
    predicted = Rational(2, 3) * shapes["130"] + Rational(1, 3) * shapes["160"]
    residual = shapes["140"] - predicted
    tv = sum(abs(x) for x in residual) / 2
    i = 3  # preregistered 110--140 GeV bin, also the maximum observed residual
    a, b, c = shapes["130"][i], shapes["140"][i], shapes["160"][i]
    variance = b * (1 - b) / totals["140"] + Rational(4, 9) * a * (1 - a) / totals["130"] + Rational(1, 9) * c * (1 - c) / totals["160"]
    z_squared = residual[i] ** 2 / variance
    checks = {
        "normalized_shapes": all(sum(shapes[m]) == 1 for m in shapes),
        "linear_prediction_normalized": sum(predicted) == 1,
        "exact_linear_closure_fails": any(x != 0 for x in residual),
        "tv_obstruction_positive": tv > 0,
        "central_bin_residual_nonzero": residual[i] != 0,
        "finite_count_standardized_residual_nonzero": z_squared > 0,
        "deliberate_zero_residual_claim_fails": sum(x ** 2 for x in residual) != 0,
    }
    checks = {k: bool(v) for k, v in checks.items()}
    result = {
        "work_package": "WP255",
        "normalized_shapes_exact": {m: [str(x) for x in shapes[m]] for m in shapes},
        "linear_140_prediction_exact": [str(x) for x in predicted],
        "residual_exact": [str(x) for x in residual],
        "total_variation_exact": str(tv), "total_variation_decimal": float(tv),
        "largest_bin": "110--140 GeV", "largest_bin_residual_decimal": float(residual[i]),
        "diagnostic_z_squared_exact": str(z_squared), "diagnostic_z_decimal_signed": -float(z_squared ** Rational(1, 2)),
        "classification": "finite-pilot leave-one-out test rejects exact linear transport of normalized visible-mass shapes",
        "smallest_exact_falsifier": "any one of the recorded nonzero bin residuals",
        "remaining_instrument_gate": "derive and validate a source-authorized response transport or simulate the actual pole masses directly; include weighted completion and correlated uncertainties",
        "checks": checks, "passed": all(checks.values()),
    }
    (ROOT / "results/wp255_signal_shape_transport_closure.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]: raise SystemExit(1)

if __name__ == "__main__": main()
