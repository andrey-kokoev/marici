#!/usr/bin/env python3
"""Exact associativity test for Shannon entropy as an outcome-refinement cocycle."""

import json
from pathlib import Path

import sympy as sp


def h(weights):
    return -sum(x * sp.log(x) for x in weights)


def simplify_logs(expr):
    return sp.simplify(sp.expand_log(expr, force=True))


def main():
    a, b, c, d = sp.symbols("a b c d", positive=True)
    ab = a + b
    cd = c + d
    total = ab + cd

    direct = h([a / total, b / total, c / total, d / total])
    two_block = (
        h([ab / total, cd / total])
        + ab / total * h([a / ab, b / ab])
        + cd / total * h([c / cd, d / cd])
    )

    abc = a + b + c
    left_nested = (
        h([abc / total, d / total])
        + abc / total
        * (
            h([ab / abc, c / abc])
            + ab / abc * h([a / ab, b / ab])
        )
    )

    checks = {
        "two_block_grouping": simplify_logs(direct - two_block) == 0,
        "nested_refinement_associativity": simplify_logs(direct - left_nested) == 0,
        "refinement_paths_agree": simplify_logs(two_block - left_nested) == 0,
    }

    payload = {
        "schema": "marici.shannon-refinement-cocycle.v1",
        "checks": checks,
        "all_passed": all(checks.values()),
        "interpretation": (
            "Shannon entropy is an associative additive cocycle on typed finite "
            "outcome refinements. The value added by a refinement is the "
            "coarse-state-weighted conditional entropy of its fibers."
        ),
    }
    out = Path(__file__).parents[1] / "results" / "shannon-refinement-cocycle.json"
    out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
