"""Audit whether the naive four-mark to five-mark formula descends."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
import physical_four_mark_residue_twisted_derham as m

OUT = Path(__file__).resolve().parents[1] / "results" / "physical_branch_union_relation_descent.json"


def main() -> None:
    ambient, cutoff, gamma = 14, 7, 5
    domain_names = ("g1", "g2", "g3", "g23")
    target_names = ("g1", "g2", "g3", "g23", "g31")
    _, domain_columns, domain_pivots, _ = m.presentation(
        domain_names, gamma, ambient, cutoff, minimum_q_level=1
    )
    _, target_columns, target_pivots, _ = m.presentation(
        target_names, gamma, ambient, cutoff, minimum_q_level=1
    )
    _, q = m.fiber_data(2, 3, 4)
    domain_labels = {column: label for label, column in domain_columns.items()}
    tested = failures = missing_terms = 0
    for row in domain_pivots.values():
        image = {}
        complete = True
        for column, coefficient in row.items():
            k_pole, *rest = domain_labels[column]
            exponent = rest.pop()
            target_levels = (*rest, 1)
            for term, value in m.multiply_monomial(q["g31"], exponent):
                label = (k_pole, *target_levels, term)
                if label not in target_columns:
                    missing_terms += 1
                    complete = False
                    continue
                m.add_value(image, target_columns[label], coefficient * value)
        if not complete:
            continue
        tested += 1
        if m.reduce_row(image, target_pivots):
            failures += 1
    payload = {
        "schema": "marici.physical-branch-union-relation-descent.v1",
        "prime": m.PRIME,
        "ambient": ambient,
        "cutoff": cutoff,
        "domain_pivot_relations": len(domain_pivots),
        "fully_tested_relations": tested,
        "missing_target_terms": missing_terms,
        "nonzero_mapped_relations": failures,
        "descends": failures == 0 and missing_terms == 0,
        "conclusion": "naive multiplication by the missing mark does not define a map of the finite quotient presentations",
        "invalidates": [
            "the proposed rank-25 branch sum",
            "the proposed transverse quotient line",
            "its Q-support test",
            "its Kato-line identification",
            "the proposed 15+5+5+1 filtration"
        ],
        "passed": failures > 0 and missing_terms == 0,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
