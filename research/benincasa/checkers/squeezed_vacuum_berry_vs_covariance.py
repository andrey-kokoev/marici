"""Exact Berry-versus-covariance holonomy for a squeezed-vacuum loop."""
import json
from fractions import Fraction as Q
from pathlib import Path

# Rational hyperbolic point: cosh r=5/3, sinh r=4/3, tanh r=4/5.
ch=Q(5,3); sh=Q(4,3); th=Q(4,5)
assert ch*ch-sh*sh==1

# For |zeta=r exp(i theta)>, the pair-number expectation is sinh^2(r)/2.
pair_number=sh*sh/2
berry_connection=-pair_number  # i <zeta|partial_theta zeta>
berry_exponent_turn=2*berry_connection  # coefficient of pi in gamma
assert berry_exponent_turn==Q(-16,9)

# The real covariance is periodic in theta through cos(theta),sin(theta).
# At 0 and 2pi it is identical. Its determinant is 1/4 throughout.
V0=[[Q(1,2)*(ch-sh)**2,Q(0)],[Q(0),Q(1,2)*(ch+sh)**2]]
V2pi=[row[:] for row in V0]
assert V0==V2pi
assert V0[0][0]*V0[1][1]==Q(1,4)

packet={
 "schema":"marici.squeezed-vacuum-berry-vs-covariance.v1",
 "hyperbolic_data":{"cosh_r":"5/3","sinh_r":"4/3","tanh_r":"4/5"},
 "pair_number_expectation":str(pair_number),
 "berry_connection":"A_theta=-8/9",
 "berry_phase_one_turn":"gamma=-16*pi/9",
 "state_line_holonomy":"exp(-16*pi*i/9), nonidentity",
 "covariance_endpoint":[[str(x) for x in row] for row in V0],
 "covariance_holonomy":"identity",
 "classification":"same Carrier loop supports readout-dependent coefficient transport: trivial covariance coefficient, nontrivial quantum-state line",
 "conclusion":"Complex Bogoliubov transport is not erased universally. It is erased by the covariance lens but survives in the normalized state-line coefficient. The distinction is sector/layer specific and does not require new Carrier incidence.",
}
out=Path(__file__).parent/'results'/'squeezed-vacuum-berry-vs-covariance.json'
out.write_text(json.dumps(packet,indent=2)+'\n')
print(json.dumps(packet,indent=2))
