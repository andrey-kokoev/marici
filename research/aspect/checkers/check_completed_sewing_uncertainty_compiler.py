from copy import deepcopy
import importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]; MODULE=ROOT/"checkers"/"compile_completed_sewing_uncertainty.py"; EXAMPLE=ROOT/"contracts"/"completed-sewing-uncertainty.example.json"; RESULT=ROOT/"results"/"completed_sewing_uncertainty_compiler.json"
spec=importlib.util.spec_from_file_location("threshold",MODULE);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

def main():
    b=json.loads(EXAMPLE.read_text()); positive=m.compile_threshold(b); assert positive["accepted"] and 0.078<positive["total_residual_threshold"]<0.079
    hostiles={}
    for name,key,value in (("zero_variance_rejected","sigma_squared","0"),("negative_bias_rejected","systematic_frobenius_bias_bound","-1"),("postoutcome_binding_rejected","independently_frozen_before_science_outcomes",False),("missing_epoch_rejected","calibration_epoch","")):
        x=deepcopy(b);x[key]=value;hostiles[name]=not m.compile_threshold(x)["accepted"]
    assert all(hostiles.values());out={"schema":"marici.aspect.completed-sewing-uncertainty-compiler-check.v1","status":"pass","example_is_not_physical_authority":True,"positive_example":positive,"deliberate_failures":hostiles,"physical_threshold_compiled":False,"missing_physical_inputs":["measured quadrature variance upper bound","measured systematic Frobenius bias bound"]}
    RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))
if __name__=="__main__":main()
