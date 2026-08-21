"""Exact linear-norm and fiber enumeration for A4 -> C3."""

import json
from pathlib import Path

VECTORS = [(0, 0), (0, 1), (1, 0), (1, 1)]


def add(v, w):
    return (v[0] ^ w[0], v[1] ^ w[1])


def mat_vec(a, v):
    return ((a[0][0] * v[0] ^ a[0][1] * v[1]),
            (a[1][0] * v[0] ^ a[1][1] * v[1]))


I = ((1, 0), (0, 1))
A = ((0, 1), (1, 1))


def mat_mul(a, b):
    cols = [(b[0][j], b[1][j]) for j in range(2)]
    rows = [a[0], a[1]]
    return tuple(tuple((r[0] * c[0]) ^ (r[1] * c[1]) for c in cols) for r in rows)


def mat_pow(a, n):
    out = I
    for _ in range(n):
        out = mat_mul(out, a)
    return out


def mul(x, y, action):
    v, h = x
    w, j = y
    return (add(v, mat_vec(mat_pow(action, h), w)), (h + j) % 3)


def power(x, n, action):
    out = ((0, 0), 0)
    for _ in range(n):
        out = mul(out, x, action)
    return out


def rank2(images):
    return len(set(images)).bit_length() - 1


def run(action, name):
    group = [(v, h) for h in range(3) for v in VECTORS]
    cases = []
    checks = 0
    for n in range(1, 10):
        for h in range(3):
            source = [(v, h) for v in VECTORS]
            target = [(v, (n * h) % 3) for v in VECTORS]
            images = [power(x, n, action) for x in source]
            compatible = sorted(images) == sorted(target)
            linear_images = [power((v, h), n, action)[0] for v in VECTORS]
            rank = rank2(linear_images)
            assert compatible == (rank == 2)
            checks += len(source) * len(group)
            cases.append({"group": name, "n": n, "fiber": h,
                          "linear_rank": rank, "compatible": compatible})
    return cases, checks


def main():
    hostile_cases, hostile_checks = run(A, "A4_to_C3")
    control_cases, control_checks = run(I, "C2xC2xC3_to_C3")
    hostile = next(c for c in hostile_cases if c["n"] == 3 and c["fiber"] == 1)
    control = next(c for c in control_cases if c["n"] == 3 and c["fiber"] == 1)
    assert hostile == {"group": "A4_to_C3", "n": 3, "fiber": 1,
                       "linear_rank": 0, "compatible": False}
    assert control["linear_rank"] == 2 and control["compatible"]
    result = {
        "theorem": "semidirect fiber compatibility iff the geometric-sum linear norm has full rank",
        "hostile_case": hostile,
        "direct_product_control": control,
        "fiber_index_cases": len(hostile_cases) + len(control_cases),
        "coefficient_value_checks": hostile_checks + control_checks,
        "status": "pass",
    }
    out = Path(__file__).parents[1] / "results" / "semidirect-linear-norm-adams-gate.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
