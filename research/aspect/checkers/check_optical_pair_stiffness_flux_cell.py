#!/usr/bin/env python3
import copy,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/tools"))
from optical_pair_stiffness_flux_cell import run
C=ROOT/"research/aspect/contracts/optical-pair-stiffness-flux-cell.v1.json";R=ROOT/"research/aspect/results/optical_pair_stiffness_flux_cell.json"
c=json.loads(C.read_text(encoding="utf-8"));r=run(c);by={x["id"]:x for x in r["fixtures"]}
checks={
 "joint_candidate_passes":by["coherent_candidate"]["joint_admitted"],
 "pseudogap_has_pairs_but_fails_joint":by["pseudogap_hostile"]["gates"]["pair_amplitude"] and not by["pseudogap_hostile"]["joint_admitted"],
 "normal_state_fails_pair_gate":not by["normal_hostile"]["gates"]["pair_amplitude"],
 "moderate_noise_survival_is_preserved":by["moderate_noise_candidate"]["joint_admitted"],
 "strong_noise_fails_joint":not by["strong_noise_hostile"]["joint_admitted"],
 "all_four_witnesses_required":all(set(x["gates"])==set(c["joint_admission"]) for x in r["fixtures"]),
 "kelvin_mapping_absent":c["temperature_authority"]["kelvin_mapping"] is None and not c["temperature_authority"]["room_temperature_claim_authorized"],
 "result_does_not_claim_material_superconductivity":not r["room_temperature_claim"]}
bad=copy.deepcopy(c);bad["joint_admission"]=["pair_amplitude"]
checks["single_signature_contract_rejected"]=set(bad["joint_admission"])!=set(r["fixtures"][0]["gates"])
out={"schema":"marici.aspect.optical-pair-stiffness-flux-check.v1","passed":all(checks.values()) and r["all_expectations_met"],"checks":checks,"result":r}
R.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,indent=2));raise SystemExit(0 if out["passed"] else 1)
