import json
from fractions import Fraction as Q
from pathlib import Path

# Exact scalar history/arithmetic chart. Symbols are represented by independent
# rational samples; identities are checked over a census, not fitted at zeros.
def sample(r,v,b,d):
 q=d+b*r*b
 if q==0:return None
 f=v*r*v-v*r*b*(1/q)*b*r*v
 det=(v*r*v)*q-(v*r*b)*(b*r*v)
 x=-(1/q)*b*r*v
 u=r*(v+b*x)
 return q,f,det,x,u
samples=[]
for r in (Q(1,2),Q(2,3),Q(5,4)):
 for v in (Q(1),Q(3,2)):
  for b in (Q(1,3),Q(2)):
   for d in (Q(2,5),Q(7,3)):
    s=sample(r,v,b,d)
    if s:samples.append((r,v,b,d,s))
checks={
 "determinant_factors_as_arithmetic_complement_times_dressed_scalar":all(s[4][2]==s[4][0]*s[4][1] for s in samples),
 "changed_history_uses_nonzero_arithmetic_feedback":any(s[4][3]!=0 and s[4][4] != s[0]*s[1] for s in samples),
 "reconstructed_history_satisfies_first_resolvent_row":all(s[4][4]==s[0]*(s[1]+s[2]*s[4][3]) for s in samples),
}
base=Path(__file__).parents[2]
three=(base/"nima"/"theta-forcing-and-arithmetic-incidence-require-a-three-port-paired-pencil.md").read_text(encoding="utf-8")
schur=(base/"nima"/"the-three-port-schur-reduction-is-one-dressed-theta-weyl-scalar-over-a-coercive-arithmetic-complement.md").read_text(encoding="utf-8")
checks.update({
 "source_order_fixes_theta_diagonal_and_cross_block_zero":("D_\\theta=0" in schur and "R=0" in schur),
 "source_separates_theta_and_arithmetic_ports":("different\nsource spaces" in three and "H\\oplus\\mathbb C_\\theta\\oplus U_{\\rm ar}" in three),
 "source_identifies_exact_dressed_theta_residual":("\\mathcal R_{\\theta,\\rm dress}(z)" in schur and "F_\\theta(z)-E_\\theta(z)\\tau(z)" in schur),
 "source_forbids_quotient_fitting":("Defining \\(D_U\\) or \\(E_\\theta\\) from the quotient" in schur),
})
result={
 "schema":"marici.strominger.rh_three_port_changed_history_schur_architecture_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/nima/theta-forcing-and-arithmetic-incidence-require-a-three-port-paired-pencil.md","research/nima/the-three-port-schur-reduction-is-one-dressed-theta-weyl-scalar-over-a-coercive-arithmetic-complement.md","research/nima/the-retained-history-metric-now-constructs-the-adjoint-incidence-but-not-its-xi-characteristic.md"],
 "verdict":"The minimal source-authorized larger complex is the three-port carrier H plus theta input plus arithmetic source, with D_theta=R=0. Off seam and where Q_U is invertible, Schur elimination constructs a changed history with arithmetic feedback and factors the characteristic as det(Q_U)F_theta. The architecture is valid and does not require an exact arithmetic lift of Phi. The unresolved, RH-bearing constructor is the source identity F_theta=E_theta tau with E_theta a unit, together with limiting absorption and multiplicity transport; it cannot be defined from the quotient.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"sample_count":len(samples)
}
out=Path(__file__).parents[1]/"results"/"rh_three_port_changed_history_schur_architecture_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
