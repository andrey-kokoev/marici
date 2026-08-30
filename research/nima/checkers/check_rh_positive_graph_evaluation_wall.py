from fractions import Fraction as F
import json
from pathlib import Path


H = ((F(1), F(0)), (F(0), F(1)))
x = (F(1), F(-1))
ell = (F(1), F(1))


def matvec(matrix, vector):
    return tuple(sum(matrix[i][j] * vector[j] for j in range(2)) for i in range(2))


def add(left, right):
    return tuple(a + b for a, b in zip(left, right))


def sub(left, right):
    return tuple(a - b for a, b in zip(left, right))


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


y = matvec(H, x)
sum_port = add(x, y)
difference_port = sub(x, y)
scalar_endpoint = dot(ell, sum_port)

assert sum_port == (F(2), F(-2))
assert sum_port != (F(0), F(0))
assert difference_port == (F(0), F(0))
assert scalar_endpoint == 0

result = {
    "schema": "marici.rh-positive-graph-evaluation-wall.v1",
    "positive_graph": "H=I",
    "state": "x=(1,-1), y=Hx",
    "sum_carrier": ["2", "-2"],
    "sum_carrier_nonzero": True,
    "difference_carrier_zero": True,
    "scalar_evaluation": "ell=(1,1)",
    "scalar_sum_readout": "0",
    "conclusion": "positive_graph_excludes_full_antipodal_sum_but_not_scalar_projection_zero",
    "missing_gate": "bordered_evaluation_wall_lifting_scalar_zero_to_carrier_zero",
}

out = Path(__file__).parents[1] / "results" / "rh-positive-graph-evaluation-wall.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
