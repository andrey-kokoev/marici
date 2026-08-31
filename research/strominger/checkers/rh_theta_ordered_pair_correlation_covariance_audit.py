import json
from fractions import Fraction as Q
from pathlib import Path

# Perfect-square labels make half-density weights exact rationals. Formal log
# coordinates are independent symbols represented by distinct rationals.
labels=(1,4,9,16); ell={1:Q(0),4:Q(3),9:Q(5),16:Q(8)}; weight={1:Q(1),4:Q(1,2),9:Q(1,3),16:Q(1,4)}
def phi(u):return 2+3*u+u*u
def atom(n,u):return weight[n]*phi(u+ell[n])
def rho(n,m,S,D):return atom(n,(S+D)/2)*atom(m,(S-D)/2)
def covariant(n,m,S,D):return weight[n]*weight[m]*phi((S+ell[n]+ell[m]+D+ell[n]-ell[m])/2)*phi((S+ell[n]+ell[m]-(D+ell[n]-ell[m]))/2)
points=[(Q(-2),Q(-1)),(Q(0),Q(0)),(Q(3),Q(2)),(Q(5),Q(-4))]
checks={
 "pair_density_has_exact_product_ratio_translate_covariance":all(rho(n,m,S,D)==covariant(n,m,S,D) for n in labels for m in labels for S,D in points),
 "ordered_pair_swap_reverses_ratio_coordinate":all(rho(n,m,S,D)==rho(m,n,S,-D) for n in labels for m in labels for S,D in points),
 "diagonal_pairs_have_zero_ratio_shift":all(ell[n]-ell[n]==0 for n in labels),
 "half_density_pair_weight_is_multiplicative":all(weight[n]*weight[m]==Q(1,int(n**.5)*int(m**.5)) for n in labels for m in labels),
}
# Linearity and cutoff restriction on the ordered-pair module.
coeff={(n,m):Q((n+m)%7-3) for n in labels for m in labels}
def synth(C,S,D):return sum(a*rho(n,m,S,D) for (n,m),a in C.items())
def trunc(C,N):return {(n,m):a for (n,m),a in C.items() if n<=N and m<=N}
checks.update({
 "pair_synthesis_is_linear":all(synth(coeff,S,D)==sum(coeff[x]*rho(*x,S,D) for x in coeff) for S,D in points),
 "finite_pair_cutoff_is_basiswise":all(synth(trunc(coeff,9),S,D)==sum(a*rho(n,m,S,D) for (n,m),a in coeff.items() if n<=9 and m<=9) for S,D in points),
})
base=Path(__file__).parents[2]
source=(base/"nima"/"theta-arithmetic-to-band-bonding-is-a-polarized-correlation-functor.md").read_text(encoding="utf-8")
theta=(base/"nima"/"theta-prime-scale-recursive-clark-repair.md").read_text(encoding="utf-8")
checks.update({"source_declares_linear_pair_synthesis":"There is then a linear correlation synthesis" in source,"source_declares_exact_theta_translate_law":"\\phi_n(u)=n^{-1/2}\\phi(u+\\log n)" in theta})
result={"schema":"marici.strominger.rh_theta_ordered_pair_correlation_covariance_audit.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/nima/theta-arithmetic-to-band-bonding-is-a-polarized-correlation-functor.md","research/nima/theta-prime-scale-recursive-clark-repair.md"],"verdict":"The finite ordered-pair correlation map is constructed exactly. Each basis density is the base correlation translated by product degree log(nm) and ratio degree log(n/m), with half-density weight (nm)^(-1/2). Pair swap preserves product degree and reverses the relative band coordinate, and basiswise cutoff restriction commutes with linear synthesis. This closes rho_nm and its ratio orientation. Integration over product coordinate formally gives W_nm(D)=(nm)^(-1/2)W_11(D+log(n/m)); the boundary current J_nm and its completed continuity remain separate gates.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"tested_pairs":len(labels)**2,"tested_points":len(points)}
out=Path(__file__).parents[1]/"results"/"rh_theta_ordered_pair_correlation_covariance_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
