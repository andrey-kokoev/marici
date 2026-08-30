import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp85_pinching_coherent_task_package.json"
d58=json.loads((ROOT/"results"/"wp58_commutator_score_selector_gate.json").read_text(encoding="utf-8"))
d66=json.loads((ROOT/"results"/"wp66_positive_channel_inventory.json").read_text(encoding="utf-8"))
d78=json.loads((ROOT/"results"/"wp78_positive_randomized_constructor_resources.json").read_text(encoding="utf-8"))
d84=json.loads((ROOT/"results"/"wp84_constructor_certificate_noninheritance.json").read_text(encoding="utf-8"))
w=(-1+s.sqrt(3)*s.I)/2; D=s.diag(1,w,w**2)
H=s.Matrix([[2,1+s.I,3],[1-s.I,5,2*s.I],[3,-2*s.I,7]])
E=lambda X:s.simplify(sum(((D**k)*X*(D**(-k)) for k in range(3)),s.zeros(3))/3)
EH=E(H); EEH=E(EH)
fields={
 "proper_operation_attribute":{"mathematical":True,"physical":True},
 "independent_normalization":{"mathematical":True,"physical":False},
 "independent_source_authority":{"mathematical":None,"physical":False},
 "task_specific_instrument":{"mathematical":True,"physical":False},
 "repeatability_degradation":{"mathematical":True,"physical":False},
 "own_ensemble_prediction":{"mathematical":True,"physical":False}}
gates={"WP58_dependency":all(d58["gates"].values()),"WP66_dependency":all(d66["gates"].values()),
 "WP78_dependency":all(d78["gates"].values()),"WP84_dependency":all(d84["gates"].values()),
 "task_is_exactly_idempotent":s.simplify(EEH-EH)==s.zeros(3),"task_image_is_proper":EH!=H,
 "normalization_is_prefit_group_average":d78["branches"]==3,"source_authority_absent":not d66["candidates"]["hu_spectral_pinching"]["source_authorized"],
 "all_six_instrument_resources_absent":not any(d78["resources"].values()),
 "physical_degradation_untyped":True,"own_prediction_is_commuting_locus":d58["classification"]["minimum_locus"].startswith("commuting"),
 "ensemble_prediction_fails":not d66["candidates"]["hu_spectral_pinching"]["ensemble_survives"],
 "package_is_not_physical_constructor":not all(v["physical"] for v in fields.values())}
result={"schema":"marici.flavor.pinching-coherent-task-package.v1","task":"T_E:(Hu,Hd)->(Hu,E_Hu(Hd))","attribute":"[Hu,Hd]=0","fields":fields,
 "missing_physical_cut":["source_authority","task_specific_instrument_and_degradation","ensemble_survival"],
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
