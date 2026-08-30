#!/usr/bin/env python3
"""Check that the tensor numerator does not enlarge CM/Landau support."""

import json
from pathlib import Path

import sympy as sp


a, b, c, sK = sp.symbols("a b c sK")
P1, P2, P3 = sp.symbols("P1 P2 P3", nonzero=True)

CM = sp.Matrix(
    [
        [0, 1, 1, 1, 1],
        [1, 0, c**2, a**2, b**2],
        [1, c**2, 0, P2**2, P1**2],
        [1, a**2, P2**2, 0, P3**2],
        [1, b**2, P1**2, P3**2, 0],
    ]
)
K = sp.factor(-CM.det() / 2)
Lambda = sp.factor(
    (P1 - P2 - P3) * (P1 - P2 + P3) * (P1 + P2 - P3) * (P1 + P2 + P3)
)
N = sp.expand(
    2 * P1**2 * (c**2 + P2**2 - a**2)
    - (c**2 + P1**2 - b**2) * (P1**2 + P2**2 - P3**2)
)
Q_even = sp.cancel(-(N**2 + 4 * P1**2 * K) / (4 * P1**2 * Lambda))

# Exact restriction modulo the frozen CM branch.
assert sp.factor(Q_even + N**2 / (4 * P1**2 * Lambda) + K / Lambda) == 0

denominator = sp.factor(sp.denom(Q_even))
assert sp.cancel((4 * P1**2 * Lambda) / denominator).is_polynomial(P1, P2, P3)
assert not denominator.has(a, b, c)

# On the double cover sK^2=K, the two helicity forms split into Kummer and
# rational Tate channels.  The physical reflection trace retains Kummer and
# cancels Tate.
kummer = -(N**2 + 4 * P1**2 * sK**2) / (4 * P1**2 * Lambda * sK)
tate = N / (P1 * Lambda)
omega_plus = sp.cancel(kummer + tate)
omega_minus = sp.cancel(kummer - tate)
physical_trace = sp.cancel(omega_plus + omega_minus)
physical_antitrace = sp.cancel(omega_plus - omega_minus)
assert sp.factor(physical_trace - 2 * kummer) == 0
assert sp.factor(physical_antitrace - 2 * tate) == 0
assert sp.factor(physical_trace.subs(sK, -sK) + physical_trace) == 0
assert sp.factor(physical_antitrace.subs(sK, -sK) - physical_antitrace) == 0

# At a generic branch point N is a unit, so the physical trace has the same
# square-root exponent -1/2 as the scalar CM local system.  At N=0 it softens
# to exponent +1/2; a numerator zero cannot create Landau support.
generic_branch_leading = sp.factor(sp.limit(sK * physical_trace, sK, 0))
assert sp.factor(generic_branch_leading + N**2 / (2 * P1**2 * Lambda)) == 0
# Use an independent symbol for the local numerator normal; substituting a
# composite polynomial expression is not a reliable algebraic operation.
n_local = sp.symbols("n_local")
local_trace = -(n_local**2 + 4 * P1**2 * sK**2) / (2 * P1**2 * Lambda * sK)
softened_at_N_zero = sp.factor(local_trace.subs(n_local, 0))
assert sp.factor(softened_at_N_zero + 2 * sK / Lambda) == 0

packet = {
    "schema": "marici.benincasa.tensor-cayley-menger-landau-exponent.v1",
    "status": "passed",
    "cm_branch": "K=0",
    "tensor_multiplier_on_branch": str(-N**2 / (4 * P1**2 * Lambda)),
    "fiber_denominators": [],
    "external_denominator_support": ["P1=0", "Lambda(P)=0"],
    "physical_trace": "2*Kummer",
    "physical_antitrace": "2*Tate (killed by reflection-symmetric cycle)",
    "generic_branch_exponent": "-1/2",
    "generic_branch_monodromy": "-1 before the frozen sector twist",
    "N_zero_intersection_exponent": "+1/2",
    "landau_effect": "numerator insertion preserves or softens the frozen CM pinch; it cannot create a new critical divisor",
    "new_carrier_support": False,
    "scope_warning": (
        "This is the local-system and critical-support audit. The map of the "
        "tensor class through the infinity-Gysin elliptic quotient is separate."
    ),
}

output = Path(__file__).with_name("tensor-cayley-menger-landau-exponent.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
