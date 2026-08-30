"""Exact temporal contract for a state-establishing flavor scale calibration."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp548 = load("wp548_cross_locus_scale_reference_gate.json")

weights = [sp.Integer(x) for x in (1, 2, 3, 5, 7, 11)]
base_rows = sp.Matrix([[c, -c, 0] for c in weights] + [[0, 0, 1]])
interface_row = sp.Matrix([[0, 1, -1]])
active_rows = base_rows.col_join(interface_row)
scale_kernel = sp.Matrix([1, 1, 0])

validity_budget = 3
states = ("unlinked", "valid_3", "valid_2", "valid_1", "expired")


def is_valid(state):
    return state.startswith("valid_")


def age(state):
    if state == "valid_3":
        return "valid_2"
    if state == "valid_2":
        return "valid_1"
    if state == "valid_1":
        return "expired"
    return state


def step(state, event):
    if event == "calibration_success":
        return "valid_3", "reference_readback"
    if event == "calibration_null":
        return state, "no_reference_readback"
    if event == "fitted_row":
        return state, "compiler_reject"
    if event == "wait":
        return age(state), "clock_advance"
    if event == "physics_trial":
        if is_valid(state):
            return age(state), "accepted_readout"
        return state, "invalid_readout"
    raise ValueError(event)


def replay(events):
    state = "unlinked"
    observations = []
    for event in events:
        state, observation = step(state, event)
        observations.append(observation)
    return state, observations


successful_history = [
    "calibration_success",
    "physics_trial",
    "physics_trial",
    "physics_trial",
    "physics_trial",
]
success_state, success_observations = replay(successful_history)

deleted_history = successful_history[1:]
deleted_state, deleted_observations = replay(deleted_history)

expired_history = ["calibration_success", "wait", "wait", "wait", "physics_trial"]
expired_state, expired_observations = replay(expired_history)

null_history = ["calibration_null", "physics_trial"]
null_state, null_observations = replay(null_history)

fitted_history = ["fitted_row", "physics_trial"]
fitted_state, fitted_observations = replay(fitted_history)

checks = {
    "dependency_passed": bool(wp548["passed"]),
    "state_space_is_finite_and_typed": len(states) == validity_budget + 2,
    "successful_calibration_establishes_valid_state": step("unlinked", "calibration_success")
    == ("valid_3", "reference_readback"),
    "successful_calibration_reveals_and_establishes": step("expired", "calibration_success")
    == ("valid_3", "reference_readback"),
    "three_trials_are_accepted_with_budget_three": success_observations[1:4]
    == ["accepted_readout"] * 3,
    "fourth_trial_after_budget_is_rejected": success_observations[4] == "invalid_readout"
    and success_state == "expired",
    "expiry_forbids_late_readout": expired_observations[-1] == "invalid_readout"
    and expired_state == "expired",
    "null_calibration_does_not_establish_interface": null_observations
    == ["no_reference_readback", "invalid_readout"]
    and null_state == "unlinked",
    "fitted_row_is_compiler_rejected": fitted_observations
    == ["compiler_reject", "invalid_readout"]
    and fitted_state == "unlinked",
    "deletion_replay_invalidates_dependent_readouts": deleted_observations
    == ["invalid_readout"] * 4
    and deleted_state == "unlinked",
    "inactive_contract_has_rank_two": base_rows.rank() == 2,
    "inactive_contract_restores_scale_kernel": base_rows * scale_kernel == sp.zeros(7, 1),
    "valid_contract_has_rank_three": active_rows.rank() == 3,
    "valid_contract_has_zero_kernel": len(active_rows.nullspace()) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

transition_table = {}
for state in states:
    transition_table[state] = {}
    for event in (
        "calibration_success",
        "calibration_null",
        "fitted_row",
        "wait",
        "physics_trial",
    ):
        next_state, observation = step(state, event)
        transition_table[state][event] = {
            "next_state": next_state,
            "observation": observation,
        }

result = {
    "work_package": "WP549",
    "domain": "A bounded temporal contract for the still-propositional WP548 P_scale interface, with three accepted physics trials per successful calibration.",
    "states": list(states),
    "events": [
        "calibration_success",
        "calibration_null",
        "fitted_row",
        "wait",
        "physics_trial",
    ],
    "transition_table": transition_table,
    "support_contract": {
        "accepted_language": "Every accepted_readout has a preceding calibration_success whose validity budget has not expired.",
        "forbidden_histories": [
            "physics_trial accepted before calibration_success",
            "physics_trial accepted after validity expiry",
            "calibration_null followed by accepted physics_trial",
            "fitted_row followed by accepted physics_trial",
        ],
        "null_outcome": "calibration_null is an observed completed trial and leaves the interface unestablished.",
    },
    "state_establishing_event": {
        "event": "calibration_success",
        "reveals": "the named transfer chain produced a reference readback",
        "establishes": "the shared flavor/comb frame for three declared physics trials",
        "consumes": "one validity unit per physics trial or wait step",
    },
    "rank_by_state": {
        "unlinked_or_expired": base_rows.rank(),
        "valid": active_rows.rank(),
        "deletion_replay_kernel": [str(x) for x in scale_kernel],
    },
    "theorem": "A P_scale row has detector authority only as the post-state of a successful calibration event. The finite automaton admits physics readout during a three-step validity window, rejects null, fitted, pre-calibration and expired histories, and restores the exact (1,1,0) scale kernel when the calibration event is deleted.",
    "classification": "Exact temporal interface acceptance theorem and deletion replay. It does not realize P_scale or select the flavor source.",
    "selector": bool(wp548["selector"]),
    "instrument": "Temporal contract specified; physical transfer chain, readback distribution, disturbance model, and covariance remain to be realized.",
    "smallest_exact_falsifier": "Delete calibration_success from a history containing an accepted physics readout. If the compiler still retains rank three or accepts the readout, it has converted a fitted row into authority.",
    "remaining_gate": "Implement the named P_scale apparatus and replace the three-step illustrative validity budget with independently calibrated drift, disturbance, cost, and covariance dynamics.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp549_temporal_scale_calibration_contract.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
