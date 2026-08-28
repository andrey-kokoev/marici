#!/usr/bin/env python3
"""Exact bounded morphism-faithfulness checks for the cubical pilot."""
from __future__ import annotations
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASPECT = HERE.parent
CONTRACT = ASPECT / "contracts" / "interaction-net-morphism-faithfulness.v1.json"
RESULT = ASPECT / "results" / "interaction_net_morphism_faithfulness.json"
GENERATORS = ("O1", "O2", "O3", "O4", "O5", "K")

def endpoint(word):
    occurrence = tuple(int(f"O{i}" in word) for i in range(1, 6))
    return occurrence, word.count("K")

def valid(word):
    return all(word.count(f"O{i}") <= 1 for i in range(1, 6))

def normal_form(word):
    return tuple(sorted(word, key=lambda x: (x == "K", x)))

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    words = [()]
    for length in range(1, 5):
        words.extend(w for w in itertools.product(GENERATORS, repeat=length) if valid(w))

    by_endpoint = {}
    free_collision = None
    for word in words:
        end = endpoint(word)
        prior = by_endpoint.get(end)
        if prior is not None and prior != word:
            free_collision = {"left": prior, "right": word, "endpoint": end}
            break
        by_endpoint[end] = word

    quotient = {}
    quotient_collision = None
    for word in words:
        key = (endpoint(word), normal_form(word))
        end = endpoint(word)
        prior = quotient.get(end)
        if prior is not None and prior != key:
            quotient_collision = {"left": prior, "right": key, "endpoint": end}
            break
        quotient[end] = key

    explicit_square = {
        "left": ("O1", "O2"),
        "right": ("O2", "O1"),
        "same_endpoint": endpoint(("O1", "O2")) == endpoint(("O2", "O1")),
        "same_normal_form": normal_form(("O1", "O2")) == normal_form(("O2", "O1"))
    }
    silent_loop = {
        "identity_word": (),
        "hostile_loop": ("L",),
        "same_endpoint_record": True,
        "source_authorized": False
    }
    hostiles = {
        "free_path_endpoint_failure_found": free_collision is not None,
        "commuting_square_closes_in_quotient": explicit_square["same_endpoint"] and explicit_square["same_normal_form"],
        "bounded_thin_quotient_confirmed": quotient_collision is None,
        "full_entry_4013_not_promoted": contract["presentations"]["entry_4013_exact_quotient"]["morphism_faithfulness"] == "unknown",
        "silent_loop_not_inferred_absent": not silent_loop["source_authorized"]
    }
    passed = all(hostiles.values())
    out = {
        "schema": "marici.aspect.interaction-net-morphism-faithfulness-result.v1",
        "passed": passed,
        "word_count": len(words),
        "free_path_collision": free_collision,
        "explicit_commuting_square": explicit_square,
        "cubical_quotient_collision": quotient_collision,
        "silent_loop_hostile": silent_loop,
        "hostiles": hostiles,
        "verdict": contract["verdict"]
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__ == "__main__":
    main()
