import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"first_raw_acquisition_portfolio.json"


def run(script):
    p=subprocess.run([sys.executable,str(ROOT/"checkers"/script)],capture_output=True,text=True,check=False)
    assert p.returncode==0,p.stderr


def main():
    for script in ("check_environment_port_tomography_run_analyzer.py",
                   "check_sealed_controller_replay_run_analyzer.py",
                   "check_four_atom_cross_scale_hostile.py",
                   "check_comb_referenced_flavor_comparison.py",
                   "check_laboratory_portfolio_schedule.py",
                   "check_apparatus_calendar_compiler.py",
                   "check_six_rung_tower.py"):
        run(script)
    env=json.loads((ROOT/"results"/"environment_port_tomography_run_analyzer.json").read_text())
    replay=json.loads((ROOT/"results"/"sealed_controller_replay_run_analyzer_v2.json").read_text())
    cross=json.loads((ROOT/"results"/"four_atom_cross_scale_hostile.json").read_text())
    comb=json.loads((ROOT/"results"/"comb_referenced_flavor_comparison.json").read_text())
    schedule=json.loads((ROOT/"results"/"laboratory_portfolio_schedule.json").read_text())
    binding=json.loads((ROOT/"contracts"/"apparatus-capacity-binding.v1.json").read_text())
    requirements={
        "1_environment_port_raw_contract_and_analyzer":env["status"]=="pass" and env["contract_attempted_trials"]==40000000,
        "2_sealed_controller_replay_raw_contract_and_analyzer":replay["status"]=="pass" and replay["contract_attempted_trials"]==80000000,
        "3_mixed_prime_common_prefix_handoff_artifact":(ROOT/"contracts"/"mixed-prime-incidence-handoff.v1.json").exists(),
        "4_four_atom_cross_scale_hostile_in_rung_five":cross["status"]=="pass" and not cross["pairwise_reciprocal_balance_is_sufficient"],
        "5_comb_referenced_flavor_instrument_without_selector_overclaim":comb["status"]=="pass" and not comb["source_selector_derived"],
        "6a_prototype_costs_replaced_by_acquisition_counts":schedule["status"]=="pass" and schedule["resource_totals"]["attempted_optical_trials"]==128000000,
        "6b_calendar_authority_bound_to_measured_apparatus":all(x["status"]=="bound" for x in binding["required_measured_inputs"]),
    }
    out={"schema":"marici.aspect.first-raw-acquisition-portfolio-audit.v1","status":"partial",
         "requirements":requirements,"completed_requirement_count":sum(requirements.values()),
         "requirement_count":len(requirements),"acquisition_authoritative":all(v for k,v in requirements.items() if k!="6b_calendar_authority_bound_to_measured_apparatus"),
         "calendar_authoritative":requirements["6b_calendar_authority_bound_to_measured_apparatus"],
         "missing_external_binding":[x["key"] for x in binding["required_measured_inputs"] if x["status"]!="bound"],
         "next_action":"bind independently measured apparatus rates, reconfiguration durations, and coherent environment-port availability; then compute and rerun the calendar schedule"}
    assert out["completed_requirement_count"]==6 and not out["calendar_authoritative"]
    RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))


if __name__=="__main__":main()
