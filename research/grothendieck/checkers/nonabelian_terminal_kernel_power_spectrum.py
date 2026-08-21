"""Exact power-permutation spectra for S3 and Q8."""

from itertools import permutations
from math import gcd
import json
from pathlib import Path


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def qmul(x, y):
    sx, ax = x
    sy, ay = y
    if ax == 0:
        return (sx * sy, ay)
    if ay == 0:
        return (sx * sy, ax)
    if ax == ay:
        return (-sx * sy, 0)
    table = {(1, 2): (1, 3), (2, 3): (1, 1), (3, 1): (1, 2),
             (2, 1): (-1, 3), (3, 2): (-1, 1), (1, 3): (-1, 2)}
    sign, axis = table[(ax, ay)]
    return (sx * sy * sign, axis)


def power(x, n, mul, identity):
    out = identity
    for _ in range(n):
        out = mul(out, x)
    return out


def run(name, group, mul, identity, exponent):
    survivors = []
    checks = 0
    for n in range(1, 25):
        images = [power(x, n, mul, identity) for x in group]
        compatible = len(set(images)) == len(group)
        predicted = gcd(n, exponent) == 1
        assert compatible == predicted, (name, n, compatible, predicted)
        checks += len(group) * len(group)
        if compatible:
            survivors.append(n)
    return {"group": name, "order": len(group), "exponent": exponent,
            "survivors_1_to_24": survivors, "checks": checks}


def main():
    s3 = list(permutations(range(3)))
    q8 = [(sign, axis) for axis in range(4) for sign in (-1, 1)]
    families = [
        run("S3", s3, compose, (0, 1, 2), 6),
        run("Q8", q8, qmul, (1, 0), 4),
    ]
    result = {
        "theorem": "terminal power compatibility iff gcd(n,exp(K))=1",
        "families": families,
        "index_cases": 48,
        "coefficient_value_checks": sum(x["checks"] for x in families),
        "status": "pass",
    }
    out = Path(__file__).parents[1] / "results" / "nonabelian-terminal-kernel-power-spectrum.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
