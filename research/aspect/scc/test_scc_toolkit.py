#!/usr/bin/env python3
import tempfile
from pathlib import Path
import scc_toolkit as T
from categorical_apparatus_compiler import compile_categorical_apparatus

def main():
 m=T.migrate({"diagram":True});assert m["layers"]["base_computad"]["status"]=="not_constructed" and m["migration_residuals"]
 m=T.migrate({"diagram":True,"diagram_locator":"x","cells":True,"cells_locator":"y"});assert m["compiler_check"]["passed"] and m["layers"]["cells_and_laws"]["depends_on"]==["base_computad"]
 assert T.batch_audit({"contracts":[{"id":"a","contract":{"layers":{},"conformance":{}}}]})["passed"]
 assert not T.batch_audit({"contracts":[]})["passed"]
 assert T.profile_diff({"before":{},"after":{"base_incidence":True}})["changes"][0]["change"]=="gain"
 assert not T.profile_diff({"before":{},"after":{"base_incidence":"yes"}})["passed"]
 assert not T.promotion_lint({"literal_zero":True})["passed"]
 assert T.promotion_lint({"literal_zero":True,"literal_zero_witness":"w"})["passed"]
 with tempfile.TemporaryDirectory() as d:
  Path(d,"x").write_text("x");assert T.provenance_lock({"artifacts":["x"]},d)["passed"]
  assert not T.provenance_lock({"artifacts":["../x"]},d)["passed"]
 case={"cases":[{"id":"h","compiler":"a","contract":{"layers":{},"conformance":{}},"expected_pass":True}]};assert T.hostile_replay(case,{"a":compile_categorical_apparatus})["passed"]
 assert not T.hostile_replay({"cases":[{"compiler":"missing","expected_pass":True}]},{})["passed"]
 v=T.dependency_view({"target_claim":"identity_from_equivalence","supplied":{}});assert v["first_missing"]=="weak_equivalence_class" and len(v["edges"])==2
 d=T.dead_claims({"supplied":{"a":True},"claims":{"b":["a"],"c":["b"]}});assert d["passed"] and d["live_claims"]==["b","c"]
 assert not T.dead_claims({"supplied":{},"claims":{"c":["a"]}})["passed"]
 assert not T.monotonicity({"less_evidence":{},"more_evidence":{"x":1},"less_strength":2,"more_strength":1})["passed"]
 assert T.fixtures()["passed"]
 assert not T.schema_compat({"old":{"properties":{"a":{"type":"string"}}},"new":{"properties":{"a":{"type":"integer"}}}})["compatible"]
 n=T.normalize({"compiler":"x","result":{"passed":False}});assert n["operation_succeeded"] and not n["subject_passed"]
 assert T.residual_census({"residuals":[{"kind":"cutoff_error","codomain":"E","packet":"I","cutoff":1,"derivative_order":0,"tail_bound":"1"}]})["passed"]
 assert not T.residual_census({"residuals":[{"id":"bad","kind":"observer_invisible","codomain":"Q"}]})["passed"]
 assert T.coverage({"gates":["g"],"fixtures":[{"gate":"g","outcome":"pass"},{"gate":"g","outcome":"fail"}]})["passed"]
 b=T.budget_sensitivity({"initial_margin":"3","squares":[{"type":"localization","direction":"upper","cost":"1"},{"type":"completion_observation","direction":"upper","cost":"1/2"}]});assert b["dominant_index"]==0 and b["headroom"]=="3/2"
 assert not T.budget_sensitivity({"initial_margin":"1","squares":[{"type":"bad","direction":"upper","cost":"0"}]})["passed"]
 axes={k:"x" for k in T.AXES};assert T.interface_match({"left":axes,"right":dict(axes)})["passed"]
 assert not T.interface_match({"left":{},"right":{}})["passed"]
 mixed=T.batch_audit({"contracts":[{"id":"r","kind":"categorical_residual","contract":{"residual":{"kind":"presentation_residual","codomain":"P"}}},{"id":"d","kind":"explanation_debug","contract":{"target_claim":"identity_from_equivalence","supplied":{"weak_equivalence_class":True,"localization":True,"univalent_completion":True}}}]});assert mixed["passed"]
 nested=T.promotion_lint({"reports":[{"literal_zero":True}]});assert not nested["passed"] and nested["findings"][0]["path"]=="/reports/0"
 assert T.dependency_view({"target_claim":"identity_from_equivalence","supplied":{}})["dot"].startswith("digraph")
 with tempfile.TemporaryDirectory() as d:
  Path(d,"x.json").write_text('{"schema":"example.v1"}');assert T.provenance_lock({"artifacts":["x.json"]},d)["artifacts"][0]["schema_identity"]=="example.v1"
 assert b["stages"][0]["fraction_of_total_cost"]=="2/3"
 assert T.interface_match({"left":axes,"right":dict(axes)})["descriptor_pullback"]=="compatible_descriptors_only"
 print("SCC maintenance toolkit: 36 checks passed")
if __name__=="__main__":main()
