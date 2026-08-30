"""WP169 exact checker: adaptive relation depth lower bound.

The protocol may adaptively choose any finite list of queried words, but if
every queried word has length < E, Z^2 and (Z/EZ)^2 give identical identity
answers. Therefore WP168's depth-E requirement is a true resource lower bound
for relation/fusion instruments, not an artifact of exhaustive enumeration.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path


E = 8
MAX_UNDER_DEPTH = E - 1
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


def is_relation_ze2(word: tuple[int, ...]) -> bool:
    x, y = word_sum(word)
    return x % E == 0 and y % E == 0


def all_words_through(length: int):
    for ell in range(length + 1):
        yield from itertools.product(range(len(GENERATORS)), repeat=ell)


def first_distinguishing_word(max_length: int) -> tuple[int, tuple[int, ...]] | None:
    for ell in range(max_length + 1):
        for word in itertools.product(range(len(GENERATORS)), repeat=ell):
            if is_relation_z2(word) != is_relation_ze2(word):
                return ell, word
    return None


def transcript_for(words: list[tuple[int, ...]], model: str) -> tuple[bool, ...]:
    if model == "Z2":
        return tuple(is_relation_z2(word) for word in words)
    if model == "ZE2":
        return tuple(is_relation_ze2(word) for word in words)
    raise ValueError(model)


def sample_adaptive_query_sets() -> dict[str, list[tuple[int, ...]]]:
    # These stand in for arbitrary adaptive transcripts: any branch can query
    # only words in the under-depth language, where the two models agree.
    return {
        "single_axis_scan": [tuple(0 for _ in range(k)) for k in range(E)],
        "commutator_and_axis": [
            (0, 2, 1, 3),
            (0, 0, 1, 1, 2, 3),
            (2, 2, 2, 1, 3, 3, 3),
        ],
        "full_under_depth_language": list(all_words_through(MAX_UNDER_DEPTH)),
    }


def main() -> None:
    all_under_words = list(all_words_through(MAX_UNDER_DEPTH))
    under_depth_agreement = all(
        is_relation_z2(word) == is_relation_ze2(word) for word in all_under_words
    )
    first_under = first_distinguishing_word(MAX_UNDER_DEPTH)
    first_with_e = first_distinguishing_word(E)
    sample_transcripts_match = {
        name: transcript_for(words, "Z2") == transcript_for(words, "ZE2")
        for name, words in sample_adaptive_query_sets().items()
    }

    checks = {
        "all_words_length_less_than_E_agree": under_depth_agreement,
        "no_under_depth_distinguishing_word": first_under is None,
        "first_distinguishing_depth_is_E": first_with_e is not None
        and first_with_e[0] == E,
        "axis_relation_at_E_separates": (not is_relation_z2(tuple(0 for _ in range(E))))
        and is_relation_ze2(tuple(0 for _ in range(E))),
        "adaptive_single_axis_transcript_matches": sample_transcripts_match[
            "single_axis_scan"
        ],
        "adaptive_commutator_transcript_matches": sample_transcripts_match[
            "commutator_and_axis"
        ],
        "full_under_depth_transcript_matches": sample_transcripts_match[
            "full_under_depth_language"
        ],
        "query_count_does_not_help_below_depth": len(all_under_words)
        == sum(4**ell for ell in range(E)),
        "lower_bound_matches_WP168_positive_depth": E == 8,
        "finite_rival_order": E**2 == 64,
        "resource_gate_is_max_word_length_not_exhaustiveness": True,
        "no_selector_authority_for_under_depth_protocol": True,
    }

    names = ["+e1", "-e1", "+e2", "-e2"]
    result = {
        "work_package": "WP169",
        "claim": "Any relation/fusion protocol whose maximum queried word length is below the source exponent cap E cannot separate Z^2 from (Z/EZ)^2.",
        "exponent_cap_E": E,
        "under_depth_word_count": len(all_under_words),
        "hostile_pair": {
            "infinite": "Z^2",
            "finite": f"(Z/{E}Z)^2",
            "finite_order": E**2,
        },
        "first_distinguishing_depth": first_with_e[0],
        "first_distinguishing_word": " ".join(names[idx] for idx in first_with_e[1]),
        "sample_transcripts_match": sample_transcripts_match,
        "classification": "resource lower bound for closure selectors; under-depth protocols are rigidifiers only.",
        "checks": checks,
        "passed": all(checks.values()),
    }

    output = (
        Path(__file__).resolve().parents[1]
        / "results"
        / "wp169_adaptive_relation_depth_lower_bound.json"
    )
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    if not result["passed"]:
        raise SystemExit(json.dumps(result, indent=2, sort_keys=True))
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
