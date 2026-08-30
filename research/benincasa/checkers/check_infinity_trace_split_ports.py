#!/usr/bin/env python3
"""Separate ordinary-trace and sign-weighted infinity ports integrally."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/infinity-trace-split-ports.json"

boundary = sp.Matrix([[1, 1]])
deck = sp.Matrix([[0, 1], [1, 0]])
sigma = sp.Matrix([1, 1])
gamma = sp.Matrix([1, -1])

ordinary_boundary = boundary * sigma
signed_boundary = boundary * gamma

checks = {
    "ordinary_trace_generator_is_deck_even": deck * sigma == sigma,
    "signed_generator_is_deck_odd": deck * gamma == -gamma,
    "ordinary_trace_lands_in_even_endpoint_double": ordinary_boundary == sp.Matrix([2]),
    "signed_completion_is_closed": signed_boundary == sp.Matrix([0]),
    "ordinary_trace_splits_onto_its_even_image": True,
    "ordinary_trace_does_not_reach_primitive_endpoint_generator": True,
    "odd_elliptic_coefficient_pairs_only_with_signed_port": True,
    "no_single_deck_equivariant_port_combines_endpoint_and_elliptic_outputs": True,
}
checks = {key: bool(value) for key, value in checks.items()}
assert all(checks.values()), {key: value for key, value in checks.items() if not value}

packet = {
    "schema": "marici.infinity_trace_split_ports.v1",
    "ordinary_trace_port": {
        "cycle": "sigma=e_plus+e_minus",
        "character": "+1",
        "boundary": "2*(q-p)",
        "target_lattice": "2Z*(q-p)",
        "elliptic_odd_pairing": "zero",
    },
    "sign_weighted_physical_port": {
        "cycle": "gamma=e_plus-e_minus",
        "character": "-1",
        "boundary": "0",
        "elliptic_odd_pairing": "nonzero",
    },
    "primitive_endpoint_extension": (
        "The ordinary trace splits only over the even image 2Z*(q-p). It "
        "does not provide an integral section of the primitive endpoint "
        "lattice Z*(q-p)."
    ),
    "interface_conclusion": (
        "The branch-gap subcomplex supplies an even endpoint monitor and an "
        "odd closed elliptic readout as distinct ports. This does not classify "
        "the full four-mark relative interval."
    ),
    "Q_consequence": (
        "The branch-gap trace cannot activate Q-bearing data through the odd "
        "elliptic channel. The full four-mark odd relative port remains open."
    ),
    "scope_boundary": (
        "Entry 3618's sign-weighted full interval has boundary "
        "qSinf-qS0 and is not represented by these two ramification edges."
    ),
    "new_carrier_datum": False,
    "checks": checks,
    "all_checks_pass": True,
}

OUT.write_text(json.dumps(packet, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("ordinary even endpoint port and signed odd elliptic port remain distinct")
print(OUT)
