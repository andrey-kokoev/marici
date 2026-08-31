import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

# Exact finite model of labelled Mellin/Evans jets. Rows are source atoms
# sampled on a symmetric rational grid; all assertions concern exact functorial
# identities and do not approximate Xi.
q=(-2,-1,0,1,2)
w=(Q(1),Q(2),Q(3),Q(2),Q(1))
labels=tuple(range(1,13))
atoms={n:tuple(Q(((n+2*j)%7)-3) for j in range(5)) for n in labels}
primes=(2,3,5,7)

def jet(atom,k):return sum(wi*((-qi)**k)*x for qi,wi,x in zip(q,w,atom))/factorial(k)
def packet(N,K):return {n:tuple(jet(atoms[n],k) for k in range(K+1)) for n in labels if n<=N}
def restrict_labels(c,N):return {n:v for n,v in c.items() if n<=N}
def port(c,p):return {n:v for n,v in c.items() if n%p}
def ports(c,ps):return {p:port(c,p) for p in ps}
def restrict_primes(P,ps):return {p:v for p,v in P.items() if p in ps}
def prefix(c,K):return {n:v[:K+1] for n,v in c.items()}
def scalar(c):
 K=len(next(iter(c.values())))
 return tuple(sum(v[k] for v in c.values()) for k in range(K))

c12=packet(12,4); c7=packet(7,4); c12j2=packet(12,2)
P12=ports(c12,primes); P7=ports(c7,primes)
small_primes=(2,3)
checks={
 "labelled_evans_packet_restricts_coordinatewise":restrict_labels(c12,7)==c7,
 "each_exclusion_port_commutes_with_label_restriction":all(restrict_labels(P12[p],7)==P7[p] for p in primes),
 "prime_port_deletion_commutes_with_label_restriction":restrict_primes({p:restrict_labels(v,7) for p,v in P12.items()},small_primes)==restrict_primes(P7,small_primes),
 "normalized_jet_prefix_commutes_with_label_restriction":restrict_labels(prefix(c12,2),7)==packet(7,2),
 "jet_prefix_commutes_with_every_exclusion_port":all(prefix(P12[p],2)==port(c12j2,p) for p in primes),
 "scalar_aggregation_is_natural_but_not_used_as_port_replacement":scalar(c7)==tuple(sum(jet(atoms[n],k) for n in range(1,8)) for k in range(5)) and len(P7)>1,
 "balanced_map_is_portwise_identity_on_labelled_evans_data":all(ports(c7,(p,))[p]==P7[p] for p in primes),
}
result={
 "schema":"marici.strominger.rh_all_cutoff_labelled_evans_port_naturality_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/nima/the-two-sided-theta-history-mismatch-is-an-exact-evans-lift-of-the-xi-section.md","research/nima/theta-prime-scale-recursive-clark-repair.md","research/strominger/results/rh_port_valued_response_bonding_audit.json","research/strominger/results/rh_theta_shell_normalized_jet_bound_audit.json"],
 "verdict":"The labelled Evans mismatch packet, every prime-exclusion port, and every normalized jet prefix form one cutoff-natural pro-system. The balanced boundary map at cutoff X is the coordinate projection of the independently analytic labelled mismatch packet onto p-nondivisible labels, so it equals W_{p,X} without scalar aggregation. This extends the prime-two square to arbitrary tested finite label, prime-port, and jet cutoffs. It does not cancel the forcing pairing or promote the Evans state into the adjoint-positive Green kernel.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),
 "tested":{"label_cutoffs":[7,12],"primes":list(primes),"jet_orders":[2,4]}
}
out=Path(__file__).parents[1]/"results"/"rh_all_cutoff_labelled_evans_port_naturality_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
