import importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
contract_path=ROOT/"research/aspect/contracts/optical-bath-energy-calibration.v1.json"
result_path=ROOT/"research/aspect/results/optical_bath_energy_calibration.json"
spec=importlib.util.spec_from_file_location("cal",ROOT/"research/aspect/tools/optical_bath_energy_calibration.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
contract=json.loads(contract_path.read_text(encoding="utf-8")); result=mod.run(contract)
by_id={x["id"]:x for x in result["fixtures"]}
checks={
 "equilibrium_candidate_admitted":by_id["equilibrium_candidate"]["admitted"],
 "gain_changed_candidate_admitted":by_id["gain_changed_candidate"]["admitted"],
 "absolute_gain_cancels":result["gain_invariance_relative_error"]<=contract["preregistered_thresholds"]["gain_invariance_relative_error_max"],
 "colored_bath_rejected":not by_id["colored_bath_hostile"]["admitted"],
 "scale_alias_rejected":not by_id["scale_alias_hostile"]["admitted"],
 "full_spectra_retained":all(len(x["noise_psd"])==16 and len(x["susceptibility_im"])==16 for x in result["fixtures"]),
 "no_material_claim":not result["material_room_temperature_claim"]
}
packet={"schema":"marici.aspect.optical-bath-energy-calibration-check.v1","passed":all(checks.values()),"checks":checks,"result":result}
result_path.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2)); raise SystemExit(0 if packet["passed"] else 1)
