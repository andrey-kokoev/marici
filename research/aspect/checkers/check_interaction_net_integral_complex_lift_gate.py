#!/usr/bin/env python3
"""Check readiness for a whole-complex integral barcode lift and reject rowwise substitutes."""
import json, math
from functools import reduce
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"interaction-net-integral-complex-lift-gate.v1.json"
RESULT=ASPECT/"results"/"interaction_net_integral_complex_lift_gate.json"
def gcd_all(xs): return reduce(math.gcd,(abs(int(x)) for x in xs),0)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def saturated_rank_one(generator): return gcd_all(generator)==1
def primitive(covector): return gcd_all(covector)==1
def valid_covector(covector,relations): return primitive(covector) and all(dot(covector,r)==0 for r in relations)
def candidate_status(path,required):
 if not path.exists(): return "awaiting_source_integral_complex",False,[]
 packet=json.loads(path.read_text(encoding="utf-8")); missing=[k for k in required if k not in packet]
 return ("present_shape_valid" if not missing and packet.get("passed") else "present_invalid"),not missing and bool(packet.get("passed")),missing
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); candidate=ROOT/c["candidate_packet"]
 relation=[1,1,1]; relations=[relation]; covectors=[[1,-1,0],[0,1,-1]]
 fixture={"free_rank":3,"relation_rank":1,"quotient_rank":2,"relation":relation,"covectors":covectors}
 nonsaturated=[2,2,2]; bad_incidence=[1,0,0]; nonprimitive=[2,-2,0]
 status,present_valid,missing=candidate_status(candidate,c["required_top_level"])
 checks={"primitive_relation_saturated":saturated_rank_one(relation),"quotient_rank_two":fixture["free_rank"]-fixture["relation_rank"]==fixture["quotient_rank"],"dual_covectors_valid":all(valid_covector(v,relations) for v in covectors),"good_prime_support_stable":all([x%p!=0 for x in relation]==[True,True,True] for p in c["good_primes"]),"nonsaturated_hostile_rejected":not saturated_rank_one(nonsaturated),"incidence_hostile_rejected":not valid_covector(bad_incidence,relations),"nonprimitive_hostile_rejected":not valid_covector(nonprimitive,relations),"coefficientwise_crt_prohibited":"coefficientwise_crt_as_complex_lift" in c["prohibitions"],"promotion_order_integral_first":c["promotion_order"][0]=="integral_complex" and c["promotion_order"][-1]=="optical_compiler","candidate_ingestion_ready":status in ("awaiting_source_integral_complex","present_shape_valid"),"claim_boundary":not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.interaction-net-integral-complex-lift-gate-result.v1","passed":all(checks.values()),"status":status,"candidate_present_valid":present_valid,"candidate_missing_fields":missing,"checks":checks,"synthetic_fixture":fixture,"scientific_conclusion":"whole_integral_complex_required_before_optical_covectors"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__": main()
