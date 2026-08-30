from copy import deepcopy
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; MODULE=ROOT/"checkers"/"analyze_sealed_controller_replay_run.py"; RESULT=ROOT/"results"/"sealed_controller_replay_run_analyzer.json"
spec=importlib.util.spec_from_file_location("replay",MODULE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)


def rows(n=128):
    out=[]
    for ci,(arm,bound,actual,target) in enumerate(sorted(m.cells())):
        for i in range(n):
            hit=4+m.TREATMENTS.index(target)*2
            out.append({"trial_key":f"{arm}-{bound}-{actual}-{target}-{i}","acquisition_epoch":"replay-1","arm":arm,
                        "transcript_bound_predecessor":bound,"actual_predecessor":actual,"target":target,
                        "controller_transcript_key":f"tx-{bound}-{target}","sealed_payload_digest":f"digest-{bound}-{target}",
                        "controller_input_manifest":"transcript_bound_predecessor,target,calibration_epoch","correction_command":f"cmd-{bound}-{target}",
                        "target_outcome":str(int(i<hit)),"reset_monitor_outcome":"0","reset_failure":str(int(i==0)),
                        "acquisition_block":f"block-{i}","within_block_position":str((ci+i)%128),"sealed_schedule_key":"replay-schedule-1"})
    return out


def main():
    good=rows();positive=m.assess(good,64);assert positive["accepted"]
    adaptive=deepcopy(good)
    for r in adaptive:
        if r["arm"]=="sealed_replay" and r["actual_predecessor"]=="R1": r["target_outcome"]="1" if int(r["trial_key"].rsplit("-",1)[1])<32 else "0"
    sidechannel=deepcopy(good)
    for r in sidechannel:r["controller_input_manifest"]+=",actual_predecessor"
    mutable=deepcopy(good);mutable[0]["correction_command"]="adaptive-command"
    missing=good[:-128]
    grouped=deepcopy(good)
    for r in grouped:r["acquisition_block"]=r["arm"]
    hostiles={"live_invariant_but_replay_adaptation_rejected":not m.assess(adaptive,64)["accepted"],
              "actual_predecessor_sidechannel_rejected":not m.assess(sidechannel,64)["accepted"],
              "mutable_transcript_rejected":not m.assess(mutable,64)["accepted"],
              "missing_cell_rejected":not m.assess(missing,128)["accepted"],
              "grouped_acquisition_rejected":not m.assess(grouped,128)["accepted"]}
    assert all(hostiles.values())
    out={"schema":"marici.aspect.sealed-controller-replay-run-analyzer-check.v1","status":"pass","positive_fixture":positive,
         "deliberate_failures":hostiles,"contract_attempted_trials":128000000}
    RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))


if __name__=="__main__":main()
