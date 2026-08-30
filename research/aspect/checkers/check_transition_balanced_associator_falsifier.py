from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "transition_balanced_associator_falsifier.json"

def cyclic_pairs(word):
    return Counter((word[i - 1], word[i]) for i in range(len(word)))

def cell_means(word, carryover):
    totals = {symbol: F(0) for symbol in range(4)}
    counts = Counter(word)
    for i, current in enumerate(word):
        totals[current] += carryover[word[i - 1]]
    return {symbol: totals[symbol] / counts[symbol] for symbol in range(4)}

def associator(means):
    return ((means[0] - means[1]) + (means[2] - means[3])) / 2

def main():
    grouped = [0] * 4 + [1] * 4 + [2] * 4 + [3] * 4
    transition_balanced = [0, 0, 1, 0, 2, 0, 3, 1, 1, 2, 1, 3, 2, 2, 3, 3]
    carryover = {0: F(3, 5), 1: F(0), 2: F(0), 3: F(0)}
    assert Counter(grouped) == Counter(transition_balanced) == Counter({i: 4 for i in range(4)})
    grouped_pairs = cyclic_pairs(grouped)
    balanced_pairs = cyclic_pairs(transition_balanced)
    assert set(balanced_pairs) == {(a, b) for a in range(4) for b in range(4)}
    assert set(balanced_pairs.values()) == {1}
    assert set(grouped_pairs.values()) != {1}
    grouped_means = cell_means(grouped, carryover)
    balanced_means = cell_means(transition_balanced, carryover)
    grouped_false_associator = associator(grouped_means)
    balanced_associator = associator(balanced_means)
    assert grouped_false_associator == F(3, 20)
    assert balanced_associator == 0
    out = {
        "schema": "marici.aspect.transition-balanced-associator-falsifier.v1",
        "status": "pass",
        "treatment_key": {"0": "L1", "1": "R2", "2": "L2", "3": "R1"},
        "grouped_schedule": grouped,
        "transition_balanced_schedule": transition_balanced,
        "current_treatment_counts": {str(k): v for k, v in Counter(grouped).items()},
        "balanced_ordered_pair_multiplicity": 1,
        "carryover_by_previous_treatment": {str(k): str(v) for k, v in carryover.items()},
        "grouped_cell_means": {str(k): str(v) for k, v in grouped_means.items()},
        "balanced_cell_means": {str(k): str(v) for k, v in balanced_means.items()},
        "grouped_false_associator": str(grouped_false_associator),
        "transition_balanced_associator": str(balanced_associator),
        "scope": "exact cancellation of arbitrary additive first-order carryover depending only on the immediately preceding treatment",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))

if __name__ == "__main__":
    main()
