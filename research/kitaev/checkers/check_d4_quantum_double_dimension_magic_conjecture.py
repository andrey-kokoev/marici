#!/usr/bin/env python3
"""Hostile D(D4) test of the quantum-dimension-to-Wilson-spectrum conjecture."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "d4-quantum-double-dimension-magic-conjecture.json"
I = sp.I


def mul(g, h):
    a, b = g
    c, d = h
    return ((a + (-1) ** b * c) % 4, (b + d) % 2)


ELEMENTS = [(a, b) for a in range(4) for b in range(2)]
E = (0, 0)


def inv(g):
    return next(h for h in ELEMENTS if mul(g, h) == E and mul(h, g) == E)


def conj(q, g):
    return mul(mul(q, g), inv(q))


def commutes(g, h):
    return mul(g, h) == mul(h, g)


CLASSES = [
    ("1", (0, 0)),
    ("r2", (2, 0)),
    ("r", (1, 0)),
    ("s", (0, 1)),
    ("rs", (1, 1)),
]


def conjugacy_class(rep):
    return sorted({conj(q, rep) for q in ELEMENTS})


def transporter(rep, g):
    return next(q for q in ELEMENTS if conj(q, rep) == g)


def irreps(class_name):
    if class_name in ("1", "r2"):
        rows = []
        for er in (1, -1):
            for es in (1, -1):
                rows.append((f"chi{er:+d}{es:+d}", 1,
                             lambda z, er=er, es=es: er ** z[0] * es ** z[1]))
        def standard(z):
            return {0: 2, 1: 0, 2: -2, 3: 0}[z[0]] if z[1] == 0 else 0
        rows.append(("std", 2, standard))
        return rows
    if class_name == "r":
        return [(f"k{k}", 1, lambda z, k=k: I ** (k * z[0])) for k in range(4)]
    if class_name == "s":
        return [
            (f"uv{u:+d}{v:+d}", 1,
             lambda z, u=u, v=v: u ** ((z[0] // 2) % 2) * v ** z[1])
            for u in (1, -1) for v in (1, -1)
        ]
    if class_name == "rs":
        def value(z, u, v):
            if z[1] == 0:
                return u ** ((z[0] // 2) % 2)
            return u ** (((z[0] - 1) // 2) % 2) * v
        return [
            (f"uv{u:+d}{v:+d}", 1, lambda z, u=u, v=v: value(z, u, v))
            for u in (1, -1) for v in (1, -1)
        ]
    raise AssertionError(class_name)


def main() -> None:
    sectors = []
    for class_name, rep in CLASSES:
        members = conjugacy_class(rep)
        for irrep_name, irrep_dimension, character in irreps(class_name):
            sectors.append({
                "label": f"{class_name}:{irrep_name}",
                "class": class_name,
                "rep": rep,
                "members": members,
                "irrep": irrep_name,
                "irrep_dimension": irrep_dimension,
                "dimension": len(members) * irrep_dimension,
                "character": character,
            })
    assert len(sectors) == 22

    S = sp.zeros(22)
    for i, left in enumerate(sectors):
        for j, right in enumerate(sectors):
            total = 0
            for g in left["members"]:
                qg = transporter(left["rep"], g)
                for h in right["members"]:
                    if not commutes(g, h):
                        continue
                    qh = transporter(right["rep"], h)
                    zl = conj(inv(qg), h)
                    zr = conj(inv(qh), g)
                    total += sp.conjugate(left["character"](zl)) * sp.conjugate(right["character"](zr))
            S[i, j] = sp.simplify(total / 8)
    assert S == S.T
    assert sp.simplify(S * sp.conjugate(S.T)) == sp.eye(22)

    vacuum = next(i for i, sector in enumerate(sectors)
                  if sector["class"] == "1" and sector["irrep"] == "chi+1+1")
    recovered_dimensions = [sp.simplify(S[vacuum, i] / S[vacuum, vacuum]) for i in range(22)]
    assert recovered_dimensions == [sector["dimension"] for sector in sectors]

    spectra_by_dimension = defaultdict(dict)
    nonintegral_rows = []
    for i, sector in enumerate(sectors):
        eigenvalues = [sp.simplify(S[i, a] / S[vacuum, a]) for a in range(22)]
        if not all(value.is_integer is True for value in eigenvalues):
            nonintegral_rows.append(sector["label"])
            continue
        residues = [int(value) % 4 for value in eigenvalues]
        histogram = dict(sorted(Counter(residues).items()))
        spectra_by_dimension[sector["dimension"]][sector["label"]] = histogram
    assert not nonintegral_rows

    counterexamples = []
    for dimension, rows in spectra_by_dimension.items():
        labels = list(rows)
        for i, left in enumerate(labels):
            for right in labels[i + 1:]:
                if rows[left] != rows[right]:
                    counterexamples.append({
                        "dimension": dimension,
                        "left": left,
                        "left_spectrum": rows[left],
                        "right": right,
                        "right_spectrum": rows[right],
                    })
    assert counterexamples
    nonvacuum_counterexamples = [
        row for row in counterexamples
        if row["left"] != sectors[vacuum]["label"] and row["right"] != sectors[vacuum]["label"]
    ]
    assert not nonvacuum_counterexamples

    distinct_spectra_per_dimension = {
        str(dimension): len({json.dumps(histogram, sort_keys=True) for histogram in rows.values()})
        for dimension, rows in spectra_by_dimension.items()
    }
    result = {
        "schema": "marici.kitaev.d4-quantum-double-dimension-magic-conjecture.v1",
        "group": "D4 of order 8",
        "sector_count": len(sectors),
        "dimension_census": dict(sorted(Counter(sector["dimension"] for sector in sectors).items())),
        "modular_checks": {"S_symmetric": True, "S_unitary": True, "dimensions_recovered": True},
        "all_wilson_character_eigenvalues_integral": True,
        "distinct_quarter_spectra_per_dimension": distinct_spectra_per_dimension,
        "representative_nonvacuum_spectrum_per_dimension": {
            str(dimension): next(
                histogram for label, histogram in rows.items()
                if label != sectors[vacuum]["label"]
            )
            for dimension, rows in spectra_by_dimension.items()
        },
        "first_counterexample": counterexamples[0],
        "nonvacuum_counterexample_count": len(nonvacuum_counterexamples),
        "counterexample_count": len(counterexamples),
        "universal_conjecture": {
            "statement": "quantum dimension alone determines the unitary-conjugacy class of exp(2 pi i W_x/4) in D(G)",
            "status": "naive vacuum-inclusive form falsified; nonvacuum form survives D(D4)",
            "surviving_s3_result": "in D(S3), dimension and quarter-spectrum partitions coincide exactly",
        },
        "replacement_frontier": "test D(A4), where nonvacuum pure-charge and flux sectors both have dimension three",
        "verdict": "D(D4) falsifies only the naive vacuum-inclusive dimension-to-spectrum conjecture: the vacuum identity loop differs from the other seven dimension-one sectors. The strengthened nonvacuum conjecture survives this test: all seven nonvacuum dimension-one sectors share one quarter spectrum and all fourteen dimension-two sectors share one. D(A4) is the next hostile case because dimension-three pure-charge and flux sectors coexist.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
