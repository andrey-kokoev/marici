import importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
cp=ROOT/"research/aspect/contracts/synchronized-optical-material-acquisition.v1.json"
rp=ROOT/"research/aspect/results/synchronized_optical_material_acquisition.json"
spec=importlib.util.spec_from_file_location("acq",ROOT/"research/aspect/tools/synchronized_optical_material_acquisition.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
c=json.loads(cp.read_text(encoding="utf-8")); r=mod.run(c); by={x["id"]:x for x in r["fixtures"]}
checks={
 "synchronized_packet_admitted":by["synchronized_candidate"]["admitted"],
 "mixed_run_rejected":not by["mixed_run_hostile"]["admitted"],
 "mixed_sample_rejected":not by["mixed_sample_hostile"]["admitted"],
 "missing_covariance_rejected":not by["missing_covariance_hostile"]["admitted"],
 "uncertainty_inflation_rejected":not by["uncertainty_inflation_hostile"]["admitted"],
 "mixed_calibration_rejected":not by["mixed_calibration_hostile"]["admitted"],
 "raw_packets_retained":all("packet" in x for x in r["fixtures"]),
 "hardware_execution_not_fabricated":not r["hardware_acquisition_executed"]
}
out={"schema":"marici.aspect.synchronized-optical-material-acquisition-check.v1","passed":all(checks.values()),"checks":checks,"result":r}
rp.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2)); raise SystemExit(0 if out["passed"] else 1)
