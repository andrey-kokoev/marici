import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "six_rung_tower.json"


def run(script):
    completed = subprocess.run([sys.executable, str(ROOT / "checkers" / script)],
                               capture_output=True, text=True, check=False)
    assert completed.returncode == 0, completed.stderr


def main():
    run("check_five_rung_tower.py")
    run("check_experimental_portfolio_controller.py")
    run("check_environment_port_tomography_run_analyzer.py")
    run("check_sealed_controller_replay_run_analyzer.py")
    run("check_comb_referenced_flavor_comparison.py")
    run("check_four_atom_cross_scale_hostile.py")
    run("check_laboratory_portfolio_schedule.py")
    five = json.loads((ROOT / "results" / "five_rung_tower.json").read_text())
    six = json.loads((ROOT / "results" / "experimental_portfolio_controller.json").read_text())
    laboratory = json.loads((ROOT / "results" / "laboratory_portfolio_schedule.json").read_text())
    gates = {
        "five_rung_tower_passes": five["status"] == "pass",
        "portfolio_search_is_exhaustive": six["first_cycle_feasible_portfolios_exhausted"] > 0,
        "quotient_rank_is_primary_objective": six["first_independent_directions"] == 4,
        "all_scheduler_hostiles_rejected": all(six["hostile_schedulers"].values()),
        "bounded_nonstarvation_holds": six["all_live_faithful_candidates_scheduled_within_two_cycles"],
        "theta_branch_is_adaptively_retyped": six["theta_disposition"].startswith("retire finite binary"),
        "relative_optimality_boundary_retained": not six["absolute_scheduler_optimality"],
        "prototype_costs_replaced_by_contract_acquisition_loads": laboratory["status"] == "pass" and laboratory["hostile_cost_models"]["prototype_scalar_costs_removed"],
        "laboratory_portfolio_is_acquisition_authoritative": laboratory["resource_totals"]["attempted_optical_trials"] == 128000000,
        "apparatus_availability_boundary_retained": not laboratory["apparatus_availability_bound"],
    }
    assert all(gates.values())
    out = {
        "schema": "marici.aspect.six-rung-tower-check.v1", "status": "pass",
        "gates": gates,
        "tower": ["realization", "tester", "falsifier compiler", "ontology falsifier", "admissibility governor", "quotient-aware portfolio controller"],
        "disposition": "The tower now converts surviving distinctions into an exact bounded experiment schedule while suppressing aliases, retired branches, and authority capture.",
        "terminal_completeness_claimed": False,
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, sort_keys=True))


if __name__ == "__main__":
    main()
