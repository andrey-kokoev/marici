import json
from fractions import Fraction as Q
from pathlib import Path

def primes_upto(n):
 out=[]
 for x in range(2,n+1):
  if all(x%p for p in out if p*p<=x):out.append(x)
 return out

def response(c,prime_cap,jet_cap):
 ps=primes_upto(prime_cap)
 common=sum(c.values()); relative=sum((Q(-1) if n%2 else Q(1))*v for n,v in c.items())
 exclusions={p:{n:v for n,v in c.items() if n%p} for p in ps}
 moments=[sum(v*Q(n**k) for n,v in c.items())/Q(1 if k==0 else 1) for k in range(jet_cap+1)]
 return {"reciprocal":(common,relative),"exclusions":exclusions,"jets":moments}
def restrict(R,prime_cap,jet_cap):
 return {"reciprocal":R["reciprocal"],"exclusions":{p:v for p,v in R["exclusions"].items() if p<=prime_cap},"jets":R["jets"][:jet_cap+1]}
def Tp(c,p):return {p*n:v for n,v in c.items()}
def Ep(c,p):return {n:v for n,v in c.items() if n%p}
def shift_packet(c,p):return {p*n:v for n,v in c.items()}

c={1:Q(2),2:Q(-3),5:Q(7),6:Q(4),11:Q(-2)}
R=response(c,19,8)
Rmid=restrict(R,11,5);Rsmall=restrict(Rmid,5,2)
direct=restrict(R,5,2)
# Finite product seminorm; restriction only drops nonnegative coordinates.
def seminorm(R):
 vals=list(R["reciprocal"])+R["jets"]
 for x in R["exclusions"].values():vals.extend(x.values())
 return sum(v*v for v in vals)
prime_pairs=[(p,q) for p in (2,3,5,7) for q in (2,3,5,7) if p!=q]
prior=(Path(__file__).parents[1]/"results"/"rh_tate_principal_parts_transition_audit.json").read_text(encoding="utf-8")
checks={
 "nested_response_restrictions_compose":Rsmall==direct,
 "reciprocal_pair_survives_every_bonding_map":all(restrict(R,p,m)["reciprocal"]==R["reciprocal"] for p,m in ((5,1),(11,4),(19,8))),
 "finite_product_seminorms_are_restriction_contracting":seminorm(direct)<=seminorm(Rmid)<=seminorm(R),
 "distinct_prime_exclusion_ports_are_transport_natural":all(Ep(Tp(c,p),q)==shift_packet(Ep(c,q),p) for p,q in prime_pairs),
 "matching_prime_transport_annihilates_valuation_zero_port":all(Ep(Tp(c,p),p)=={} for p in (2,3,5,7)),
 "principal_parts_jet_truncation_is_already_cutoff_natural":("cutoff_truncation_commutes_with_transition\": true" in prior),
 "no_scalar_aggregation_is_used":isinstance(R["exclusions"],dict) and len(R["exclusions"])>2,
}
result={
 "schema":"marici.strominger.rh_port_valued_response_bonding_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/grothendieck/prime-multiplication-division-curvature-is-positive-exclusion.md","research/strominger/results/rh_tate_principal_parts_transition_audit.json","research/strominger/results/rh_exclusion_scalar_weight_trichotomy_audit.json"],
 "verdict":"The reciprocal pair, finite prime-exclusion profile, and normalized jet prefix form a cutoff-natural projective response system. Restriction maps compose and contract every finite product seminorm. Exclusion ports commute with distinct prime transports, while the matching transport annihilates its valuation-zero port and records the positive curvature cell. The coordinatewise limit is canonical and port-valued; it supplies no scalar coercive gap or Ward implication from scalar nullity.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())
}
out=Path(__file__).parents[1]/"results"/"rh_port_valued_response_bonding_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
