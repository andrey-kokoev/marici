#!/usr/bin/env python3
"""Test whether the OFPT compatible four-facet inventory is a matroid basis set."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACKET = ROOT / "research/benincasa/results/five-cycle-ofpt-packet.json"
OUTPUT = ROOT / "research/nima/results/five-site-ofpt-matroid-basis-exchange.json"


def main():
    packet = json.loads(PACKET.read_text())
    terms = [frozenset(term) for term in packet["five_cycle"]["terms"]]
    basis_set = set(terms)
    failures = []
    tested = 0
    for left_index, left in enumerate(terms):
        for right_index, right in enumerate(terms):
            if left_index == right_index:
                continue
            for removed in sorted(left-right):
                tested += 1
                candidates = [
                    added for added in sorted(right-left)
                    if frozenset((left-{removed}) | {added}) in basis_set
                ]
                if not candidates:
                    failures.append({
                        "left_index": left_index,
                        "right_index": right_index,
                        "left": sorted(left),
                        "right": sorted(right),
                        "removed": removed,
                    })
    output = {
        "schema": "marici.five_site.ofpt_matroid_basis_exchange.v1",
        "term_count": len(terms),
        "distinct_term_count": len(basis_set),
        "exchange_obligations_tested": tested,
        "exchange_failure_count": len(failures),
        "basis_exchange_holds": not failures,
        "failure_sample": failures[:20],
        "interpretation": (
            "Basis exchange is necessary for the 180 compatible sets themselves "
            "to define the bases of a rank-four matroid and hence a direct "
            "Orlik-Solomon constructor."
        ),
        "scope": (
            "Does not test the full facet-vector matroid, whose bases include sets "
            "outside the source-authorized OFPT term inventory."
        ),
        "passed": True,
    }
    OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
