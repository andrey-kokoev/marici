#!/usr/bin/env python3
"""Exact finite functoriality and no-retraction audit for U on typed graphs."""

from itertools import product


def graph(nodes, edges):
    return {"nodes": nodes, "edges": set(edges)}


def extend(x):
    nodes = dict(x["nodes"])
    edges = set(x["edges"])
    for n in x["nodes"]:
        nodes[f"m:{n}"] = ("object", "meta")
        nodes[f"r:{n}"] = ("record", "meta")
        edges.add((f"m:{n}", n, "models"))
        edges.add((f"r:{n}", f"m:{n}", "classifies"))
    return graph(nodes, edges)


def is_morphism(x, y, f):
    if set(f) != set(x["nodes"]):
        return False
    if any(f[n] not in y["nodes"] for n in x["nodes"]):
        return False
    if any(x["nodes"][n] != y["nodes"][f[n]] for n in x["nodes"]):
        return False
    return all((f[a], f[b], role) in y["edges"] for a, b, role in x["edges"])


def u_map(f):
    out = dict(f)
    for n, image in f.items():
        out[f"m:{n}"] = f"m:{image}"
        out[f"r:{n}"] = f"r:{image}"
    return out


def compose(g, f):
    return {n: g[f[n]] for n in f}


def strict_retractions(x):
    ux = extend(x)
    originals = list(x["nodes"])
    new = [n for n in ux["nodes"] if n not in x["nodes"]]
    for images in product(originals, repeat=len(new)):
        candidate = {n: n for n in originals}
        candidate.update(dict(zip(new, images)))
        if is_morphism(ux, x, candidate):
            yield candidate


def main():
    x = graph(
        {"a": ("object", "physical"), "b": ("record", "physical")},
        {("b", "a", "warrants")},
    )
    y = graph(
        {"A": ("object", "physical"), "B": ("record", "physical"),
         "C": ("object", "physical")},
        {("B", "A", "warrants")},
    )
    z = graph(
        {"p": ("object", "physical"), "q": ("record", "physical"),
         "s": ("object", "physical")},
        {("q", "p", "warrants")},
    )
    f = {"a": "A", "b": "B"}
    g = {"A": "p", "B": "q", "C": "s"}
    assert is_morphism(x, y, f)
    assert is_morphism(y, z, g)

    ux, uy, uz = extend(x), extend(y), extend(z)
    uf, ug = u_map(f), u_map(g)
    assert is_morphism(ux, uy, uf)
    assert is_morphism(uy, uz, ug)

    identity = {n: n for n in x["nodes"]}
    assert u_map(identity) == {n: n for n in ux["nodes"]}
    assert u_map(compose(g, f)) == compose(ug, uf)

    assert list(strict_retractions(x)) == []

    print("PASS: U preserves strict typed-graph morphisms")
    print("PASS: U preserves identity and composition on the finite diagram")
    print("PASS: exhaustive search finds no strict retraction U(X) -> X")


if __name__ == "__main__":
    main()
