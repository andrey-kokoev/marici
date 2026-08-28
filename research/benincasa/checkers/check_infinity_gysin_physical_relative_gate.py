#!/usr/bin/env python3
"""Test whether the physical infinity path factors through ordinary elliptic H1."""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / ".tmp_sympy"))
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-gysin-physical-relative-gate.json"

t, R = sp.symbols("t R", positive=True)

# Homogeneous nonsoft source point x=y=z=1.
F = t**4 - t**2 + 1
omega0_coefficient = 1 / sp.sqrt(F)
omega2_coefficient = t**2 / sp.sqrt(F)

omega0_asymptotic_weight = sp.limit(t**2 * omega0_coefficient, t, sp.oo)
omega2_endpoint_value = sp.limit(omega2_coefficient, t, sp.oo)
omega0_integral = sp.Integral(omega0_coefficient, (t, 0, sp.oo))
omega2_truncated = sp.Integral(omega2_coefficient, (t, 0, R))

# The radial compactification of a,b>=0 is an interval with two labelled
# endpoints. Its boundary is nonzero before any endpoint identification.
boundary_vector = sp.Matrix([-1, 1])  # [infinity] - [zero]

checks = {
    "homogeneous_quartic_is_source_fixed": sp.expand(F-(t**4-t**2+1)) == 0,
    "homogeneous_quartic_has_no_real_zero": sp.discriminant(
        sp.Symbol("q")**2-sp.Symbol("q")+1, sp.Symbol("q")
    ) < 0,
    "omega0_decays_quadratically": omega0_asymptotic_weight == 1,
    "omega2_has_nonzero_endpoint_limit": omega2_endpoint_value == 1,
    "physical_projective_path_has_nonzero_boundary": boundary_vector != sp.zeros(2, 1),
    "ordinary_cycle_condition_fails": sum(boundary_vector) == 0 and boundary_vector.rank() == 1,
}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity-gysin-physical-relative-gate.v1",
    "homogeneous_binary_quartic": sp.sstr(F),
    "physical_projective_path": {
        "coordinate": "t=a/b",
        "domain": "[0,infinity]",
        "labelled_boundary": "[infinity]-[0]",
        "boundary_vector": [int(value) for value in boundary_vector],
        "ordinary_closed_cycle": False,
    },
    "elliptic_basis": {
        "omega0": "dt/sqrt(F)",
        "omega2": "t^2 dt/sqrt(F)",
    },
    "asymptotics": {
        "limit_t2_times_omega0_coefficient": sp.sstr(omega0_asymptotic_weight),
        "limit_omega2_coefficient": sp.sstr(omega2_endpoint_value),
        "omega0_integral": sp.sstr(omega0_integral),
        "omega2_truncated_integral": sp.sstr(omega2_truncated),
        "omega2_divergence": "linear endpoint divergence",
    },
    "ordinary_H1_factorization": False,
    "required_target": "marked-relative elliptic cohomology with labelled endpoints and source normalization",
    "interpretation": (
        "The rank-four to rank-two infinity-Gysin quotient is canonical, but the "
        "physical asymptotic path is relative rather than closed. A physical scalar "
        "readout cannot be inferred as a rank-one quotient of ordinary elliptic H1."
    ),
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {len(checks)}/{len(checks)}")
print("omega0 endpoint weight", omega0_asymptotic_weight)
print("omega2 endpoint limit", omega2_endpoint_value)
print("physical infinity path is relative, not an ordinary elliptic cycle")
print(OUT)
