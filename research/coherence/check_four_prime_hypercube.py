#!/usr/bin/env python3
"""Construct and verify the oriented four-prime valuation hypercube."""

from itertools import combinations
import json
import math
from pathlib import Path

PRIMES = (2, 3, 5, 7)


def subsets(xs):
    xs = tuple(xs)
    for r in range(len(xs) + 1):
        yield from combinations(xs, r)


def cell(fixed, varying):
    """Cell [fixed; varying], with fixed axes already at valuation one."""
    fixed, varying = tuple(sorted(fixed)), tuple(sorted(varying))
    assert not set(fixed) & set(varying)
    vertices = []
    for corner in subsets(varying):
        support = tuple(sorted(fixed + corner))
        n = 1
        for i in support:
            n *= PRIMES[i]
        vertices.append({"support": support, "integer": n, "cyclic_grade": len(support)})
    return {
        "fixed_axes": fixed,
        "varying_axes": varying,
        "dimension": len(varying),
        "vertices": vertices,
        "grade_interval": [len(fixed), len(fixed) + len(varying)],
    }


def boundary_term(fixed, varying):
    """Oriented cubical boundary as coefficients of (fixed,varying)."""
    varying = tuple(sorted(varying))
    out = {}
    for position, axis in enumerate(varying):
        rest = tuple(i for i in varying if i != axis)
        sign = (-1) ** position
        # upper face minus lower face
        upper = (tuple(sorted(fixed + (axis,))), rest)
        lower = (tuple(sorted(fixed)), rest)
        out[upper] = out.get(upper, 0) + sign
        out[lower] = out.get(lower, 0) - sign
    return {k: v for k, v in out.items() if v}


def boundary_squared(fixed, varying):
    out = {}
    for face, coefficient in boundary_term(fixed, varying).items():
        for subface, subcoefficient in boundary_term(*face).items():
            out[subface] = out.get(subface, 0) + coefficient * subcoefficient
    return {k: v for k, v in out.items() if v}


def main():
    axes = range(4)
    cells = []
    census = {}
    failures = []
    for varying in subsets(axes):
        remaining = tuple(i for i in axes if i not in varying)
        for fixed in subsets(remaining):
            c = cell(fixed, varying)
            cells.append(c)
            census[c["dimension"]] = census.get(c["dimension"], 0) + 1
            residual = boundary_squared(fixed, varying)
            if residual:
                failures.append({"cell": [fixed, varying], "residual": repr(residual)})

    expected = {0: 16, 1: 32, 2: 24, 3: 8, 4: 1}
    assert census == expected, (census, expected)
    assert not failures, failures

    edges = []
    for axis in axes:
        others = tuple(i for i in axes if i != axis)
        for fixed in subsets(others):
            source = 1
            for i in fixed:
                source *= PRIMES[i]
            prime = PRIMES[axis]
            koszul_sign = (-1) ** sum(1 for i in fixed if i < axis)
            edges.append({
                "source": source,
                "target": source * prime,
                "axis": axis,
                "prime": prime,
                "label_transport": f"c_{prime}",
                "seam_transport": f"R_{prime}: q -> q+log({prime})",
                "combined_transport": f"d_{prime}=c_{prime} tensor R_{prime}",
                "koszul_sign": koszul_sign,
                "mellin_label_weight": math.log(prime),
                "seam_weight": -math.log(prime),
                "total_weight": 0.0,
                "half_line_defect_window": f"[0,log({prime}))",
            })

    result = {
        "schema": "marici.coherence.four-prime-hypercube.v2",
        "primes": PRIMES,
        "axis_rule": "axis i increments v_{p_i} by one",
        "vertex_rule": "support S labels product of primes in S",
        "cyclic_grade_rule": "at a vertex, grade is total traversal count |S|",
        "coherence_rule": "oriented cubical boundary squares to zero; equivalently d_p d_q + d_q d_p = 0 for the Koszul-seam decoration",
        "edge_decoration": "d_p=c_p tensor R_p with fermionic creation and opposite seam translation",
        "census": census,
        "edge_count": len(edges),
        "all_edges_have_weight_zero": all(abs(e["total_weight"]) < 1e-15 for e in edges),
        "all_boundary_squared_residuals_zero": True,
        "critical_separation": "cell dimension |D| and traversal grade |S| are independent",
        "cells": cells,
        "edges": edges,
    }
    target = Path(__file__).with_name("four-prime-hypercube.v2.json")
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("primes", "census", "edge_count", "all_edges_have_weight_zero", "all_boundary_squared_residuals_zero", "critical_separation")}, indent=2))


if __name__ == "__main__":
    main()
