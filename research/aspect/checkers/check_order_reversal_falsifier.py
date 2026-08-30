from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "order_reversal_falsifier.json"


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def matvec(a, v):
    return [sum(row[j] * v[j] for j in range(len(v))) for row in a]


def main():
    a = [[F(1), F(1)], [F(0), F(1)]]
    b = [[F(1), F(0)], [F(1), F(1)]]
    forward = matmul(a, b)
    reverse = matmul(b, a)
    state = [F(1), F(0)]
    forward_output = matvec(forward, state)
    reverse_output = matvec(reverse, state)
    assert forward != reverse
    assert forward_output != reverse_output
    out = {
        "schema": "marici.aspect.order-reversal-falsifier.v1", "status": "pass",
        "operation_multiset_equal": True,
        "forward_product": [[str(x) for x in row] for row in forward],
        "reverse_product": [[str(x) for x in row] for row in reverse],
        "forward_output": [str(x) for x in forward_output],
        "reverse_output": [str(x) for x in reverse_output],
        "order_independent": False,
        "required_gate": "cyclic, reversed, and independently permuted superblocks have equal calibrated target laws",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
