from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "blinding_reset_falsifier.json"


def rank(matrix):
    a = [list(map(F, row)) for row in matrix]
    rows, cols, pivot_row = len(a), len(a[0]), 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                factor = a[r][col]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
    return pivot_row


def norm_inf(matrix):
    return max(sum(abs(x) for x in row) for row in matrix)


def predecessor_spread(outputs):
    return max(max(values) - min(values) for values in outputs.values())


def main():
    identity = [[F(int(i == j)) for j in range(4)] for i in range(4)]
    blind = [[F(1, 4)] * 4 for _ in range(4)]
    predecessor_outputs = {target: [F(target, 5)] * 4 for target in range(4)}
    assert predecessor_spread(predecessor_outputs) == 0
    assert rank(identity) == 4 and rank(blind) == 1
    identity_condition = norm_inf(identity) * norm_inf(identity)
    assert identity_condition == 1
    out = {
        "schema": "marici.aspect.blinding-reset-falsifier.v1", "status": "pass",
        "predecessor_invariance_passes_for_blind_reset": True,
        "blind_reset_transfer_rank": rank(blind),
        "information_preserving_reset_transfer_rank": rank(identity),
        "information_preserving_reconstruction_condition_infinity_norm": str(identity_condition),
        "blind_reset_reconstructible": False,
        "required_joint_gate": "predecessor invariance and full-rank bounded target reconstruction must pass simultaneously",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
