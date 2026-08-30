"""Exact finite test of counterfactual reach versus mechanism rigidity."""

import itertools
import json
from pathlib import Path


N = 4
MECHANISMS = tuple(itertools.product(range(N), repeat=N))
IDENTITY = tuple(range(N))
SWAP_01 = (1, 0, 2, 3)
SWAP_23 = (0, 1, 3, 2)
SWAP_12 = (0, 2, 1, 3)


def compose(second, first):
    return tuple(second[first[x]] for x in range(N))


def natural(mechanism, generators):
    return all(compose(mechanism, g) == compose(g, mechanism) for g in generators)


def actual_fit(mechanism):
    return mechanism[0] == 0


def survivors(generators):
    return tuple(m for m in MECHANISMS if actual_fit(m) and natural(m, generators))


def orbit(start, generators):
    reached = {start}
    changed = True
    while changed:
        changed = False
        for point in tuple(reached):
            for g in generators:
                image = g[point]
                if image not in reached:
                    reached.add(image)
                    changed = True
    return tuple(sorted(reached))


def main():
    none = survivors(())
    disconnected = survivors((SWAP_01, SWAP_23))
    connected = survivors((SWAP_01, SWAP_23, SWAP_12))
    checks = {
        "actual_record_alone_leaves_sixty_four_mechanisms": len(none) == 64,
        "single_component_swap_leaves_a_rival": len(disconnected) > 1,
        "disconnected_orbit_misses_second_component": orbit(0, (SWAP_01, SWAP_23)) == (0, 1),
        "surviving_disconnected_rival_is_not_identity": any(m != IDENTITY for m in disconnected),
        "bridge_swap_connects_all_sources": orbit(0, (SWAP_01, SWAP_23, SWAP_12)) == (0, 1, 2, 3),
        "connected_counterfactual_action_selects_identity": connected == (IDENTITY,),
        "identity_is_natural_for_all_generators": natural(IDENTITY, (SWAP_01, SWAP_23, SWAP_12)),
        "bridge_strictly_reduces_survivor_space": len(connected) < len(disconnected),
    }
    payload = {
        "schema": "marici.sontag.counterfactual_centralizer_rigidity.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "survivors": {
            "actual_only": none,
            "swap_01_and_swap_23": disconnected,
            "plus_bridge_swap_12": connected,
        },
        "survivor_counts": {
            "actual_only": len(none),
            "disconnected_counterfactuals": len(disconnected),
            "connected_counterfactuals": len(connected),
        },
        "verdict": (
            "Naturality is explanatory only relative to a sufficiently discriminating, "
            "independently admitted counterfactual action. A disconnected source-variation "
            "orbit leaves a nontrivial mechanism centralizer; adding a bridge generator makes "
            "the four-source action rigid and uniquely selects identity among actual-fit maps."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "counterfactual_centralizer_rigidity.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["all_passed"] else 1)


if __name__ == "__main__":
    main()
