import json
from fractions import Fraction as Q
from pathlib import Path
from math import sqrt

# For a scalar contraction of modulus r, the Cayley impedance lower margin is
# (1-r)/(1+r). Prime delays have r=p^{-1/2}; the worst case is p=2.
primes=(2,3,5,7,11,13,17,19,23,29,31)
margins={p:(1-1/sqrt(p))/(1+1/sqrt(p)) for p in primes}
claimed=3-2*sqrt(2)
checks={
 "every_prime_delay_is_strict_on_the_seam":all(1/sqrt(p)<1 for p in primes),
 "worst_prime_is_two":min(margins,key=margins.get)==2,
 "uniform_margin_matches_claimed_constant":abs(margins[2]-claimed)<1e-14,
 "no_finite_prime_direction_is_lossless":all(abs(1/sqrt(p)-1)>1e-14 for p in primes),
}
base=Path(__file__).parents[2]
gap=(base/"nima"/"the-uniform-cayley-impedance-gap-overcoerces-the-seam-and-cannot-carry-the-xi-divisor.md").read_text(encoding="utf-8")
complement=(base/"nima"/"the-strict-cayley-law-overcoerces-the-square-source-block-but-remains-valid-as-the-three-port-complement.md").read_text(encoding="utf-8")
checks.update({
 "source_fixes_half_density_modulus":("|S_p(x)|=p^{-1/2}" in gap),
 "source_retains_strict_gap_on_arithmetic_coordinate":("\\operatorname{Im}D_U\n\\ge(3-2\\sqrt2)I" in complement),
 "lossless_limit_is_only_a_named_alternative":("Lossless seam limit" in gap and "None may be selected after inspecting Xi zeros" in gap),
})
result={
 "schema":"marici.strominger.rh_prime_delay_controlled_degeneracy_no_go.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/nima/the-uniform-cayley-impedance-gap-overcoerces-the-seam-and-cannot-carry-the-xi-divisor.md","research/nima/the-strict-cayley-law-overcoerces-the-square-source-block-but-remains-valid-as-the-three-port-complement.md","research/nima/a-strict-same-sign-arithmetic-complement-cannot-create-a-dressed-seam-zero.md"],
 "verdict":"The source prime-delay law cannot supply a controlled degenerating arithmetic line. Its half-density modulus is p^{-1/2}, so every seam direction is strictly contractive and the Cayley margin is uniformly bounded below by 3-2sqrt(2), attained at p=2. A lossless seam line would require a different source constructor or normalization; it is only a named alternative in the current packets. Controlled degeneracy is therefore falsified for the existing prime-delay complement, while the zero-diagonal theta defect remains a separate three-port possibility.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),
 "minimum_margin":margins[2],"tested_primes":list(primes)
}
out=Path(__file__).parents[1]/"results"/"rh_prime_delay_controlled_degeneracy_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
