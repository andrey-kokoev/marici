from copy import deepcopy
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
MODULE=ROOT/"checkers"/"compile_apparatus_calendar.py"
RESULT=ROOT/"results"/"apparatus_calendar_compiler.json"
EXAMPLE=ROOT/"contracts"/"apparatus-capacity-measurement.example.json"
spec=importlib.util.spec_from_file_location("calendar",MODULE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)


def main():
    binding=json.loads(EXAMPLE.read_text());positive=m.compile_calendar(binding);assert positive["accepted"]
    assert positive["duration_seconds"]=={
        "environment_port_tomography":"5200",
        "sealed_controller_replay":"4800",
        "comb_referenced_flavor_comparison":"2080"}
    assert positive["selected_optical_instruments"]==["comb_referenced_flavor_comparison","environment_port_tomography"]
    assert positive["unscheduled_optical_instruments"]==["sealed_controller_replay"]
    assert positive["selected_optical_seconds"]=="7280" and positive["feasible_subsets_exhausted"]==8
    hostiles={}
    mutations={"unfrozen_binding_rejected":("independently_frozen_before_science_outcomes",False),
               "missing_environment_port_rejected":("coherent_environment_port_available",False),
               "zero_rate_rejected":("environment_tomography_effective_attempt_rate_hz","0"),
               "negative_setup_rejected":("controller_replay_reconfiguration_seconds_per_cell","-1"),
               "missing_epoch_rejected":("calibration_epoch","")}
    mutations["zero_available_time_rejected"]=("available_optical_seconds","0")
    for name,(key,value) in mutations.items():
        hostile=deepcopy(binding);hostile[key]=value;hostiles[name]=not m.compile_calendar(hostile)["accepted"]
    alias=deepcopy(binding);alias["environment_tomography_effective_attempt_rate_hz"]="not-a-rate"
    hostiles["malformed_rate_rejected"]=not m.compile_calendar(alias)["accepted"]
    assert all(hostiles.values())
    out={"schema":"marici.aspect.apparatus-calendar-compiler-check.v1","status":"pass",
         "example_is_not_physical_authority":"EXAMPLE-NOT-PHYSICAL-AUTHORITY" in binding["calibration_epoch"],
         "positive_example":positive,"deliberate_failures":hostiles,
         "real_apparatus_calendar_compiled":False,
         "missing_real_binding_contract":"contracts/apparatus-capacity-binding.v1.json"}
    RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))


if __name__=="__main__":main()
