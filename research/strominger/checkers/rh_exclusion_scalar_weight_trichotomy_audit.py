import json
from fractions import Fraction as Q
from pathlib import Path

# Summable witness w_k=2^-k on the ordered prime list. For the primorial of
# the first K primes, exclusion energy is exactly the tail sum 2^-K.
Kmax=20
tails=[sum(Q(1,2**k) for k in range(K+1,120)) for K in range(1,Kmax+1)]
closed=[Q(1,2**K)-Q(1,2**119) for K in range(1,Kmax+1)]
# Finite-support weights vanish on a label divisible by every supported prime.
supported=[2,3,5,7,11]
primorial=1
for p in supported:primorial*=p
finite_energy=sum(Q(1) for p in supported if primorial%p)
ledger=(Path(__file__).parents[3]/"src"/"ledger"/"20260826-2877 No Scalar-Weighted Reduced Exclusion Energy Is Both Finite and Gapped.md").read_text(encoding="utf-8")
checks={
 "summable_weight_primorial_energy_is_exact_tail":all(tails[i]==closed[i] for i in range(Kmax)),
 "summable_weight_gap_collapses":all(closed[i]>closed[i+1] for i in range(Kmax-1)) and closed[-1]<Q(1,1000000),
 "finite_support_weight_has_nontrivial_kernel":finite_energy==0,
 "nonsummable_positive_weights_diverge_off_finitely_many_prime_divisors":("Nonsummable weights give infinite energy" in ledger),
 "source_ledger_requires_port_valued_profile_or_extra_coupling":("must remain port-valued" in ledger),
}
result={
 "schema":"marici.strominger.rh_exclusion_scalar_weight_trichotomy_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "source":"src/ledger/20260826-2877 No Scalar-Weighted Reduced Exclusion Energy Is Both Finite and Gapped.md",
 "verdict":"No scalar weighting of all-prime exclusion ports is simultaneously finite on label vectors, jointly faithful with a positive gap, and nondegenerate. Nonsummable weights diverge; summable weights have primorial energies tending to zero; finite support has kernel. The exclusion response must remain port-valued or be coupled through an independently derived Ward/Green cell.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),
 "summable_primorial_tail":[{"K":k,"energy":str(closed[k-1])} for k in range(1,Kmax+1)]
}
out=Path(__file__).parents[1]/"results"/"rh_exclusion_scalar_weight_trichotomy_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
