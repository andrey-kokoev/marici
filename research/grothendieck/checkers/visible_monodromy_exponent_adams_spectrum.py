"""Exact nonfaithful-action tests for the visible exponent criterion."""

from itertools import product
from math import gcd
import json
from pathlib import Path


def mmul(a, b, p):
    r = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(r)) % p
                       for j in range(r)) for i in range(r))


def mvec(a, v, p):
    return tuple(sum(a[i][j] * v[j] for j in range(len(v))) % p
                 for i in range(len(v)))


def ident(r):
    return tuple(tuple(int(i == j) for j in range(r)) for i in range(r))


def mpow(a, n, p):
    out = ident(len(a))
    for _ in range(n):
        out = mmul(out, a, p)
    return out


def norm_image(a, h, v, n, p, image_order):
    total = (0,) * len(v)
    ah = mpow(a, h % image_order, p)
    x = ident(len(a))
    for _ in range(n):
        w = mvec(x, v, p)
        total = tuple((u + z) % p for u, z in zip(total, w))
        x = mmul(x, ah, p)
    return total


def run(name, p, quotient_order, image_order, action, dimension):
    vs = list(product(range(p), repeat=dimension))
    survivors = []
    old_full_exponent_mismatches = []
    checks = 0
    for n in range(1, 31):
        global_ok = True
        for h in range(quotient_order):
            images = [norm_image(action, h, v, n, p, image_order) for v in vs]
            global_ok &= len(set(images)) == len(vs)
            checks += len(vs) * len(vs)
        predicted = gcd(n, p * image_order) == 1
        assert global_ok == predicted, (name, n, global_ok, predicted)
        if global_ok:
            survivors.append(n)
        if global_ok != (gcd(n, p * quotient_order) == 1):
            old_full_exponent_mismatches.append(n)
    return {"group": name, "p": p, "quotient_order": quotient_order,
            "visible_image_exponent": image_order, "survivors_1_to_30": survivors,
            "full_exponent_false_predictions": old_full_exponent_mismatches,
            "checks": checks}


def main():
    c15 = run("F2^2_semidirect_C15_via_C3", 2, 15, 3,
              ((0, 1), (1, 1)), 2)
    trivial = run("F2_times_C3_trivial_action", 2, 3, 1, ((1,),), 1)
    assert 5 in c15["survivors_1_to_30"] and 5 in c15["full_exponent_false_predictions"]
    assert 3 in trivial["survivors_1_to_30"] and 3 in trivial["full_exponent_false_predictions"]
    result = {
        "theorem": "global compatibility iff gcd(n,p*exp(image action))=1",
        "families": [c15, trivial],
        "index_cases": 60,
        "coefficient_value_checks": c15["checks"] + trivial["checks"],
        "status": "pass",
    }
    out = Path(__file__).parents[1] / "results" / "visible-monodromy-exponent-adams-spectrum.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
