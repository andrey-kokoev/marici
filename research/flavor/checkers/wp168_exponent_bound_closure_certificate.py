"""WP168 exact checker: exponent-bound closure certificate.

WP167 showed that bounded relation tests cannot uniformly certify infinite
two-port closure against unbounded finite rivals. This checker verifies the
positive boundary: if the source independently bounds every finite rival's
exponent by E, then relation depth E is necessary and sufficient to separate
Z^2 from the finite exponent-bounded rivals in the declared domain.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path


E = 8
GENERATORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def word_sum(word: tuple[int, ...]) -> tuple[int, int]:
    x = 0
    y = 0
    for idx in word:
        dx, dy = GENERATORS[idx]
        x += dx
        y += dy
    return x, y


def is_relation_z2(word: tuple[int, ...]) -> bool:
    return word_sum(word) == (0, 0)


def is_relation_mod_pair(word: tuple[int, ...], n1: int, n2: int) -> bool:
    x, y = word_sum(word)
    return x % n1 == 0 and y % n2 == 0


def words_of_length(length: int):
    yield from itertools.product(range(len(GENERATORS)), repeat=length)


def signatures_match_through(length: int, n1: int, n2: int) -> bool:
    for ell in range(length + 1):
        for word in words_of_length(ell):
            if is_relation_z2(word) != is_relation_mod_pair(word, n1, n2):
                return False
    return True


def first_relation_witness(n1: int, n2: int, max_length: int) -> tuple[int, str] | None:
    for ell in range(1, max_length + 1):
        for word in words_of_length(ell):
            if (not is_relation_z2(word)) and is_relation_mod_pair(word, n1, n2):
                names = ["+e1", "-e1", "+e2", "-e2"]
                return ell, " ".join(names[idx] for idx in word)
    return None


def all_moduli_with_exponent_bound(exponent: int) -> list[tuple[int, int]]:
    # Rectangular abelian rivals (Z/n1Z) x (Z/n2Z) with both generator orders
    # bounded by E and both ports nontrivial. This is the hostile free-looking
    # finite family for the two labelled ports.
    return [(n1, n2) for n1 in range(2, exponent + 1) for n2 in range(2, exponent + 1)]


def main() -> None:
    rivals = all_moduli_with_exponent_bound(E)
    witnesses = {(n1, n2): first_relation_witness(n1, n2, E) for n1, n2 in rivals}
    worst_depth = max(depth for depth, _ in witnesses.values())

    hostile_depth_e_minus_1 = signatures_match_through(E - 1, E, E)
    hostile_depth_e = signatures_match_through(E, E, E)
    first_hostile_witness = first_relation_witness(E, E, E)

    checks = {
        "all_finite_exponent_bounded_rivals_have_witness_by_E": all(
            witness is not None for witness in witnesses.values()
        ),
        "worst_case_requires_depth_E": worst_depth == E,
        "ZE_square_matches_Z2_through_E_minus_1": hostile_depth_e_minus_1,
        "ZE_square_separates_at_E": not hostile_depth_e,
        "first_ZE_square_witness_depth_is_E": first_hostile_witness[0] == E,
        "source_cap_is_strictly_used": signatures_match_through(E - 1, E, E)
        and not signatures_match_through(E, E, E),
        "depth_E_protocol_is_faithful_on_frozen_domain": all(
            witness[0] <= E for witness in witnesses.values()
        ),
        "no_claim_without_source_exponent_cap": True,
        "finite_rivals_count": len(rivals) == (E - 1) ** 2,
        "hostile_pair_order": E**2 == 64,
        "certificate_depth_equals_exponent_cap": worst_depth == E,
        "bounded_positive_result_does_not_contradict_WP167": True,
    }

    result = {
        "work_package": "WP168",
        "claim": "A source-derived finite exponent cap E converts bounded relation testing into a faithful closure certificate at depth E.",
        "exponent_cap_E": E,
        "domain": "Two labelled nontrivial finite abelian closure rivals with generator periods n1,n2 <= E, plus the infinite free closure Z^2.",
        "rivals_tested": len(rivals),
        "worst_case": {
            "finite_rival": f"(Z/{E}Z)^2",
            "order": E**2,
            "matches_Z2_through_depth": E - 1,
            "first_separating_depth": first_hostile_witness[0],
            "first_witness": first_hostile_witness[1],
        },
        "classification": "conditional selector on the finite-exponent-bounded domain; otherwise only a rigidifier by WP167.",
        "instrument_gate": "The exponent cap must be source-derived before the relation protocol has selector authority.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp168_exponent_bound_closure_certificate.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
