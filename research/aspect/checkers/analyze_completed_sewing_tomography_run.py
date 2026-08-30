import argparse, csv, json
from collections import Counter, defaultdict
from pathlib import Path
import sympy as s

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/"contracts"/"completed-sewing-tomography-acquisition.v1.json"

def assess(rows):
    c=json.loads(CONTRACT.read_text()); ports=c["ports"]; directions=c["directions"]
    expected={(d,i,o) for d in directions for i in ports for o in ports}; seen={}; settings=defaultdict(set)
    epochs=set(); los=set(); metrics=set(); envs=set(); digests=defaultdict(set); complete=True; source_ok=True; calibrated=True; trials_ok=True
    required=set(c["required_columns"])
    for row in rows:
        complete &= required<=set(row) and all(row.get(k,"")!="" for k in required)
        key=(row.get("direction"),row.get("input_port"),row.get("output_port"))
        if key not in expected or key in seen: complete=False; continue
        try: z=s.Rational(row["amplitude_re"])+s.I*s.Rational(row["amplitude_im"]); trials=int(row["trial_count"])
        except (ValueError,TypeError): complete=False; continue
        seen[key]=z; settings[row["direction"]].add((row["setting_key"],row["input_port"]))
        epochs.add(row["acquisition_epoch"]); los.add(row["common_lo_key"]); metrics.add(row["source_metric_key"]); envs.add(row["environment_manifest"]); digests[row["direction"]].add(row["source_map_digest"])
        source_ok &= row["source_derived_before_outcomes"]=="true"; calibrated &= row["calibration_status"]=="pass"; trials_ok &= trials>=c["minimum_trials_per_setting"]
    all_cells=set(seen)==expected
    def matrix(direction): return s.Matrix([[seen[(direction,i,o)] for i in ports] for o in ports])
    if all_cells:
        F=matrix("forward"); R=matrix("reverse"); unit=s.simplify(s.conjugate(F).T*F-s.eye(6)); inverse=s.simplify(R*F-s.eye(6))
    else: F=R=None; unit=inverse=None
    setting_ok=all(len(settings[d])==6 and len({k for k,_ in settings[d]})==6 and len({i for _,i in settings[d]})==6 for d in directions)
    gates={"complete_unique_72_cell_record":complete and all_cells,"twelve_unique_basis_settings":setting_ok,"one_epoch_lo_metric_and_environment":len(epochs)==len(los)==len(metrics)==len(envs)==1,"one_frozen_digest_per_direction":all(len(digests[d])==1 for d in directions),"source_derived_before_outcomes":source_ok,"all_calibrations_pass":calibrated,"minimum_trials_per_setting":trials_ok,"forward_map_unitary":unit==s.zeros(6) if unit is not None else False,"reverse_composes_to_identity":inverse==s.zeros(6) if inverse is not None else False}
    return {"accepted":all(gates.values()),"gates":gates,"forward_unitarity_residual":str(unit),"reverse_composition_residual":str(inverse),"record_count":len(seen),"setting_count":sum(len({k for k,_ in settings[d]}) for d in directions)}

def main():
    p=argparse.ArgumentParser(); p.add_argument("input_csv",type=Path); p.add_argument("--output",type=Path,required=True); a=p.parse_args()
    with a.input_csv.open(newline="",encoding="utf-8") as h:r=assess(csv.DictReader(h))
    r["schema"]="marici.aspect.completed-sewing-tomography-run-analysis.v1"; a.output.write_text(json.dumps(r,indent=2)+"\n"); print(json.dumps(r,sort_keys=True)); raise SystemExit(0 if r["accepted"] else 1)
if __name__=="__main__":main()
