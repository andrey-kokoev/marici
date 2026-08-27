from copy import deepcopy
from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "three-wing-associator-preregistration.v1.json"
RESULT = ROOT / "results" / "three_wing_associator_preregistration.json"


def expected(gamma, cosine, route):
    if route in ("direct_ternary", "left_bracket", "right_bracket"):
        return gamma * cosine
    return F(0)


def fixture(contract):
    cells = []
    for gamma in (F(3, 5), F(0)):
        for cosine in (F(1), F(0), F(-1), F(0)):
            cells.append({
                "gamma": gamma, "cosine": cosine,
                "proper": {name: F(0) for name in contract["proper_phase_estimands"]},
                "routes": {route: expected(gamma, cosine, route) for route in contract["routes"]},
            })
    return {
        "records": list(contract["required_records"]), "cells": cells,
        "epochs": ["epoch-23"] * 4,
        "transfer_left": (F(3, 5), F(4, 5)),
        "transfer_right": (F(3, 5), F(4, 5)),
        "delay_left": F(0), "delay_right": F(0),
        "triad_left": (F(1, 8), F(0)), "triad_right": (F(1, 8), F(0)),
        "process_phase_left": F(0), "process_phase_right": F(0),
        "hardware_crossed": True,
        "transitions_balanced": True,
        "reset_certified": True,
        "reset_suite": {key: True for key in (
            "target_reconstruction", "coherent_process", "reset_insertion",
            "higher_history", "order_family", "depth_law", "cross_context",
            "synchronous_spectrum")},
        "compiler_interventions": {key: True for key in (
            "amplitude_cross_sweep", "three_back_hankel", "context_order_factorial",
            "period_31_spectrum", "flux_dual_gain", "controller_replay",
            "environment_tomography", "joint_signed_residual")},
        "ABBA_moments": (F(0), F(0), F(4)),
        "minimum_trials": 1000000,
    }


def assess(data, contract):
    eps = F(1, 20)
    records = set(contract["required_records"]) <= set(data["records"])
    epochs = len(set(data["epochs"])) == 1
    transfer = data["transfer_left"] == data["transfer_right"]
    delays = data["delay_left"] == data["delay_right"]
    triads = data["triad_left"] == data["triad_right"]
    process_phases = data["process_phase_left"] == data["process_phase_right"]
    hardware_crossed = data["hardware_crossed"]
    transitions_balanced = data["transitions_balanced"]
    reset_certified = data["reset_certified"]
    reset_suite = data["reset_suite"]
    compiler = data["compiler_interventions"]
    proper = all(abs(value) <= eps for cell in data["cells"] for value in cell["proper"].values())
    direct = all(abs(cell["routes"]["direct_ternary"] - cell["gamma"] * cell["cosine"]) <= eps
                 for cell in data["cells"])
    left = all(abs(cell["routes"]["left_bracket"] - cell["routes"]["direct_ternary"]) <= eps
               for cell in data["cells"])
    right = all(abs(cell["routes"]["right_bracket"] - cell["routes"]["direct_ternary"]) <= eps
                for cell in data["cells"])
    associator = all(abs(cell["routes"]["left_bracket"] - cell["routes"]["right_bracket"]) <= eps
                     for cell in data["cells"])
    destructive = all(abs(cell["routes"]["destructive_pairwise"]) <= eps for cell in data["cells"])
    zero_control = all(cell["gamma"] != 0 or all(abs(x) <= eps for x in cell["routes"].values())
                       for cell in data["cells"])
    abba = data["ABBA_moments"][:2] == (F(0), F(0))
    counts = data["minimum_trials"] >= contract["minimum_effective_trials_per_primary_proportion"]
    gates = {
        "complete_full_outcome_record": records,
        "single_shared_calibration_epoch": epochs,
        "left_right_transfer_matrices_match": transfer,
        "left_right_delays_match": delays,
        "left_right_complex_Bargmann_triads_match": triads,
        "left_right_three_body_process_phases_match": process_phases,
        "logical_bracketing_is_crossed_with_physical_hardware": hardware_crossed,
        "crossed_treatment_transitions_are_first_order_balanced": transitions_balanced,
        "memory_erasing_reset_is_independently_certified": reset_certified,
        "reset_target_transfer_is_full_rank_and_boundedly_reconstructible": reset_suite["target_reconstruction"],
        "reset_preserves_informationally_complete_coherent_process": reset_suite["coherent_process"],
        "direct_ternary_curve_is_invariant_under_reset_insertion": reset_suite["reset_insertion"],
        "reset_higher_history_rank_does_not_exceed_admitted_model": reset_suite["higher_history"],
        "reset_laws_are_invariant_under_order_family": reset_suite["order_family"],
        "reset_depth_zero_through_ten_obeys_frozen_recurrence": reset_suite["depth_law"],
        "one_reset_identity_transports_across_all_contexts": reset_suite["cross_context"],
        "schedule_synchronous_residuals_are_null": reset_suite["synchronous_spectrum"],
        "coherence_amplitude_cross_sweep_is_null": compiler["amplitude_cross_sweep"],
        "three_back_history_rank_does_not_exceed_admitted_model": compiler["three_back_hankel"],
        "context_order_interaction_is_null": compiler["context_order_factorial"],
        "prime_period_31_residual_is_null": compiler["period_31_spectrum"],
        "spanning_flux_dual_gain_transfer_is_consistent": compiler["flux_dual_gain"],
        "sealed_reset_controller_replay_is_invariant": compiler["controller_replay"],
        "environment_port_coherent_tomography_is_reconstructible": compiler["environment_tomography"],
        "joint_signed_mutation_residual_direction_is_null": compiler["joint_signed_residual"],
        "proper_phase_marginals_are_null": proper,
        "direct_ternary_curve_present": direct,
        "left_bracket_curve_matches_direct": left,
        "right_bracket_curve_matches_direct": right,
        "associator_residual_is_null": associator,
        "destructive_pairwise_route_is_null": destructive,
        "zero_source_coherence_control_is_null": zero_control,
        "ABBA_ancillary_phase_gate_passes": abba,
        "minimum_counts_and_familywise_budget_pass": counts,
    }
    return gates, all(gates.values())


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    good = fixture(contract)
    gates, accepted = assess(good, contract)
    assert accepted

    pair_leak = deepcopy(good)
    pair_leak["cells"][0]["proper"]["AB"] = F(1, 5)
    quarter_turn = deepcopy(good)
    quarter_turn["cells"][0]["routes"]["right_bracket"] = F(0)
    destructive_leak = deepcopy(good)
    destructive_leak["cells"][0]["routes"]["destructive_pairwise"] = F(3, 5)
    postselected = deepcopy(good)
    postselected["records"].remove("all_no_click_flags")
    stale = deepcopy(good)
    stale["epochs"] = ["epoch-23", "epoch-23", "epoch-24", "epoch-23"]
    transfer_mismatch = deepcopy(good)
    transfer_mismatch["transfer_right"] = (F(4, 5), F(3, 5))
    triad_mismatch = deepcopy(good)
    triad_mismatch["triad_right"] = (F(-1, 8), F(0))
    process_phase_mismatch = deepcopy(good)
    process_phase_mismatch["process_phase_right"] = F(1)
    fixed_hardware = deepcopy(good)
    fixed_hardware["hardware_crossed"] = False
    memory_unbalanced = deepcopy(good)
    memory_unbalanced["transitions_balanced"] = False
    reset_uncertified = deepcopy(good)
    reset_uncertified["reset_certified"] = False
    reset_suite_hostiles = {}
    for key in good["reset_suite"]:
        hostile = deepcopy(good)
        hostile["reset_suite"][key] = False
        reset_suite_hostiles[f"reset_{key}_hostile_rejected"] = not assess(hostile, contract)[1]
    compiler_hostiles = {}
    for key in good["compiler_interventions"]:
        hostile = deepcopy(good)
        hostile["compiler_interventions"][key] = False
        compiler_hostiles[f"compiler_{key}_hostile_rejected"] = not assess(hostile, contract)[1]

    failures = {
        "pairwise_phase_leakage_rejected": not assess(pair_leak, contract)[1],
        "quarter_turn_bracketing_offset_rejected": not assess(quarter_turn, contract)[1],
        "destructive_pairwise_fringe_rejected": not assess(destructive_leak, contract)[1],
        "no_click_postselection_rejected": not assess(postselected, contract)[1],
        "stale_route_epoch_rejected": not assess(stale, contract)[1],
        "transfer_matrix_mismatch_rejected": not assess(transfer_mismatch, contract)[1],
        "pairwise_matched_but_triad_phase_mismatch_rejected": not assess(triad_mismatch, contract)[1],
        "lower_arity_matched_but_three_body_process_phase_rejected": not assess(process_phase_mismatch, contract)[1],
        "fixed_hardware_bracketing_confounder_rejected": not assess(fixed_hardware, contract)[1],
        "first_order_route_memory_confounder_rejected": not assess(memory_unbalanced, contract)[1],
        "transition_specific_memory_without_reset_rejected": not assess(reset_uncertified, contract)[1],
    }
    failures.update(reset_suite_hostiles)
    failures.update(compiler_hostiles)
    assert all(failures.values())

    # Six proper marginals plus direct, destructive, and four crossed
    # logical-bracketing/hardware cells.
    primary = 2 * 4 * (6 + 6)
    n = contract["minimum_effective_trials_per_primary_proportion"]
    eps = F(1, 20)
    familywise = F(primary, 4 * n) / (eps * eps)
    assert primary == 96 and familywise == F(6, 625)

    out = {
        "schema": "marici.aspect.three-wing-associator-preregistration-check.v1",
        "status": "pass", "positive_fixture_accepted": accepted,
        "positive_gates": gates, "deliberate_failures": failures,
        "primary_proportion_count": primary,
        "minimum_effective_trials_per_primary_proportion": n,
        "familywise_error_upper_bound": str(familywise),
        "decisive_null": "left-bracket minus right-bracket ternary curve is zero while direct ternary visibility is nonzero and every proper phase marginal is zero",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
