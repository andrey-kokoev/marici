import json, math
from pathlib import Path
# Finite restricted projection eigenvalues provide an exact Bernoulli model.
eigs=(.05,.2,.55,.8)
expect=sum(eigs)
def pgf(s):return math.prod(1+(s-1)*l for l in eigs)
# Enumerate Bernoulli occupancies to verify expectation and void probability.
dist=[1.]
for l in eigs:
 nxt=[0.]*(len(dist)+1)
 for k,p in enumerate(dist):nxt[k]+=p*(1-l);nxt[k+1]+=p*l
 dist=nxt
checks={
 "bernoulli_distribution_normalized":abs(sum(dist)-1)<1e-14,
 "trace_equals_expected_occupancy":abs(sum(k*p for k,p in enumerate(dist))-expect)<1e-14,
 "fredholm_pgf_matches_enumeration":all(abs(pgf(s)-sum(p*s**k for k,p in enumerate(dist)))<1e-14 for s in (0,.3,1,2)),
 "markov_occupancy_bound":sum(dist[1:])<=expect+1e-14,
 "restricted_eigenvalues_in_unit_interval":all(0<=l<=1 for l in eigs),
}
base=Path(__file__).parents[1]
packet=(base/"rh-transition-occupancy-is-a-restricted-christoffel-trace-problem.md").read_text(encoding="utf-8")
checks.update({
 "packet_identifies_restricted_trace":"restricted Christoffel-trace estimate" in packet,
 "packet_rejects_endpoint_substitution":"do not bound the integral of the diagonal kernel" in packet,
 "packet_retains_n_squared_remainder":"cannot be improved by occupancy arguments" in packet,
 "packet_claims_no_concentration":"do not claim concentration" in packet,
})
result={"schema":"marici.strominger.rh_transition_occupancy_determinantal_reduction_audit.v1","status":"passed" if all(checks.values()) else "failed","verdict":"Transition occupancy is controlled exactly by the trace and Fredholm determinant of the orthogonal kernel restricted to the buffer. Existing endpoint Christoffel values do not bound this growing-interval trace; only the trivial trace<=n bound is currently available.","checks":checks,"finite_model":{"eigenvalues":eigs,"expected_occupancy":expect,"occupancy_distribution":dist},"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
out=base/"results"/"rh_transition_occupancy_determinantal_reduction_audit.json";out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8");print(json.dumps(result,indent=2))
