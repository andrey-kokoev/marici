from fractions import Fraction as F
import json
from pathlib import Path


R = [F(2), F(3), F(4)]
H0 = [[F(int(i == j)) for j in range(3)] for i in range(3)]
Ht = [[H0[i][j] / (R[i] * R[j]) for j in range(3)] for i in range(3)]

fixed_residual = [[Ht[i][j] - H0[i][j] for j in range(3)] for i in range(3)]
assert any(x != 0 for row in fixed_residual for x in row)
assert all(Ht[i][i] > 0 for i in range(3))
assert all(Ht[i][j] == 0 for i in range(3) for j in range(3) if i != j)

# A fixed graph H must satisfy H_ij/(r_i r_j)=H_ij. Since every product is
# greater than one, every entry is forced to vanish.
fixed_allowed = [
    (i, j) for i in range(3) for j in range(3) if R[i] * R[j] == 1
]
assert fixed_allowed == []

result = {
    "schema": "marici.rh-moving-positive-polarization.v1",
    "reciprocal_transport": "E=diag(R,R^-1)",
    "R": ["2", "3", "4"],
    "initial_positive_graph": "H0=I",
    "transported_graph": [[str(x) for x in row] for row in Ht],
    "transported_graph_positive": True,
    "nonzero_fixed_graph_exists": False,
    "fixed_graph_equation": "R^-1 H R^-1=H",
    "conclusion": "positive_polarization_must_move",
}

out = Path(__file__).parents[1] / "results" / "rh-moving-positive-polarization.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
