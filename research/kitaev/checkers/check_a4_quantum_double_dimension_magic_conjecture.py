#!/usr/bin/env python3
"""Hostile nonvacuum D(A4) test of dimension-to-quarter-spectrum conjecture."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "a4-quantum-double-dimension-magic-conjecture.json"
W = sp.exp(2 * sp.pi * sp.I / 3).expand(complex=True)
E = (0, 1, 2, 3)


def mul(p, q):
    return tuple(p[q[i]] for i in range(4))


def inv(p):
    return tuple(p.index(i) for i in range(4))


def parity(p):
    return sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4)) % 2


G = [p for p in __import__("itertools").permutations(range(4)) if parity(p) == 0]


def conj(q, g):
    return mul(mul(q, g), inv(q))


def class_of(g):
    return sorted({conj(q, g) for q in G})


classes = []
remaining = set(G)
while remaining:
    g = min(remaining)
    c = class_of(g)
    classes.append(c)
    remaining -= set(c)
classes.sort(key=lambda c: (len(c), c))
assert [len(c) for c in classes] == [1, 3, 4, 4]
C1, CV, C3A, C3B = classes
CLASS_NAMES = {tuple(C1): "1", tuple(CV): "V", tuple(C3A): "3a", tuple(C3B): "3b"}


def class_name(g):
    return next(CLASS_NAMES[tuple(c)] for c in classes if g in c)


def transporter(rep, g):
    return next(q for q in G if conj(q, rep) == g)


def centralizer(rep):
    return [g for g in G if mul(g, rep) == mul(rep, g)]


def power(g, n):
    out = E
    for _ in range(n):
        out = mul(out, g)
    return out


def irreps(name, rep):
    if name == "1":
        rows = []
        for k in range(3):
            def one_dim(z, k=k):
                return {"1": 1, "V": 1, "3a": W ** k, "3b": W ** (2 * k)}[class_name(z)]
            rows.append((f"chi{k}", 1, one_dim))
        rows.append(("std3", 3, lambda z: {"1": 3, "V": -1, "3a": 0, "3b": 0}[class_name(z)]))
        return rows
    if name == "V":
        nontrivial = [z for z in centralizer(rep) if z != E]
        a = rep
        b = next(z for z in nontrivial if z != a)
        coordinates = {E: (0, 0), a: (1, 0), b: (0, 1), mul(a, b): (1, 1)}
        return [
            (f"uv{u}{v}", 1, lambda z, u=u, v=v: (-1) ** (u * coordinates[z][0] + v * coordinates[z][1]))
            for u in range(2) for v in range(2)
        ]
    coordinates = {power(rep, t): t for t in range(3)}
    return [(f"k{k}", 1, lambda z, k=k: W ** (k * coordinates[z])) for k in range(3)]


def main() -> None:
    sectors = []
    for members in classes:
        rep = members[0]
        name = CLASS_NAMES[tuple(members)]
        for irrep_name, irrep_dim, character in irreps(name, rep):
            sectors.append({"label": f"{name}:{irrep_name}", "class": name, "rep": rep,
                            "members": members, "irrep_dimension": irrep_dim,
                            "dimension": len(members) * irrep_dim, "character": character})
    assert len(sectors) == 14
    S = sp.zeros(14)
    for i, left in enumerate(sectors):
        for j, right in enumerate(sectors):
            total = 0
            for g in left["members"]:
                qg = transporter(left["rep"], g)
                for h in right["members"]:
                    if mul(g, h) != mul(h, g):
                        continue
                    qh = transporter(right["rep"], h)
                    total += sp.conjugate(left["character"](conj(inv(qg), h))) * sp.conjugate(right["character"](conj(inv(qh), g)))
            S[i, j] = sp.simplify(sp.expand_complex(total / 12))
    assert S == S.T
    assert sp.simplify(sp.expand_complex(S * sp.conjugate(S.T))) == sp.eye(14)
    vacuum = next(i for i, x in enumerate(sectors) if x["label"] == "1:chi0")
    assert [sp.simplify(S[vacuum, i] / S[vacuum, vacuum]) for i in range(14)] == [x["dimension"] for x in sectors]

    rows = defaultdict(dict)
    nonintegral = []
    for i, sector in enumerate(sectors):
        eigenvalues = [sp.simplify(sp.expand_complex(S[i, a] / S[vacuum, a])) for a in range(14)]
        if not all(value.is_integer is True for value in eigenvalues):
            nonintegral.append({"label": sector["label"], "eigenvalues": [str(v) for v in eigenvalues]})
            continue
        residues = [int(v) % 4 for v in eigenvalues]
        rows[sector["dimension"]][sector["label"]] = dict(sorted(Counter(residues).items()))
    assert len(nonintegral) == 8
    nonvac_counterexamples = []
    for dimension, group in rows.items():
        labels = [x for x in group if x != "1:chi0"]
        for n, left in enumerate(labels):
            for right in labels[n + 1:]:
                if group[left] != group[right]:
                    nonvac_counterexamples.append({"dimension": dimension, "left": left,
                                                   "left_spectrum": group[left], "right": right,
                                                   "right_spectrum": group[right]})
    assert not nonvac_counterexamples
    result = {
        "schema": "marici.kitaev.a4-quantum-double-dimension-magic-conjecture.v1",
        "group": "A4 of order 12",
        "sector_count": 14,
        "dimension_census": dict(sorted(Counter(x["dimension"] for x in sectors).items())),
        "modular_checks": {"S_symmetric": True, "S_unitary": True, "dimensions_recovered": True},
        "typed_self_adjoint_integral_row_count": sum(len(group) for group in rows.values()),
        "excluded_nonhermitian_or_nonintegral_rows": [row["label"] for row in nonintegral],
        "nonvacuum_counterexample_count": len(nonvac_counterexamples),
        "distinct_quarter_spectra_per_dimension": {
            str(d): len({json.dumps(v, sort_keys=True) for v in group.values()}) for d, group in rows.items()
        },
        "conjecture_status": "survives on the typed self-adjoint integral nonvacuum domain",
        "verdict": "D(A4) does not falsify the strengthened conjecture. On the correctly typed self-adjoint integral Wilson domain, the dimension-three pure charge and all four dimension-three flux sectors have the same quarter-evolution spectrum. Eight complex rows are excluded because raw quarter evolution is not a Hermitian-Hamiltonian operation there. Together with D(D4), this is corroboration across two hostile non-Abelian doubles, not a general proof.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
