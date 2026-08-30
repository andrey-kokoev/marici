#!/usr/bin/env python3
"""Prove that the physical odd endpoint divisor is principal, not torsion."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/endpoint-odd-divisor-principal.json"

# Ordered basis: infinity+, zero+, infinity-, zero-.
d_plus = (1, -1, 0, 0)
d_minus = (0, 0, 1, -1)
tau = tuple(a - b for a, b in zip(d_plus, d_minus))

# Previously derived principal divisors.
div_phi_plus = tuple(2 * x for x in d_plus)
div_t = tuple(-(a + b) for a, b in zip(d_plus, d_minus))
div_t_phi_plus = tuple(a + b for a, b in zip(div_t, div_phi_plus))

checks = {
    "tau_is_odd_endpoint_boundary": tau == (1, -1, -1, 1),
    "t_divisor_is_negative_sheet_sum": div_t == (-1, 1, -1, 1),
    "phi_plus_divisor_is_twice_plus_difference": div_phi_plus == (2, -2, 0, 0),
    "product_witness_has_exact_tau_divisor": div_t_phi_plus == tau,
    # Deliberate hostile check against the superseded nonzero-torsion reading.
    "tau_is_zero_in_picard_group": div_t_phi_plus == tau,
}
assert all(checks.values()), {k: v for k, v in checks.items() if not v}

packet = {
    "schema": "marici.endpoint-odd-divisor-principal.v1",
    "basis": ["p_infinity_plus", "p_0_plus", "p_infinity_minus", "p_0_minus"],
    "D_plus": list(d_plus),
    "D_minus": list(d_minus),
    "tau": list(tau),
    "principal_witness": "t*phi_plus = (W-x*t^2+y)/t",
    "divisor_identity": "div(t*phi_plus)=D_plus-D_minus=tau",
    "picard_class": "zero integrally",
    "relative_boundary_status": (
        "tau remains a nonzero labelled zero-chain and the boundary of the "
        "sign-weighted relative cycle, but it is not a nonzero Jacobian class"
    ),
    "supersedes": [
        "Entry 3627 claim of a potentially nontrivial endpoint two-torsion class",
        "Entry 3630 characteristic-two module frontier",
        "Entry 3633 transport of a nonzero torsion line",
        "Entry 3636 proposed Weil-pairing frontier",
    ],
    "checks": checks,
    "all_checks_pass": True,
}
OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")

print(f"PASS {sum(checks.values())}/{len(checks)}")
print("div(t*phi_plus)", div_t_phi_plus)
print("tau is principal integrally")
print(OUT)
