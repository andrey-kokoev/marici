from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "321_vs_2x21_plus1.json"


def joint(x):
    return ((1 + x) / 4, (1 - x) / 4, (1 - x) / 4, (1 + x) / 4)


def marginals(p):
    p00, p01, p10, p11 = p
    return (p00 + p01, p10 + p11), (p00 + p10, p01 + p11)


def parity(p):
    p00, p01, p10, p11 = p
    return (p00 + p11) - (p01 + p10)


def main():
    flat = joint(F(0))
    relational = joint(F(3, 5))
    assert marginals(flat) == marginals(relational) == ((F(1, 2), F(1, 2)),) * 2
    assert parity(flat) == 0
    assert parity(relational) == F(3, 5)

    kernel_vector = (F(1), F(-1), F(-1), F(1))
    assert marginals(kernel_vector) == ((F(0), F(0)), (F(0), F(0)))
    assert parity(kernel_vector) == 4

    out = {
        "schema": "marici.aspect.321-vs-2x21-plus1.v1",
        "status": "pass",
        "single_tower_failure": "local totalization sends the relational parity vector (1,-1,-1,1) to zero",
        "flat_joint": [str(x) for x in flat],
        "relational_joint": [str(x) for x in relational],
        "common_local_marginals": [["1/2", "1/2"], ["1/2", "1/2"]],
        "parities": {"flat": "0", "relational": "3/5"},
        "working_architecture": "two local 2+1 witness/mate systems retain a common instance key; the outer +1 acts on their paired record before marginal quotient",
        "necessary_gate": "if either local completion discards the pairing key, 2(2+1)+1 degenerates to the same failure as 3+2+1",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
