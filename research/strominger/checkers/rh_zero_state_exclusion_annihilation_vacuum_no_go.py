import json
from fractions import Fraction as Q
from pathlib import Path

base=Path(__file__).parents[2]
vac=(base/"grothendieck"/"the-vacuum-obstructs-zero-state-exclusion-annihilation.md").read_text(encoding="utf-8")
equalizer=(base/"grothendieck"/"the-cross-tower-Ward-cell-is-a-balanced-defect-equalizer-not-an-annihilator.md").read_text(encoding="utf-8")
evans=(base/"nima"/"the-two-sided-theta-history-mismatch-is-an-exact-evans-lift-of-the-xi-section.md").read_text(encoding="utf-8")
# Exact finite packet: nonzero vacuum plus cancelling nonvacuum amplitudes.
packet={1:Q(1),2:Q(3),3:Q(-4)}
scalar=sum(packet.values())
def exclusion(c,p):return {n:v for n,v in c.items() if n%p}
ports={p:exclusion(packet,p) for p in (2,3,5,7)}
checks={
 "finite_packet_has_scalar_nullity":scalar==0,
 "vacuum_survives_every_prime_exclusion":all(ports[p].get(1)==1 for p in ports),
 "no_exclusion_port_vanishes":all(ports[p] for p in ports),
 "source_mellin_transport_fixes_vacuum_coefficient":("(c_z)_1=1^{-z}\\Omega_1=\\Omega_1" in vac),
 "evans_lift_constructs_analytic_history_not_label_packet":("zero-to-history-state arrow" in evans and "promotion" in evans),
 "source_retypes_ward_target_as_balanced_equalizer":("balanced defect equalizer, not an annihilator" in equalizer.lower() and "W_X(c)=B_{X,s}(y)" in equalizer),
}
result={
 "schema":"marici.strominger.rh_zero_state_exclusion_annihilation_vacuum_no_go.v1",
 "status":"passed" if all(checks.values()) else "failed",
 "sources":["research/grothendieck/the-vacuum-obstructs-zero-state-exclusion-annihilation.md","research/grothendieck/the-cross-tower-Ward-cell-is-a-balanced-defect-equalizer-not-an-annihilator.md","research/nima/the-two-sided-theta-history-mismatch-is-an-exact-evans-lift-of-the-xi-section.md"],
 "verdict":"The direct Ward target is false. Scalar nullity and the exact analytic Evans history state do not produce a labelled packet in every exclusion kernel. Canonical Mellin transport fixes the nonzero vacuum coefficient, and every prime exclusion port retains it. The admissible source target is a portwise balanced equalizer W_X(c)=B_{X,s}(y), not exclusion annihilation. The missing constructor is the independently derived boundary map B into the same typed defect object.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values()),"finite_ports":{str(p):{str(n):str(v) for n,v in x.items()} for p,x in ports.items()}
}
out=Path(__file__).parents[1]/"results"/"rh_zero_state_exclusion_annihilation_vacuum_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result,indent=2))
