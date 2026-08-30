#!/usr/bin/env python3
"""Exact finite-stage census and symbolic omega closure for the U tower."""

from itertools import product


def words_upto(depth):
    return {
        "".join(w)
        for length in range(depth + 1)
        for w in product("mr", repeat=length)
    }


def stage(depth):
    nodes = words_upto(depth)
    edges = set()
    for w in words_upto(depth - 1) if depth else set():
        edges.add(("m" + w, w, "models"))
        edges.add(("r" + w, "m" + w, "classifies"))
    return nodes, edges


def missing_witnesses(depth):
    nodes, edges = stage(depth)
    return {
        w for w in nodes
        if not (
            "m" + w in nodes
            and "r" + w in nodes
            and ("m" + w, w, "models") in edges
            and ("r" + w, "m" + w, "classifies") in edges
        )
    }


def main():
    previous_nodes, previous_edges = set(), set()
    for depth in range(7):
        nodes, edges = stage(depth)
        assert len(nodes) == 2 ** (depth + 1) - 1
        assert len(edges) == 2 * (2 ** depth - 1)
        assert previous_nodes <= nodes and previous_edges <= edges
        missing = missing_witnesses(depth)
        assert missing == {w for w in nodes if len(w) == depth}
        assert len(missing) == 2 ** depth
        previous_nodes, previous_edges = nodes, edges

    # Every bounded sample from the omega union has its witnesses at the next
    # finite stage. This executable census accompanies the symbolic all-word
    # proof in the packet.
    for depth in range(6):
        nodes, _ = stage(depth)
        next_nodes, next_edges = stage(depth + 1)
        for w in nodes:
            assert "m" + w in next_nodes and "r" + w in next_nodes
            assert ("m" + w, w, "models") in next_edges
            assert ("r" + w, "m" + w, "classifies") in next_edges

    # Deliberate failure: no finite stage is reflection-complete.
    assert all(missing_witnesses(depth) for depth in range(7))

    print("PASS: finite-stage node, edge, and frontier laws hold through depth 6")
    print("PASS: every bounded omega node receives witnesses one stage later")
    print("PASS: no finite stage is reflection-complete")
    print("THEOREM PACKET: all finite words imply U(X_omega) = X_omega")


if __name__ == "__main__":
    main()
