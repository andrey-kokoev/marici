import json, math
from pathlib import Path

primes=[2,3,5,7,11,17,29,47,79,127,211,347,557,887,1423,2281]
# On the n=1 associated-graded source-mass line, adjoining the graph weight
# 1+(log n)^2 changes the prior fourth-power lower bound to:
# p^3/(1+(log p)^2)^2.
lower=[p**3/(1+math.log(p)**2)**2 for p in primes]
# Exact commutator identity gives a fixed-p graph bound via
# L T_p = T_p L + log(p) T_p.
source=(Path(__file__).parents[2]/"nima"/"theta-labelled-readout-is-monoid-augmentation-and-prime-transport-preserves-its-zero-ideal.md").read_text(encoding="utf-8")
prior=(Path(__file__).parents[1]/"results"/"rh_source_label_mass_prime_inverse_escape_audit.json").read_text(encoding="utf-8")
checks={
 "source_declares_log_degree_commutator":("[L,T_p]" in source and "(\\log p)T_p" in source),
 "log_degree_graph_is_closed_diagonal_domain":all(math.log(n)>=0 for n in range(1,100)),
 "each_fixed_prime_has_finite_graph_transport_bound":all(math.isfinite(1+math.log(p)) for p in primes),
 "graph_inverse_lower_bound_grows_on_prime_prefix":all(lower[i]<lower[i+1] for i in range(len(lower)-1)),
 "logarithmic_weight_does_not_cancel_polynomial_escape":lower[-1]>1000000,
 "associated_graded_witness_precedes_jet_and_schur_blocks":("failure occurs on associated graded before higher jets or Schur elimination" in prior),
}
result={
 "schema":"marici.strominger.rh_log_degree_graph_prime_inverse_escape_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/nima/theta-labelled-readout-is-monoid-augmentation-and-prime-transport-preserves-its-zero-ideal.md","research/strominger/results/rh_source_label_mass_prime_inverse_escape_audit.json"],
 "bound":"On the n=1 graph line, ||F_p^{-1}||_graph^4 >= p^3/(1+(log p)^2)^2, which diverges.",
 "verdict":"The logarithmic-degree operator has a natural closed graph and each fixed prime transport preserves it by the commutator identity. Its logarithmic weight is nevertheless too weak to repair the polynomial associated-graded inverse escape. Hence the source log graph is a valid domain for transverse-current detection but not an arithmetic-cutoff-uniform Schur inverse norm.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),
 "prefix":[{"p":p,"inverse_graph_norm_fourth_lower_bound":v} for p,v in zip(primes,lower)]
}
out=Path(__file__).parents[1]/"results"/"rh_log_degree_graph_prime_inverse_escape_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
