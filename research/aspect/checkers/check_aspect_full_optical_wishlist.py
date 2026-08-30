#!/usr/bin/env python3
"""Check the staged optical wishlist and its inference barriers."""
import json, math
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"aspect-full-optical-wishlist.v1.json"
RESULT=ASPECT/"results"/"aspect_full_optical_wishlist.json"
def randomness_bits(s):
    if s<2 or s>2*math.sqrt(2): return 0.0
    return -math.log2((1+math.sqrt(max(0.0,2-s*s/4)))/2)
def promotable(p,required): return all(p.get(k) for k in required)
def main():
    c=json.loads(CONTRACT.read_text(encoding="utf-8")); q=math.sqrt(2)
    chsh=2*q; eta=2/(1+q); kcbs=math.sqrt(5); orient=2/(3*math.sqrt(3))
    complete={k:True for k in c["promotion_requires"]}; missing=dict(complete,uncertainty_rule=False)
    finite={"characteristic_zero_lift":False,"normalization":True,"analyzer_compilation":True,"source_authority":True}
    lifted={k:True for k in c["source_lift_gate"]["requires"]}
    checks={
      "ten_rungs_present":len(c["rungs"])==10 and len(set(c["rungs"]))==10,
      "chsh_separates_local":chsh>2,"chsh_fixture":abs(chsh-2.8284271247461903)<1e-14,
      "efficiency_fixture":abs(eta-0.8284271247461901)<1e-14,
      "kcbs_separates_noncontextual":kcbs>2,"orientation_nonzero":orient>0.38,
      "randomness_zero_at_local":abs(randomness_bits(2))<1e-15,
      "randomness_positive_above_local":randomness_bits(2.4)>0,
      "randomness_one_at_tsirelson":abs(randomness_bits(chsh)-1)<1e-12,
      "complete_promotes":promotable(complete,c["promotion_requires"]),
      "missing_uncertainty_blocks":not promotable(missing,c["promotion_requires"]),
      "finite_field_blocks":not all(finite.get(k) for k in c["source_lift_gate"]["requires"]),
      "authorized_lift_enters":all(lifted.values()),
      "no_clicks_retained":all(k in c["required_raw_fields"] for k in ("no_click_a","no_click_b")),
      "setting_health_retained":"setting_source_health" in c["required_raw_fields"],
      "orientation_smuggling_prohibited":"pairwise_data_as_orientation" in c["prohibitions"],
      "claim_boundary":not any(c["claim_boundary"].values())}
    out={"schema":"marici.aspect.full-optical-wishlist-result.v1","passed":all(checks.values()),"fixtures":{"chsh":chsh,"efficiency_threshold":eta,"kcbs":kcbs,"mirror_contrast":orient,"randomness_bits_at_2_4":randomness_bits(2.4),"randomness_bits_at_tsirelson":randomness_bits(chsh)},"checks":checks,"physical_status":"not_run","next_physical_build":"shared-ledger mirror-cocycle plus randomized-CHSH acquisition"}
    RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__": main()

