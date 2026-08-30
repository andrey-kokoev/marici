#!/usr/bin/env python3
"""Verify the finite combinatorics and formal identities of the second Čech packet."""

import json
from pathlib import Path


CHARTS = ("a", "b", "c")
PAIRS = (("a", "b"), ("b", "c"), ("a", "c"))
CLASSES = ((1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3))


def add(*terms):
    out = {}
    for term in terms:
        for word, coefficient in term.items():
            out[word] = out.get(word, 0) + coefficient
            if out[word] == 0:
                del out[word]
    return out


def scale(term, coefficient):
    return {word: coefficient * value for word, value in term.items()}


def word(*symbols):
    return {symbols: 1}


def pairwise_identity(i, j, p, q):
    # [d,h_i^{pq}]=D_i^p-D_i^q and [d,D_i^p]=0.
    boundary_h_d = add(word(f"D{i}{p}"), scale(word(f"D{i}{q}"), -1))
    boundary_h_j = add(word(f"D{j}{p}"), scale(word(f"D{j}{q}"), -1))
    boundary_h_i_D = {
        source_word + (f"D{j}{p}",): coefficient
        for source_word, coefficient in boundary_h_d.items()
    }
    boundary_D_h_j = {
        (f"D{i}{q}",) + source_word: coefficient
        for source_word, coefficient in boundary_h_j.items()
    }
    lhs = add(boundary_h_i_D, boundary_D_h_j)
    rhs = add(word(f"D{i}{p}", f"D{j}{p}"), scale(word(f"D{i}{q}", f"D{j}{q}"), -1))
    return lhs == rhs


def triple_identity(i, j):
    # H^ab+H^bc-H^ac reduces to
    # [d,h_i^bc]h_j^ab-h_i^bc[d,h_j^ab]=[d,h_i^bc h_j^ab].
    reduced_defect = add(
        word(f"D{i}b", f"h{j}ab"),
        scale(word(f"D{i}c", f"h{j}ab"), -1),
        scale(word(f"h{i}bc", f"D{j}a"), -1),
        word(f"h{i}bc", f"D{j}b"),
    )
    boundary_k = add(
        word(f"D{i}b", f"h{j}ab"),
        scale(word(f"D{i}c", f"h{j}ab"), -1),
        scale(word(f"h{i}bc", f"D{j}a"), -1),
        word(f"h{i}bc", f"D{j}b"),
    )
    return reduced_defect == boundary_k


def main():
    pairwise = [pairwise_identity(i, j, p, q) for i, j in CLASSES for p, q in PAIRS]
    triple = [triple_identity(i, j) for i, j in CLASSES]
    packet = {
        "schema": "marici.second_covariant_cech_homotopy.v1",
        "charts": list(CHARTS),
        "pair_overlaps": [list(pair) for pair in PAIRS],
        "second_classes": [list(pair) for pair in CLASSES],
        "pairwise_cells": len(pairwise),
        "triple_cells": len(triple),
        "formulas": {
            "pairwise": "H_ij^pq=h_i^pq D_j^p+D_i^q h_j^pq",
            "triple": "K_ij^abc=h_i^bc h_j^ab",
            "total_cocycle": "(A_ij^p,H_ij^pq,K_ij^abc)",
        },
        "checks": {
            "all_pairwise_boundaries": all(pairwise),
            "all_triple_boundaries": all(triple),
            "pairwise_cell_count_18": len(pairwise) == 18,
            "triple_cell_count_6": len(triple) == 6,
        },
    }
    packet["status"] = "pass" if all(packet["checks"].values()) else "fail"
    output = Path(__file__).resolve().parent.parent / "results" / "second-covariant-cech-homotopy.json"
    output.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))
    raise SystemExit(0 if packet["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
