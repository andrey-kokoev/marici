from copy import deepcopy
import importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; MODULE=ROOT/"checkers"/"analyze_completed_sewing_tomography_run.py"; RESULT=ROOT/"results"/"completed_sewing_tomography_run_analyzer.json"
spec=importlib.util.spec_from_file_location("sewing",MODULE); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
PORTS=["primitive","prime_square","seam","endpoint","connected_tail","archimedean"]

def rows():
    out=[]
    for direction in ("forward","reverse"):
        for i,inp in enumerate(PORTS):
            for o,outp in enumerate(PORTS):
                out.append({"acquisition_epoch":"sewing-1","direction":direction,"input_port":inp,"output_port":outp,"amplitude_re":str(int(o==5-i)),"amplitude_im":"0","common_lo_key":"lo-1","source_map_digest":f"source-derived-{direction}","source_metric_key":"metric-1","environment_manifest":"all-six-plus-dilation","source_derived_before_outcomes":"true","calibration_status":"pass","trial_count":"1000000","setting_key":f"{direction}-{inp}"})
    return out

def main():
    good=rows(); positive=m.assess(good); assert positive["accepted"]
    anisotropic=deepcopy(good)
    for r in anisotropic:
        if r["direction"]=="forward" and r["input_port"]=="primitive" and r["output_port"]=="archimedean":r["amplitude_re"]="2"
        if r["direction"]=="forward" and r["input_port"]=="prime_square" and r["output_port"]=="connected_tail":r["amplitude_re"]="1/2"
    wrong_reverse=deepcopy(good); wrong_reverse[0]["amplitude_re"]="1"
    split_lo=deepcopy(good)
    for r in split_lo:
        if r["direction"]=="reverse":r["common_lo_key"]="lo-2"
    unfrozen=deepcopy(good); unfrozen[0]["source_derived_before_outcomes"]="false"
    env=deepcopy(good); env[0]["environment_manifest"]="five-ports-only"
    hostiles={"determinant_style_anisotropic_gain_rejected":not m.assess(anisotropic)["accepted"],"assumed_reverse_rejected":not m.assess(wrong_reverse)["accepted"],"split_phase_reference_rejected":not m.assess(split_lo)["accepted"],"postoutcome_source_fit_rejected":not m.assess(unfrozen)["accepted"],"environment_omission_rejected":not m.assess(env)["accepted"],"missing_archimedean_cell_rejected":not m.assess(good[:-1])["accepted"]}
    assert all(hostiles.values()); out={"schema":"marici.aspect.completed-sewing-tomography-run-analyzer-check.v1","status":"pass","positive_fixture":positive,"deliberate_failures":hostiles,"contract_setting_count":12,"contract_complex_cells":72,"contract_attempted_trials":12000000,"physical_uncertainty_threshold_bound":False}
    RESULT.write_text(json.dumps(out,indent=2)+"\n"); print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
