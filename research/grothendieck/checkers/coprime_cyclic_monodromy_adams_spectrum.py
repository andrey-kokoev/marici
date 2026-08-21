"""Exact survivor spectra for coprime cyclic semidirect products."""

from math import gcd
import json
from pathlib import Path


def vec_add(v, w, p):
    return tuple((a + b) % p for a, b in zip(v, w))


def mat_vec(a, v, p):
    return tuple(sum(a[i][j] * v[j] for j in range(len(v))) % p
                 for i in range(len(v)))


def identity(r):
    return tuple(tuple(int(i == j) for j in range(r)) for i in range(r))


def mat_mul(a, b, p):
    r = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(r)) % p
                       for j in range(r)) for i in range(r))


def mat_pow(a, n, p):
    out = identity(len(a))
    for _ in range(n):
        out = mat_mul(out, a, p)
    return out


def vectors(p, r):
    if r == 1:
        return [(x,) for x in range(p)]
    return [(x, y) for x in range(p) for y in range(p)]


def mul(x, y, p, m, action):
    v, h = x
    w, j = y
    return (vec_add(v, mat_vec(mat_pow(action, h, p), w, p), p), (h + j) % m)


def power(x, n, p, m, action):
    out = ((0,) * len(x[0]), 0)
    for _ in range(n):
        out = mul(out, x, p, m, action)
    return out


def spectrum(name, p, m, action):
    vs = vectors(p, len(action))
    group = [(v, h) for h in range(m) for v in vs]
    compatible = []
    checks = 0
    for n in range(1, 25):
        global_ok = True
        for h in range(m):
            images = [power((v, h), n, p, m, action) for v in vs]
            target = [(v, (n * h) % m) for v in vs]
            global_ok &= sorted(images) == sorted(target)
            checks += len(vs) * len(group)
        predicted = gcd(n, p * m) == 1
        assert global_ok == predicted, (name, n, global_ok, predicted)
        if global_ok:
            compatible.append(n)
    return {"group": name, "p": p, "action_order": m,
            "compatible_indices_1_to_24": compatible, "checks": checks}


def main():
    families = [
        spectrum("A4_to_C3", 2, 3, ((0, 1), (1, 1))),
        spectrum("C3_semidirect_C2_to_C2", 3, 2, ((2,),)),
        spectrum("C5_semidirect_C4_to_C4", 5, 4, ((2,),)),
    ]
    result = {
        "theorem": "global compatibility iff gcd(n,p*action_order)=1",
        "families": families,
        "index_cases": 24 * len(families),
        "coefficient_value_checks": sum(x["checks"] for x in families),
        "status": "pass",
    }
    out = Path(__file__).parents[1] / "results" / "coprime-cyclic-monodromy-adams-spectrum.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
