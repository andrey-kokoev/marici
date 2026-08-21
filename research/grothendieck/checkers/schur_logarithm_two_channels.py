"""Exact finite trace audit of the first two Schur-logarithm channels."""

from fractions import Fraction as F


eigenvalues = [F(1, 2), F(1, 3), F(1, 5)]
trace_one = sum(eigenvalues)
trace_two = sum(x * x for x in eigenvalues)
linear_channel = trace_one
quadratic_channel = trace_two / 2

assert linear_channel == F(31, 30)
assert quadratic_channel == F(361, 1800)

result = {
    "trace_X": str(trace_one),
    "one_half_trace_X_squared": str(quadratic_channel),
    "linear_coefficient": "1",
    "quadratic_coefficient": "1/2",
    "coefficients_forced_by_single_log_determinant": True,
    "critical_schatten_threshold": "only n=1,2 require relative renormalization for X in S3",
}

if __name__ == "__main__":
    import json
    from pathlib import Path

    output = Path(__file__).parents[1] / "results" / "schur-logarithm-two-channels.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for key, value in result.items():
        print(f"{key}={value}")

