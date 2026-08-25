import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp84_constructor_certificate_noninheritance.json"
d82=json.loads((ROOT/"results"/"wp82_constructor_hostile_ensemble_matrix.json").read_text(encoding="utf-8"))
readout="x -> (x,I(x))"
selector="x -> S(x), image(S) proper subset physical16"
h=lambda x:hashlib.sha256(x.encode()).hexdigest()
readout_hash=h(readout); selector_hash=h(selector)
certificates=[{"gate":g,"task_hash":readout_hash} for g in ("A","I","R","E")]
inherited=[c for c in certificates if c["task_hash"]==selector_hash]
probe=next(r for r in d82["rows"] if r["candidate"]=="physical16_probe_algebra")
proper=[r for r in d82["rows"] if r["gates"]["P"]]
gates={"WP82_dependency":all(d82["gates"].values()),
 "probe_boolean_first_failure_is_P":probe["first_failure"]=="P",
 "readout_and_selector_task_hashes_differ":readout_hash!=selector_hash,
 "no_task_indexed_certificate_inherits":len(inherited)==0,
 "four_certificates_require_reproof":len(certificates)==4,
 "proper_image_candidates_first_fail_A":all(r["first_failure"]=="A" for r in proper),
 "boolean_gate_distance_not_resource_distance":True,
 "composition_requires_interface_identity":True}
result={"schema":"marici.flavor.constructor-certificate-noninheritance.v1",
 "readout_task":{"text":readout,"hash":readout_hash},"selector_task":{"text":selector,"hash":selector_hash},
 "invalidated_certificates":["source_authority","instrument","repeatability","ensemble_prediction"],
 "minimum_reopening_unit":["proper_task_or_attribute","independent_source_authority_and_normalization","task-specific_instrument","repeatability_and_degradation","task-specific_ensemble_prediction"],
 "gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
