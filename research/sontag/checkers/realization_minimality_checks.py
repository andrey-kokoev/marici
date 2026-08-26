"""Exact rational realization/minimality checks."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mpow(a, n):
    result = [[F(i == j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):
        result = mm(result, a)
    return result


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def markov(a, b, c, k):
    return mm(c, mm(mpow(a, k), b))[0][0]


def main():
    A = [[F(1, 2)]]
    B = [[F(1)]]
    C = [[F(1)]]
    sequence = [markov(A, B, C, k) for k in range(8)]
    hankel = [[sequence[0], sequence[1]], [sequence[1], sequence[2]]]

    A_aug = [[F(1, 2), 0], [0, F(2)]]
    B_aug = [[F(1)], [0]]
    C_aug = [[F(1), 0]]
    augmented_sequence = [markov(A_aug, B_aug, C_aug, k) for k in range(8)]
    hidden = [[F(0)], [F(1)]]
    hidden_outputs = [mm(C_aug, mm(mpow(A_aug, k), hidden))[0][0] for k in range(8)]

    # Similarity mixes the hidden direction while preserving behavior.
    T = [[F(1), F(1)], [0, F(1)]]
    T_inv = [[F(1), F(-1)], [0, F(1)]]
    A_sim = mm(T, mm(A_aug, T_inv))
    B_sim = mm(T, B_aug)
    C_sim = mm(C_aug, T_inv)
    similar_sequence = [markov(A_sim, B_sim, C_sim, k) for k in range(8)]

    reach_aug = [[B_aug[0][0], mm(A_aug, B_aug)[0][0]],
                 [B_aug[1][0], mm(A_aug, B_aug)[1][0]]]
    observe_aug = C_aug + mm(C_aug, A_aug)

    checks = {
        "minimal_markov_parameters_are_geometric": sequence == [F(1, 2) ** k for k in range(8)],
        "hankel_rank_is_one": det2(hankel) == 0 and any(value != 0 for row in hankel for value in row),
        "one_state_witness_is_reachable": B[0][0] != 0,
        "one_state_witness_is_observable": C[0][0] != 0,
        "augmented_transfer_is_identical": augmented_sequence == sequence,
        "augmented_hidden_state_has_zero_history": hidden != [[0], [0]] and all(value == 0 for value in hidden_outputs),
        "augmented_hidden_mode_is_unstable": A_aug[1][1] > 1,
        "augmented_reachability_rank_is_one": det2(reach_aug) == 0 and reach_aug[0][0] != 0,
        "augmented_observability_rank_is_one": det2(observe_aug) == 0 and observe_aug[0][0] != 0,
        "reachable_observable_quotient_matches_minimal": A_aug[0][0] == A[0][0] and B_aug[0][0] == B[0][0] and C_aug[0][0] == C[0][0],
        "similarity_changes_presentation": A_sim != A_aug and C_sim != C_aug,
        "similarity_preserves_external_behavior": similar_sequence == sequence,
    }

    result = {
        "schema": "marici.sontag.realization-minimality.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "passed": sum(checks.values()),
        "total": len(checks),
        "witnesses": {
            "minimal_markov_parameters_k0_to_k7": [str(value) for value in sequence],
            "hankel": [[str(value) for value in row] for row in hankel],
            "augmented_A": [[str(value) for value in row] for row in A_aug],
            "hidden_state": [str(value[0]) for value in hidden],
            "similar_A": [[str(value) for value in row] for row in A_sim],
            "similar_B": [[str(value) for value in row] for row in B_sim],
            "similar_C": [[str(value) for value in row] for row in C_sim],
        },
        "claim_boundary": "finite-dimensional rational discrete-time SISO realization only",
    }
    output = Path(__file__).parents[1] / "results" / "realization_minimality.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "pass" else 1)


if __name__ == "__main__":
    main()
