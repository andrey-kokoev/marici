"""Exact finite audit of centralizer rigidity versus authorized source quotient."""

import itertools
import json
from pathlib import Path


N = 4
CYCLE = (1, 2, 3, 0)
MECHANISMS = tuple(itertools.product(range(N), repeat=N))


def compose(second, first):
    return tuple(second[first[x]] for x in range(N))


def natural(mechanism):
    return compose(mechanism, CYCLE) == compose(CYCLE, mechanism)


def parity(value):
    return value % 2


def high_bit(value):
    return value // 2


def coarse_actual_fit(mechanism):
    return parity(mechanism[0]) == parity(0)


def faithful_actual_fit(mechanism):
    return (parity(mechanism[0]), high_bit(mechanism[0])) == (0, 0)


def induced_mod2(mechanism):
    values = {}
    for source in range(N):
        key = parity(source)
        image = parity(mechanism[source])
        if key in values and values[key] != image:
            return None
        values[key] = image
    return tuple(values[key] for key in (0, 1))


def main():
    natural_maps = tuple(m for m in MECHANISMS if natural(m))
    coarse = tuple(m for m in natural_maps if coarse_actual_fit(m))
    faithful = tuple(m for m in natural_maps if faithful_actual_fit(m))
    quotient_maps = {induced_mod2(m) for m in coarse}
    identity = (0, 1, 2, 3)
    shift_two = (2, 3, 0, 1)

    checks = {
        "transitive_cycle_has_four_natural_mechanisms": len(natural_maps) == 4,
        "coarse_parity_actual_record_leaves_two": set(coarse) == {identity, shift_two},
        "surviving_pair_is_distinct_on_z4_source": identity != shift_two,
        "surviving_pair_has_same_mod2_quotient_map": quotient_maps == {(0, 1)},
        "shift_two_preserves_mod2_source_classes": induced_mod2(shift_two) == (0, 1),
        "parity_plus_high_bit_is_faithful_on_z4": len({(parity(x), high_bit(x)) for x in range(N)}) == N,
        "faithful_actual_probe_selects_identity": faithful == (identity,),
        "transitive_action_still_has_nontrivial_centralizer": len(natural_maps) > 1,
    }
    payload = {
        "schema": "marici.sontag.rigidity_modulo_authorized_gauge.v1",
        "passed": sum(checks.values()),
        "total": len(checks),
        "all_passed": all(checks.values()),
        "checks": checks,
        "natural_mechanisms": natural_maps,
        "coarse_survivors": coarse,
        "induced_mod2_maps": sorted(quotient_maps),
        "faithful_survivors": faithful,
        "verdict": (
            "Transitive counterfactual reach does not imply rigidity: coarse parity readout "
            "leaves identity and shift-by-two. They are one mechanism on the authorized Z2 "
            "source quotient but distinct unresolved mechanisms on a Z4 source. A faithful "
            "Z4 probe separates them. Explanatory rigidity must therefore be stated modulo "
            "a source-derived gauge quotient and checked in coordinates faithful on it."
        ),
    }
    output = Path(__file__).parents[1] / "results" / "rigidity_modulo_authorized_gauge.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if payload["all_passed"] else 1)


if __name__ == "__main__":
    main()
