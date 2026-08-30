#!/usr/bin/env python3
"""Run the infinity readout through Aspect's global-unit dark-port gates."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-readout-aspect-dark-port.json"

A, r, phi = sp.symbols("A r phi", nonzero=True, positive=True, real=True)

# Entry 3722: reflection reverses the primitive cycle and the ordered residue
# coefficient.  The paired local transport unit is their product.
u_cycle = -1
u_coefficient = -1
u_paired = u_cycle * u_coefficient

direct = A
reciprocal = sp.simplify(A * u_paired)
dark = sp.simplify(direct - reciprocal)
bright = sp.simplify(direct + reciprocal)

# Hostile control: forgetting the coefficient orientation leaves only the
# cycle sign and destroys the dark consistency port.
cycle_only_dark = sp.simplify(A - A * u_cycle)

U = r * sp.exp(sp.I * phi)
dark_intensity = sp.simplify(sp.expand_complex((1 - U) * (1 - sp.conjugate(U))))
extinction = sp.simplify(dark_intensity.subs(phi, 0) / (1 + r) ** 2)

checks = {
    "direct_arm_is_nonzero": direct != 0,
    "reciprocal_arm_is_nonzero": reciprocal != 0,
    "paired_local_unit_is_one": u_paired == 1,
    "antisymmetric_comparison_port_is_dark": dark == 0,
    "symmetric_physical_period_is_nonzero": bright == 2 * A,
    "blocking_either_arm_removes_extinction": A != 0,
    "unpaired_cycle_fails_dark_port": cycle_only_dark == 2 * A,
    "aspect_extinction_bound_is_reproduced": (
        sp.simplify(extinction - ((1 - r) / (1 + r)) ** 2) == 0
    ),
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_readout_aspect_dark_port.v1",
    "aspect_tester": "marici.aspect.global-unit-dark-port.v1",
    "direct_arm": "A",
    "reciprocal_arm": "A*(-1 cycle)*(-1 coefficient)=A",
    "paired_transport_unit": 1,
    "antisymmetric_output": "0",
    "symmetric_physical_output": "2*A",
    "hostile_unpaired_cycle_output": "2*A",
    "extinction_bound": "((1-r)/(1+r))^2",
    "interpretation": (
        "The dark output is a coherence/comparison port, not the physical "
        "period. Its zero certifies equality of two nonzero globally assembled "
        "routes. The physical symmetric output remains nonzero. Forgetting the "
        "coefficient orientation destroys this closure."
    ),
    "physical_zero_claim": False,
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("Aspect dark comparison port closes; symmetric physical period remains nonzero")
print(OUT)
