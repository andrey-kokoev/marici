#!/usr/bin/env python3
"""Exact time-weight audit for the conformally coupled scalar--graviton vertex."""

import json
from pathlib import Path

import sympy as sp


eta, eta_star, k2, k4, energy, eps = sp.symbols(
    "eta eta_star k2 k4 energy eps", nonzero=True
)
bx, by = sp.symbols("bx by")

# The Delta=2 specialization of the source bulk-to-boundary propagator,
# normalized to one at eta=eta_star.  The eta_star phase is immaterial in
# the late-time limit but retaining it makes the normalization exact.
K2 = eta / eta_star * sp.exp(sp.I * k2 * (eta - eta_star))
K4 = eta / eta_star * sp.exp(sp.I * k4 * (eta - eta_star))
vertex_weight = sp.Rational(1, 2) / eta**2

integrand = sp.simplify(vertex_weight * K2 * K4)
expected = (
    sp.exp(sp.I * (k2 + k4) * eta)
    * sp.exp(-sp.I * (k2 + k4) * eta_star)
    / (2 * eta_star**2)
)
assert sp.simplify(integrand - expected) == 0
assert not integrand.has(eta**-1)

# With the standard damped past contour, i times the exponential time
# integral is the ordinary simple energy pole.  We record the algebraic
# antiderivative rather than asking a CAS to reason about the contour.
damped_energy = energy - sp.I * eps
primitive_at_zero = 1 / (sp.I * damped_energy)
wavefunction_seed = sp.simplify(sp.I * primitive_at_zero)
assert wavefunction_seed == 1 / damped_energy

A = bx**2 - by**2
B = 2 * bx * by
tensor_seed = sp.Matrix([A + sp.I * B, A - sp.I * B]) / 4
assert sp.simplify(tensor_seed[0] - (bx + sp.I * by) ** 2 / 4) == 0
assert sp.simplify(tensor_seed[1] - (bx - sp.I * by) ** 2 / 4) == 0

packet = {
    "schema": "marici.benincasa.cc-scalar-tensor-time-weight.v1",
    "status": "passed",
    "primary_source": {
        "paper": "Baumann et al., arXiv:2005.04234v3",
        "bulk_to_boundary": "page 55, equations (6.13)-(6.14)",
        "local_vertex": "page 58, equation (6.22)",
        "three_point_factorization": "page 64, equations (6.48)-(6.51)",
        "channel_completion": "page 50, equations (5.48)-(5.50), and page 70, section 6.4",
    },
    "delta_2_mode": "(eta/eta_star)*exp(i*k*(eta-eta_star))",
    "time_weight": {
        "raw_vertex": "1/(2*eta^2)",
        "two_scalar_product": "eta^2/eta_star^2 times the exponential",
        "reduced_integrand": str(integrand),
        "eta_power_after_reduction": 0,
        "wavefunction_seed": str(wavefunction_seed),
        "pole_order": 1,
        "classification": "strict cancellation; no local marked-pole-order shift",
    },
    "helicity_seed": [str(value) for value in tensor_seed],
    "ward_completion": {
        "local_statement": "the TT vertex is a quadratic momentum numerator multiplying the same exponential seed",
        "global_statement": "the source Ward identity correlates exchange channels and the contact term",
        "coupling_relation": "kappa_g=kappa_c=kappa",
        "strict_local_multiplication_is_full_system": False,
    },
    "new_carrier_support": False,
    "scope_warning": (
        "The eta cancellation types the local insertion. It does not construct "
        "the full one-loop tensor connection or authorize omission of the "
        "source-correlated Ward contact and channel completion."
    ),
}

output = Path(__file__).with_name("cc-scalar-tensor-time-weight.json")
output.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(packet, indent=2, sort_keys=True))
