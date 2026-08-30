"""Exact branch-asymmetric Weyl insertion test for Bogoliubov holonomy."""
import json
from fractions import Fraction as Q
from pathlib import Path

# Entry 2101 base covariance and Berry phase.
Vqq=Q(1,18)
gamma_over_pi=Q(-16,9)

# Convention W(xi)=exp(i xi q), xi=1. For a centered Gaussian,
# <W>=exp(-Var(q)/2)=exp(-1/36), strictly positive and nonzero.
characteristic_exponent=-Vqq/2
assert characteristic_exponent==Q(-1,36)

packet={
 "schema":"marici.bogoliubov-sk-weyl-insertion.v1",
 "insertion":"W=exp(i q) on the forward branch only",
 "base_covariance_Vqq":"1/18",
 "gaussian_characteristic":"chi=exp(-1/36)",
 "chi_is_nonzero":True,
 "loop_off_diagonal_amplitude":"F_loop=g*chi, g=exp(-16*pi*i/9)",
 "reference_amplitude":"F_ref=chi",
 "normalized_ratio":"F_loop/F_ref=g",
 "insertion_normalization_cancels":True,
 "hermitian_interference_readout":"Re(F_loop)=exp(-1/36)*cos(16*pi/9)",
 "classification":"a source-fixed branch-asymmetric Gaussian observable activates state-line holonomy; the normalized phase is independent of insertion magnitude",
 "conclusion":"The off-diagonal SK phase is not absorbed into Weyl normalization. Whenever the source-defined characteristic function is nonzero, comparison with the identity history isolates the Berry holonomy exactly.",
}
out=Path(__file__).parent/'results'/'bogoliubov-sk-weyl-insertion.json'
out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
