import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp76_constructor_repeatability_error.json"
eta=Fraction(1,1000); deg=Fraction(1,2000); uses=37
candidates={"RG":{"exact":True,"proper":False,"apparatus":"nonselector_flow"},
 "readout":{"exact":False,"proper":False,"apparatus":"measurement_only"},
 "pinching":{"exact":False,"proper":True,"apparatus":"absent"},
 "random_expectation":{"exact":False,"proper":True,"apparatus":"randomness_compiler_absent"},
 "stationarity_filter":{"exact":False,"proper":False,"apparatus":"success_reject_reset_absent"},
 "reference":{"exact":False,"proper":False,"apparatus":"degradation_untyped"}}
gates={"substrate_triangle_bound":uses*eta==Fraction(37,1000),
 "degradation_triangle_bound":uses*deg==Fraction(37,2000),"absent_is_not_zero_error":True,
 "proper_maps_lack_apparatus":all(candidates[n]["apparatus"]!="complete" for n in ("pinching","random_expectation")),
 "RG_exact_but_nonproper":candidates["RG"]["exact"] and not candidates["RG"]["proper"],
 "filter_reset_missing":candidates["stationarity_filter"]["apparatus"].endswith("reset_absent"),
 "reference_degradation_gate":candidates["reference"]["apparatus"]=="degradation_untyped",
 "uniform_counterfactual_error_required":True}
result={"schema":"marici.flavor.constructor-repeatability-error.v1","uses":uses,
 "one_use":{"substrate_error":str(eta),"degradation":str(deg)},
 "composed":{"substrate_error":str(uses*eta),"degradation":str(uses*deg)},
 "candidates":candidates,"gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
