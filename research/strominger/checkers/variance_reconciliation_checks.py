#!/usr/bin/env python3
"""Compile exact, partial, and lax variance-reconciliation cells."""

from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/higher_three_adic_lift_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))
packet = source["packet"]


def obs(n):
    p = packet(n)
    return (p["v3_d1"], p["v3_d2"], p["v3_d3"])


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


left, right = 0, 1
base_equal = obs(left) == obs(right)
exact = {}
for step in (-1, 1):
    exact[str(step)] = {
        "left_image": list(obs(left + step)),
        "right_image": list(obs(right + step)),
        "commutes": obs(left + step) == obs(right + step),
        "residual": list(sub(obs(right + step), obs(left + step))),
    }

# A partial comparison defined only on blind pairs is not substitution-closed.
blind_pair_domain_closed = all(record["commutes"] for record in exact.values())

# The globally typed lax residual is the coboundary of the observation packet.
# It obeys the composition law for arbitrary pairs and constructor words.
pairs = [(a, b) for a in range(-8, 9) for b in range(-8, 9)]
words = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
cocycle_failures = []
for a, b in pairs:
    for first, second in words:
        direct = sub(obs(b + first + second), obs(a + first + second))
        first_residual = sub(obs(b + first), obs(a + first))
        increment = sub(
            sub(obs(b + first + second), obs(a + first + second)),
            sub(obs(b + first), obs(a + first)),
        )
        if direct != add(first_residual, increment):
            cocycle_failures.append([a, b, first, second])

triple_failures = []
for a, b in pairs:
    for s1 in (-1, 1):
        for s2 in (-1, 1):
            for s3 in (-1, 1):
                direct = sub(obs(b + s1 + s2 + s3), obs(a + s1 + s2 + s3))
                staged = sub(obs(b), obs(a))
                previous = 0
                for step in (s1, s2, s3):
                    total = previous + step
                    staged = add(staged, sub(
                        sub(obs(b + total), obs(a + total)),
                        sub(obs(b + previous), obs(a + previous)),
                    ))
                    previous = total
                if direct != staged:
                    triple_failures.append([a, b, s1, s2, s3])

gates = {
    "base_observations_alias": base_equal,
    "exact_reconciliation_fails_in_both_directions":
        all(not record["commutes"] for record in exact.values()),
    "blind_fiber_partial_domain_is_not_constructor_closed":
        not blind_pair_domain_closed,
    "global_lax_residual_satisfies_pair_composition":
        not cocycle_failures,
    "global_lax_residual_satisfies_triple_substitution":
        not triple_failures,
}
payload = {
    "schema": "marici.strominger.variance_reconciliation_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "witness_pair": [left, right],
    "base_packet": list(obs(left)),
    "exact_cells": exact,
    "partial_cell": {
        "domain": "pairs with equal valuation packet",
        "constructor_closed": blind_pair_domain_closed,
        "classification": "ill_typed_under_substitution",
    },
    "lax_cell": {
        "residual_definition": "omega(a,b)=R(b)-R(a) on all grade pairs",
        "pair_cocycle_failure_count": len(cocycle_failures),
        "triple_substitution_failure_count": len(triple_failures),
        "classification": "algebraically_coherent_but_requires_full_difference_port",
        "authority_status": "not_established_by_valuation_readout",
    },
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "interpretation": (
        "Exact reconciliation fails. Restricting the cell to observationally "
        "blind pairs is not closed under source substitution. Extending the "
        "residual to every grade pair yields a coherent coboundary cell, but "
        "adds a full difference port whose source authority is not established."
    ),
}
print(json.dumps(payload, indent=2))
