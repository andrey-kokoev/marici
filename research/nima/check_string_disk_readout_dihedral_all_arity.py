#!/usr/bin/env python3
"""Finite exact controls for the all-arity disk-readout dihedral character."""

import json
from pathlib import Path


def audit(n):
    identity = tuple(range(n))
    r = tuple((i + 1) % n for i in range(n))
    s = tuple((-i) % n for i in range(n))

    def compose(g, h):
        return tuple(g[h[i]] for i in range(n))

    def power(g, k):
        out = identity
        for _ in range(k):
            out = compose(g, out)
        return out

    def inverse(g):
        out = [0] * n
        for i, image in enumerate(g):
            out[image] = i
        return tuple(out)

    normal = {}
    for parity in (0, 1):
        for k in range(n):
            g = power(r, k)
            if parity:
                g = compose(s, g)
            normal[g] = (k, parity)
    assert len(normal) == 2 * n

    def chi(g):
        return (-1) ** (n * normal[g][1])

    products = 0
    commutators = set()
    for g in normal:
        for h in normal:
            assert chi(compose(g, h)) == chi(g) * chi(h)
            comm = compose(compose(compose(g, h), inverse(g)), inverse(h))
            commutators.add(comm)
            products += 1
    assert all(chi(g) == 1 for g in commutators)
    expected_order = n if n % 2 else n // 2
    assert len(commutators) == expected_order
    return {
        "arity": n,
        "group_order": 2 * n,
        "commutator_order": len(commutators),
        "rotation_character": chi(r),
        "reflection_character": chi(s),
        "abelianization": "C2" if n % 2 else "C2 x C2",
        "product_checks": products,
        "all_commutators_killed": True,
    }


audits = [audit(n) for n in range(3, 17)]
result = {
    "schema": "marici.nima.string_disk_readout_dihedral_all_arity.v1",
    "audited_arities": [row["arity"] for row in audits],
    "audits": audits,
    "theorem_character": "chi_n(r)=1, chi_n(s)=(-1)^n",
    "passed": True,
}
out = Path(__file__).with_name("results") / "string-disk-readout-dihedral-all-arity.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

