from fractions import Fraction
import json
from pathlib import Path


# Hostile A: bounded rank-one trace norm, but the eigenvalue approaches -1.
hostile_a = []
for n in (2, 4, 8, 16, 32, 64):
    k = -Fraction(n - 1, n)
    hostile_a.append({
        "n": n,
        "trace_norm": str(abs(k)),
        "determinant": str(1 + k),
        "inverse_norm": str(Fraction(1, 1 + k)),
    })
assert hostile_a[-1]["determinant"] == "1/64"

# Hostile B: a fixed safe eigenvalue repeated with growing rank. The inverse
# gap is uniform, but the determinant still collapses because trace mass grows.
hostile_b = []
for rank in (1, 2, 4, 8):
    determinant = Fraction(1, 2) ** rank
    hostile_b.append({
        "rank": rank,
        "inverse_norm": "2",
        "trace_norm": str(Fraction(rank, 2)),
        "determinant": str(determinant),
    })
assert hostile_b[-1]["determinant"] == "1/256"

# Safe finite compiler fixture: total trace mass <= 1/2 and operator norm <= 1/2.
safe_eigenvalues = [Fraction(1, 4), -Fraction(1, 4)]
safe_det = (1 + safe_eigenvalues[0]) * (1 + safe_eigenvalues[1])
assert safe_det == Fraction(15, 16)

result = {
    "schema": "marici.rh-relative-fredholm-unit-gate.v1",
    "bounded_trace_norm_alone_fails": hostile_a,
    "uniform_inverse_gap_alone_fails": hostile_b,
    "safe_fixture": {
        "eigenvalues": ["1/4", "-1/4"],
        "trace_norm": "1/2",
        "inverse_norm_bound": "4/3",
        "determinant": "15/16",
    },
    "required_joint_gate": [
        "uniform_trace_class_mass",
        "uniform_inverse_control",
        "trace_norm_convergence",
    ],
}

out = Path(__file__).parents[1] / "results" / "rh-relative-fredholm-unit-gate.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
