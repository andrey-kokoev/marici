"""Exact minimal interference witness for pointwise replay certificates."""

import itertools
import json
from pathlib import Path


def compose(second, first):
    return tuple(second[first[state]] for state in range(len(first)))


def preserves_globally(mapping, replay):
    return all(replay[mapping[state]] == replay[state] for state in range(len(mapping)))


def witnesses(size):
    base = 0
    maps = tuple(itertools.product(range(size), repeat=size))
    for replay_tail in itertools.product((0, 1), repeat=size - 1):
        replay = (0,) + replay_tail
        for first in maps:
            if replay[first[base]] != replay[base]:
                continue
            for second in maps:
                if replay[second[base]] != replay[base]:
                    continue
                composite = compose(second, first)
                if replay[composite[base]] != replay[base]:
                    yield replay, first, second, composite


def all_global_pairs_compose(size):
    maps = tuple(itertools.product(range(size), repeat=size))
    for replay in itertools.product((0, 1), repeat=size):
        good = tuple(mapping for mapping in maps if preserves_globally(mapping, replay))
        for first in good:
            for second in good:
                if not preserves_globally(compose(second, first), replay):
                    return False
    return True


def main():
    small_counts = {size: sum(1 for _ in witnesses(size)) for size in (1, 2)}
    replay, first, second, composite = next(witnesses(3))
    intermediate = first[0]

    checks = {
        "no_one_state_interference_witness": small_counts[1] == 0,
        "no_two_state_interference_witness": small_counts[2] == 0,
        "three_state_witness_exists": replay is not None,
        "first_extension_passes_at_base": replay[first[0]] == replay[0],
        "second_extension_passes_at_base": replay[second[0]] == replay[0],
        "composite_fails_at_base": replay[composite[0]] != replay[0],
        "second_fails_on_reachable_intermediate": replay[second[intermediate]] != replay[intermediate],
        "first_is_not_a_global_replay_morphism": not preserves_globally(first, replay),
        "second_is_not_a_global_replay_morphism": not preserves_globally(second, replay),
        "global_replay_morphisms_compose_for_three_states": all_global_pairs_compose(3),
    }
    payload = {
        "schema": "marici.sontag.replay_preservation_composition.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "minimal_witness": {
            "states": 3,
            "base": 0,
            "replay": replay,
            "first": first,
            "second": second,
            "composite_second_after_first": composite,
            "intermediate": intermediate,
        },
        "verdict": (
            "Pointwise base-packet replay certificates are not compositional; the smallest "
            "interference witness has three states. No new higher coherence datum is needed "
            "when extensions are globally typed replay morphisms. For partial certificates, "
            "the missing coherence obligation is that the later extension preserve replay "
            "on the earlier extension's reachable image."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "replay_preservation_composition.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["all_passed"] else 1)


if __name__ == "__main__":
    main()
