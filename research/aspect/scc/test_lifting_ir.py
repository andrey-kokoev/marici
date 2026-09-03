#!/usr/bin/env python3
from lifting_ir import compile_lifting_ir as C

def layer(id,base,state="coherent_section",**kw):
 x={"id":id,"base_ref":base,"state":state,"kind":"mathematical","projection":"forget_"+id,"inhabitance_witness":"inh_"+id,"selector":"select_"+id,"selector_invariance_witness":"inv_"+id,"section_coherence_witness":"coh_"+id};x.update(kw);return x
def main():
 c={"root_object":"R","layers":[layer("A","R"),layer("B","A:total")]};r=C(c);assert r["passed"] and r["explanation_complete"] and len(r["forgetful_projections"])==2
 c={"root_object":"R","layers":[layer("A","R","empty_fiber",emptiness_witness="empty") ]};r=C(c);assert r["first_obstruction"]["obstruction"]=="empty_fiber" and r["surviving_prefix"]==[]
 c={"root_object":"R","layers":[layer("A","R","multiple_fillers",multiplicity_witness="two") ]};assert C(c)["first_obstruction"]["obstruction"]=="unresolved_multiplicity"
 c={"root_object":"R","layers":[layer("A","R","selected") ]};assert C(c)["first_obstruction"]["obstruction"]=="section_coherence_not_verified"
 c={"root_object":"R","layers":[layer("A","wrong") ]};assert C(c)["first_failed_gate"]=="tower_order"
 c={"root_object":"R","layers":[{"id":"Readout","base_ref":"R","kind":"readout","state":"not_constructed"}]};assert C(c)["passed"] and C(c)["physical_readout_status"]=="not_constructed"
 c={"root_object":"R","layers":[layer("Readout","R",kind="readout") ]};assert C(c)["first_failed_gate"]=="readout_authority"
 c={"root_object":"R","layers":[layer("Readout","R",kind="readout",source_locator="s",detector_map="d",record_ontology="o") ]};assert C(c)["physical_readout_status"]=="coherent_section"
 c={"root_object":"R","layers":[layer("A","R")],"identity_claims":[{"kind":"univalent_identity"}]};assert C(c)["first_failed_gate"]=="identity_witness"
 cert={"status":"kernel_checked_conditional","source_sha256":"1"*64,"object_sha256":"2"*64};c={"root_object":"R","layers":[layer("A","R",unimath_certificate=cert)]};assert C(c)["passed"]
 print("lifting IR: 10 checks passed")
if __name__=="__main__":main()
