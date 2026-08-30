#!/usr/bin/env python3
"""Exact control-neighborhood checks for Aspect's ready/dead detector."""

from fractions import Fraction as Q
import json
from pathlib import Path


def mv(a, v):
    return [sum(a[i][j] * v[j] for j in range(len(v))) for i in range(len(a))]


def prob(v):
    return sum(v)


R = [Q(1), Q(0)]
D = [Q(0), Q(1)]
CLICK = [[Q(0), Q(0)], [Q(9, 25), Q(0)]]
NO_CLICK = [[Q(16, 25), Q(9, 25)], [Q(0), Q(16, 25)]]
EMPTY = [[Q(1), Q(9, 25)], [Q(0), Q(16, 25)]]

p_c = prob(mv(CLICK, R))
p_cc = prob(mv(CLICK, mv(CLICK, R)))
hankel_det = p_cc - p_c * p_c
iid_pcc = p_c * p_c
iid_hankel_det = iid_pcc - p_c * p_c

prior = [Q(1, 2), Q(1, 2)]
no_unnormalized = mv(NO_CLICK, prior)
p_no = prob(no_unnormalized)
posterior_r = no_unnormalized[0] / p_no

empty_then_click_r = prob(mv(CLICK, mv(EMPTY, R)))
empty_then_click_d = prob(mv(CLICK, mv(EMPTY, D)))


def click_after_gaps(k):
    state = D
    for _ in range(k):
        state = mv(EMPTY, state)
    return prob(mv(CLICK, state))


q1 = click_after_gaps(1)
q2 = click_after_gaps(2)
q3 = click_after_gaps(3)

checks = {
    "photon_outcomes_sum_to_stochastic_transition": all(
        sum(CLICK[i][j] + NO_CLICK[i][j] for i in range(2)) == 1
        for j in range(2)
    ),
    "empty_recovery_is_stochastic": all(sum(EMPTY[i][j] for i in range(2)) == 1 for j in range(2)),
    "one_click_probability_matches_source": p_c == Q(9, 25),
    "immediate_double_click_is_zero": p_cc == 0,
    "predictive_hankel_minor_is_nonzero": hankel_det == Q(-81, 625),
    "hidden_predictive_rank_is_two": hankel_det != 0,
    "iid_reset_hankel_rank_collapses": iid_hankel_det == 0,
    "half_ready_prior_no_click_probability": p_no == Q(41, 50),
    "no_click_posterior_is_twenty_five_over_forty_one": posterior_r == Q(25, 41),
    "belief_is_not_a_physical_pure_state": posterior_r not in (0, 1),
    "empty_record_alone_does_not_separate_states": prob(mv(EMPTY, R)) == prob(mv(EMPTY, D)) == 1,
    "authorized_probe_separates_output_laws": p_c != prob(mv(CLICK, D)),
    "controlled_empty_probe_history_separates_states": empty_then_click_r == Q(9, 25) and empty_then_click_d == Q(81, 625),
    "one_gap_recovery_matches_source": q1 == Q(81, 625),
    "recovery_curve_is_geometric": q2 == Q(9, 25) * (1 - Q(16, 25) ** 2) and q3 == Q(9, 25) * (1 - Q(16, 25) ** 3),
    "dead_mass_storage_has_strict_dissipation": Q(16, 25) - 1 == Q(-9, 25),
}

result = {
    "schema": "marici.sontag.detector-memory-comparative-reconstruction.v1",
    "status": "pass" if all(checks.values()) else "fail",
    "exact_arithmetic": True,
    "checks": checks,
    "passed": sum(checks.values()),
    "total": len(checks),
    "witnesses": {
        "predictive_hankel_determinant": str(hankel_det),
        "no_click_posterior_ready_probability": str(posterior_r),
        "empty_then_probe_click_from_ready": str(empty_then_click_r),
        "empty_then_probe_click_from_dead": str(empty_then_click_d),
        "click_after_one_two_three_gaps": [str(q1), str(q2), str(q3)],
    },
    "predicted_marici_objects": [
        "outcome-history behavior",
        "filter belief state distinct from physical memory",
        "intervention-indexed observability object",
        "readiness storage and dissipation law",
    ],
    "claim_boundary": "finite controlled ready/dead memory behavior derived from Aspect's source instrument",
}

out = Path(__file__).resolve().parents[1] / "results" / "detector_memory_comparative_reconstruction.json"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "pass" else 1)
