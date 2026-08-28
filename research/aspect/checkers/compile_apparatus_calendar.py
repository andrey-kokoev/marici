import argparse
from fractions import Fraction as F
from itertools import combinations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PORTFOLIO=ROOT/"contracts"/"laboratory-portfolio-acquisition.v1.json"

INSTRUMENTS={
    "environment_port_tomography":("environment_tomography_effective_attempt_rate_hz","environment_tomography_reconfiguration_seconds_per_cell"),
    "sealed_controller_replay":("controller_replay_effective_attempt_rate_hz","controller_replay_reconfiguration_seconds_per_cell"),
    "comb_referenced_flavor_comparison":("comb_comparison_effective_attempt_rate_hz","comb_comparison_reconfiguration_seconds_per_cell"),
}


def parse_positive(value):
    try:q=F(str(value))
    except (ValueError,ZeroDivisionError):return None
    return q if q>0 else None


def compile_calendar(binding):
    portfolio=json.loads(PORTFOLIO.read_text())
    gates={"recognized_binding_schema":binding.get("schema")=="marici.aspect.apparatus-capacity-measurement.v1",
           "one_nonempty_calibration_epoch":bool(binding.get("calibration_epoch")),
           "binding_frozen_before_science_outcomes":binding.get("independently_frozen_before_science_outcomes") is True,
           "coherent_environment_port_available":binding.get("coherent_environment_port_available") is True}
    available=parse_positive(binding.get("available_optical_seconds"))
    gates["available_optical_seconds_positive"]=available is not None
    durations={}; priorities={}
    for item in portfolio["candidates"]:
        key=item["key"]
        if key not in INSTRUMENTS:continue
        rate_key,setup_key=INSTRUMENTS[key];rate=parse_positive(binding.get(rate_key));setup=parse_positive(binding.get(setup_key))
        gates[f"{key}_rate_positive"]=rate is not None;gates[f"{key}_setup_positive"]=setup is not None
        if rate is not None and setup is not None:
            duration=F(item["attempted_optical_trials"],1)/rate+F(item["optical_setting_cells"],1)*setup
            durations[key]=duration;priorities[key]=F(len(item["gains"]),1)/duration
    accepted=all(gates.values()) and len(durations)==3
    selected=[];searched=0
    if accepted:
        item_by_key={i["key"]:i for i in portfolio["candidates"]}
        feasible=[]
        keys=sorted(durations)
        for n in range(len(keys)+1):
            for subset in combinations(keys,n):
                searched+=1;total=sum((durations[k] for k in subset),F(0))
                if total<=available:
                    gains=set().union(*(set(item_by_key[k]["gains"]) for k in subset)) if subset else set()
                    sectors={item_by_key[k]["sector"] for k in subset}
                    feasible.append((len(gains),len(sectors),-total,tuple(subset)))
        selected=list(max(feasible)[3])
    order=sorted(selected,key=lambda k:(-priorities[k],k)) if accepted else []
    total=sum((durations[k] for k in selected),F(0)) if accepted else None
    return {"accepted":accepted,"gates":gates,"ordered_optical_schedule":order,
            "duration_seconds":{k:str(v) for k,v in durations.items()},
            "available_optical_seconds":str(available) if available is not None else None,
            "feasible_subsets_exhausted":searched,
            "selected_optical_instruments":selected,
            "unscheduled_optical_instruments":sorted(set(durations)-set(selected)),
            "selected_optical_seconds":str(total) if total is not None else None,
            "priority_laws":{
                "environment_before_controller":"2*D_controller >= D_environment",
                "environment_before_comb":"2*D_comb >= D_environment",
                "controller_before_comb":"D_controller <= D_comb"},
            "arithmetic_parallel_member":"mixed_prime_incidence: 400 exact cases on a separate resource axis"}


def main():
    p=argparse.ArgumentParser();p.add_argument("binding",type=Path);p.add_argument("--output",type=Path,required=True);a=p.parse_args()
    result=compile_calendar(json.loads(a.binding.read_text()));result["schema"]="marici.aspect.apparatus-calendar.v1";result["binding"]=str(a.binding)
    a.output.write_text(json.dumps(result,indent=2)+"\n");print(json.dumps(result,sort_keys=True));raise SystemExit(0 if result["accepted"] else 1)


if __name__=="__main__":main()
