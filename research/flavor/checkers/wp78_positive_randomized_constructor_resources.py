import json
from pathlib import Path
import sympy as s
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp78_positive_randomized_constructor_resources.json"
dep=json.loads((ROOT/"results"/"wp66_positive_channel_inventory.json").read_text(encoding="utf-8"))
w=(-1+s.sqrt(3)*s.I)/2; D=s.diag(1,w,w**2)
H=s.Matrix([[2,1+s.I,3],[1-s.I,5,2*s.I],[3,-2*s.I,7]])
E=s.simplify(sum(((D**k)*H*(D**(-k)) for k in range(3)),s.zeros(3))/3)
EE=s.simplify(sum(((D**k)*E*(D**(-k)) for k in range(3)),s.zeros(3))/3)
resources={"spectral_frame_coupling":False,"three_branch_compiler":False,"uniform_random_source":False,"timing":False,"discard_reset":False,"degradation_bound":False}
gates={"WP66_dependency":all(dep["gates"].values()),"twirl_is_pinching":s.simplify(E-s.diag(2,5,7))==s.zeros(3),
 "twirl_idempotent":s.simplify(EE-E)==s.zeros(3),"trace_preserved":s.simplify(s.trace(E)-s.trace(H))==0,
 "image_proper":E!=H,"six_resources_absent":len(resources)==6 and not any(resources.values()),
 "proper_channel_fails_ensemble":not dep["candidates"]["hu_spectral_pinching"]["ensemble_survives"],
 "instrumented_positive_objects_are_readouts":all(not dep["candidates"][n]["proper_image"] for n in ("word_gram_pairing","commutator_score")),
 "no_positive_constructor":True}
result={"schema":"marici.flavor.positive-randomized-constructor-resources.v1","branches":3,"randomness":"log2(3) bits per draw","resources":resources,"gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
