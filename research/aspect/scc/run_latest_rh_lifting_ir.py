#!/usr/bin/env python3
"""Apply lifting IR to Voevodsky's current categorical RH form-core model."""
import hashlib,json
from pathlib import Path
from lifting_ir import compile_lifting_ir
ROOT=Path(__file__).resolve().parents[3]
source=ROOT/"research/voevodsky/categorical-rh-proof-bracket-form-core-v1.json"
data=json.loads(source.read_text(encoding="utf-8"));digest=hashlib.sha256(source.read_bytes()).hexdigest()
contract={"root_object":"arithmetic_source_A","layers":[
 {"id":"necessary_restriction_bracket","base_ref":"arithmetic_source_A","total_ref":"necessary_restriction_bracket:total","kind":"mathematical","state":"coherent_section","projection":"forget_packet_restriction","inhabitance_witness":str(source),"selector":"typed_restriction_j_star","selector_invariance_witness":"necessary_chain_typed","section_coherence_witness":"finite_packet_PSD_is_necessary"},
 {"id":"common_closed_form_domain","base_ref":"necessary_restriction_bracket:total","total_ref":"common_closed_form_domain:total","kind":"mathematical","state":"not_constructed"},
 {"id":"gaussian_jet_form_core","base_ref":"common_closed_form_domain:total","total_ref":"gaussian_jet_form_core:total","kind":"mathematical","state":"not_constructed"},
 {"id":"source_Weil_comparison","base_ref":"gaussian_jet_form_core:total","total_ref":"source_Weil_comparison:total","kind":"mathematical","state":"not_constructed"},
 {"id":"RH_implication","base_ref":"source_Weil_comparison:total","kind":"mathematical","state":"not_constructed"}]}
report=compile_lifting_ir(contract)
result={"schema":"marici.scc.latest-rh-lifting-ir.v1","source":str(source.relative_to(ROOT)),"source_sha256":digest,"source_status":data["status"],"report":report,"interpretation":{"necessary_direction":"survives as typed restriction bracket","first_missing_object":"common closed or closable realization of A and B on D(Q)","acceptance_test":data["acceptance_test"],"rh_conclusion":"not admitted"}}
out=Path(__file__).parent/"latest_rh_lifting_ir_results.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"source_sha256":digest,"compiled":report["passed"],"complete":report.get("explanation_complete"),"first_obstruction":report.get("first_obstruction"),"surviving_prefix":report.get("surviving_prefix"),"rh_conclusion":"not admitted"},indent=2));raise SystemExit(0 if report["passed"] else 1)
