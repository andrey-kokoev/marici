#!/usr/bin/env python3
"""Apply lifting IR to four bounded materialized SCC examples."""
import json
from pathlib import Path
from lifting_ir import compile_lifting_ir

def coherent(id,base,projection,**kw):
 x={"id":id,"base_ref":base,"total_ref":id+":total","kind":"mathematical","state":"coherent_section","projection":projection,"inhabitance_witness":id+":inhabitance","selector":id+":selector","selector_invariance_witness":id+":invariance","section_coherence_witness":id+":coherence"};x.update(kw);return x
examples={
 "window_localization":{
  "root_object":"periodic_2pi_chart","layers":[coherent("partition","periodic_2pi_chart","forget_partition"),coherent("directed_budget","partition:total","forget_budget"),{"id":"physical_readout","base_ref":"directed_budget:total","kind":"readout","state":"not_constructed"}]},
 "optical_gram_reconstruction":{
  "root_object":"two_route_amplitudes","layers":[coherent("gram_invariants","two_route_amplitudes","forget_invariants"),coherent("four_intensity_formula","gram_invariants:total","forget_formula"),{"id":"laboratory_record","base_ref":"four_intensity_formula:total","kind":"readout","state":"not_constructed"}]},
 "theta_rh_registry_model":{
  "root_object":"theta_rh_corrected_g4_v2","layers":[{"id":"registered_evidence","base_ref":"theta_rh_corrected_g4_v2","total_ref":"registered_evidence:total","kind":"mathematical","state":"inhabited","projection":"forget_registered_evidence","inhabitance_witness":"research/aspect/scc/models.v1.json#theta-rh-corrected-g4-v2"},{"id":"categorical_completion","base_ref":"registered_evidence:total","kind":"mathematical","state":"not_constructed"}]},
 "kernel_checked_tower":{
  "root_object":"formal_base","layers":[coherent("completion","formal_base","forget_completion",unimath_certificate={"status":"kernel_checked_conditional","source_sha256":"d32638ad45ae2e5c32ac2c31834633439f07766c825cf4ffcbf2a203726b7722","object_sha256":"b7dbc4f5c01f32847c176641dc3cbe9cc469b4a82ce411243d575bbf89002152"}),coherent("certificates","completion:total","forget_certificates"),{"id":"physical_readout","base_ref":"certificates:total","kind":"readout","state":"not_constructed"}]}
}
reports={k:compile_lifting_ir(v) for k,v in examples.items()}
result={"schema":"marici.scc.lifting-ir-examples.v1","reports":reports,"summary":{k:{"compiled":r["passed"],"complete":r.get("explanation_complete"),"first_obstruction":r.get("first_obstruction"),"surviving_prefix":r.get("surviving_prefix")} for k,r in reports.items()}}
out=Path(__file__).parent/"lifting_ir_examples_results.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result["summary"],indent=2));raise SystemExit(0 if all(r["passed"] for r in reports.values()) else 1)
