import json
from fractions import Fraction as Q
from pathlib import Path

# Quotient mixed-current matrix J=diag(4,-4). Coupling a scalar theta channel
# of bare value m through g gives Schur scalar m-g^T J^{-1}g.
def shift(g):return (g[0]*g[0]-g[1]*g[1])/Q(4)
def schur(m,g):return m-shift(g)
def det3(m,g):
 # det [[m,g1,g2],[g1,4,0],[g2,0,-4]] = det(J)*Schur
 return -Q(16)*m+Q(4)*g[0]*g[0]-Q(4)*g[1]*g[1]
examples={
 "positive_line":((Q(1),Q(0)),Q(1,4)),
 "negative_line":((Q(0),Q(1)),Q(-1,4)),
 "isotropic_line":((Q(1),Q(1)),Q(0)),
}
checks={
 "block_determinant_matches_krein_schur_formula":all(det3(Q(m,7),g)==-16*schur(Q(m,7),g) for m in range(-5,6) for g,_ in examples.values()),
 "positive_and_negative_couplings_shift_oppositely":shift(examples["positive_line"][0])>0 and shift(examples["negative_line"][0])<0,
 "isotropic_coupling_produces_no_shift":shift(examples["isotropic_line"][0])==0,
 "same_krein_signature_allows_distinct_kernel_locations":len({shift(g) for g,_ in examples.values()})==3,
 "kernel_can_be_created_only_after_coupling_and_bare_value_are_fixed":all(schur(target,g)==0 for g,target in examples.values()),
}
base=Path(__file__).parents[2]
gap=(base/"nima"/"the-uniform-cayley-impedance-gap-overcoerces-the-seam-and-cannot-carry-the-xi-divisor.md").read_text(encoding="utf-8")
mixed=(base/"grothendieck"/"theta-green-transfer-mixed-bezoutian.md").read_text(encoding="utf-8")
checks.update({
 "source_requires_a_krein_signature_theorem":("must be replaced by a Krein-signature theorem" in gap),
 "mixed_bezoutian_packet_requires_new_comparison_information":("stronger comparison relation between \\(K\\) and \\(\\Phi\\)" in mixed),
})
result={
 "schema":"marici.strominger.rh_krein_plane_coupling_indeterminacy_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/strominger/results/rh_bilateral_mixed_current_krein_signature_audit.json","research/nima/the-uniform-cayley-impedance-gap-overcoerces-the-seam-and-cannot-carry-the-xi-divisor.md","research/grothendieck/theta-green-transfer-mixed-bezoutian.md"],
 "verdict":"The (1,1) Krein signature alone does not determine a seam kernel or preserve off-seam invertibility. Coupling through the positive, negative, or isotropic line shifts the scalar Schur characteristic by +1/4, -1/4, or 0 respectively. All use the same mixed-current plane. Therefore inserting the bilateral current without a source map from its X,X' coordinates to the three-port theta/history carrier would fit the divisor. The current supplies an admissible indefinite defect space, but the active kernel test is blocked at a missing source-fixed coupling/comparison theorem.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),
 "schur_shifts":{k:str(shift(g)) for k,(g,_) in examples.items()}
}
out=Path(__file__).parents[1]/"results"/"rh_krein_plane_coupling_indeterminacy_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
