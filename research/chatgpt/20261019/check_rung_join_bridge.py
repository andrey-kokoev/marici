#!/usr/bin/env python3
"""Exact finite controls for the Marici rung / homotopy-join comparison.

This independent checker follows the formulas inspected in the repository.
It does not execute Marici's Agda sources, prove a Hopf invariant, or infer an
infinite-space theorem from finite calculations. All linear ranks are over Q.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
import json
from pathlib import Path
from typing import Iterable

CHECKS: Counter[str] = Counter()


def check(condition: bool, label: str) -> None:
    CHECKS[label] += 1
    if not condition:
        raise AssertionError(label)


def faces(maximal: Iterable[tuple[int, ...]]) -> dict[int, list[tuple[int, ...]]]:
    found: dict[int, set[tuple[int, ...]]] = {}
    for simplex in maximal:
        simplex = tuple(sorted(simplex))
        for size in range(1, len(simplex) + 1):
            found.setdefault(size - 1, set()).update(combinations(simplex, size))
    return {degree: sorted(ss) for degree, ss in sorted(found.items())}


def boundary_columns(complex_: dict[int, list[tuple[int, ...]]], degree: int):
    if degree == 0:
        return [{} for _ in complex_.get(0, [])]
    index = {s: i for i, s in enumerate(complex_.get(degree - 1, []))}
    return [
        {index[s[:j] + s[j+1:]]: Fraction((-1) ** j) for j in range(len(s))}
        for s in complex_.get(degree, [])
    ]


def rational_rank(columns: list[dict[int, Fraction]]) -> int:
    """Sparse exact column elimination; no floating point or rank tolerance."""
    pivots: dict[int, dict[int, Fraction]] = {}
    for original in columns:
        column = dict(original)
        while column:
            pivot = min(column)
            a = column[pivot]
            if pivot not in pivots:
                pivots[pivot] = {i: value / a for i, value in column.items()}
                break
            for i, value in pivots[pivot].items():
                new = column.get(i, Fraction(0)) - a * value
                if new:
                    column[i] = new
                else:
                    column.pop(i, None)
    return len(pivots)


def homology(complex_: dict[int, list[tuple[int, ...]]]) -> dict:
    last = max(complex_, default=0)
    columns = {d: boundary_columns(complex_, d) for d in range(last + 1)}
    for d in range(2, last + 1):
        for col in columns[d]:
            twice: dict[int, Fraction] = {}
            for row, coeff in col.items():
                for target, value in columns[d-1][row].items():
                    twice[target] = twice.get(target, Fraction(0)) + coeff * value
            check(all(value == 0 for value in twice.values()), "boundary_squared_zero")
    ranks = {d: rational_rank(columns[d]) for d in columns}
    betti = [len(complex_.get(d, [])) - ranks[d] - ranks.get(d+1, 0)
             for d in range(last+1)]
    return {"f_vector": [len(complex_.get(d, [])) for d in range(last+1)],
            "boundary_ranks_Q": [ranks[d] for d in range(last+1)], "betti_Q": betti}


def cycle(n: int, offset: int = 0) -> list[tuple[int, int]]:
    return [tuple(sorted((offset+i, offset+(i+1) % n))) for i in range(n)]


def join_cycles(m: int) -> dict[int, list[tuple[int, ...]]]:
    facets = [tuple(v for edge in edges for v in edge)
              for edges in product(*(cycle(4, 4*k) for k in range(m)))]
    return faces(facets)


def graph_iso(edges_a: list[tuple[int, int]], edges_b: list[tuple[int, int]], n: int) -> bool:
    target = {tuple(sorted(e)) for e in edges_b}
    return any({tuple(sorted((p[u], p[v]))) for u, v in edges_a} == target
               for p in permutations(range(n)))


def line_graph(edges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    return [(i, j) for i, j in combinations(range(len(edges)), 2)
            if set(edges[i]) & set(edges[j])]


def main(output: Path) -> None:
    report: dict = {}
    # Retained homotopy-total formula specialized to finite sets.
    # The membership witness here is unique; higher-valued cases use the theorem.
    maps_tested = 0
    for n in range(5):
        for k in range(1, 4):
            for values in product(range(k), repeat=n):
                total = [(key, row) for key in range(k) for row in range(n)
                         if values[row] == key]
                check(sorted(row for _, row in total) == list(range(n)), "table_total_recovery")
                check(all((values[row], row) == (key, row) for key, row in total), "table_total_inverse")
                maps_tested += 1
    report["finite_table_maps_checked"] = maps_tested

    # Both source and target indexed row presentations retain the same span.
    for n, m in product(range(1, 6), repeat=2):
        rows = list(product(range(n), range(m)))
        by_source = {a: [(a, b) for b in range(m)] for a in range(n)}
        by_target = {b: [(a, b) for a in range(n)] for b in range(m)}
        check(sorted(x for group in by_source.values() for x in group) == rows,
              "complete_pair_source_recovery")
        check(sorted(x for group in by_target.values() for x in group) == rows,
              "complete_pair_target_recovery")

    report["circle"] = homology(faces(cycle(4)))
    check(report["circle"]["betti_Q"] == [1, 1], "circle_homology")
    # A finite model for the two-point-span homotopy pushout has two parallel edges.
    rank_parallel = rational_rank([{0: Fraction(-1), 1: Fraction(1)}] * 2)
    report["two_point_span_homotopy_pushout"] = {"vertices": 2, "edges": 2,
                                               "betti_Q": [2-rank_parallel, 2-rank_parallel]}
    check(rank_parallel == 1, "two_point_span_circle")

    old = cycle(4)
    line_reports = []
    for iteration in range(1, 7):
        new = line_graph(old)
        check(graph_iso(new, cycle(4), 4), "line_graph_cycle_fixed_point")
        line_reports.append({"iteration": iteration, **homology(faces(new))})
        old = new
    report["line_graph_on_cycle"] = line_reports

    # Different realizations of the same two four-vertex endpoint inventories.
    cross_only = [(a, b) for a in range(4) for b in range(4, 8)]
    report["discrete_complete_pair_span"] = homology(faces(cross_only))
    report["cycle_edges_and_cross_edges_no_higher_cells"] = homology(
        faces(cross_only + cycle(4) + cycle(4, 4)))
    check(report["discrete_complete_pair_span"]["betti_Q"] == [1, 9], "discrete_span_not_hopf_total")
    check(report["cycle_edges_and_cross_edges_no_higher_cells"]["betti_Q"] == [1, 17],
          "one_skeleton_not_hopf_total")

    joins = []
    for m in (1, 2, 3):
        h = homology(join_cycles(m))
        expected = [1] + [0] * (2*m-2) + [1]
        check(h["betti_Q"] == expected, "full_circle_join_homology")
        joins.append({"circle_factors": m, **h})
    report["full_circle_joins"] = joins

    # Every D4 x D4 relabelling extends to the full two-cycle join.
    full = join_cycles(2)
    d4 = [tuple((sign*i + shift) % 4 for i in range(4))
          for sign in (1, -1) for shift in range(4)]
    for p, q in product(d4, repeat=2):
        perm = tuple(p) + tuple(x+4 for x in q)
        for d, ss in full.items():
            image = {tuple(sorted(perm[v] for v in s)) for s in ss}
            check(image == set(ss), "join_dihedral_covariance")

    # All fibers are nonempty but there is no edge-compatible section of C8 -> C4.
    cover_edges = {frozenset(e) for e in cycle(8)}
    sections = []
    for bits in product((0, 1), repeat=4):
        section = tuple(i + 4*bits[i] for i in range(4))
        if all(frozenset((section[i], section[(i+1) % 4])) in cover_edges for i in range(4)):
            sections.append(section)
    check(len(sections) == 0, "connected_double_cover_no_section")
    trivial_edges = {frozenset(e) for e in cycle(4) + cycle(4, 4)}
    trivial_sections = []
    for bits in product((0, 1), repeat=4):
        section = tuple(i + 4*bits[i] for i in range(4))
        if all(frozenset((section[i], section[(i+1) % 4])) in trivial_edges for i in range(4)):
            trivial_sections.append(section)
    check(len(trivial_sections) == 2, "trivial_double_cover_two_sections")
    report["finite_cover_control"] = {"vertexwise_choices": 16,
        "connected_C8_cover_sections": sections, "trivial_cover_sections": trivial_sections,
        "scope": "A finite covering-space control, not a numerical proof about the Hopf bundle."}

    # Finite C_N test of (E x T)/G, with E another G-torsor. This does NOT
    # replace continuous U(1) by C_N in the topological theorem.
    finite_orbits = []
    for n in range(2, 10):
        orbits = {frozenset((((a+g) % n), ((t+g) % n)) for g in range(n))
                  for a, t in product(range(n), repeat=2)}
        differences = [{(a-t) % n for a, t in orbit} for orbit in orbits]
        check(len(orbits) == n and all(len(x) == 1 for x in differences), "diagonal_product_quotient")
        finite_orbits.append({"group_order": n, "orbit_count": len(orbits)})
    report["finite_diagonal_orbit_controls"] = finite_orbits
    report["not_machine_proved"] = [
        "Marici Agda compilation or native admission of the new join-span request",
        "Continuous Hopf-bundle nonsection theorem",
        "Homotopy-orbit pushout and projective-space identifications",
        "Sequential homotopy-colimit equivalence to BU(1)",
        "Original tetrahedral A4 action or nonabelian gauge structure"]
    report["status"] = "pass"
    report["counts"] = dict(sorted(CHECKS.items()))
    report["total_assertions"] = sum(CHECKS.values())
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": report["status"], "assertions": report["total_assertions"],
        "circle_joins": joins, "discrete_span_betti": report["discrete_complete_pair_span"]["betti_Q"],
        "cover_sections": len(sections), "output": str(output)}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path(__file__).with_name("rung_join_cofiber_bridge_results.json"))
    args = parser.parse_args()
    main(args.output)
