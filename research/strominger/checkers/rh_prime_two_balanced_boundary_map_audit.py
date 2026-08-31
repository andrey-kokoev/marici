import json
from fractions import Fraction as Q
from pathlib import Path

# Smallest labelled cutoff C={e1,e2}; prime-two exclusion retains e1.
def W2(c):return (c[0],Q(0))
def response(c):return (c[0]+c[1],c[0]-c[1]) # common, relative
def B2(y):return ((y[0]+y[1])/2,Q(0))
packets=[(Q(a),Q(b)) for a in range(-4,5) for b in range(-4,5)]
null_packets=[c for c in packets if sum(c)==0]
base=Path(__file__).parents[2]
evans=(base/"nima"/"the-two-sided-theta-history-mismatch-is-an-exact-evans-lift-of-the-xi-section.md").read_text(encoding="utf-8")
responses=(base/"grothendieck"/"the-single-adjoint-response-is-a-codiagonal-shadow-of-two-sector-local-responses.md").read_text(encoding="utf-8")
checks={
 "common_relative_mate_reconstructs_prime_two_exclusion":all(B2(response(c))==W2(c) for c in packets),
 "on_scalar_null_pullback_boundary_map_is_half_relative_row":all(B2(response(c))==(response(c)[1]/2,Q(0)) for c in null_packets),
 "vacuum_component_is_retained":B2(response((Q(1),Q(-1))))==(Q(1),Q(0)),
 "boundary_map_uses_source_common_relative_pair":("natural output basis is the pair" in responses and "r_\\Delta" in responses),
 "evans_state_is_analytic_and_requires_promotion":("history state" in evans and "sole RH-bearing promotion" in evans),
 "evans_packet_does_not_declare_labelled_relative_response":("labelled relative response" not in evans),
}
result={
 "schema":"marici.strominger.rh_prime_two_balanced_boundary_map_audit.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/grothendieck/the-single-adjoint-response-is-a-codiagonal-shadow-of-two-sector-local-responses.md","research/grothendieck/the-cross-tower-Ward-cell-is-a-balanced-defect-equalizer-not-an-annihilator.md","research/nima/the-two-sided-theta-history-mismatch-is-an-exact-evans-lift-of-the-xi-section.md"],
 "verdict":"At the two-label, prime-two cutoff, the source common/relative response pair canonically reconstructs the exclusion port: W_2(c)=B_2(Sigma,Delta)=((Sigma+Delta)/2)e_1, and on scalar nullity this is (Delta/2)e_1. The vacuum is retained. This constructs the finite balanced boundary map algebraically. It does not close the Ward cell because the analytic Evans history state supplies seam matching but no independently derived labelled relative response Delta. The live interface is the Evans-to-relative-response map, not the exclusion residual itself.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())
}
out=Path(__file__).parents[1]/"results"/"rh_prime_two_balanced_boundary_map_audit.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
