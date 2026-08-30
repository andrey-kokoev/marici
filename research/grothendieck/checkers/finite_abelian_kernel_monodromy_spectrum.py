"""Exact non-field controls for finite abelian kernel monodromy."""

from itertools import product
from math import gcd
import json
from pathlib import Path


def ident(r):
    return tuple(tuple(int(i == j) for j in range(r)) for i in range(r))


def mmul(a, b, modulus):
    r = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(r)) % modulus
                       for j in range(r)) for i in range(r))


def mvec(a, v, modulus):
    return tuple(sum(a[i][j] * v[j] for j in range(len(v))) % modulus
                 for i in range(len(v)))


def mpow(a, n, modulus):
    out = ident(len(a))
    for _ in range(n):
        out = mmul(out, a, modulus)
    return out


def norm_image(action, h, v, n, modulus):
    ah = mpow(action, h, modulus)
    x = ident(len(action))
    total = (0,) * len(v)
    for _ in range(n):
        w = mvec(x, v, modulus)
        total = tuple((u + z) % modulus for u, z in zip(total, w))
        x = mmul(x, ah, modulus)
    return total


def run(name, modulus, rank, action_order, action):
    kernel = list(product(range(modulus), repeat=rank))
    survivors = []
    checks = 0
    for n in range(1, 25):
        global_ok = True
        for h in range(action_order):
            images = [norm_image(action, h, v, n, modulus) for v in kernel]
            global_ok &= len(set(images)) == len(kernel)
            checks += len(kernel) * len(kernel)
        predicted = gcd(n, modulus * action_order) == 1
        assert global_ok == predicted, (name, n, global_ok, predicted)
        if global_ok:
            survivors.append(n)
    return {"group": name, "kernel_exponent": modulus,
            "visible_action_exponent": action_order,
            "survivors_1_to_24": survivors, "checks": checks}


def main():
    families = [
        run("C4_semidirect_C2", 4, 1, 2, ((3,),)),
        run("C9_semidirect_C2", 9, 1, 2, ((8,),)),
        run("C4xC4_semidirect_C3", 4, 2, 3, ((0, 3), (1, 3))),
    ]
    result = {
        "theorem": "global compatibility iff gcd(n,exp(K)*exp(M))=1",
        "families": families,
        "index_cases": 72,
        "coefficient_value_checks": sum(x["checks"] for x in families),
        "status": "pass",
    }
    out = Path(__file__).parents[1] / "results" / "finite-abelian-kernel-monodromy-spectrum.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
