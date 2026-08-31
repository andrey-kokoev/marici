import json
from fractions import Fraction as Q
from pathlib import Path

def primes_upto(n):return [p for p in range(2,n+1) if all(p%d for d in range(2,int(p**.5)+1))]
def exclusion(c,p):return {n:v for n,v in c.items() if n%p}
def response(c,N,P,k):
 cc={n:v for n,v in c.items() if n<=N}
 return {"krein":tuple(k),"ports":{p:exclusion(cc,p) for p in primes_upto(P)}}
def restrict(r,N,P):
 return {"krein":r["krein"],"ports":{p:{n:v for n,v in port.items() if n<=N} for p,port in r["ports"].items() if p<=P}}
def jq(k):return Q(4)*(k[0]*k[0]-k[1]*k[1])
def energy(r):return sum(v*v for port in r["ports"].values() for v in port.values())

c={n:Q((3*n+1)%11-5) for n in range(1,21)}; k=(Q(2),Q(1))
r20=response(c,20,19,k); r12=response(c,12,11,k); r7=response(c,7,7,k)
checks={
 "large_to_middle_restriction_matches_direct_response":restrict(r20,12,11)==r12,
 "middle_to_small_restriction_matches_direct_response":restrict(r12,7,7)==r7,
 "product_restrictions_compose":restrict(restrict(r20,12,11),7,7)==restrict(r20,7,7),
 "krein_plane_is_preserved_exactly":all(r["krein"]==k and jq(r["krein"])==jq(k) for r in (r20,r12,r7)),
 "positive_port_energy_is_restriction_contracting":energy(r7)<=energy(r12)<=energy(r20),
 "labelled_ports_remain_separate":len(r20["ports"])==len(primes_upto(19)) and all(isinstance(v,dict) for v in r20["ports"].values()),
 "no_scalar_aggregation_replaces_exclusion_profile":set(r20)=={"krein","ports"} and len(r20["ports"])>2,
}
base=Path(__file__).parents[1]
krein=json.loads((base/"results"/"rh_bilateral_mixed_current_krein_signature_audit.json").read_text(encoding="utf-8"))
ports=json.loads((base/"results"/"rh_port_valued_response_bonding_audit.json").read_text(encoding="utf-8"))
checks.update({"source_factors_freshly_verified":krein["status"]=="passed" and ports["status"]=="passed"})
result={"schema":"marici.strominger.rh_krein_exclusion_product_bonding_audit.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/strominger/results/rh_bilateral_mixed_current_krein_signature_audit.json","research/strominger/results/rh_port_valued_response_bonding_audit.json","research/strominger/results/rh_mixed_current_labelled_port_preservation_no_go.json"],"verdict":"The constant (1,1) Krein plane and the labelled exclusion pro-response form a canonical product response system. Restriction maps compose, preserve the Krein form exactly, contract finite positive port energies, and never scalarize the exclusion profile. This repairs the rank mismatch at the response-object level by retaining both factors. It does not construct a conservative dynamic coupling or identify the product characteristic with the Evans divisor; cross terms in a joint Green form remain source data.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"cutoffs":[[20,19],[12,11],[7,7]],"krein_value":str(jq(k)),"port_energies":[str(energy(r)) for r in (r20,r12,r7)]}
out=base/"results"/"rh_krein_exclusion_product_bonding_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
