"""Exact twisted fiber spectrum for Q8 semidirect C3."""

from math import gcd
import json
from pathlib import Path


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


def alpha(x, h):
    sign, axis = x
    if axis == 0:
        return x
    return (sign, ((axis - 1 + h) % 3) + 1)


def mul(x, y):
    k, h = x
    ell, j = y
    return (qmul(k, alpha(ell, h)), (h + j) % 3)


def power(x, n):
    out = ((1, 0), 0)
    for _ in range(n):
        out = mul(out, x)
    return out


def main():
    q8 = [(sign, axis) for axis in range(4) for sign in (-1, 1)]
    survivors = []
    failures = []
    checks = 0
    for n in range(1, 25):
        global_ok = True
        failed_fibers = []
        for h in range(3):
            images = [power((k, h), n) for k in q8]
            target = [(k, (n * h) % 3) for k in q8]
            ok = sorted(images) == sorted(target)
            global_ok &= ok
            if not ok:
                failed_fibers.append(h)
            checks += len(q8) * 24
        predicted = gcd(n, 12) == 1
        assert global_ok == predicted, (n, global_ok, predicted)
        if global_ok:
            survivors.append(n)
        else:
            failures.append({"n": n, "failed_fibers": failed_fibers})
    result = {
        "theorem_control": "Q8 semidirect C3 compatibility iff gcd(n,12)=1",
        "survivors_1_to_24": survivors,
        "failures": failures,
        "index_cases": 24,
        "coefficient_value_checks": checks,
        "status": "pass",
    }
    out = Path(__file__).parents[1] / "results" / "quaternion-monodromy-twisted-power-spectrum.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
