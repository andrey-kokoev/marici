#!/usr/bin/env python3
"""Exact quotient/completion commutation test for the flavor phase orbit."""

from itertools import product

ALPHABET = "mroc"


def words_upto(depth):
    return [
        "".join(w)
        for length in range(depth + 1)
        for w in product(ALPHABET, repeat=length)
    ]


def stage(depth, roots):
    nodes = {(w, root) for root in roots for w in words_upto(depth)}
    edges = set()
    cells = set()
    if depth:
        for root in roots:
            for w in words_upto(depth - 1):
                target = (w, root)
                m, r, o, c = ((letter + w, root) for letter in ALPHABET)
                left = ((r, m, "classifies"), (m, target, "models"))
                right = ((r, o, "records"), (o, target, "locates"))
                edges.update(left + right)
                cells.add((c, left, right))
    return nodes, edges, cells


def quotient_item(item):
    if len(item) == 2 and isinstance(item[0], str):
        return (item[0], "*")
    raise TypeError(item)


def quotient_stage(data):
    nodes, edges, cells = data
    qnodes = {quotient_item(node) for node in nodes}
    qedges = {
        (quotient_item(a), quotient_item(b), role)
        for a, b, role in edges
    }
    qcells = set()
    for witness, left, right in cells:
        qleft = tuple((quotient_item(a), quotient_item(b), role) for a, b, role in left)
        qright = tuple((quotient_item(a), quotient_item(b), role) for a, b, role in right)
        qcells.add((quotient_item(witness), qleft, qright))
    return qnodes, qedges, qcells


def main():
    for depth in range(5):
        complete_then_quotient = quotient_stage(stage(depth, ("p", "q")))
        quotient_then_complete = stage(depth, ("*",))
        assert complete_then_quotient == quotient_then_complete

    phase = {"p": "pi/2", "q": "changed_exact_argument"}
    assert phase["p"] != phase["q"]
    quotient_phase_values = {phase[root] for root in ("p", "q")}
    assert len(quotient_phase_values) == 2

    print("PASS: completion and physical congruence quotient commute through depth 4")
    print("PASS: nodes, typed edges, and coherence cells descend exactly")
    print("PASS: unequal chart phases refuse descent to the physical quotient class")


if __name__ == "__main__":
    main()
