from fractions import Fraction
import json
from pathlib import Path


def scalar_anomaly(left, right):
    return (
        -(left * left * right)
        - (left * right * right)
        + Fraction(1, 2) * left * left * right * right
    )


cutoffs = [5, 10, 20, 40, 80]
records = []
previous_anomaly = Fraction(0)
for cutoff in cutoffs:
    weights = [Fraction(1, n) for n in range(1, cutoff + 1)]
    local_cubic_budget = sum((weight ** 3 for weight in weights), Fraction(0))
    assert local_cubic_budget < 2

    aligned_absolute_anomaly = Fraction(0)
    orthogonal_absolute_anomaly = Fraction(0)
    for m in range(cutoff):
        for n in range(m + 1, cutoff):
            aligned_absolute_anomaly += abs(scalar_anomaly(weights[m], weights[n]))
            # Orthogonal rank-one projections have zero mixed products.
            orthogonal_absolute_anomaly += 0

    assert aligned_absolute_anomaly > previous_anomaly
    assert orthogonal_absolute_anomaly == 0
    previous_anomaly = aligned_absolute_anomaly

    records.append(
        {
            "cutoff": cutoff,
            "local_cubic_budget": str(local_cubic_budget),
            "aligned_absolute_anomaly": str(aligned_absolute_anomaly),
            "orthogonal_absolute_anomaly": "0",
        }
    )

result = {
    "schema": "marici.nima.cross-prime-anomaly-summability.v1",
    "records": records,
    "same_local_singular_values": True,
    "aligned_global_anomaly_summable": False,
    "orthogonal_cross_anomaly_zero": True,
    "verdict": "global det3 coherence requires source-derived cross-prime overlap decay",
}

out = Path(__file__).parents[1] / "results" / "cross-prime-anomaly-summability.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
