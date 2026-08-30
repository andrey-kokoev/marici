"""Exact finite hostiles for controlled-observability DPC and closure ontology."""

from __future__ import annotations

import json
from pathlib import Path


X = range(20)
PHASES = range(5)


def record(frequency: int, phase: int) -> tuple[int, int]:
    return frequency % 4, (frequency + phase) % 5


def crt_decode(record_value: tuple[int, int], phase: int) -> int:
    a, b_shifted = record_value
    b = (b_shifted - phase) % 5
    return (5 * a + 16 * b) % 20


def passive_fibers() -> dict[tuple[int, int], list[tuple[int, int]]]:
    fibers: dict[tuple[int, int], list[tuple[int, int]]] = {}
    for f in X:
        for phase in PHASES:
            fibers.setdefault(record(f, phase), []).append((f, phase))
    return fibers


def unknown_reference_fibers() -> dict[tuple[tuple[int, int], tuple[int, int]], int]:
    fibers: dict[tuple[tuple[int, int], tuple[int, int]], int] = {}
    for f in X:
        for reference in X:
            for phase in PHASES:
                key = record(f, phase), record(reference, phase)
                fibers[key] = fibers.get(key, 0) + 1
    return fibers


def main() -> int:
    passive = passive_fibers()
    known_reference_joint = {
        (record(f, phase), record(0, phase)): (f, phase)
        for f in X
        for phase in PHASES
    }
    unknown = unknown_reference_fibers()

    # Minimal reset hostile. The hidden predecessor is delta in {0,1}; the
    # only readout is constant. Reset maps both states to zero. Complete
    # input/output traces remain equal even though the terminal state is known.
    reset_trace = {
        delta: (("observe", 0), ("reset", None), ("observe", 0))
        for delta in (0, 1)
    }
    reset_terminal = {delta: 0 for delta in (0, 1)}

    # An admissible policy sees the same empty/constant history in both hidden
    # states and must choose the same input. The oracle policy illegally reads x.
    admitted_policy_input = {x: "probe" for x in (0, 1)}
    oracle_policy_input = {x: x for x in (0, 1)}

    # Old experiment observes coordinate a; replacement observes b. The new
    # experiment separates a new b-target, but states (0,0) and (1,0) have the
    # same new law and different old laws. No state-independent garbling from b
    # can reconstruct a.
    states = [(0, 0), (1, 0), (0, 1), (1, 1)]
    old_output = {state: state[0] for state in states}
    replacement_output = {state: state[1] for state in states}
    blackwell_counterpair = ((0, 0), (1, 0))

    # Process hostile to one-step Blackwell sufficiency. Both instruments emit
    # the same first record, hence their terminal experiments are Blackwell
    # equivalent, but they prepare different successors revealed by one later
    # probe. Output equivalence forgets active residual capability.
    first_record = {"absorptive": "click", "qnd": "click"}
    successor = {"absorptive": 0, "qnd": 1}
    sequential_trace = {
        name: (first_record[name], successor[name]) for name in first_record
    }

    # Smallest nontrivial two-closure terminal collision without using identity:
    # both idempotents act on source 0, land at 1 versus 2, and a constant
    # terminal readout hides the residual capability distinguished by r(x)=x.
    closure_a = {0: 1, 1: 1, 2: 2}
    closure_b = {0: 2, 1: 1, 2: 2}
    terminal_readout = {0: 0, 1: 0, 2: 0}
    residual_probe = {0: 0, 1: 1, 2: 2}

    # Smallest autonomous dynamics not representable as iteration of one
    # idempotent closure: the two-state toggle has an infinite alternating trace.
    toggle = {0: 1, 1: 0}
    toggle_trace = []
    state = 0
    for _ in range(6):
        toggle_trace.append(state)
        state = toggle[state]

    checks = {
        "passive_clock_fibers_are_exactly_fivefold": set(map(len, passive.values())) == {5},
        "known_zero_reference_is_jointly_injective": len(known_reference_joint) == 100,
        "known_reference_decoder_recovers_every_source": all(
            crt_decode(record(f, phase), phase) == f for f in X for phase in PHASES
        ),
        "unknown_reference_leaves_fivefold_stabilizer": set(unknown.values()) == {5},
        "reset_makes_terminal_state_certain": len(set(reset_terminal.values())) == 1,
        "reset_does_not_separate_predecessor_traces": len(set(reset_trace.values())) == 1,
        "observation_history_policy_cannot_leak_hidden_state": len(set(admitted_policy_input.values())) == 1,
        "oracle_policy_would_leak_hidden_state": len(set(oracle_policy_input.values())) == 2,
        "replacement_separates_new_b_target": replacement_output[(0, 0)] != replacement_output[(0, 1)],
        "replacement_fails_blackwell_preservation": (
            replacement_output[blackwell_counterpair[0]] == replacement_output[blackwell_counterpair[1]]
            and old_output[blackwell_counterpair[0]] != old_output[blackwell_counterpair[1]]
        ),
        "one_step_instruments_are_blackwell_equivalent": len(set(first_record.values())) == 1,
        "blackwell_equivalent_instruments_have_distinct_future_traces": (
            len(set(sequential_trace.values())) == 2
        ),
        "both_closures_are_idempotent": all(
            closure[closure[x]] == closure[x]
            for closure in (closure_a, closure_b)
            for x in closure
        ),
        "bare_terminal_readout_hides_closure_order_result": (
            terminal_readout[closure_a[0]] == terminal_readout[closure_b[0]]
        ),
        "residual_capability_separates_closure_packets": (
            residual_probe[closure_a[0]] != residual_probe[closure_b[0]]
        ),
        "two_state_toggle_is_not_idempotent": any(toggle[toggle[x]] != toggle[x] for x in toggle),
        "coalgebraic_trace_retains_temporal_alternation": toggle_trace == [0, 1, 0, 1, 0, 1],
    }

    result = {
        "schema": "marici.sontag.dpc_controlled_observability_closure_attack.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "passive_fiber_size": sorted(set(map(len, passive.values()))),
        "unknown_reference_fiber_size": sorted(set(unknown.values())),
        "blackwell_counterpair": blackwell_counterpair,
        "toggle_trace": toggle_trace,
        "verdict": (
            "Trace observability survives as the dynamic gate. Blackwell preservation is necessary only "
            "for the terminal experiment shadow and is insufficient for process preservation. "
            "A bare idempotent closure is neither sufficient state nor a universal model of dynamics; "
            "a provenance-bearing packet survives only relative to declared future interventions, "
            "while coalgebraic trace semantics cleanly covers autonomous alternation."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "dpc_controlled_observability_closure_attack.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 0 if result["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
