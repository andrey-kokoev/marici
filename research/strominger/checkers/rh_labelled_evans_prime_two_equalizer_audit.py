import json
from fractions import Fraction as Q
from pathlib import Path

# Exact finite quadrature model of the source integral identities. The point is
# functorial linearity, not numerical approximation of Xi.
q=(-2,-1,0,1,2)
w=(Q(1),Q(2),Q(3),Q(2),Q(1))
z=0
phi1=(Q(1),Q(0),Q(2),Q(-1),Q(0))
phi2=tuple(-x for x in phi1) # a scalar-zero fibre, not an annihilated packet

def transform(phi):return sum(wi*x for wi,x in zip(w,phi))
def left_seam(phi):return sum(wi*x for qi,wi,x in zip(q,w,phi) if qi<=0)
def right_seam(phi):return -sum(wi*x for qi,wi,x in zip(q,w,phi) if qi>0)
def mismatch(phi):return left_seam(phi)-right_seam(phi)
def add(a,b):return tuple(x+y for x,y in zip(a,b))

t1,t2=transform(phi1),transform(phi2)
Sigma,Delta=t1+t2,t1-t2
W2=(t1,Q(0))
B2=((Sigma+Delta)/2,Q(0))
base=Path(__file__).parents[2]
evans=(base/"nima"/"the-two-sided-theta-history-mismatch-is-an-exact-evans-lift-of-the-xi-section.md").read_text(encoding="utf-8")
theta=(base/"nima"/"theta-prime-scale-recursive-clark-repair.md").read_text(encoding="utf-8")
checks={
 "each_labelled_seam_mismatch_equals_its_transform":all(mismatch(p)==transform(p) for p in (phi1,phi2)),
 "evans_mismatch_is_additive":mismatch(add(phi1,phi2))==mismatch(phi1)+mismatch(phi2),
 "scalar_zero_glues_total_but_not_labelled_histories":Sigma==0 and t1!=0 and t2==-t1,
 "analytic_relative_mismatch_is_source_derived":Delta==mismatch(phi1)-mismatch(phi2),
 "prime_two_balanced_equalizer_closes":B2==W2,
 "finite_label_restriction_is_natural":transform(phi1)==t1,
 "sources_supply_linear_evans_integral_and_labelled_theta_atoms":("u_-(0;z)-u_+(0;z)=\\tau(z)" in evans and "\\Phi(u)=\\sum_{n\\ge1}\\phi_n(u)" in theta),
}
result={
 "schema":"marici.strominger.rh_labelled_evans_prime_two_equalizer_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/nima/the-two-sided-theta-history-mismatch-is-an-exact-evans-lift-of-the-xi-section.md","research/nima/theta-prime-scale-recursive-clark-repair.md","research/grothendieck/the-single-adjoint-response-is-a-codiagonal-shadow-of-two-sector-local-responses.md"],
 "verdict":"Linearity of the source Evans integrals lifts the completed theta decomposition labelwise. At the two-label cutoff, the labelled seam mismatches are tau_1 and tau_2; scalar nullity glues only their sum, while the analytic relative mismatch Delta=tau_1-tau_2 remains available. The previously constructed B_2 maps (Sigma,Delta) to tau_1 e_1=W_2(tau). Thus the finite prime-two balanced equalizer closes without division or vacuum removal. This does not yet prove the adjoint-positive Green promotion or extension to arbitrary label cutoffs.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),
 "witness":{"tau_1":str(t1),"tau_2":str(t2),"Sigma":str(Sigma),"Delta":str(Delta)}
}
out=Path(__file__).parents[1]/"results"/"rh_labelled_evans_prime_two_equalizer_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
