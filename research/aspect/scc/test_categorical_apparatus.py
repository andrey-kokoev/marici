#!/usr/bin/env python3
from categorical_apparatus_compiler import compile_categorical_apparatus as A
from categorical_residual_compiler import compile_categorical_residual as R

def base():
 return {"layers":{"base_computad":{"status":"constructed","artifact_locator":"x"}},
 "conformance":{"base_incidence":True}}

def main():
 assert A(base())["passed"]
 x=base();x["layers"]["cells_and_laws"]={"status":"constructed","artifact_locator":"y","depends_on":["base_computad"]};assert A(x)["passed"]
 x=base();x["layers"]["partial_completion"]={"status":"constructed","artifact_locator":"y","depends_on":["cells_and_laws"]};assert A(x)["first_failed_gate"]=="dependency_dag"
 x=base();x["ports"]={"univalent_completion":{"presentation":"Rezk","equivalences_as_identity_paths_verified":True}};assert A(x)["first_failed_gate"]=="univalent_completion"
 x=base();x["ports"]={"localization":{"weak_equivalence_class_locator":"W","universal_inversion_verified":True},"univalent_completion":{"presentation":"Rezk","equivalences_as_identity_paths_verified":True}};assert A(x)["passed"]
 x=base();x["ports"]={"observational_quotient":{"record_ontology":"R"}};assert A(x)["first_failed_gate"]=="observational_quotient"
 x=base();x["filler"]={"exists":True,"selected":True};assert A(x)["first_failed_gate"]=="strict_selection"
 x=base();x["horn_coverage"]=[{"dimension":2,"boundary_locator":"b","filler_type":"f","coverage_bound":3}];assert A(x)["passed"]
 x=base();x["conformance"]={"physical_backend":True};assert A(x)["first_failed_gate"]=="physical_backend"
 assert R({"residual":{"kind":"presentation_residual","codomain":"P"}})["passed"]
 assert R({"residual":{"kind":"observer_invisible","codomain":"kerO/G"}})["first_failed_gate"]=="observer_quotient"
 r={"kind":"observer_invisible","codomain":"kerO/G","gauge_in_observer_kernel_witness":"w","literal_zero":True};assert R({"residual":r})["first_failed_gate"]=="zero_promotion"
 r={"kind":"observer_invisible","codomain":"kerO/G","gauge_in_observer_kernel_witness":"w"};assert R({"residual":r})["passed"]
 r={"kind":"cutoff_error","codomain":"E","packet":"I","cutoff":8,"derivative_order":2,"tail_bound":"1/8"};assert R({"residual":r,"comparison_squares":[{"type":"completion_observation","tail_residual":"1/8"}]})["passed"]
 assert R({"residual":{"kind":"substantive_positive","codomain":"R"},"comparison_squares":[{"type":"coherence_positivity"}]})["first_failed_gate"]=="comparison_square"
 print("categorical apparatus: 15 checks passed")
if __name__=="__main__":main()
