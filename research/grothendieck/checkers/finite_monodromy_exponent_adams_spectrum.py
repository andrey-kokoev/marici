"""Exact spectra for noncyclic and nonabelian finite monodromy."""

from itertools import product
from math import gcd, lcm
import json
from pathlib import Path


def ident(r):
    return tuple(tuple(int(i == j) for j in range(r)) for i in range(r))


def mmul(a, b, p):
    r = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(r)) % p
                       for j in range(r)) for i in range(r))


def mvec(a, v, p):
    return tuple(sum(a[i][j] * v[j] for j in range(len(v))) % p
                 for i in range(len(v)))


def mpow(a, n, p):
    out = ident(len(a))
    for _ in range(n):
        out = mmul(out, a, p)
    return out


def closure(generators, p):
    seen = {ident(len(generators[0]))}
    frontier = list(seen)
    while frontier:
        x = frontier.pop()
        for g in generators:
            y = mmul(x, g, p)
            if y not in seen:
                seen.add(y)
                frontier.append(y)
    return sorted(seen)


def order(a, p):
    x = ident(len(a))
    for n in range(1, 1000):
        x = mmul(x, a, p)
        if x == ident(len(a)):
            return n
    raise AssertionError("order bound")


def linear_norm_image(a, v, n, p):
    total = (0,) * len(v)
    x = ident(len(a))
    for _ in range(n):
        total = tuple((u + w) % p for u, w in zip(total, mvec(x, v, p)))
        x = mmul(x, a, p)
    return total


def run(name, p, generators):
    group = closure(generators, p)
    exponent = lcm(*(order(h, p) for h in group))
    vs = list(product(range(p), repeat=len(generators[0])))
    survivors = []
    checks = 0
    for n in range(1, 25):
        global_ok = True
        for h in group:
            images = [linear_norm_image(h, v, n, p) for v in vs]
            global_ok &= len(set(images)) == len(vs)
            checks += len(vs) * len(vs)
        predicted = gcd(n, p * exponent) == 1
        assert global_ok == predicted, (name, n, global_ok, predicted)
        if global_ok:
            survivors.append(n)
    return {"group": name, "p": p, "group_order": len(group),
            "exponent": exponent, "survivors_1_to_24": survivors,
            "checks": checks}


def main():
    s3 = run("S3_on_F5^2", 5, [((0, 4), (1, 4)), ((0, 1), (1, 0))])
    v4 = run("V4_on_F3^2", 3, [((2, 0), (0, 1)), ((1, 0), (0, 2))])
    assert s3["group_order"] == 6 and s3["exponent"] == 6
    assert v4["group_order"] == 4 and v4["exponent"] == 2
    result = {
        "theorem": "global compatibility iff gcd(n,p*exp(H))=1",
        "families": [s3, v4],
        "index_cases": 48,
        "coefficient_value_checks": s3["checks"] + v4["checks"],
        "status": "pass",
    }
    out = Path(__file__).parents[1] / "results" / "finite-monodromy-exponent-adams-spectrum.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
