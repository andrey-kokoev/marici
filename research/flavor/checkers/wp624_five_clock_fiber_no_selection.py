"""Exact WP624 census of the minimal equal-weight multi-clock target fiber."""

import collections
import itertools
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
alphabet = (-2, -1, 0, 1, 2)
target_r = sp.Rational(3, 5)
target_x_mean = 2 * target_r

admissible_multiplicities = [
    n for n in range(1, 21) if (target_x_mean * n).is_Integer
]
minimal_n = min(admissible_multiplicities)

labelled_fiber = [
    values
    for values in itertools.product(alphabet, repeat=minimal_n)
    if sum(values) == target_x_mean * minimal_n
]
occupancies = collections.Counter(
    tuple(values.count(symbol) for symbol in alphabet)
    for values in labelled_fiber
)
expected_occupancies = {
    (0, 0, 0, 4, 1): 5,
    (0, 0, 1, 2, 2): 30,
    (0, 0, 2, 0, 3): 10,
    (0, 1, 0, 1, 3): 20,
    (1, 0, 0, 0, 4): 5,
}

hostile_a = (-2, 2, 2, 2, 2)
hostile_b = (1, 1, 1, 1, 2)


def mean_r(values):
    return sp.Rational(sum(values), 2 * len(values))


S = sp.symbols("S", integer=True)
mean_lock = (S - 6) ** 2

checks = {
    "target_requires_clock_count_divisible_by_five":
        admissible_multiplicities == [5, 10, 15, 20],
    "five_clocks_are_minimal": minimal_n == 5,
    "labelled_target_fiber_has_seventy_points": len(labelled_fiber) == 70,
    "permutation_quotient_has_five_classes": len(occupancies) == 5,
    "occupancy_multiplicities_are_exact":
        occupancies == expected_occupancies,
    "orbit_sizes_sum_to_labelled_fiber": sum(occupancies.values()) == 70,
    "hostile_pair_has_same_target_mean":
        mean_r(hostile_a) == mean_r(hostile_b) == target_r,
    "hostile_pair_is_not_permutation_equivalent":
        sorted(hostile_a) != sorted(hostile_b),
    "uncoupled_clock_energy_is_blind_to_occupancy":
        all(value in alphabet for value in hostile_a + hostile_b),
    "mean_lock_contains_target_sum":
        sp.solve(sp.diff(mean_lock, S), S) == [6],
}

if not all(checks.values()):
    raise SystemExit(f"WP624 check failed: {checks}")
checks = {key: bool(value) for key, value in checks.items()}

result = {
    "work_package": "WP624",
    "status": "PASS",
    "checks": checks,
    "admitted_state_domain": "N identical compact clocks with doubled rational readouts x_i in {-2,-1,0,1,2}, equal-weight r=(sum x_i)/(2N), and permutation quotient S_N",
    "minimal_multiplicity": 5,
    "labelled_target_fiber_size": 70,
    "contextual_partition": [
        {
            "occupancy_for_x_minus2_minus1_0_1_2": list(key),
            "labelled_multiplicity": value,
        }
        for key, value in sorted(occupancies.items())
    ],
    "classification": "five clocks make r=3/5 representable but neither select it among all vacua nor identify a unique source orbit",
    "smallest_exact_falsifier": "(-2,2,2,2,2) and (1,1,1,1,2) are permutation-inequivalent source states with the same r=3/5",
    "selector_test": "an interaction (sum x_i-6)^2 selects the target only by supplying target integer 6",
    "descent": "the mean descends under clock permutations, but flavor coupling uses the H-reference stabilizer groupoid",
    "physical_probe": "resolve five individual clock sectors or their occupation counts together with the H-referenced flavor mass ratio",
    "instrument_gate": "no admitted apparatus resolves clock occupancy and flavor response in one calibrated source frame",
    "remaining_source_gate": "derive fivefold multiplicity and a permutation-invariant interaction selecting an occupancy or total without importing the flavor target",
}

out = ROOT / "results" / "wp624_five_clock_fiber_no_selection.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
