from copy import deepcopy
import importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; MODULE=ROOT/"checkers"/"analyze_sealed_controller_replay_run_v2.py"; RESULT=ROOT/"results"/"sealed_controller_replay_run_analyzer_v2.json"
spec=importlib.util.spec_from_file_location("replay_v2",MODULE); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)

def rows(n=80):
    out=[]
    for ci,(arm,bound,actual,target) in enumerate(sorted(m.cells())):
        for i in range(n):
            hit=4+m.TREATMENTS.index(target)*2
            out.append({"trial_key":f"{arm}-{bound}-{actual}-{target}-{i}","acquisition_epoch":"replay-2","arm":arm,"transcript_bound_predecessor":bound,"actual_predecessor":actual,"target":target,"controller_transcript_key":f"tx-{bound}-{target}","sealed_payload_digest":f"digest-{bound}-{target}","controller_input_manifest":"transcript_bound_predecessor,target,calibration_epoch","correction_command":f"cmd-{bound}-{target}","target_outcome":str(int(i<hit)),"reset_monitor_outcome":"0","reset_failure":str(int(i==0)),"acquisition_block":f"block-{i}","within_block_position":str((ci+i)%80),"sealed_schedule_key":"replay-schedule-2"})
    return out

def main():
    good=rows(); positive=m.assess(good,64); assert positive["accepted"] and positive["cell_count_lower_bound"]==80
    adaptive=deepcopy(good)
    for r in adaptive:
        if r["arm"]=="sealed_replay" and r["actual_predecessor"]=="R1": r["target_outcome"]="1" if int(r["trial_key"].rsplit("-",1)[1])<32 else "0"
    side=deepcopy(good)
    for r in side:r["controller_input_manifest"]+=",actual_predecessor"
    mutable=deepcopy(good); mutable[0]["correction_command"]="adaptive-command"
    illegal=deepcopy(good); illegal[0]["transcript_bound_predecessor"]="R1" if illegal[0]["actual_predecessor"]!="R1" else "L1"
    missing=good[:-80]; grouped=deepcopy(good)
    for r in grouped:r["acquisition_block"]=r["arm"]
    hostiles={"replay_adaptation_rejected":not m.assess(adaptive,64)["accepted"],"actual_predecessor_sidechannel_rejected":not m.assess(side,64)["accepted"],"mutable_transcript_rejected":not m.assess(mutable,64)["accepted"],"missing_cell_rejected":not m.assess(missing,80)["accepted"],"illegal_live_counterfactual_bound_cell_rejected":not m.assess(illegal,64)["accepted"],"grouped_acquisition_rejected":not m.assess(grouped,80)["accepted"]}
    assert all(hostiles.values()); out={"schema":"marici.aspect.sealed-controller-replay-run-analyzer-check.v2","status":"pass","positive_fixture":positive,"deliberate_failures":hostiles,"contract_attempted_trials":80000000,"removed_redundant_live_cells":48,"trial_reduction_fraction":"3/8"}
    RESULT.write_text(json.dumps(out,indent=2)+"\n"); print(json.dumps(out,sort_keys=True))
if __name__=="__main__": main()
