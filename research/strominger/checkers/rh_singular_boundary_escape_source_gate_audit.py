import json
from pathlib import Path

base=Path(__file__).parents[2]
schur=(base/"nima"/"the-three-port-schur-reduction-is-one-dressed-theta-weyl-scalar-over-a-coercive-arithmetic-complement.md").read_text(encoding="utf-8")
green=(base/"nima"/"the-maximal-isotropic-green-identity-gives-off-seam-invertibility-once-index-zero-is-fixed.md").read_text(encoding="utf-8")
boundary=(base/"grothendieck"/"the-finite-full-boundary-packet-closes-as-a-fourier-stable-pro-gram-extension.md").read_text(encoding="utf-8")
passive=(base/"nima"/"a-strict-same-sign-arithmetic-complement-cannot-create-a-dressed-seam-zero.md").read_text(encoding="utf-8")
checks={
 "schur_packet_requires_limiting_absorption_on_seam":("requires a source limiting-absorption or rigged-history theorem" in schur),
 "scalar_analytic_continuation_is_explicitly_insufficient":("Scalar analytic\ncontinuation of \\(F_\\theta\\) is insufficient" in schur),
 "finite_boundary_packet_does_not_construct_restricted_product_limit":("unresolved theorem is passage to the\nrestricted-product limit" in boundary),
 "green_theorem_requires_same-pencil_bulk_readback":("exact equality between that G3 form and the kernel\nbulk term remains" in green),
 "passive_no_go_lists_singular_boundary_only_as_alternative":("a singular boundary value invalidates the ordinary quadratic-form" in passive),
 "source_packets_do_not_claim_boundary_value_constructor":("showing that the dressed Schur expression and reconstructed state have\nboundary values" in schur and "must be proved" in schur),
}
result={
 "schema":"marici.strominger.rh_singular_boundary_escape_source_gate_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/nima/the-three-port-schur-reduction-is-one-dressed-theta-weyl-scalar-over-a-coercive-arithmetic-complement.md","research/nima/the-maximal-isotropic-green-identity-gives-off-seam-invertibility-once-index-zero-is-fixed.md","research/grothendieck/the-finite-full-boundary-packet-closes-as-a-fourier-stable-pro-gram-extension.md","research/nima/a-strict-same-sign-arithmetic-complement-cannot-create-a-dressed-seam-zero.md"],
 "verdict":"The singular-boundary escape is not presently constructed. The authoritative Schur packet requires a source limiting-absorption or rigged-history theorem and states that scalar analytic continuation is insufficient. The finite full boundary packet stops before restricted-product completion, and the Green theorem still lacks same-pencil bulk readback. Consequently no map exists on which maximal-isotropic membership or labelled-port boundary compatibility can be tested. Singular boundary behavior remains a named alternative, not evidence against the passive no-go.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())
}
out=Path(__file__).parents[1]/"results"/"rh_singular_boundary_escape_source_gate_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
