import json
from pathlib import Path


def partition(states, signatures):
    blocks = {}
    for state in states:
        key = tuple(f(state) for f in signatures)
        blocks.setdefault(key, []).append(state)
    return sorted((sorted(block, key=str) for block in blocks.values()), key=str)


def iterates(step, readout, depth):
    probes = []
    for n in range(depth + 1):
        def probe(state, n=n):
            for _ in range(n):
                state = step(state)
            return readout(state)
        probes.append(probe)
    return probes


def main():
    # Delayed separation: a0 and b0 agree through depth one, separate at two.
    delayed_states = ["a0", "b0", "a1", "b1", "a2", "b2"]
    delayed_step = {
        "a0": "a1", "b0": "b1",
        "a1": "a2", "b1": "b2",
        "a2": "a2", "b2": "b2",
    }.__getitem__
    delayed_readout = lambda s: 1 if s == "b2" else 0
    delayed_depth1 = tuple(p("a0") == p("b0") for p in iterates(delayed_step, delayed_readout, 1))
    delayed_depth2 = tuple(p("a0") == p("b0") for p in iterates(delayed_step, delayed_readout, 2))

    # Permanent aliasing: contexts toggle only the hidden second bit while the
    # readout sees only the first.  The finite generated monoid is {id,toggle}.
    states = [(a, b) for a in (0, 1) for b in (0, 1)]
    toggle = lambda x: (x[0], x[1] ^ 1)
    readout = lambda x: x[0]
    full_context_probes = [readout, lambda x: readout(toggle(x))]
    contextual_partition = partition(states, full_context_probes)
    expected_partition = [[(0, 0), (0, 1)], [(1, 0), (1, 1)]]

    # Unauthorized enlargement by the second-bit probe would make the source
    # faithful; this demonstrates that faithfulness is language-relative.
    enlarged_partition = partition(states, full_context_probes + [lambda x: x[1]])

    # Every generated contextual readout factors through the canonical class
    # label, here the first bit.
    quotient = lambda x: x[0]
    factors_through_quotient = all(
        all(p(x) == p(y) for x in states for y in states if quotient(x) == quotient(y))
        for p in full_context_probes
    )

    gates = {
        "one_step_closure_misses_delayed_distinction": all(delayed_depth1),
        "two_step_composition_detects_delayed_distinction": delayed_depth2 == (True, True, False),
        "full_generated_context_can_remain_nonfaithful": contextual_partition == expected_partition,
        "unauthorized_probe_would_refine_to_singletons": all(len(block) == 1 for block in enlarged_partition),
        "all_authorized_contexts_factor_through_contextual_quotient": factors_through_quotient,
    }
    assert all(gates.values()), gates

    result = {
        "schema": "marici.contextual-faithfulness-falsifier.v1",
        "gates": gates,
        "delayed": {
            "equal_through_depth_one": list(delayed_depth1),
            "equal_through_depth_two": list(delayed_depth2),
        },
        "permanent_aliasing": {
            "contextual_partition": contextual_partition,
            "enlarged_partition": enlarged_partition,
        },
        "conclusion": "context closure defines a canonical operational quotient but need not separate source states",
    }
    out = Path(__file__).parents[1] / "results" / "contextual-faithfulness-falsifier.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
