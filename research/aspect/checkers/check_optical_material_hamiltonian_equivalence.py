import importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
contract_path=ROOT/"research/aspect/contracts/optical-material-hamiltonian-equivalence.v1.json"
result_path=ROOT/"research/aspect/results/optical_material_hamiltonian_equivalence.json"
spec=importlib.util.spec_from_file_location("equiv",ROOT/"research/aspect/tools/optical_material_hamiltonian_equivalence.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
contract=json.loads(contract_path.read_text(encoding="utf-8")); result=mod.run(contract)
by_id={x["id"]:x for x in result["fixtures"]}
hostile=by_id["independent_fit_hostile"]
checks={
 "shared_candidate_admitted":by_id["shared_transport_candidate"]["admitted"],
 "independent_fit_hostile_rejected":not hostile["admitted"],
 "hostile_channels_fit_individually":hostile["gates"]["each_channel_identifiable"],
 "hostile_fails_shared_transport":not hostile["gates"]["one_shared_transport"],
 "hostile_fails_transport_coherence":not hostile["gates"]["transport_coherence"],
 "single_channel_drift_rejected":not by_id["single_channel_drift_hostile"]["admitted"],
 "full_packets_retained":all(set(x["measured_packet"])==set(contract["channels"]) for x in result["fixtures"]),
 "no_material_claim":not result["material_superconductivity_established"]
}
packet={"schema":"marici.aspect.optical-material-hamiltonian-equivalence-check.v1","passed":all(checks.values()),"checks":checks,"result":result}
result_path.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet,indent=2)); raise SystemExit(0 if packet["passed"] else 1)
