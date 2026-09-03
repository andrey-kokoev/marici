#!/usr/bin/env python3
from explanation_debugger import debug_explanation as D,propagate_comparison_budget as B

def main():
 r=D({"target_claim":"observational_equivalence","supplied":{}});assert r["first_missing_arrow"]=="weak_equivalence_class" and r["minimal_obstruction"]==["weak_equivalence_class"]
 supplied={x:True for x in ("weak_equivalence_class","localization","univalent_completion")}
 r=D({"target_claim":"observational_equivalence","supplied":supplied});assert r["first_missing_arrow"]=="record_ontology" and "physical_backend" in r["retract_downstream"]
 supplied.update({x:True for x in ("record_ontology","detector_map","physical_interface","descent_authority","observational_quotient")})
 assert D({"target_claim":"observational_equivalence","supplied":supplied})["passed"]
 assert D({"target_claim":"strict_selected_filler","supplied":{"filler_family":True}})["first_missing_arrow"]=="selection_map"
 assert D({"target_claim":"cross_sector_composition","supplied":{"sector_vertices":True}})["first_missing_arrow"]=="overlap_incidence"
 assert D({"target_claim":"bounded_completeness","supplied":{"horn_boundaries":True}})["first_missing_arrow"]=="horn_fillers"
 assert not D({"target_claim":"unknown","supplied":{}})["passed"]
 r=B({"initial_margin":"3","squares":[{"type":"localization","direction":"upper","cost":"1/2"},{"type":"completion_observation","direction":"upper","cost":"1"}]});assert r["passed"] and r["residual_margin"]=="3/2"
 r=B({"initial_margin":"1","squares":[{"type":"coherence_positivity","direction":"upper","cost":"1"}]});assert r["first_exhausted_square"]==0
 assert B({"initial_margin":"1","squares":[{"type":"localization","direction":"point","cost":"0"}]})["first_failed_gate"]=="bound_direction"
 assert B({"initial_margin":"1","squares":[{"type":"bad","direction":"upper","cost":"0"}]})["first_failed_gate"]=="square_type"
 print("explanation debugger: 11 checks passed")
if __name__=="__main__":main()
