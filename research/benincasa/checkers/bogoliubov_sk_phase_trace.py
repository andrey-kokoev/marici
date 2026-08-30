"""Exact Schwinger-Keldysh trace test for Bogoliubov geometric phase."""
import json
from fractions import Fraction as Q
from pathlib import Path

gamma_over_pi=Q(-16,9)
assert not (gamma_over_pi.denominator==1 and gamma_over_pi.numerator%2==0)

# On the returned state ray U_loop=e^{i gamma}. The normalized closed contour
# pairs U_+ with U_-^dagger, so phases cancel. A mixed history matrix element
# (loop on +, identity on -) retains the relative phase.
packet={
 "schema":"marici.bogoliubov-sk-phase-trace.v1",
 "state_line_holonomy":"g=exp(-16*pi*i/9)",
 "closed_identical_branches":{"expression":"Tr(g rho g^*)","value":"1"},
 "loop_vs_identity_influence":{"expression":"Tr(g rho)","value":"g"},
 "identity_vs_loop_influence":{"expression":"Tr(rho g^*)","value":"g^*"},
 "normalized_unitarity_identity":"Z[J,J]=1",
 "native_sk_doubling_supplies_occurrence_pair":True,
 "native_closed_trace_activates_common_phase":False,
 "branch_asymmetry_required":True,
 "classification":"SK Carrier supplies the cross-history port, but the physical trace cancels common state-line holonomy; only branch-asymmetric source or insertion can expose it",
 "conclusion":"Occurrence structure is necessary but not sufficient for observability. The source/readout must populate the off-diagonal history sector; otherwise unitarity projects the Berry phase out.",
}
out=Path(__file__).parent/'results'/'bogoliubov-sk-phase-trace.json'
out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
