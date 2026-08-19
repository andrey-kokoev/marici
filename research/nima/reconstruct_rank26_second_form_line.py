"""Estimate rational degrees of the moving-wall second fundamental form."""

import json
from collections import Counter
from pathlib import Path

import check_rank26_multifiber_signature as model

P = model.base.PRIME
TRAINING = 10


def powers(value, degree):
    out = [1]
    for _ in range(degree):
        out.append(out[-1] * value % P)
    return out


def evaluate(coefficients, value):
    return sum(coefficient * power for coefficient, power in zip(coefficients, powers(value, len(coefficients) - 1))) % P


def fit(values):
    training = values[:TRAINING]
    for total in range(9):
        for numerator_degree in range(total + 1):
            denominator_degree = total - numerator_degree
            unknowns = numerator_degree + denominator_degree + 2
            if unknowns > TRAINING:
                continue
            rows = []
            for t, value in training:
                rows.append(
                    powers(t, numerator_degree)
                    + [(-value * power) % P for power in powers(t, denominator_degree)]
                )
            kernel = model.nullspace(rows, unknowns)
            if len(kernel) != 1:
                continue
            candidate = kernel[0]
            numerator = candidate[: numerator_degree + 1]
            denominator = candidate[numerator_degree + 1 :]
            if not any(denominator):
                continue
            valid = True
            for t, value in values:
                den = evaluate(denominator, t)
                if not den or evaluate(numerator, t) != value * den % P:
                    valid = False
                    break
            if valid:
                return {
                    "numerator_degree": numerator_degree,
                    "denominator_degree": denominator_degree,
                    "numerator": numerator,
                    "denominator": denominator,
                }
    return None


samples, rejected = [], []
for t in range(1, 41):
    point = (2 + t, 3 + 2 * t, 7 + 4 * t)
    try:
        item = model.sample(point)
    except (StopIteration, KeyError, AssertionError) as error:
        rejected.append({"t": t, "point": list(point), "reason": type(error).__name__})
        continue
    signature = [
        item["numerator_rank"], item["augmented_rank"],
        item["second_fundamental_form_rank"], item["common_kernel_rank"],
        item["kernel_derivative_closure_rank"],
    ]
    if signature != [25, 26, 3, 22, 26]:
        rejected.append({"t": t, "point": list(point), "reason": f"signature={signature}"})
        continue
    item["t"] = t
    samples.append(item)
    print(f"sample {len(samples)}/13: t={t}, point={point}", flush=True)
    if len(samples) == 13:
        break
if len(samples) < 13:
    raise RuntimeError(f"only {len(samples)} admissible samples; rejected={rejected}")

fits = []
for axis in range(3):
    for coordinate in range(25):
        values = [(item["t"], item["second_fundamental_form_rows"][axis][coordinate]) for item in samples]
        fits.append({"axis": axis, "coordinate": coordinate, "fit": fit(values)})

successful = [item for item in fits if item["fit"] is not None]
histogram = Counter(
    (item["fit"]["numerator_degree"], item["fit"]["denominator_degree"])
    for item in successful
)
payload = {
    "schema": "marici.rank26-second-form-line-reconstruction.v1",
    "field": P,
    "line": "(X1,X2,X3)=(2+t,3+2t,7+4t)",
    "training_samples": TRAINING,
    "held_out_samples": 3,
    "sample_parameters": [item["t"] for item in samples],
    "rejected_samples": rejected,
    "common_basis": all(item["numerator_basis_labels"] == samples[0]["numerator_basis_labels"] for item in samples),
    "entry_count": len(fits),
    "successful_fit_count": len(successful),
    "degree_histogram": {f"{n}/{d}": count for (n, d), count in sorted(histogram.items())},
    "fits": fits,
    "status": "all_entries_reconstructed_and_heldout_verified" if len(successful) == len(fits) else "degree_bound_insufficient",
}
Path(__file__).with_name("rank26-second-form-line-reconstruction.json").write_text(
    json.dumps(payload, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps({key: value for key, value in payload.items() if key != "fits"}, indent=2))
