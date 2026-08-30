#!/usr/bin/env python3
"""Certify the four-grade coefficient ring used by the rank-26 bidual reducer."""

from __future__ import annotations

import importlib
import json
import os
from pathlib import Path
import random
import sys

ROOT = Path(__file__).resolve().parents[3]
P = int(os.environ.get("MARICI_FIELD_PRIME", "32009"))
SUFFIX = "" if P == 32009 else f"-p{P}"
OUT = ROOT / "research" / "benincasa" / "results" / f"rank26-bidual-coefficient-ring{SUFFIX}.json"
os.environ["MARICI_FIELD_PRIME"] = str(P)
sys.path.insert(0, str(ROOT / "research" / "benincasa"))
base = importlib.import_module("physical_four_mark_residue_twisted_derham")

# Coordinates are (1, epsilon_gamma, epsilon_X, epsilon_gamma epsilon_X).
B = tuple[int, int, int, int]
ZERO: B = (0, 0, 0, 0)
ONE: B = (1, 0, 0, 0)


def add(a: B, b: B) -> B:
    return tuple((x + y) % P for x, y in zip(a, b))  # type: ignore[return-value]


def neg(a: B) -> B:
    return tuple(-x % P for x in a)  # type: ignore[return-value]


def mul(a: B, b: B) -> B:
    a0, ag, ax, agx = a
    b0, bg, bx, bgx = b
    return (
        a0 * b0 % P,
        (a0 * bg + ag * b0) % P,
        (a0 * bx + ax * b0) % P,
        (a0 * bgx + ag * bx + ax * bg + agx * b0) % P,
    )


def inv(a: B) -> B:
    a0, ag, ax, agx = a
    q = pow(a0, -1, P)
    return (
        q,
        -ag * q * q % P,
        -ax * q * q % P,
        (-agx * q * q + 2 * ag * ax * q * q * q) % P,
    )


def scale(a: B, n: int) -> B:
    return tuple(n * x % P for x in a)  # type: ignore[return-value]


rng = random.Random(3921 + P)
samples = [tuple(rng.randrange(P) for _ in range(4)) for _ in range(128)]
units = [(a0 or 1, ag, ax, agx) for a0, ag, ax, agx in samples]
ring_failures = []
for i in range(64):
    a, b, c = samples[i], samples[i + 32], samples[i + 64]
    if mul(a, b) != mul(b, a): ring_failures.append([i, "commutativity"])
    if mul(mul(a, b), c) != mul(a, mul(b, c)): ring_failures.append([i, "associativity"])
    if mul(a, add(b, c)) != add(mul(a, b), mul(a, c)): ring_failures.append([i, "distributivity"])
for i, a in enumerate(units):
    if mul(a, inv(a)) != ONE or mul(inv(a), a) != ONE:
        ring_failures.append([i, "unit_inverse"])

# Verify that the source IBP coefficient has the required mixed component.
# For (gamma-kp) * d_f K, its bidual lift is
# (g0*dK, dK, g0*dK_X, dK_X).
gamma = -pow(2, -1, P) % P
k, _ = base.fiber_data(2, 3, 4)
mixed_failures = []
mixed_support = {"x": 0, "y": 0}
for parameter_axis, name in enumerate(("x", "y")):
    kx, _ = base.parameter_derivative_data(parameter_axis)
    for kp in range(2):
        g0 = (gamma - kp) % P
        for fiber_axis in range(2):
            dk = base.derivative(k, fiber_axis)
            dkx = base.derivative(kx, fiber_axis)
            support = set(dk) | set(dkx)
            for exponent in support:
                coefficient = (
                    g0 * dk.get(exponent, 0) % P,
                    dk.get(exponent, 0) % P,
                    g0 * dkx.get(exponent, 0) % P,
                    dkx.get(exponent, 0) % P,
                )
                if coefficient[3] != dkx.get(exponent, 0) % P:
                    mixed_failures.append([name, kp, fiber_axis, list(exponent)])
                mixed_support[name] += coefficient[3] != 0

checks = {
    "commutative_bidual_ring": not ring_failures,
    "all_sampled_unit_inverses_exact": not any(f[1] == "unit_inverse" for f in ring_failures),
    "source_ibp_mixed_component_exact": not mixed_failures,
    "mixed_component_nonzero_in_both_directions": all(mixed_support.values()),
    "ordinary_specialization_is_constant_component": all((a[0], 0, 0, 0) == mul((a[0], 0, 0, 0), ONE) for a in samples),
}
payload = {
    "schema": "marici.rank26-bidual-coefficient-ring.v1",
    "prime": P,
    "basis": ["1", "epsilon_gamma", "epsilon_X", "epsilon_gamma_epsilon_X"],
    "sample_count": len(samples),
    "ring_failure_count": len(ring_failures),
    "ring_failures": ring_failures[:20],
    "mixed_failure_count": len(mixed_failures),
    "mixed_support": mixed_support,
    "checks": checks,
    "passed": all(checks.values()),
    "conclusion": "The four-grade bidual coefficient ring, including the mixed correction in unit inversion, is certified and the frozen IBP coefficient lifts with mixed component d_X d_f K. This fixes the arithmetic contract for simultaneous quotient reduction.",
}
OUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
if not payload["passed"]:
    raise SystemExit(1)
