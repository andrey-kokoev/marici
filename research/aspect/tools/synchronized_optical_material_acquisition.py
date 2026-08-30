"""Construct and audit synchronized uncertainty-bearing acquisition packets."""
import json, sys
from pathlib import Path

def choose(values,index):
    return values[index%len(values)]

def make_packet(contract, fixture):
    channels={}
    for i,name in enumerate(contract["required_channels"]):
        sigma=fixture["sigma"]
        channels[name]={
            "run_id":choose(fixture["run_ids"],i),
            "sample_id":choose(fixture["sample_ids"],i),
            "calibration_id":choose(fixture["calibration_ids"],i),
            "control_coordinates":[0.10,0.25,0.40,0.55,0.70,0.85],
            "values":[round((i+1)*0.1+j*0.01,6) for j in range(6)],
            "sigma":[sigma]*6,
            "covariance_diagonal":[sigma*sigma]*6 if fixture["include_covariance"] else None
        }
    return {"packet_id":fixture["id"],"channels":channels}

def audit(contract,fixture):
    packet=make_packet(contract,fixture); channels=packet["channels"]; u=contract["uncertainty"]
    complete=set(channels)==set(contract["required_channels"])
    same_run=len({x["run_id"] for x in channels.values()})==1
    same_sample=len({x["sample_id"] for x in channels.values()})==1
    same_calibration=len({x["calibration_id"] for x in channels.values()})==1
    support=all(len(x["values"])==contract["required_points_per_channel"] and
                len(x["control_coordinates"])==len(x["values"]) for x in channels.values())
    covariance=all(x["covariance_diagonal"] is not None and
                   len(x["covariance_diagonal"])==len(x["values"]) and
                   all(v>0 for v in x["covariance_diagonal"]) for x in channels.values())
    bounded=all(all(u["sigma_min"]<=s<=u["sigma_max"] for s in x["sigma"]) for x in channels.values())
    gates={"channel_completeness":complete,"same_run":same_run,"same_sample":same_sample,
           "same_calibration":same_calibration,"aligned_support":support,
           "covariance_present_positive":covariance,"uncertainty_preregistered":bounded}
    admitted=all(gates.values())
    return {"id":fixture["id"],"packet":packet,"gates":gates,"admitted":admitted,
            "expected_admit":fixture["expect_admit"],"expectation_met":admitted==fixture["expect_admit"]}

def run(contract):
    fixtures=[audit(contract,f) for f in contract["fixtures"]]
    return {"schema":"marici.aspect.synchronized-optical-material-acquisition-result.v1",
            "fixtures":fixtures,"all_expectations_met":all(x["expectation_met"] for x in fixtures),
            "hardware_acquisition_executed":False}

def main(argv):
    if len(argv)!=3:
        print("usage: synchronized_optical_material_acquisition.py CONTRACT RESULT",file=sys.stderr); return 2
    c=json.loads(Path(argv[1]).read_text(encoding="utf-8")); r=run(c)
    Path(argv[2]).write_text(json.dumps(r,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(r,indent=2)); return 0 if r["all_expectations_met"] else 1
if __name__=="__main__": raise SystemExit(main(sys.argv))
