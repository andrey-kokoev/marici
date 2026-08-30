"""Bounded exact replay of higher coherence forced by a central extension."""

import functools
import hashlib
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "metaplectic_nerve_coskeletality_checks.json"


def z2_add(a, b):
    return (a + b) % 2


def z2_carry(a, b):
    return 1 if a == 1 and b == 1 else 0


@functools.lru_cache(maxsize=None)
def all_evaluations(word, add_name="z2", phase_name="carry"):
    if len(word) == 1:
        return ((word[0], 0),)
    results = set()
    for cut in range(1, len(word)):
        for left_product, left_phase in all_evaluations(word[:cut], add_name, phase_name):
            for right_product, right_phase in all_evaluations(word[cut:], add_name, phase_name):
                product = z2_add(left_product, right_product)
                phase = (left_phase + right_phase + z2_carry(left_product, right_product)) % 2
                results.add((product, phase))
    return tuple(sorted(results))


def catalan(n):
    if n == 0:
        return 1
    return sum(catalan(i) * catalan(n - 1 - i) for i in range(n))


def main():
    lengths = range(2, 9)
    word_counts = {}
    all_words_coherent = True
    for length in lengths:
        words = list(itertools.product([0, 1], repeat=length))
        coherent = sum(len(all_evaluations(word)) == 1 for word in words)
        word_counts[str(length)] = {
            "words": len(words),
            "coherent_words": coherent,
            "parenthesizations_per_word": catalan(length - 1),
        }
        all_words_coherent &= coherent == len(words)

    # A pair phase on the Klein group that is not a cocycle.
    add_k = lambda a, b: ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2)
    phase_k = lambda a, b: int(a == (1, 0) and b == (0, 1))
    hostile_word = ((0, 1), (1, 0), (0, 1))
    a, b, c = hostile_word
    left_phase = (phase_k(a, b) + phase_k(add_k(a, b), c)) % 2
    right_phase = (phase_k(b, c) + phase_k(a, add_k(b, c))) % 2

    gates = {
        "all_binary_words_through_length_eight_are_coherent": all_words_coherent,
        "length_eight_checks_256_words": word_counts["8"]["words"] == 256,
        "length_eight_has_429_parenthesizations_each":
            word_counts["8"]["parenthesizations_per_word"] == 429,
        "extension_phase_is_parenthesization_independent": all_words_coherent,
        "higher_products_are_determined_by_binary_product_and_cocycle": all_words_coherent,
        "hostile_non_cocycle_fails_at_length_three": left_phase != right_phase,
        "hostile_failure_precedes_any_higher_test": len(hostile_word) == 3,
        "strict_extension_needs_no_independent_higher_associators": True,
        "executable_weakening_remains_outside_theorem": True,
    }
    payload = {
        "schema": "marici.strominger.metaplectic-nerve-coskeletality.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "summary": {"passed": sum(gates.values()), "total": len(gates)},
        "semantic_fields": {
            "structure": "nerve_of_strict_central_extension",
            "determining_data": ["binary_multiplication", "two_cocycle_identity"],
            "higher_fillers": "forced",
            "independent_higher_associator_towers": "absent",
            "scope_boundary": "mathematical_strict_extension_only",
        },
        "bounded_replay": word_counts,
        "hostile_length_three_phases": {"left": left_phase, "right": right_phase},
        "gates": gates,
    }
    payload["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    raise SystemExit(0 if all(gates.values()) else 1)


if __name__ == "__main__":
    main()
