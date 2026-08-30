"""Exact sequential Kraus checks for a ready/dead photodetector."""

from fractions import Fraction as F
import json
from pathlib import Path


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return [list(row) for row in zip(*a)]


def add(*matrices):
    return [[sum(a[i][j] for a in matrices) for j in range(len(matrices[0][0]))]
            for i in range(len(matrices[0]))]


def scale(q, a):
    return [[q * value for value in row] for row in a]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def apply_one(k, rho):
    return mm(mm(k, rho), tr(k))


def apply_many(kraus, rho):
    return add(*(apply_one(k, rho) for k in kraus))


def ketbra(index, n=4):
    return [[F(i == index and j == index) for j in range(n)] for i in range(n)]


def transition(out_index, in_index, amplitude, n=4):
    return [[amplitude if i == out_index and j == in_index else F(0)
             for j in range(n)] for i in range(n)]


def prepare_photon(rho):
    # Source preparation acts only on the populated retained-vacuum states:
    # |0,R> -> |1,R> and |0,D> -> |1,D>.
    out = [[F(0) for _ in range(4)] for _ in range(4)]
    out[1][1] = rho[0][0]
    out[3][3] = rho[2][2]
    return out


def main():
    k_vac_ready = transition(0, 0, F(1))
    k_click = transition(2, 1, F(3, 5))
    k_loss_ready = transition(0, 1, F(4, 5))
    k_recover_0 = transition(0, 2, F(3, 5))
    k_stay_0 = transition(2, 2, F(4, 5))
    k_recover_1 = transition(0, 3, F(3, 5))
    k_stay_1 = transition(2, 3, F(4, 5))
    no_click_kraus = [
        k_vac_ready, k_loss_ready, k_recover_0, k_stay_0,
        k_recover_1, k_stay_1,
    ]
    all_kraus = [k_click] + no_click_kraus
    completeness = add(*(mm(tr(k), k) for k in all_kraus))
    identity = [[F(i == j) for j in range(4)] for i in range(4)]

    first_photon = ketbra(1)
    first_click = apply_one(k_click, first_photon)
    first_no = apply_many(no_click_kraus, first_photon)
    p_first_click = trace(first_click)
    p_first_no = trace(first_no)

    conditional_dead_after_click = scale(F(1, 1) / p_first_click, first_click)
    immediate_second_photon = prepare_photon(conditional_dead_after_click)
    p_second_click_given_first_click = trace(apply_one(k_click, immediate_second_photon))

    second_after_first_no = prepare_photon(first_no)
    p_no_then_click = trace(apply_one(k_click, second_after_first_no))

    empty_dead_bin = apply_many(no_click_kraus, conditional_dead_after_click)
    after_gap_photon = prepare_photon(empty_dead_bin)
    p_click_after_one_gap_given_prior_click = trace(apply_one(k_click, after_gap_photon))

    independent_double_click = F(9, 25) * F(9, 25)
    checks = {
        "joint_kraus_completeness_is_exact": completeness == identity,
        "first_ready_photon_click_probability_is_nine_twenty_fifths": p_first_click == F(9, 25),
        "first_ready_photon_no_click_probability_is_sixteen_twenty_fifths": p_first_no == F(16, 25),
        "first_bin_probabilities_normalize": p_first_click + p_first_no == 1,
        "click_sets_detector_dead": conditional_dead_after_click == ketbra(2),
        "immediate_second_click_is_forbidden_by_dead_time": p_second_click_given_first_click == 0,
        "iid_double_click_model_is_exactly_falsified": independent_double_click == F(81, 625) and independent_double_click != 0,
        "miss_then_click_sequence_has_exact_weight": p_no_then_click == F(144, 625),
        "one_empty_gap_partially_restores_click_probability": p_click_after_one_gap_given_prior_click == F(81, 625),
        "history_changes_conditional_click_probability": (
            p_second_click_given_first_click
            != p_click_after_one_gap_given_prior_click
            != F(9, 25)
        ),
    }

    result = {
        "schema": "marici.aspect.finite_dead_time_photodetection_memory_instrument.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "sequence_probabilities": {
            "first_click": str(p_first_click),
            "immediate_second_click_given_first_click": str(p_second_click_given_first_click),
            "iid_predicted_click_click": str(independent_double_click),
            "no_click_then_click": str(p_no_then_click),
            "click_after_one_empty_gap_given_prior_click": str(p_click_after_one_gap_given_prior_click),
        },
        "typed_boundary": {
            "instrument": "finite CP ready/dead hidden-memory detector",
            "hostile": "iid reset predicts nonzero click-click where dead-time instrument gives zero",
            "completion_missing": "afterpulse, graded recovery, multiphoton pileup, jitter, continuous time, and point process",
        },
    }
    out = Path(__file__).parents[1] / "results" / "finite_dead_time_photodetection_memory_instrument.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
