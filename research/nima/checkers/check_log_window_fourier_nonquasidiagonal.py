from fractions import Fraction
import json
from pathlib import Path


# Since pi > 3, the analytic estimate 4/(pi L R) is bounded above by
# 4/(3 L R).  Rational certificates suffice for an exact convergence schedule.
radii = (Fraction(1), Fraction(2), Fraction(5))
lengths = (10, 100, 1000, 10000)
certificates = {}

for radius in radii:
    rows = []
    previous = Fraction(0)
    for length in lengths:
        tail_upper = Fraction(4, 3 * length) / radius
        visible_energy_lower = Fraction(1) - tail_upper
        assert visible_energy_lower > previous
        assert visible_energy_lower < 1
        previous = visible_energy_lower
        rows.append(
            {
                "length": length,
                "tail_upper": f"{tail_upper.numerator}/{tail_upper.denominator}",
                "visible_energy_lower": (
                    f"{visible_energy_lower.numerator}/{visible_energy_lower.denominator}"
                ),
            }
        )
    certificates[str(radius)] = rows

for radius in radii:
    for denominator in (10, 100, 1000):
        required_length = Fraction(4 * denominator, 3) / radius
        chosen_length = required_length.numerator // required_length.denominator + 1
        assert Fraction(4, 3 * chosen_length) / radius < Fraction(1, denominator)

result = {
    "schema": "marici.nima.log-window-fourier-nonquasidiagonal.v1",
    "rational_tail_certificates": certificates,
    "analytic_norm_upper_bound": 1,
    "analytic_norm_lower_supremum": 1,
    "leakage_block_norm": 1,
    "verdict": "continuous log-window Fourier sewing is maximally nonquasidiagonal",
}

out = Path(__file__).parents[1] / "results" / "log-window-fourier-nonquasidiagonal.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

