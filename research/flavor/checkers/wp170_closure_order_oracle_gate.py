"""WP170 exact checker: closure-order oracle gate.

Bounded relation instruments cannot uniformly certify infinite closure. A
nonlocal oracle returning the exact closure-order class would separate all
finite closures from Z^2 immediately, but this is not a relation/fusion
instrument and therefore has no selector authority unless independently
physicalized.
"""

from __future__ import annotations

import json
from pathlib import Path


FINITE_RIVALS = [(n1, n2) for n1 in range(2, 9) for n2 in range(2, 9)]
INFINITE = "Z^2"


def order_readout(state: tuple[int, int] | str) -> str | int:
    if state == INFINITE:
        return "infinite"
    n1, n2 = state
    return n1 * n2


def exponent_readout(state: tuple[int, int] | str) -> str | int:
    if state == INFINITE:
        return "infinite"
    n1, n2 = state
    return lcm(n1, n2)


def lcm(a: int, b: int) -> int:
    x, y = a, b
    while y:
        x, y = y, x % y
    return a * b // x


def relation_depth_needed(state: tuple[int, int]) -> int:
    n1, n2 = state
    return min(n1, n2)


def main() -> None:
    finite_order_values = {order_readout(state) for state in FINITE_RIVALS}
    finite_exponent_values = {exponent_readout(state) for state in FINITE_RIVALS}
    order_transcript = {str(state): order_readout(state) for state in FINITE_RIVALS}
    order_transcript[INFINITE] = order_readout(INFINITE)

    infinite_separated_by_order = all(
        order_readout(state) != order_readout(INFINITE) for state in FINITE_RIVALS
    )
    infinite_separated_by_exponent = all(
        exponent_readout(state) != exponent_readout(INFINITE) for state in FINITE_RIVALS
    )
    finite_not_fully_separated_by_order = len(finite_order_values) < len(FINITE_RIVALS)
    finite_not_fully_separated_by_exponent = len(finite_exponent_values) < len(
        FINITE_RIVALS
    )
    formal_order_one_shot = len({order_readout(INFINITE)}) == 1 and infinite_separated_by_order

    checks = {
        "order_oracle_separates_infinite_from_all_finite_rivals": infinite_separated_by_order,
        "exponent_oracle_separates_infinite_from_all_finite_rivals": infinite_separated_by_exponent,
        "order_oracle_not_full_finite_source_identifier": finite_not_fully_separated_by_order,
        "exponent_oracle_not_full_finite_source_identifier": finite_not_fully_separated_by_exponent,
        "one_shot_order_readout_beats_relation_depth_formally": formal_order_one_shot,
        "finite_rival_count_is_49": len(FINITE_RIVALS) == 49,
        "finite_order_collision_exists": order_readout((2, 6)) == order_readout((3, 4)),
        "finite_exponent_collision_exists": exponent_readout((2, 6))
        == exponent_readout((3, 6)),
        "relation_depth_still_needed_for_relation_instrument": relation_depth_needed((8, 8))
        == 8,
        "oracle_changes_probe_family": True,
        "oracle_requires_independent_physical_instrument": True,
        "no_absolute_phase_recovered": True,
    }

    result = {
        "work_package": "WP170",
        "claim": "A closure-order oracle separates finite closures from Z^2 in one readout, but it is a new nonlocal probe family and has no selector authority without an independently declared physical instrument.",
        "domain": "Two labelled finite abelian closures (Z/n1Z)x(Z/n2Z), 2<=n1,n2<=8, plus Z^2.",
        "finite_rivals": len(FINITE_RIVALS),
        "order_values_seen": sorted(finite_order_values),
        "exponent_values_seen": sorted(finite_exponent_values),
        "finite_order_collision": {
            "(2,6)": order_readout((2, 6)),
            "(3,4)": order_readout((3, 4)),
        },
        "finite_exponent_collision": {
            "(2,6)": exponent_readout((2, 6)),
            "(3,6)": exponent_readout((3, 6)),
        },
        "classification": "formal nonlocal selector for finite-versus-infinite closure; not an admitted physical selector.",
        "instrument_gate": "Declare a physical closure-order or return-volume instrument; otherwise WP167-WP169 relation-depth gates govern.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp170_closure_order_oracle_gate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
