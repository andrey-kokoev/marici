"""WP167 exact checker: bounded closure certification no-go.

The checker compares the identity-relation language of Z^2 and (Z/NZ)^2
for words of bounded length in the fixed generators +/-e1, +/-e2.
It is dependency-free by construction.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path


L = 7
HOSTILE_N = L + 1
GENERATORS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def word_sum(word: tuple[int, ...]) -> tuple[int, int]:
    x = 0
    y = 0
    for idx in word:
        dx, dy = GENERATORS[idx]
        x += dx
        y += dy
    return x, y


def is_relation_in_z2(word: tuple[int, ...]) -> bool:
    return word_sum(word) == (0, 0)


def is_relation_mod_n(word: tuple[int, ...], n: int) -> bool:
    x, y = word_sum(word)
    return x % n == 0 and y % n == 0


def words_through(length: int):
    for ell in range(length + 1):
        yield from itertools.product(range(len(GENERATORS)), repeat=ell)


def relation_signature(length: int, n: int) -> tuple[bool, ...]:
    return tuple(is_relation_mod_n(word, n) for word in words_through(length))


def z2_signature(length: int) -> tuple[bool, ...]:
    return tuple(is_relation_in_z2(word) for word in words_through(length))


def first_distinguishing_length(n: int, max_length: int) -> int | None:
    for ell in range(max_length + 1):
        for word in itertools.product(range(len(GENERATORS)), repeat=ell):
            if is_relation_in_z2(word) != is_relation_mod_n(word, n):
                return ell
    return None


def bounded_relation_theorem_holds(max_l: int) -> bool:
    for length in range(1, max_l + 1):
        n = length + 1
        for a in range(-length, length + 1):
            for b in range(-length, length + 1):
                z2_identity = a == 0 and b == 0
                mod_identity = a % n == 0 and b % n == 0
                if z2_identity != mod_identity:
                    return False
    return True


def main() -> None:
    z2_sig = z2_signature(L)
    hostile_sig = relation_signature(L, HOSTILE_N)
    relation_count = sum(1 for item in z2_sig if item)
    total_words = len(z2_sig)

    depth_8_witness = tuple(0 for _ in range(HOSTILE_N))
    depth_7_witness_for_n7 = tuple(0 for _ in range(L))

    hostile_ns_through_l = []
    for n in range(2, HOSTILE_N + 1):
        if z2_signature(L) == relation_signature(L, n):
            hostile_ns_through_l.append(n)

    checks = {
        "total_words_through_L": total_words == sum(4**ell for ell in range(L + 1)),
        "hostile_relation_language_matches_through_L": z2_sig == hostile_sig,
        "nonempty_exact_relation_sector": relation_count > 0,
        "depth_8_witness_not_relation_in_Z2": not is_relation_in_z2(depth_8_witness),
        "depth_8_witness_relation_in_Z8_square": is_relation_mod_n(
            depth_8_witness, HOSTILE_N
        ),
        "N_equals_L_distinguished_at_depth_L": (
            is_relation_in_z2(depth_7_witness_for_n7)
            != is_relation_mod_n(depth_7_witness_for_n7, L)
        ),
        "smallest_hostile_N_for_depth_L_is_L_plus_1": hostile_ns_through_l
        == [HOSTILE_N],
        "hostile_finite_group_size_is_64": HOSTILE_N**2 == 64,
        "first_distinguishing_depth_for_hostile_is_8": first_distinguishing_length(
            HOSTILE_N, HOSTILE_N
        )
        == HOSTILE_N,
        "bounded_relation_theorem_holds_through_12": bounded_relation_theorem_holds(
            12
        ),
        "strict_bound_is_N_greater_than_L": HOSTILE_N > L,
        "finite_depth_protocol_not_uniform_certificate": (
            z2_sig == hostile_sig
            and is_relation_mod_n(depth_8_witness, HOSTILE_N)
            and not is_relation_in_z2(depth_8_witness)
        ),
    }

    result = {
        "work_package": "WP167",
        "claim": "No bounded relation/fusion protocol of word-depth L can uniformly certify infinite two-holonomy closure against finite rivals.",
        "fixed_generators": ["+e1", "-e1", "+e2", "-e2"],
        "depth_L": L,
        "hostile_pair": {
            "infinite_source": "Z^2",
            "finite_rival": f"(Z/{HOSTILE_N}Z)^2",
            "finite_rival_order": HOSTILE_N**2,
        },
        "total_words_through_L": total_words,
        "identity_relation_count_through_L": relation_count,
        "smallest_hostile_N_for_depth_L": HOSTILE_N,
        "first_distinguishing_word": "+e1^8",
        "first_distinguishing_depth": HOSTILE_N,
        "strict_counterexample": {
            "N_equals_L": L,
            "word": "+e1^7",
            "distinguishes_at_depth_L": checks["N_equals_L_distinguished_at_depth_L"],
        },
        "scope_boundary": "Relation language only, in the declared finite generator set. This does not rule out a separately typed nonlocal physical observable.",
        "classification": "bounded finite-certification no-go for infinite closure; instrument gate remains open.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp167_bounded_closure_certification_no_go.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
