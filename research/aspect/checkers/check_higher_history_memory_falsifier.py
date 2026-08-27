from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "higher_history_memory_falsifier.json"


def rank(matrix):
    a = [list(map(F, row)) for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        a[r] = [x / a[r][c] for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def main():
    # Rows are controlled two-step histories a->c->R; columns are three suffix probes.
    # Averaging over the unrecorded two-back label a makes every one-step law identical.
    hankel = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
    one_step_marginal = [sum(row[col] for row in hankel) / 3 for col in range(3)]
    assert one_step_marginal == [F(1, 3)] * 3
    assert rank(hankel) == 3
    assumed_ready_dead_rank = 2
    out = {
        "schema": "marici.aspect.higher-history-memory-falsifier.v1", "status": "pass",
        "one_step_marginal_by_suffix_probe": [str(x) for x in one_step_marginal],
        "one_step_predecessor_test_passes": True,
        "controlled_history_hankel": [[str(x) for x in row] for row in hankel],
        "controlled_history_predictive_rank": rank(hankel),
        "assumed_ready_dead_predictive_rank": assumed_ready_dead_rank,
        "model_enlargement_forced": rank(hankel) > assumed_ready_dead_rank,
        "required_histories": "a -> c -> reset -> b, with a and c retained as separate intervention labels",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
