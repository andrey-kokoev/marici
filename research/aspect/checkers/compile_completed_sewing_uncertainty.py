import argparse, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def compile_threshold(binding):
    try: sigma2=float(binding.get("sigma_squared")); bias=float(binding.get("systematic_frobenius_bias_bound"))
    except (TypeError,ValueError): sigma2=bias=-1
    gates={"recognized_schema":binding.get("schema")=="marici.aspect.completed-sewing-uncertainty-binding.v1","calibration_epoch_present":bool(binding.get("calibration_epoch")),"frozen_before_science":binding.get("independently_frozen_before_science_outcomes") is True,"variance_bound_positive":sigma2>0,"systematic_bias_nonnegative":bias>=0}
    if all(gates.values()):
        alpha=.01; m=144; n=1_000_000
        epsilon=math.sqrt(2*sigma2*math.log(2*m/alpha)/n); radius=math.sqrt(72)*epsilon; statistical=2*radius+radius*radius; threshold=statistical+bias
    else: epsilon=radius=statistical=threshold=None
    return {"accepted":all(gates.values()),"gates":gates,"familywise_confidence":"99/100","entrywise_quadrature_radius":epsilon,"map_frobenius_radius":radius,"statistical_residual_threshold":statistical,"systematic_bias_bound":bias if bias>=0 else None,"total_residual_threshold":threshold,"threshold_applies_to":["forward unitarity Frobenius residual","reverse-forward composition Frobenius residual"],"bound_method":"Gaussian mean tail bound plus union bound over 144 real components"}

def main():
    p=argparse.ArgumentParser();p.add_argument("binding",type=Path);p.add_argument("--output",type=Path,required=True);a=p.parse_args();r=compile_threshold(json.loads(a.binding.read_text()));r["schema"]="marici.aspect.completed-sewing-uncertainty-threshold.v1";a.output.write_text(json.dumps(r,indent=2)+"\n");print(json.dumps(r,sort_keys=True));raise SystemExit(0 if r["accepted"] else 1)
if __name__=="__main__":main()
