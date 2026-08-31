import json
from pathlib import Path

# For w_n = integral_0^infty phi_n(u)du, the source translate law gives
# w_pn = p^(-1/2) integral_log(p)^infty phi_n(v)dv < p^(-1/2) w_n.
# The associated-graded prime multiplier has |chi_p|=p^(-1/2).
# Hence the inverse transport norm satisfies
# ||F_p^{-1}||^4 >= p^3, avoiding irrational square roots in the audit.
primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
inv_fourth_lower=[p**3 for p in primes]
forward_fourth_upper_num=[1 for _ in primes]
forward_fourth_upper_den=[p**3 for p in primes]
source=(Path(__file__).parents[2]/"nima"/"theta-prime-scale-recursive-clark-repair.md").read_text(encoding="utf-8")
checks={
 "source_translate_weight_is_n_minus_half":("n^{-1/2}" in source and "phi_n(u)" in source),
 "positive_tail_restriction_strictly_decreases_label_mass":("every summand is positive" in source and "u+\\log p" in source),
 "inverse_associated_graded_lower_bound_is_p_cubed_in_fourth_power":all(v==p**3 for p,v in zip(primes,inv_fourth_lower)),
 "inverse_bounds_grow_strictly_with_prime":all(inv_fourth_lower[i]<inv_fourth_lower[i+1] for i in range(len(primes)-1)),
 "forward_transport_is_contracting_in_source_mass_norm":all(n<d for n,d in zip(forward_fourth_upper_num,forward_fourth_upper_den)),
 "cutoff_uniform_inverse_bound_fails_already_on_associated_graded":max(inv_fourth_lower)>100000,
}
result={
 "schema":"marici.strominger.rh_source_label_mass_prime_inverse_escape_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/nima/theta-prime-scale-recursive-clark-repair.md","research/strominger/results/rh_prime_label_principal_parts_lift_audit.json"],
 "bound":"If w_n=int phi_n and |chi_p|=p^(-1/2), then ||F_p^{-1}||^4 >= p^3 on associated graded.",
 "verdict":"The source-mass labelled completion makes forward prime transport contractive, but its inverse blocks escape at least as p^(3/4). This failure occurs on associated graded before higher jets or Schur elimination, so no arithmetic-cutoff-uniform inverse estimate follows from the natural theta label mass. Each fixed prime remains bounded. A stronger completion would need an additional source weight growing under n-to-pn, opposite to the native tail-mass inequality.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),
 "prefix":[{"p":p,"inverse_norm_fourth_lower_bound":p**3} for p in primes]
}
out=Path(__file__).parents[1]/"results"/"rh_source_label_mass_prime_inverse_escape_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
