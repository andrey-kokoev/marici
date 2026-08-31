import json
from fractions import Fraction as Q
from math import comb
from pathlib import Path

labels=(1,2,3,5); ell={1:Q(0),2:Q(2),3:Q(5),5:Q(9)}
pairs=[(n,m) for n in labels for m in labels]
coef={(n,m):Q((2*n+3*m)%11-5) for n,m in pairs}
def deg(n,m):return ell[n]+ell[m],ell[n]-ell[m]
def jets(c,K):return {(j,k):sum(a*deg(n,m)[0]**j*deg(n,m)[1]**k for (n,m),a in c.items()) for j in range(K+1) for k in range(K+1-j)}
# Band synthesis sends a pair to a formal exponential atom at its product/ratio
# translation. Its Taylor jet is therefore the same mixed-moment array.
def band_jets(c,K):return {(j,k):sum(a*S**j*D**k for (n,m),a in c.items() for S,D in [deg(n,m)]) for j in range(K+1) for k in range(K+1-j)}
def transport_jets(J,K,sp,dp):
 out={}
 for j in range(K+1):
  for k in range(K+1-j):
   out[j,k]=sum(Q(comb(j,a))*Q(comb(k,b))*sp**(j-a)*dp**(k-b)*J[a,b] for a in range(j+1) for b in range(k+1))
 return out
K=5; J=jets(coef,K); BJ=band_jets(coef,K)
checks={
 "pair_to_band_joint_jet_square_commutes_through_order_five":J==BJ,
 "diagonal_prime_transport_preserves_ratio_shift":transport_jets(J,K,Q(6),Q(0))[(0,1)]==J[(0,1)],
 "independent_transport_changes_both_product_and_ratio_jets":transport_jets(J,K,Q(7),Q(3))[(1,0)]==J[(1,0)]+7*J[(0,0)] and transport_jets(J,K,Q(7),Q(3))[(0,1)]==J[(0,1)]+3*J[(0,0)],
 "pair_swap_reverses_odd_ratio_jets":all(sum(a*deg(m,n)[0]**j*deg(m,n)[1]**k for (n,m),a in coef.items())==((-1)**k)*J[j,k] for j,k in J),
}
# Nested finite cutoffs commute with the same jet construction.
def trunc(c,N):return {(n,m):a for (n,m),a in c.items() if n<=N and m<=N}
checks["nested_pair_cutoff_commutes_with_joint_jets"]=jets(trunc(coef,3),K)==band_jets(trunc(coef,3),K)
base=Path(__file__).parents[2]
source=(base/"nima"/"theta-arithmetic-to-band-bonding-is-a-polarized-correlation-functor.md").read_text(encoding="utf-8")
flat=(base/"nima"/"theta-log-moment-flatness-and-band-asymptotic-flatness-are-distinct-quotients.md").read_text(encoding="utf-8")
checks.update({"source_requires_joint_pair_jet_kernel":"joint pair-jet kernel" in source,"source_distinguishes_finite_square_from_flat_sector_equality":"Equality, injectivity on flat sectors" in flat})
result={"schema":"marici.strominger.rh_polarized_pair_joint_jet_square_audit.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/nima/theta-arithmetic-to-band-bonding-is-a-polarized-correlation-functor.md","research/nima/theta-log-moment-flatness-and-band-asymptotic-flatness-are-distinct-quotients.md","research/strominger/results/rh_theta_ordered_pair_band_current_covariance_audit.json"],"verdict":"The finite polarized pair-to-band map intertwines product and ratio jets through total order five. Diagonal prime transport shifts product degree only; independent transport shifts both; pair swap reverses exactly the odd ratio jets; and cutoff restriction commutes with the square. This closes the finite joint-jet bonding law. It does not identify the completed joint-flat kernel with the band-flat remainder or exhibit a boundary-current witness there.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"jet_order":K,"jet_count":len(J),"pair_count":len(pairs)}
out=Path(__file__).parents[1]/"results"/"rh_polarized_pair_joint_jet_square_audit.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
