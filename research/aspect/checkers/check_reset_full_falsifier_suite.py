import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "reset-full-falsifier-suite.v1.json"
RESULT = ROOT / "results" / "reset_full_falsifier_suite.json"
PREREG = ROOT / "contracts" / "three-wing-associator-preregistration.v1.json"

SCRIPTS = {
    1: "check_blinding_reset_falsifier.py",
    2: "check_coherence_preservation_falsifier.py",
    3: "check_reset_insertion_associator_falsifier.py",
    4: "check_higher_history_memory_falsifier.py",
    5: "check_order_reversal_falsifier.py",
    6: "check_reset_depth_law_falsifier.py",
    7: "check_cross_context_reset_transport.py",
    8: "check_schedule_synchronous_adversary.py",
}

REQUIRED_GATES = {
    "reset_target_transfer_is_full_rank_and_boundedly_reconstructible",
    "reset_preserves_informationally_complete_coherent_process",
    "direct_ternary_curve_is_invariant_under_reset_insertion",
    "reset_higher_history_rank_does_not_exceed_admitted_model",
    "reset_laws_are_invariant_under_order_family",
    "reset_depth_zero_through_ten_obeys_frozen_recurrence",
    "one_reset_identity_transports_across_all_contexts",
    "schedule_synchronous_residuals_are_null",
}
GENERATED_GATES = {
    "coherence_amplitude_cross_sweep_is_null",
    "three_back_history_rank_does_not_exceed_admitted_model",
    "context_order_interaction_is_null", "prime_period_31_residual_is_null",
    "spanning_flux_dual_gain_transfer_is_consistent",
    "sealed_reset_controller_replay_is_invariant",
    "environment_port_coherent_tomography_is_reconstructible",
    "joint_signed_mutation_residual_direction_is_null",
}


def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    executions = {}
    for item in contract["required_falsifiers"]:
        index = item["index"]
        completed = subprocess.run(
            [sys.executable, str(ROOT / "checkers" / SCRIPTS[index])],
            check=False, capture_output=True, text=True,
        )
        assert completed.returncode == 0, completed.stderr
        result = json.loads((ROOT / item["result"]).read_text(encoding="utf-8"))
        assert result["status"] == "pass"
        executions[str(index)] = {"key": item["key"], "status": result["status"]}

    decisive = {
        "1_blind_rank_one": json.loads((ROOT / contract["required_falsifiers"][0]["result"]).read_text())["blind_reset_transfer_rank"] == 1,
        "2_dephasing_kills_coherence": json.loads((ROOT / contract["required_falsifiers"][1]["result"]).read_text())["dephased_output_coherence"] == "0",
        "3_reset_changes_direct_curve": not json.loads((ROOT / contract["required_falsifiers"][2]["result"]).read_text())["reset_insertion_transport_passes"],
        "4_rank_three_forces_enlargement": json.loads((ROOT / contract["required_falsifiers"][3]["result"]).read_text())["model_enlargement_forced"],
        "5_forward_reverse_differ": not json.loads((ROOT / contract["required_falsifiers"][4]["result"]).read_text())["order_independent"],
        "6_extra_mode_detected": json.loads((ROOT / contract["required_falsifiers"][5]["result"]).read_text())["extra_memory_mode_detected"],
        "7_context_transport_fails": not json.loads((ROOT / contract["required_falsifiers"][6]["result"]).read_text())["common_terminal_reset_exists"],
        "8_all_requested_periods_covered": json.loads((ROOT / contract["required_falsifiers"][7]["result"]).read_text())["periods"] == [2, 4, 8, 16, 32],
    }
    assert all(decisive.values())
    generated_run = subprocess.run(
        [sys.executable, str(ROOT / "checkers" / "check_falsifier_compiler_generated_interventions.py")],
        check=False, capture_output=True, text=True)
    assert generated_run.returncode == 0, generated_run.stderr
    generated = json.loads((ROOT / "results" / "falsifier_compiler_generated_interventions.json").read_text())
    assert generated["all_generated_interventions_operational"]
    raw_generated = {}
    for key, script, result_name in (
        ("environment_port_tomography", "check_environment_port_tomography_run_analyzer.py", "environment_port_tomography_run_analyzer.json"),
        ("sealed_controller_replay", "check_sealed_controller_replay_run_analyzer_v2.py", "sealed_controller_replay_run_analyzer_v2.json"),
    ):
        completed = subprocess.run([sys.executable, str(ROOT / "checkers" / script)],
                                   check=False, capture_output=True, text=True)
        assert completed.returncode == 0, completed.stderr
        raw_result = json.loads((ROOT / "results" / result_name).read_text())
        raw_generated[key] = raw_result["status"] == "pass"
    assert all(raw_generated.values())
    prereg = json.loads(PREREG.read_text(encoding="utf-8"))
    integration = (REQUIRED_GATES | GENERATED_GATES) <= set(prereg["acceptance_gates"])
    assert integration
    out = {
        "schema": "marici.aspect.reset-full-falsifier-suite-check.v1", "status": "pass",
        "executions": executions, "decisive_witnesses": decisive,
        "all_eight_falsifiers_executed": len(executions) == 8,
        "all_eight_repair_gates_integrated_into_associator_preregistration": integration,
        "all_eight_generated_interventions_operational_and_integrated": integration,
        "raw_generated_intervention_analyzers": raw_generated,
        "physical_reset_qualified": False,
        "physical_boundary": "no apparatus record was supplied; exact completion here is the requested falsifier architecture, not empirical reset certification",
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
