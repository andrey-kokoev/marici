#!/usr/bin/env python3
"""Exact audit separating positive survival from faithful observability."""

import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational, simplify


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/positivity-survival-vs-faithfulness.json"


def main():
    e1 = Matrix([1, 0])
    e2 = Matrix([0, 1])

    # Maximally projectively mixing replacer: positive survival, no faithfulness.
    replacer = Matrix([[1, 1], [1, 1]])
    assert replacer * e1 == replacer * e2 == Matrix([1, 1])
    hidden = e1 - e2
    assert replacer * hidden == Matrix.zeros(2, 1)
    assert replacer.rank() == 1
    positive_samples = [Matrix([1, 0]), Matrix([0, 2]), Matrix([3, 4])]
    assert all(all(entry > 0 for entry in replacer * x) for x in positive_samples)

    # Constant projective cross-ratio, collapsing anchored boundary margin.
    epsilons = [Rational(1, 2), Rational(1, 4), Rational(1, 8), Rational(1, 16)]
    cross_ratios = []
    normalized_minima = []
    for eps in epsilons:
        matrix = Matrix([[1, 1], [eps, 2 * eps]])
        cross_ratio = simplify(matrix[0, 0] * matrix[1, 1] / (matrix[0, 1] * matrix[1, 0]))
        cross_ratios.append(str(cross_ratio))
        image = matrix * e1
        normalized = image / sum(image)
        normalized_minima.append(str(min(normalized)))
    assert set(cross_ratios) == {"2"}
    assert normalized_minima[-1] == "1/17"

    # Scalar attenuation leaves projective data unchanged and kills radial gain.
    base = Matrix([[2, 1], [1, 2]])
    attenuation = []
    for cutoff in [1, 2, 4, 8, 16]:
        scaled = base / cutoff
        cross_ratio = simplify(scaled[0, 0] * scaled[1, 1] / (scaled[0, 1] * scaled[1, 0]))
        column_gain = sum(scaled * e1)
        attenuation.append({"cutoff": cutoff, "cross_ratio": str(cross_ratio), "radial_gain": str(column_gain)})
    assert {item["cross_ratio"] for item in attenuation} == {"4"}
    assert attenuation[-1]["radial_gain"] == "3/16"

    # Positive diagonal conjugation preserves cross-ratio but changes raw entries.
    diagonal = Matrix.diag(10, Rational(1, 10))
    gauged = diagonal * base * diagonal.inv()
    original_ratio = simplify(base[0, 0] * base[1, 1] / (base[0, 1] * base[1, 0]))
    gauged_ratio = simplify(gauged[0, 0] * gauged[1, 1] / (gauged[0, 1] * gauged[1, 0]))
    assert original_ratio == gauged_ratio == 4
    assert min(gauged) != min(base)

    payload = {
        "schema": "marici.kitaev.positivity_survival_vs_faithfulness.v1",
        "status": "pass",
        "replacer_hostile": {
            "positivity_improving_on_nonzero_positive_samples": True,
            "rank": replacer.rank(),
            "distinct_normalized_inputs_same_output": True,
            "hidden_signed_state": [int(v) for v in hidden],
        },
        "projective_boundary_hostile": {
            "cross_ratios": cross_ratios,
            "normalized_coordinate_minima": normalized_minima,
            "bounded_projective_spread_with_boundary_escape": True,
        },
        "radial_attenuation_hostile": attenuation,
        "diagonal_gauge_hostile": {
            "cross_ratio_preserved": True,
            "raw_coordinate_margin_preserved": False,
        },
        "independent_requirements": [
            "source cone membership",
            "radial gain",
            "anchored interior margin",
            "contextual kernel separation",
        ],
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": ["theta/Tate cone", "arithmetic correspondence", "completion theorem", "RH"],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
