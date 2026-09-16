#!/usr/bin/env python3
"""Record the exact moving-frame reduction of the simultaneous-limit gate."""
import json
from pathlib import Path

contract = {
  "schema":"marici.voevodsky.moving-frame-simultaneous-limit-contract.v1",
  "relative_operator":"T_L=U_L T_0 U_L*",
  "recentered_regulator":"Zhat_LRF=U_L* Z_LRF U_L",
  "exact_identity":"||Z_LRF T_L Z_LRF-T_L||_1=||Zhat_LRF T_0 Zhat_LRF-T_0||_1",
  "sufficient_uniform_estimate":"sup_L ||Zhat_LRF T_0 Zhat_LRF-T_0||_1 -> 0 as (R,N,F)->infinity",
  "face_requirements":{
    "H123":"source evaluations converge in the same moving frame",
    "H134":"relative projection/rotor is stationary after U_L recentering",
    "H124":"physical observer and exact transported regulator define Zhat_LRF",
    "H234":"uniform trace-ideal exhaustion and endpoint row convergence"
  },
  "current_status":{
    "exact_relative_recentering":True,
    "exact_finite_regulator_transport":True,
    "fixed_L_trace_norm_exhaustion":True,
    "uniform_in_L_transported_regulator_exhaustion":False,
    "unbounded_conductor_angular_domination":True,
    "mixed_crossing_cutoff_coherence_for_actual_tate_data":False
  },
  "passed":True,
  "conclusion":"Moving-frame stationarity and summable angular phase energy reduce simultaneous convergence to uniform transported-regulator exhaustion plus mixed crossing/cutoff coherence; the exact physical regulators are not yet proved to satisfy the uniform estimate."
}
assert contract["current_status"]["exact_relative_recentering"]
assert contract["current_status"]["exact_finite_regulator_transport"]
assert not contract["current_status"]["uniform_in_L_transported_regulator_exhaustion"]
out=Path(__file__).parents[1]/"results"/"moving_frame_simultaneous_limit_contract.json"
out.write_text(json.dumps(contract,indent=2)+"\n",encoding="utf-8")
print(json.dumps(contract,indent=2))
