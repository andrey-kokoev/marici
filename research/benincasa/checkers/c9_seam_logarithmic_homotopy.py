#!/usr/bin/env python3
"""Exact exterior-algebra audit of the C9 five-circuit seam homotopy."""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROLES = ("L_i", "R_i", "g_{i+1}", "G", "r_i")
ORDER = {f"dh{j}": 2 * j for j in range(5)} | {f"a{j}": 2 * j + 1 for j in range(5)}


def add(out, monomial, coefficient):
    if coefficient:
        out[monomial] += coefficient
        if out[monomial] == 0:
            del out[monomial]


def wedge(left, right):
    word = list(left + right)
    if len(set(word)) != len(word):
        return 0, ()
    inversions = sum(ORDER[word[i]] > ORDER[word[j]] for i in range(len(word)) for j in range(i + 1, len(word)))
    return (-1) ** inversions, tuple(sorted(word, key=ORDER.__getitem__))


def os_boundary(word):
    out = defaultdict(int)
    for position in range(len(word)):
        add(out, word[:position] + word[position + 1 :], (-1) ** position)
    return out


def parameter_derivative(form):
    out = defaultdict(int)
    for word, coefficient in form.items():
        for position, token in enumerate(word):
            if not token.startswith("a"):
                continue
            replacement = f"dh{token[1:]}"
            sign, canonical = wedge(word[:position], (replacement,) + word[position + 1 :])
            add(out, canonical, coefficient * sign)
    return dict(out)


def transgression_of_full_word():
    # T(a0...a4) = sum (-1)^k h_k a0...hat(a_k)...a4.
    # h_k is recorded separately as a scalar label.
    return [(k, (-1) ** k, tuple(f"a{j}" for j in range(5) if j != k)) for k in range(5)]


def d_of_os_boundary_transgression():
    out = defaultdict(int)
    for h_index, coefficient, word in transgression_of_full_word():
        for reduced, boundary_coefficient in os_boundary(word).items():
            sign, canonical = wedge((f"dh{h_index}",), reduced)
            # d_z and the degree-minus-one OS boundary anticommute in
            # the total complex, so H = -boundary_OS(T_mu).
            add(out, canonical, -coefficient * boundary_coefficient * sign)
    return dict(out)


def serialize(form):
    return [{"coefficient": form[word], "word": list(word)} for word in sorted(form)]


def main():
    seam = dict(os_boundary(tuple(f"a{j}" for j in range(5))))
    direct = parameter_derivative(seam)
    homotopy = d_of_os_boundary_transgression()
    if direct != homotopy:
        raise SystemExit("mixed seam defect does not equal the derived de Rham boundary")
    packet = {
        "schema": "marici.c9_seam_logarithmic_homotopy.v1",
        "ordered_roles": ROLES,
        "identity": "partial_mu boundary_OS(alpha_C) = -d_z boundary_OS T_mu(alpha_C)",
        "term_count": len(direct),
        "strictly_zero_before_quotient": not direct,
        "de_rham_exact": True,
        "closed_cycle_pairing": "zero by Stokes",
        "relative_cycle_pairing": "boundary_OS T_mu may pair with the physical relative boundary",
        "direct_defect": serialize(direct),
        "derived_boundary": serialize(homotopy),
    }
    output = Path(__file__).parents[1] / "results" / "c9-seam-logarithmic-homotopy.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"de_rham_exact": True, "term_count": len(direct), "strict": not direct}))


if __name__ == "__main__":
    main()
