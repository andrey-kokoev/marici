"""Exact hostile test for nonabelian power maps and Mackey fiber sums."""

from itertools import permutations, product
import json
from pathlib import Path


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def power(g, n, mul, identity):
    out = identity
    for _ in range(n):
        out = mul(out, g)
    return out


def fiber_bijection(groups, quotient, q, mul, identity, n):
    failures = []
    value_checks = 0
    for h in quotient:
        source = [g for g in groups if q(g) == h]
        target_h = power(h, n, lambda a, b: (a + b) % 2, 0)
        target = [g for g in groups if q(g) == target_h]
        images = [power(g, n, mul, identity) for g in source]
        ok = sorted(images) == sorted(target)
        value_checks += len(groups) * len(source)
        if not ok:
            failures.append({"fiber": h, "images": [str(x) for x in images],
                             "target": [str(x) for x in target]})
    return not failures, failures, value_checks


def parity(p):
    inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    return inversions % 2


def main():
    s3 = list(permutations(range(3)))
    c6 = list(range(6))
    cases = []
    total_checks = 0
    for name, group, q, mul, identity in [
        ("S3_to_C2", s3, parity, compose, (0, 1, 2)),
        ("C6_to_C2", c6, lambda x: x % 2, lambda a, b: (a + b) % 6, 0),
    ]:
        for n in range(1, 7):
            compatible, failures, checks = fiber_bijection(
                group, [0, 1], q, mul, identity, n
            )
            total_checks += checks
            cases.append({"map": name, "n": n, "compatible": compatible,
                          "failure_count": len(failures), "failures": failures})

    hostile = next(c for c in cases if c["map"] == "S3_to_C2" and c["n"] == 2)
    control = next(c for c in cases if c["map"] == "C6_to_C2" and c["n"] == 2)
    assert not hostile["compatible"]
    assert control["compatible"]
    result = {
        "theorem": "fiber-sum commutation iff every induced power map on a quotient fiber is bijective",
        "hostile_case": hostile,
        "abelian_control": control,
        "case_count": len(cases),
        "coefficient_value_checks": total_checks,
        "status": "pass",
    }
    out = Path(__file__).parents[1] / "results" / "nonabelian-twisted-norm-mackey-gate.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
