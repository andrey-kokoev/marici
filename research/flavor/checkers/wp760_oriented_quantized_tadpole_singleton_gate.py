"""Exact oriented quantized-tadpole singleton-fiber audit."""
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def oriented_partitions(total):
    return [(n0, total - n0) for n0 in range(1, total) if n0 > total - n0 > 0]


def portal_contrast(n0, npi):
    r = sp.Rational(n0, npi)
    return sp.factor((r**2 - 1) ** 2 / (2 * (r**2 + 1) ** 2))


partitions = {total: oriented_partitions(total) for total in range(2, 13)}
counts = {total: len(values) for total, values in partitions.items()}
singleton_totals = [total for total, count in counts.items() if count == 1]

T3 = partitions[3]
T4 = partitions[4]
T5 = partitions[5]
delta_T3 = portal_contrast(*T3[0])
delta_T4 = portal_contrast(*T4[0])
delta_T5 = [portal_contrast(*pair) for pair in T5]

checks = {
    "fiber_count_matches_floor_formula_on_bounded_domain": all(counts[T] == (T - 1) // 2 for T in counts),
    "asymmetric_fiber_is_singleton_only_for_totals_three_and_four": singleton_totals == [3, 4],
    "total_three_uniquely_selects_oriented_pair_two_one": T3 == [(2, 1)],
    "total_four_uniquely_selects_oriented_pair_three_one": T4 == [(3, 1)],
    "total_three_predicts_contrast_nine_fiftieths": delta_T3 == sp.Rational(9, 50),
    "total_four_predicts_contrast_eight_twenty_fifths": delta_T4 == sp.Rational(8, 25),
    "total_five_has_two_oriented_pairs": T5 == [(3, 2), (4, 1)],
    "total_five_finite_fiber_is_not_singleton": len(set(delta_T5)) == 2,
    "total_five_exact_contrasts_are_distinct": set(delta_T5) == {sp.Rational(25, 338), sp.Rational(225, 578)},
    "orientation_reversal_preserves_magnitude_but_reverses_label_authority": portal_contrast(2, 1) == portal_contrast(1, 2),
}
checks = {name: bool(value) for name, value in checks.items()}
if not all(checks.values()):
    raise SystemExit(checks)

result = {
    "work_package": "WP760",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "positive integer boundary charges (n0,npi), a source-fixed total tadpole T=n0+npi, and an independently labelled orientation n0>npi",
    "faithful_coordinate": "the ordered integer pair (n0,npi), not only its total T or the unordered endpoint orbit",
    "source_candidate": "quantized boundary charge plus a topologically fixed total and oriented endpoint labeling",
    "contextual_partition": "for fixed T the admissible fiber has floor((T-1)/2) ordered asymmetric pairs",
    "selector_result": "the oriented fiber is a singleton exactly for T=3 or T=4; T=3 selects ratio 2 and contrast 9/50, while T=4 selects ratio 3 and contrast 8/25",
    "finite_fiber_warning": "T=5 already has two admissible pairs and two distinct contrasts, so quantization alone gives finite rather than singleton authority",
    "classification": "conditional discrete source selector for the boundary ratio only in the minimal T=3 or T=4 sectors; otherwise a finite-fiber rigidifier",
    "smallest_exact_falsifier": "at fixed T=5 the admissible ordered pairs (3,2) and (4,1) predict 25/338 and 225/578",
    "orientation_gate": "the unordered endpoint quotient preserves contrast magnitude but cannot authorize which labelled flavor channel has the positive sign",
    "rg_gate": "integer charges and total tadpole can be topologically stable, but no flavor source presently derives T=3 or T=4 or forbids threshold operators that shift the low-energy portal",
    "instrument_gate": "the quantized ratio predicts only a formal overlap until a labelled threshold process and calibrated detector response are derived",
    "deutschian_status": "this is the first candidate that can make the ratio hard to vary, but only after a source independently explains the exceptional minimal total and orientation",
    "next_source_gate": "search the admitted flavor compactification for a derived tadpole or index forcing T=3 or T=4 and connect its ordered charge to the physical16-labelled readout",
}
(ROOT / "results" / "wp760_oriented_quantized_tadpole_singleton_gate.json").write_text(
    json.dumps(result, indent=2) + "\n", encoding="utf-8"
)
print(json.dumps(result, indent=2))
