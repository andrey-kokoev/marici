"""Exact WP567 source-score through calibrated detector-channel theorem."""

import json
from pathlib import Path

import sympy as sp


p = sp.Matrix([sp.Rational(1, 2), sp.Rational(1, 2)])
s = sp.Matrix([1, -1])
source_tangent = sp.diag(*p) * s

channels = {
    "keep": sp.eye(2),
    "noisy": sp.Matrix(
        [
            [sp.Rational(3, 4), sp.Rational(1, 4)],
            [sp.Rational(1, 4), sp.Rational(3, 4)],
        ]
    ),
    "erase": sp.Matrix(
        [
            [sp.Rational(1, 2), sp.Rational(1, 2)],
            [sp.Rational(1, 2), sp.Rational(1, 2)],
        ]
    ),
}


def audit_channel(channel):
    q = sp.simplify(channel * p)
    q_dot = sp.simplify(channel * source_tangent)
    detector_score = sp.Matrix(
        [sp.simplify(q_dot[index] / q[index]) for index in range(q.rows)]
    )
    fisher = sp.simplify(
        sum(q_dot[index] ** 2 / q[index] for index in range(q.rows))
    )
    return {
        "column_sums": [sp.simplify(sum(channel[:, index])) for index in range(channel.cols)],
        "baseline": q,
        "tangent": q_dot,
        "score": detector_score,
        "fisher": fisher,
    }


audits = {name: audit_channel(channel) for name, channel in channels.items()}
source_fisher = sp.simplify(sum(p[index] * s[index] ** 2 for index in range(p.rows)))

checks = {
    "source_score_is_centered": sp.simplify((p.T * s)[0]) == 0,
    "all_detector_channels_are_column_stochastic": all(
        audit["column_sums"] == [1, 1] for audit in audits.values()
    ),
    "all_channels_have_same_nominal_detector_distribution": len(
        {tuple(audit["baseline"]) for audit in audits.values()}
    ) == 1,
    "keep_channel_preserves_full_fisher_information": audits["keep"]["fisher"] == source_fisher == 1,
    "noisy_channel_retains_one_quarter_information": audits["noisy"]["fisher"] == sp.Rational(1, 4),
    "erase_channel_kills_source_tangent": audits["erase"]["tangent"] == sp.zeros(2, 1),
    "erase_channel_has_zero_fisher_information": audits["erase"]["fisher"] == 0,
    "data_processing_holds_for_all_channels": all(
        sp.simplify(source_fisher - audit["fisher"]) >= 0 for audit in audits.values()
    ),
    "positive_fisher_matches_nonzero_transported_tangent": all(
        (audit["fisher"] > 0) == (audit["tangent"] != sp.zeros(2, 1))
        for audit in audits.values()
    ),
}
checks = {name: bool(value) for name, value in checks.items()}


def encode_matrix(matrix):
    return [[str(matrix[row, col]) for col in range(matrix.cols)] for row in range(matrix.rows)]


result = {
    "work_package": "WP567",
    "classification": "source-derived score plus independently calibrated detector channel is a preregisterable separator constructor, not a selector",
    "source": {
        "baseline": encode_matrix(p),
        "score": encode_matrix(s),
        "tangent": encode_matrix(source_tangent),
        "fisher": str(source_fisher),
    },
    "channels": {
        name: {
            "matrix": encode_matrix(channels[name]),
            "baseline": encode_matrix(audit["baseline"]),
            "tangent": encode_matrix(audit["tangent"]),
            "detector_score": encode_matrix(audit["score"]),
            "fisher": str(audit["fisher"]),
        }
        for name, audit in audits.items()
    },
    "faithfulness_criterion": "K diag(p0) s is nonzero, equivalently detector directional Fisher information is positive",
    "smallest_exact_falsifier": "keep and erase channels have identical nominal detector distributions but directional Fisher information 1 and 0",
    "contextual_partition": "a calibrated channel separates source points only modulo the kernel of its conditional-expectation map",
    "weak_basis_descent": "passes because the entrance score is taken along an invariant physical16 path and the exit is an event probability",
    "remaining_gate": "an independently calibrated publication-bound portal-score detector channel with null outcomes, covariance, nuisance response, and uncertainty resolution",
    "checks": checks,
    "passed": all(checks.values()),
}

out = Path(__file__).resolve().parents[1] / "results" / "wp567_four_point_score_channel_constructor.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
