#!/usr/bin/env python3
"""Exact reflection-witness criterion for strict self-model retractions."""


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
    return (
        set(f) == set(x["nodes"])
        and all(f[n] in y["nodes"] for n in x["nodes"])
        and all(x["nodes"][n] == y["nodes"][f[n]] for n in x["nodes"])
        and all((f[a], f[b], role) in y["edges"] for a, b, role in x["edges"])
    )


def witness_pairs(x, target):
    pairs = []
    for model, mt in x["nodes"].items():
        if mt != ("object", "meta"):
            continue
        if (model, target, "models") not in x["edges"]:
            continue
        for record, rt in x["nodes"].items():
            if rt == ("record", "meta") and (
                record, model, "classifies"
            ) in x["edges"]:
                pairs.append((model, record))
    return pairs


def construct_retraction(x):
    choices = {n: witness_pairs(x, n) for n in x["nodes"]}
    if any(not pairs for pairs in choices.values()):
        return None, [n for n, pairs in choices.items() if not pairs]
    mapping = {n: n for n in x["nodes"]}
    for n, pairs in choices.items():
        model, record = pairs[0]
        mapping[f"m:{n}"] = model
        mapping[f"r:{n}"] = record
    assert is_morphism(extend(x), x, mapping)
    return mapping, []


def main():
    ordinary = graph(
        {"a": ("object", "physical"), "b": ("record", "physical")},
        {("b", "a", "warrants")},
    )
    retraction, missing = construct_retraction(ordinary)
    assert retraction is None and set(missing) == {"a", "b"}

    nodes = {
        "a": ("object", "physical"),
        "b": ("record", "physical"),
        "M": ("object", "meta"),
        "R": ("record", "meta"),
    }
    edges = {("b", "a", "warrants"), ("R", "M", "classifies")}
    edges.update(("M", n, "models") for n in nodes)
    saturated = graph(nodes, edges)
    retraction, missing = construct_retraction(saturated)
    assert missing == [] and retraction is not None
    assert all(retraction[n] == n for n in saturated["nodes"])

    # Deliberate failure: removing one required model edge destroys splitting.
    broken = graph(nodes, edges - {("M", "R", "models")})
    retraction, missing = construct_retraction(broken)
    assert retraction is None and missing == ["R"]

    print("PASS: ordinary object fails exactly at missing reflection witnesses")
    print("PASS: reflection-complete finite object admits a strict retraction")
    print("PASS: deleting one witness edge destroys the retraction")


if __name__ == "__main__":
    main()
