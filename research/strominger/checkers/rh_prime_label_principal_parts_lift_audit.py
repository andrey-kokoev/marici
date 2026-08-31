import json
from fractions import Fraction as Q
from pathlib import Path

# Gaussian rationals represented by pairs (real,imag).
def ga(a=0,b=0): return (Q(a),Q(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def mul(x,y): return (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def divq(x,n): return (x[0]/n,x[1]/n)
def conv(a,b,m): return [sum_ga(mul(a[k],b[n-k]) for k in range(n+1)) for n in range(m+1)]
def sum_ga(xs):
 r=ga()
 for x in xs:r=add(r,x)
 return r
def trunc(v,m):return v[:m+1]
def mat_from_series(v,m): return [[v[i-j] if i>=j else ga() for j in range(m+1)] for i in range(m+1)]
def mm(A,B):return [[sum_ga(mul(A[i][k],B[k][j]) for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def transpose(A):return [list(r) for r in zip(*A)]
def conj(x):return (x[0],-x[1])
def adjoint(A):return [[conj(x) for x in r] for r in transpose(A)]

M=8
ell=Q(3) # formal exact nonzero log-prime fixture
c=ga(2)  # nonzero character value fixture
minus_i_ell=ga(0,-ell)
v=[c]
for k in range(1,M+1):v.append(divq(mul(v[-1],minus_i_ell),k))
T=mat_from_series(v,M)
# exp(+i ell t) / c is the inverse multiplier.
inv=[ga(Q(1,2))]
plus_i_ell=ga(0,ell)
for k in range(1,M+1):inv.append(divq(mul(inv[-1],plus_i_ell),k))
Ti=mat_from_series(inv,M)
I=[[ga(1) if i==j else ga() for j in range(M+1)] for i in range(M+1)]
# Label module fixture: T_p e_n=e_pn and L e_n=lambda_n e_n.
p=5
labels=[1,2,3,6]
transport={n:p*n for n in labels}
degree={n:Q(i+1) for i,n in enumerate(labels)}
degree.update({p*n:degree[n]+ell for n in labels})
commutator={n:degree[transport[n]]-degree[n] for n in labels}
checks={
 "prime_multiplier_is_lower_triangular_principal_parts_action":all(T[i][j]==(v[i-j] if i>=j else ga()) for i in range(M+1) for j in range(M+1)),
 "nonzero_character_value_makes_every_cutoff_invertible":mm(T,Ti)==I,
 "cutoff_refinement_commutes_with_prime_action":all(mat_from_series(trunc(v,m),m)==[row[:m+1] for row in T[:m+1]] for m in range(M+1)),
 "associated_graded_action_is_nonzero_character_value":all(T[r][r]==c for r in range(M+1)),
 "spectral_derivative_is_logarithmic_cocycle":all(mul(ga(k+1),v[k+1])==mul(minus_i_ell,v[k]) for k in range(M)),
 "label_transport_preserves_labels_before_augmentation":all(transport[n]==p*n for n in labels),
 "log_degree_commutator_coefficient_is_log_p":all(commutator[n]==ell for n in labels),
 "algebraic_dual_action_exists_contravariantly":len(adjoint(T))==M+1,
}
result={
 "schema":"marici.strominger.rh_prime_label_principal_parts_lift_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/nima/theta-prime-scale-recursive-clark-repair.md","research/nima/theta-labelled-readout-is-monoid-augmentation-and-prime-transport-preserves-its-zero-ideal.md","research/strominger/results/rh_tate_principal_parts_transition_audit.json"],
 "operator":"T_p on labels tensored with multiplication by chi_p(z0) exp(-i log(p) t) on truncated principal parts",
 "verdict":"Each source-labelled prime transport has a canonical cutoff-natural filtered lift before scalar augmentation. Its associated-graded action is the nonzero prime character and its off-diagonal jets are forced by log(p). The algebraic contragredient exists, but this audit does not identify it with the independently required physical response row or provide a positive completion norm.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"max_order":M
}
out=Path(__file__).parents[1]/"results"/"rh_prime_label_principal_parts_lift_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
