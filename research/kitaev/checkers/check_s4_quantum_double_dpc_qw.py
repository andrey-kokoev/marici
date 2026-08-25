#!/usr/bin/env python3
"""Risky predeclared D(S4) falsification test of DPC-QW."""

from __future__ import annotations

import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
K = ROOT / "research" / "kitaev"
OUT = K / "results" / "s4-quantum-double-dpc-qw.json"
E = (0, 1, 2, 3)
G = list(itertools.permutations(range(4)))
I = sp.I


def mul(p, q):
    return tuple(p[q[i]] for i in range(4))


def inv(p):
    return tuple(p.index(i) for i in range(4))


def conj(q, g):
    return mul(mul(q, g), inv(q))


def power(g, n):
    out = E
    for _ in range(n):
        out = mul(out, g)
    return out


def order(g):
    return next(n for n in range(1, 13) if power(g, n) == E)


def cycle_type(p):
    seen = set()
    lengths = []
    for i in range(4):
        if i in seen:
            continue
        j, length = i, 0
        while j not in seen:
            seen.add(j)
            length += 1
            j = p[j]
        if length > 1:
            lengths.append(length)
    fixed = 4 - sum(lengths)
    lengths.extend([1] * fixed)
    return tuple(sorted(lengths, reverse=True))


NAMES = {(1, 1, 1, 1): "1", (2, 1, 1): "2", (2, 2): "22", (3, 1): "3", (4,): "4"}


def class_name(g):
    return NAMES[cycle_type(g)]


def conjugacy_class(rep):
    return sorted({conj(q, rep) for q in G})


def centralizer(rep):
    return [g for g in G if mul(g, rep) == mul(rep, g)]


def transporter(rep, g):
    return next(q for q in G if conj(q, rep) == g)


REPS = {}
for g in G:
    REPS.setdefault(class_name(g), g)


def irreps(name, rep):
    if name == "1":
        table = {
            "triv": (1, {"1": 1, "2": 1, "22": 1, "3": 1, "4": 1}),
            "sign": (1, {"1": 1, "2": -1, "22": 1, "3": 1, "4": -1}),
            "two": (2, {"1": 2, "2": 0, "22": 2, "3": -1, "4": 0}),
            "std": (3, {"1": 3, "2": 1, "22": -1, "3": 0, "4": -1}),
            "stdsign": (3, {"1": 3, "2": -1, "22": -1, "3": 0, "4": 1}),
        }
        return [(label, dim, lambda z, row=row: row[class_name(z)]) for label, (dim, row) in table.items()]
    if name == "2":
        c = centralizer(rep)
        other = next(z for z in c if z not in (E, rep))
        coords = {E: (0, 0), rep: (1, 0), other: (0, 1), mul(rep, other): (1, 1)}
        return [(f"uv{u}{v}", 1, lambda z, u=u, v=v: (-1) ** (u * coords[z][0] + v * coords[z][1]))
                for u in range(2) for v in range(2)]
    if name == "22":
        c = centralizer(rep)
        r = next(z for z in c if order(z) == 4 and power(z, 2) == rep)
        cyclic = {power(r, t): (t, 0) for t in range(4)}
        s = next(z for z in c if order(z) == 2 and z not in cyclic)
        coords = dict(cyclic)
        coords.update({mul(power(r, t), s): (t, 1) for t in range(4)})
        rows = [(f"ab{a:+d}{b:+d}", 1,
                 lambda z, a=a, b=b: a ** coords[z][0] * b ** coords[z][1])
                for a in (1, -1) for b in (1, -1)]
        rows.append(("two", 2, lambda z: 2 if coords[z] == (0, 0) else (-2 if coords[z] == (2, 0) else 0)))
        return rows
    modulus = 3 if name == "3" else 4
    coords = {power(rep, t): t for t in range(modulus)}
    root = sp.exp(2 * sp.pi * I / modulus).expand(complex=True)
    return [(f"k{k}", 1, lambda z, k=k: root ** (k * coords[z])) for k in range(modulus)]


def main() -> None:
    class_order = ["1", "2", "22", "3", "4"]
    sectors = []
    for name in class_order:
        rep = REPS[name]
        members = conjugacy_class(rep)
        for irrep_name, irrep_dim, character in irreps(name, rep):
            sectors.append({"label": f"{name}:{irrep_name}", "class": name, "rep": rep,
                            "members": members, "dimension": len(members) * irrep_dim,
                            "character": character})
    assert len(sectors) == 21
    S = sp.zeros(21)
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
            S[i, j] = sp.simplify(sp.expand_complex(total / 24))
    assert S == S.T
    assert sp.simplify(sp.expand_complex(S * sp.conjugate(S.T))) == sp.eye(21)
    vacuum = next(i for i, x in enumerate(sectors) if x["label"] == "1:triv")
    assert [sp.simplify(S[vacuum, i] / S[vacuum, vacuum]) for i in range(21)] == [x["dimension"] for x in sectors]

    typed = defaultdict(dict)
    raw_typed = defaultdict(dict)
    excluded = []
    for i, sector in enumerate(sectors):
        eigenvalues = [sp.simplify(sp.expand_complex(S[i, a] / S[vacuum, a])) for a in range(21)]
        if not all(value.is_integer is True for value in eigenvalues):
            excluded.append(sector["label"])
            continue
        residues = [int(v) % 4 for v in eigenvalues]
        typed[sector["dimension"]][sector["label"]] = dict(sorted(Counter(residues).items()))
        raw_typed[sector["dimension"]][sector["label"]] = dict(sorted(Counter(int(v) for v in eigenvalues).items()))
    counterexamples = []
    raw_counterexamples = []
    for dimension, rows in typed.items():
        labels = [label for label in rows if label != "1:triv"]
        for n, left in enumerate(labels):
            for right in labels[n + 1:]:
                if rows[left] != rows[right]:
                    counterexamples.append({"dimension": dimension, "left": left, "left_spectrum": rows[left],
                                            "right": right, "right_spectrum": rows[right]})
                if raw_typed[dimension][left] != raw_typed[dimension][right]:
                    raw_counterexamples.append({
                        "dimension": dimension,
                        "left": left,
                        "left_raw_spectrum": raw_typed[dimension][left],
                        "right": right,
                        "right_raw_spectrum": raw_typed[dimension][right],
                    })
    modulus_counterexamples = {}
    for modulus in range(2, 13):
        failures = 0
        for dimension, rows in raw_typed.items():
            labels = [label for label in rows if label != "1:triv"]
            residue_histograms = {}
            for label in labels:
                histogram = Counter()
                for value, count in rows[label].items():
                    histogram[str(value % modulus)] += count
                residue_histograms[label] = histogram
            for n, left in enumerate(labels):
                for right in labels[n + 1:]:
                    failures += int(residue_histograms[left] != residue_histograms[right])
        modulus_counterexamples[str(modulus)] = failures
    assert modulus_counterexamples["4"] == 0
    result = {
        "schema": "marici.kitaev.s4-quantum-double-dpc-qw.v1",
        "predeclared_prediction": "zero typed nonvacuum equal-dimension quarter-spectrum counterexamples",
        "group": "S4 of order 24",
        "sector_count": 21,
        "dimension_census": dict(sorted(Counter(x["dimension"] for x in sectors).items())),
        "modular_checks": {"S_symmetric": True, "S_unitary": True, "dimensions_recovered": True},
        "typed_row_count": sum(len(rows) for rows in typed.values()),
        "excluded_row_count": len(excluded),
        "excluded_rows": excluded,
        "counterexample_count": len(counterexamples),
        "raw_integer_spectrum_counterexample_count": len(raw_counterexamples),
        "first_raw_integer_spectrum_counterexample": raw_counterexamples[0] if raw_counterexamples else None,
        "first_counterexample": counterexamples[0] if counterexamples else None,
        "distinct_spectra_per_dimension": {str(d): len({json.dumps(v, sort_keys=True) for v in rows.values()}) for d, rows in typed.items()},
        "representative_spectrum_per_dimension": {
            str(d): next(iter(rows.values())) for d, rows in typed.items()
        },
        "prediction_survives": not counterexamples,
        "stronger_modulus_independent_prediction_survives": not raw_counterexamples,
        "equal_dimension_counterexamples_by_modulus_2_through_12": modulus_counterexamples,
        "verdict": "The predeclared DPC-QW prediction survives D(S4)." if not counterexamples else "D(S4) falsifies DPC-QW with a typed nonvacuum equal-dimension counterexample.",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
