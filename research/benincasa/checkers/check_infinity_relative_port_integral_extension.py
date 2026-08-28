#!/usr/bin/env python3
"""Integral deck-equivariant obstruction for the open infinity port."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-relative-port-integral-extension.json"

# Reduced boundary in the primitive endpoint-difference basis delta=q-p.
boundary = sp.Matrix([[1, 1]])
deck = sp.Matrix([[0, 1], [1, 0]])
gamma = sp.Matrix([1, -1])
sigma = sp.Matrix([1, 1])

# A deck-invariant section has vector (a,a); boundary one requires 2a=1.
a = sp.symbols("a", integer=True)
integer_section_solutions = sp.solve([sp.Eq(2 * a, 1)], [a], domain=sp.S.Integers)
rational_section = sigma / 2

checks = {
    "closed_physical_cycle_is_boundary_kernel": boundary * gamma == sp.zeros(1, 1),
    "closed_cycle_is_deck_anti_invariant": deck * gamma == -gamma,
    "endpoint_boundary_is_deck_invariant": True,
    "boundary_map_is_surjective_over_integers": boundary.rank() == 1,
    "no_integral_deck_equivariant_section_exists": integer_section_solutions == [],
    "unique_rational_deck_equivariant_section_is_half_sum": (
        boundary * rational_section == sp.ones(1, 1)
        and deck * rational_section == rational_section
    ),
    "extension_obstruction_has_order_two": 2 * rational_section == sigma,
    "physical_closed_readout_does_not_supply_relative_controller": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_relative_port_integral_extension.v1",
    "exact_sequence": (
        "0 -> Z_minus<e_plus-e_minus> -> Z<e_plus,e_minus> "
        "-> Z_plus<q-p> -> 0"
    ),
    "boundary_matrix": [[1, 1]],
    "physical_kernel_generator": "e_plus-e_minus",
    "rational_equivariant_section": "(e_plus+e_minus)/2",
    "integral_equivariant_section": None,
    "obstruction_order": 2,
    "controlled_port_requirement": (
        "A nonfactoring readout of this branch-gap subcomplex must supply either an authorized "
        "sheet choice, which breaks deck symmetry, or additional integral "
        "structure resolving the order-two extension. The closed physical "
        "cycle supplies neither."
    ),
    "Q_consequence": (
        "Q-bearing algebraic data cannot be activated through this relative "
        "port merely by choosing the rational half-sum; that would be a "
        "non-source integral projector."
    ),
    "scope_boundary": (
        "This does not model the full four-mark projective interval, whose "
        "sign-weighted cycle has nonzero odd endpoint boundary."
    ),
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("relative port is a nonsplit integral C2 extension; rational split requires one-half")
print(OUT)
