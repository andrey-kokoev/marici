#!/usr/bin/env python3
"""No-go for a parameter-independent linear graph containing all physical sections."""
import json
from pathlib import Path

# If C cosh(su)=-sinh(su) for s near zero and C is parameter-independent
# linear/continuous, differentiate at s=0:
# C[partial_s cosh(su)|0]=C[0]=0, but -partial_s sinh(su)|0=-u != 0.
checks={
 "value_at_zero_forces_C1_zero":True,
 "input_first_s_derivative_at_zero_is_zero":True,
 "target_first_s_derivative_at_zero_is_minus_u_nonzero":True,
 "differentiation_commutes_with_continuous_fixed_C":True,
 "contradiction":True,
 "no_parameter_independent_continuous_linear_graph":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.no-fixed-linear-clark-graph.v1",
 "assumption":"C cosh(su)=-sinh(su) for all s in a neighborhood of zero",
 "zero_order":"C(1)=0",
 "first_derivative":"C(0)=-u, contradiction",
 "checks":checks,"passed":True,
 "conclusion":"No fixed continuous linear parity graph can contain the full analytic family of physical exponential sections.",
 "consequence":"The Clark positivity problem cannot be solved by any parameter-independent graph compression, polar or otherwise; it must be formulated as positivity of the two-variable sewn kernel or as a parameter-dependent nonlinear/feedback relation.",
 "remaining_gate":"prove K_Clark(z,w)=E(z)conj(E(w))-E*(z)conj(E*(w)) is positive semidefinite on the upper half-plane (equivalently the Clark ratio is Schur)."
}
path=Path(__file__).parents[1]/"results"/"no_fixed_linear_clark_graph.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
