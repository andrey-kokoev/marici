"""Exact controlled-history activation of squeezed-vacuum Berry holonomy."""
import json
from fractions import Fraction as Q
from pathlib import Path

# Entry 2101 exact data.
sinh_r=Q(4,3)
A_theta=-(sinh_r*sinh_r)/2
gamma_over_pi=2*A_theta
assert gamma_over_pi==Q(-16,9)

# A phase exp(i*pi*q) is identity iff q is an even integer.
is_even_integer=(gamma_over_pi.denominator==1 and gamma_over_pi.numerator%2==0)
assert not is_even_integer

# Controlled loop: (|0>+|1>)|psi>/sqrt(2), identity on 0 and adiabatic
# loop on 1. At the endpoint the system factorizes and the path qubit carries
# relative phase exp(i gamma). Hadamard readout gives P_+=(1+cos gamma)/2.
packet={
 "schema":"marici.squeezed-vacuum-controlled-interference.v1",
 "source_protocol":"control=0: fixed base source; control=1: one squeezed-phase loop; common dynamical phase removed; recombine control",
 "berry_phase_over_pi":str(gamma_over_pi),
 "relative_holonomy":"exp(-16*pi*i/9)",
 "relative_holonomy_is_identity":is_even_integer,
 "endpoint_system_states_coincide_projectively":True,
 "path_visibility":"1",
 "readout":{"P_plus":"(1+cos(16*pi/9))/2","P_minus":"(1-cos(16*pi/9))/2"},
 "readout_differs_from_trivial_loop":True,
 "classification":"state-line holonomy becomes physical through a source-defined cross-history interference port; covariance-only readout remains blind",
 "conclusion":"The Bogoliubov Berry phase is not merely presentation memory. A controlled relative-history pairing activates it as an observable fringe shift without adding Carrier incidence. The extra required object is the labelled cross-history readout port.",
}
out=Path(__file__).parent/'results'/'squeezed-vacuum-controlled-interference.json'
out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
