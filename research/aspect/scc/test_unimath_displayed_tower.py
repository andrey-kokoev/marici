#!/usr/bin/env python3
from unimath_displayed_tower import compile_displayed_tower as C
D="5"*64
def base():return {"module":"Tower","source_contract_sha256":D,"layers":[{"name":"Completion","kind":"mathematical"},{"name":"Certificates","kind":"mathematical"}]}
def main():
 r=C(base());assert r["passed"] and r["final_total_category"]=="Total_Certificates" and r["readout_status"]=="not_constructed"
 assert "disp_cat Base" in r["rocq_source"] and "disp_cat Total_Completion" in r["rocq_source"]
 assert "SCC_selector_type_Completion" in r["rocq_source"] and "SCC_equivalence_to_identity_Completion" in r["rocq_source"]
 assert "SCC_empty_fiber_blocks_selector_Completion" in r["rocq_source"] and "SCC_multiple_fillers_type_Completion" in r["rocq_source"]
 x=base();x["layers"].append({"name":"Readout","kind":"readout"});assert C(x)["first_failed_gate"]=="readout_authority"
 x=base();x["layers"].append({"name":"Readout","kind":"readout","source_locator":"detector:x"});assert C(x)["readout_status"]=="source_typed"
 x=base();x["layers"][0]["kind"]="readout";assert C(x)["first_failed_gate"]=="readout_order"
 x=base();x["layers"][1]["name"]="Completion";assert C(x)["first_failed_gate"]=="layer"
 x=base();x["layers"]=x["layers"][:1];assert C(x)["first_failed_gate"]=="tower"
 print("UniMath displayed tower: 9 checks passed")
if __name__=="__main__":main()
