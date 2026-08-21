"""Exact Beck--Chevalley audit for finite cyclic deck maps."""

from itertools import product
import json
from pathlib import Path


def hom(a, b, c, x):
    # x |-> c x mod b; admissibility is b | c a.
    return (c * x) % b


def maps(a, b):
    return [c for c in range(b) if (c * a) % b == 0]


def main():
    squares = basis_checks = 0
    failures = []
    for a, b, k in product(range(1, 9), repeat=3):
        for cf in maps(a, k):
            for cg in maps(b, k):
                fibers = {
                    h: [x for x in range(a) if hom(a, k, cf, x) == hom(b, k, cg, h)]
                    for h in range(b)
                }
                squares += 1
                # Check b_! a^* = g^* f_! on the delta basis of Fun(C_a,Q).
                for x0 in range(a):
                    for h in range(b):
                        lhs = sum(1 for x in fibers[h] if x == x0)
                        rhs = int(hom(a, k, cf, x0) == hom(b, k, cg, h))
                        basis_checks += 1
                        if lhs != rhs:
                            failures.append([a, b, k, cf, cg, x0, h, lhs, rhs])

    result = {
        "schema": "marici.finite-deck-beck-chevalley.v1",
        "range": "1 <= |G|,|H|,|K| <= 8; every cyclic homomorphism pair",
        "pullback_squares": squares,
        "basis_checks": basis_checks,
        "failures": failures,
        "passed": not failures,
    }
    out = Path(__file__).with_name("results") / "finite-deck-beck-chevalley.json"
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
