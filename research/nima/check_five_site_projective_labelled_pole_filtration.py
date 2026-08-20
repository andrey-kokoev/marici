#!/usr/bin/env python3
"""Certify the termwise labelled-pole filtration for projective derivatives."""

import json
from math import comb, factorial
from pathlib import Path

import check_five_site_projective_krylov_ladder as ladder
import check_five_site_projective_krylov_order_one as base

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "research/nima/results/five-site-projective-labelled-pole-filtration.json"
MAX_ORDER = 6


def normalized_bell_jets(ratios, prime):
    power_sums = [
        sum(pow(ratio, order, prime) for ratio in ratios) % prime
        for order in range(1, MAX_ORDER+1)
    ]
    logarithmic = [0]+[
        ((-1 if order % 2 else 1)*factorial(order-1)*power_sums[order-1]) % prime
        for order in range(1, MAX_ORDER+1)
    ]
    jets = [1]
    for order in range(1, MAX_ORDER+1):
        jets.append(sum(
            comb(order-1, k-1)*jets[order-k]*logarithmic[k]
            for k in range(1, order+1)
        ) % prime)
    return jets


def normalized_complete_homogeneous_jets(ratios, prime):
    homogeneous = [1]+[0]*MAX_ORDER
    for ratio in ratios:
        updated = homogeneous[:]
        for order in range(1, MAX_ORDER+1):
            updated[order] = (homogeneous[order]+ratio*updated[order-1]) % prime
        homogeneous = updated
    return [
        ((-1 if order % 2 else 1)*factorial(order)*homogeneous[order]) % prime
        for order in range(MAX_ORDER+1)
    ]


def sample_point(prime, seed):
    sample = ladder.oracle_sample(prime, seed)
    r, _ = base.r_data(sample["u"], prime)
    roots = {x*x % prime: x for x in range(prime)}
    ys = [roots[value] for value in r]
    return sample["t"], ys


term_rows = []
for index, selected in enumerate(base.trace.terms):
    labels = base.trace.common + selected
    assert len(labels) == 10
    assert len(set(labels)) == 10
    term_rows.append({
        "term_index": index,
        "base_denominator_labels": labels,
    })

checks = []
for prime, seed in ((1009, 1), (1013, 2)):
    t, ys = sample_point(prime, seed)
    checked = 0
    for row in term_rows:
        ratios = []
        for label in row["base_denominator_labels"]:
            value = base.trace.q_value(label, t, ys, prime)
            assert value
            a = sum(int(x) for x in base.trace.facets[label]["x"]) % prime
            ratios.append(a*base.trace.inv(value, prime) % prime)
        bell = normalized_bell_jets(ratios, prime)
        labelled = normalized_complete_homogeneous_jets(ratios, prime)
        assert bell == labelled
        checked += 1
    checks.append({
        "prime": prime,
        "term_count": checked,
        "orders_checked": list(range(MAX_ORDER+1)),
        "bell_equals_labelled_multiset_expansion": True,
    })

order_rows = []
for order in range(MAX_ORDER+1):
    multisets_per_term = comb(10+order-1, order)
    order_rows.append({
        "order": order,
        "additional_pole_multisets_per_term": multisets_per_term,
        "raw_labelled_occurrence_columns": len(term_rows)*multisets_per_term,
    })

output = {
    "schema": "marici.five_site.projective_labelled_pole_filtration.v1",
    "canonical_term_count": len(term_rows),
    "denominator_occurrences_per_term": 10,
    "common_occurrences_per_term": len(base.trace.common),
    "selected_occurrences_per_term": 4,
    "order_rows": order_rows,
    "finite_field_checks": checks,
    "term_rows": term_rows,
    "conclusion": (
        "Projective derivatives admit a canonical termwise labelled-pole filtration. "
        "This avoids clearing all norms into D^(r+1) and retains the source occurrence labels "
        "needed for exact-form reduction."
    ),
    "next_gate": (
        "Construct labelled primitive columns with the same pole multi-indices, then quotient "
        "by exact-form and source-term relations before any scalar rank inference."
    ),
    "passed": True,
}
OUTPUT.write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps({
    "passed": True,
    "checks": checks,
    "order_rows": order_rows,
}, sort_keys=True))
