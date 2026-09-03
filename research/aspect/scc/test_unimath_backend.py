#!/usr/bin/env python3
from unimath_backend import compile_unimath_backend as C,verify_unimath_result as V
D="0"*64

def base():return {"module":"SCCExample","source_contract_sha256":D,"weak_equivalence":{"source_category":"A","target_univalent_category":"D","functor":"F","essential_surjectivity_witness":"F_eso","fully_faithful_witness":"F_ff"}}
def main():
 r=C(base());assert r["passed"] and r["status"]=="emitted_unchecked" and len(r["obligations"])==5
 x=base();x["module"]="bad-name";assert C(x)["first_failed_gate"]=="module"
 x=base();del x["weak_equivalence"]["fully_faithful_witness"];assert C(x)["first_failed_gate"]=="weak_equivalence"
 x=base();x["displayed_layers"]=[{"name":"Structure","displayed_category":"Disp","require_univalence":True,"require_SIP":True}];r=C(x);assert "UniMath.CategoryTheory.DisplayedCats.SIP" in r["imports"] and len(r["obligations"])==8 and "SCC_total_Structure" in r["rocq_skeleton"]
 x=base();x["comparison_squares"]=[{"name":"Square","top":"t","left":"l","right":"r","bottom":"b"}];assert "SCC_square_Square" in C(x)["rocq_skeleton"]
 x=base();x["requires_bicategories"]=True;r=C(x);assert r["heavy_bicategory_dependency"]
 x=base();x["observational_quotient"]={"locator":"detector:x"};assert C(x)["external_physical_readout"]["status"]=="external_to_unimath_backend"
 r=C(base());proved={o["id"]:"proved" for o in r["obligations"]};result={"module_sha256":"1"*64,"source_contract_sha256":D,"unimath_commit":"abc","rocq_version":"9.x","kernel_checked":True,"obligations":proved,"declared_axioms":["univalence"]};assert V(r,result)["passed"]
 bad=dict(result);bad["source_contract_sha256"]="2"*64;assert V(r,bad)["first_failed_gate"]=="source_drift"
 bad=dict(result);bad["physical_backend_certified"]=True;assert V(r,bad)["first_failed_gate"]=="authority_boundary"
 print("UniMath backend: 10 checks passed")
if __name__=="__main__":main()
