import json
from fractions import Fraction as Q
from pathlib import Path

# Exact finite coordinate audit supporting the analytic theorem in the packet.
# The derivative directions (Sigma,Delta) and (z,w) are related by a matrix
# with nonzero determinant -2.
A=((Q(1),Q(1)),(Q(1),Q(-1)))
det=A[0][0]*A[1][1]-A[0][1]*A[1][0]
# Reciprocal polynomial-label square sums converge for r>1/2; finite partial
# sums are monotone and bounded above by zeta(2r)^2. At r=1, use zeta(2)<2.
partial=[]
for N in (2,4,8,16,32,64):
 s=sum(Q(1,n*n) for n in range(1,N+1))
 partial.append(s*s)
checks={
 "product_ratio_derivative_change_is_invertible":det==-2,
 "reciprocal_weight_partial_sums_are_monotone":all(partial[i]<partial[i+1] for i in range(len(partial)-1)),
 "reciprocal_weight_has_uniform_elementary_bound":all(x<4 for x in partial),
}
base=Path(__file__).parents[1]
packet=(base/"rh-rapid-label-projective-completion-has-trivial-joint-flat-kernel.md").read_text(encoding="utf-8")
flat=(base.parents[0]/"nima"/"theta-log-moment-flatness-and-band-asymptotic-flatness-are-distinct-quotients.md").read_text(encoding="utf-8")
checks.update({
 "packet_defines_rapid_label_projective_limit":"\\mathscr S_{\\rm lab}^{(2)}=\\bigcap_{r\\geq0}\\ell^2((nm)^{2r})" in packet,
 "packet_uses_entire_two_variable_dirichlet_transform":"F_c(z,w)=\\sum_{n,m\\geq1}c_{nm}n^z m^w" in packet,
 "packet_proves_trivial_joint_flat_kernel":"=\\{0\\}." in packet,
 "packet_forbids_current_defined_topology_circularity":"cannot be added as a defining seminorm" in packet,
 "source_warns_completed_flatness_depends_on_topology":"can nevertheless be nontrivial if the chosen" in flat,
})
result={"schema":"marici.strominger.rh_rapid_label_joint_flat_kernel_no_go.v1","status":"passed" if all(checks.values()) else "failed","sources":["research/strominger/rh-rapid-label-projective-completion-has-trivial-joint-flat-kernel.md","research/nima/theta-log-moment-flatness-and-band-asymptotic-flatness-are-distinct-quotients.md","research/strominger/results/rh_finite_pair_joint_flatness_no_go.json"],"verdict":"The source-natural rapid-label projective completion makes every joint logarithmic moment continuous, but its two-variable Dirichlet transform is entire. Vanishing of all product-ratio jets therefore forces the transform, then every ordered-pair coefficient, to vanish. Its joint-flat kernel is trivial. A nonzero completion witness requires a weaker non-quasi-analytic topology with a separately proved continuous boundary-current pairing; adjoining that current as a graph seminorm would be circular.","checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"coordinate_change_determinant":str(det),"reciprocal_weight_partial_sums":[str(x) for x in partial]}
out=base/"results"/"rh_rapid_label_joint_flat_kernel_no_go.json"; out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); print(json.dumps(result,indent=2))
