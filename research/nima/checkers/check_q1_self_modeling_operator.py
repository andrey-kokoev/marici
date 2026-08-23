#!/usr/bin/env python3
"""Finite closure and deliberate-failure tests for the Q-1 self-model operator."""

from copy import deepcopy

KINDS = {"object", "morphism", "obstruction", "record"}


def base_state():
    return {
        "nodes": {
            "q1_hard_core": {"kind": "object", "level": "physical"},
            "q_trivial_monodromy": {"kind": "record", "level": "physical"},
            "leray_covector": {"kind": "object", "level": "physical"},
        },
        "arrows": [
            {"src": "q_trivial_monodromy", "dst": "q1_hard_core",
             "kind": "morphism", "role": "warrants"},
        ],
    }


def extend(state, depth):
    out = deepcopy(state)
    snapshot = sorted(state["nodes"])
    for name in snapshot:
        model = f"model_d{depth}:{name}"
        readout = f"readout_d{depth}:{name}"
        out["nodes"][model] = {"kind": "object", "level": "meta"}
        out["nodes"][readout] = {"kind": "record", "level": "meta"}
        out["arrows"].extend([
            {"src": model, "dst": name, "kind": "morphism", "role": "models"},
            {"src": readout, "dst": model, "kind": "morphism", "role": "classifies"},
        ])
    return out


def validate(state):
    nodes = state["nodes"]
    assert all(v["kind"] in KINDS for v in nodes.values())
    for arrow in state["arrows"]:
        assert arrow["kind"] in KINDS
        assert arrow["src"] in nodes and arrow["dst"] in nodes
        if arrow["role"] == "warrants":
            assert nodes[arrow["src"]]["level"] == "physical", (
                "meta records may not certify physical claims"
            )


def physical_restriction(state):
    names = {n for n, v in state["nodes"].items() if v["level"] == "physical"}
    arrows = {
        (a["src"], a["dst"], a["kind"], a["role"])
        for a in state["arrows"] if a["src"] in names and a["dst"] in names
    }
    return names, arrows


def forget_depth(state, depth):
    prefix_a = f"model_d{depth}:"
    prefix_b = f"readout_d{depth}:"
    kept = {
        n: v for n, v in state["nodes"].items()
        if not (n.startswith(prefix_a) or n.startswith(prefix_b))
    }
    arrows = [
        a for a in state["arrows"]
        if a["src"] in kept and a["dst"] in kept
    ]
    return {"nodes": kept, "arrows": arrows}


def main():
    x = base_state()
    ux = extend(x, 1)
    uux = extend(ux, 2)
    validate(x)
    validate(ux)
    validate(uux)
    assert physical_restriction(ux) == physical_restriction(x)
    assert forget_depth(uux, 2) == ux

    # Deliberate failure: a meta readout must not become physical evidence.
    bad = deepcopy(ux)
    bad["arrows"].append({
        "src": "readout_d1:q1_hard_core", "dst": "q1_hard_core",
        "kind": "morphism", "role": "warrants",
    })
    rejected = False
    try:
        validate(bad)
    except AssertionError:
        rejected = True
    assert rejected

    print("PASS: Q-1 self-model extension is conservative and recursively typed")
    print("PASS: depth-two induced-subgraph truncation recovers depth one")
    print("PASS: deliberate meta-self-certification is rejected")


if __name__ == "__main__":
    main()
