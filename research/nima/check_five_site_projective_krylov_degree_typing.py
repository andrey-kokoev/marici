#!/usr/bin/env python3
"""Audit numerator-degree typing of the bounded projective Krylov ladder."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CANON = json.loads(
    (ROOT / "research/benincasa/results/five-site-asymmetric-canonical-sum.json").read_text()
)
COVER = json.loads(
    (ROOT / "research/benincasa/results/five-site-d3-marked-kummer-cover.json").read_text()
)
OUTPUT = ROOT / "research/nima/results/five-site-projective-krylov-degree-typing.json"

labels = CANON["denominator_labels"]
facets = COVER["facet_forms"]
support_counts = {0: 0, 1: 0, 2: 0}
for label in labels:
    support = sum(int(value) != 0 for value in facets[label]["y"])
    assert support in support_counts
    support_counts[support] += 1

# A zero-support norm has no u-dependence.  One- and two-root norms have
# u-degree at most two and four after descent to the Kummer base.
denominator_u_degree_bound = 2*support_counts[1] + 4*support_counts[2]
initial_numerator_degree = 11
tested_primitive_degree = 3
derivative_bounds = [
    {
        "order": order,
        "common_denominator_numerator_u_degree_upper_bound":
            initial_numerator_degree + order*denominator_u_degree_bound,
        "tested_primitive_degree": tested_primitive_degree,
    }
    for order in range(1, 7)
]

assert len(labels) == 26
assert support_counts == {0: 1, 1: 5, 2: 20}
assert denominator_u_degree_bound == 90
assert tested_primitive_degree < initial_numerator_degree

output = {
    "schema": "marici.five_site.projective_krylov_degree_typing.v1",
    "denominator_label_count": len(labels),
    "support_counts": {str(key): value for key, value in support_counts.items()},
    "denominator_u_degree_upper_bound": denominator_u_degree_bound,
    "known_weight_five_numerator_max_degree": initial_numerator_degree,
    "ladder_tested_primitive_max_degree": tested_primitive_degree,
    "derivative_degree_upper_bounds": derivative_bounds,
    "conclusion": (
        "The order-one-through-six ladder is a valid low-degree exclusion, "
        "but its linear rank growth cannot presently be interpreted as evidence "
        "for high Gauss-Manin rank because the primitive ansatz is degree-starved "
        "already before the first derivative."
    ),
    "next_gate": (
        "Derive a reduction-compatible numerator filtration or sparse polynomial-module "
        "basis before assigning rank meaning to further Krylov orders."
    ),
    "passed": True,
}
OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps(output, sort_keys=True))
