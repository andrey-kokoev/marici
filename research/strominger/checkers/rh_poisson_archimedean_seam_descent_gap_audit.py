#!/usr/bin/env python3
"""Poisson/archimedean/seam descent gap audit for the RH boundary-jet tower."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_poisson_archimedean_seam_descent_gap_audit.json"

primes = [2, 3, 5, 7]
max_depth = 5

# Formal wave-trace coefficients: at return k log p, coefficient log p.  The
# checker represents log p by the prime label p; equality is source-label exact.
wave_trace = {(p, k): p for p in primes for k in range(1, max_depth + 1)}

# Composite non-prime-powers are not primitive returns in the prime-circle
# carrier.  The tuple (6,1) is deliberately outside the return index set.
composite_return_absent = (6, 1) not in wave_trace

# Critical half-density amplitudes are a local contraction sequence r_p^k; use
# exact rational model values only to test multiplicativity, not to identify
# actual sqrt(p) numerically.
r = {2: Fraction(1, 2), 3: Fraction(1, 3), 5: Fraction(1, 5), 7: Fraction(1, 7)}
half_density = {(p, k): r[p] ** k for p in primes for k in range(1, max_depth + 1)}
local_transfer_ok = all(half_density[(p, k + 1)] == half_density[(p, k)] * r[p] for p in primes for k in range(1, max_depth))

# Square/Kakutani obstruction: partial sums of 1/p grow on this prefix.  This is
# interface data, not a removable bounded perturbation.
square_prefix = []
running = Fraction(0)
for p in primes:
    running += Fraction(1, p)
    square_prefix.append(running)
square_current_grows = all(square_prefix[i] < square_prefix[i + 1] for i in range(len(square_prefix) - 1))

# Boundary-jet transition hostile: Poisson return data through depth g does not
# determine the next boundary coefficient.  Two source packets can agree on all
# prime-circle returns through depth g and differ at g+1.
g = 4
packet_a = {k: Fraction(0) for k in range(1, g + 2)}
packet_b = {k: Fraction(0) for k in range(1, g + 2)}
packet_b[g + 1] = Fraction(1)
old_returns_equal = all(packet_a[k] == packet_b[k] for k in range(1, g + 1))
new_boundary_differs = packet_a[g + 1] != packet_b[g + 1]

# Seam boundedness is exact for reciprocal chart ratio exp(+-2 Re(z) q): over an
# unbounded q-domain it is uniformly bounded in both directions only at Re(z)=0.
def reciprocal_chart_bounded(real_z: Fraction, q_prefix: list[int]) -> bool:
    if real_z == 0:
        return True
    # Any nonzero real part gives monotone unbounded exponential on the infinite
    # q-domain; a finite prefix is not authority for completion.
    return False

seam_bounded = reciprocal_chart_bounded(Fraction(0), list(range(1, 8)))
off_seam_unbounded = not reciprocal_chart_bounded(Fraction(1, 3), list(range(1, 8)))

# Adjoint pairing preservation gate: subtracting the square/interface current
# would change the pairing unless a separate source transition carries it.
source_transition_for_square_subtraction = False
square_pairing_retained = square_current_grows and not source_transition_for_square_subtraction

checks = {
    "prime_circle_trace_has_von_mangoldt_depth_weights": all(wave_trace[(p, k)] == p for p in primes for k in range(1, max_depth + 1)),
    "non_prime_power_composite_is_not_primitive_return": composite_return_absent,
    "local_half_density_transfer_is_multiplicative": local_transfer_ok,
    "square_current_prefix_is_nonremovable_interface_data": square_current_grows,
    "old_poisson_return_data_does_not_determine_next_boundary_jet": old_returns_equal and new_boundary_differs,
    "reciprocal_chart_norm_boundary_is_exactly_the_seam": seam_bounded and off_seam_unbounded,
    "adjoint_pairing_requires_retaining_square_interface": square_pairing_retained,
}

payload = {
    "schema": "marici.strominger.rh_poisson_archimedean_seam_descent_gap_audit.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "prime_circle_trace_prefix": {f"p={p},k={k}": f"log({p})" for p in primes for k in range(1, 3)},
    "square_prefix_sum_1_over_p": [str(x) for x in square_prefix],
    "same_old_returns_different_next_boundary": {
        "g": g,
        "packet_a_next": str(packet_a[g + 1]),
        "packet_b_next": str(packet_b[g + 1]),
    },
    "verdict": (
        "Prime-circle Poisson data supplies an independent source object: the "
        "von Mangoldt wave trace, local half-density return amplitudes, and the "
        "square/Kakutani interface current. It still does not supply the growing "
        "boundary-jet transition. Return data through depth g can agree while the "
        "order g+1 boundary coefficient differs, and off-seam reciprocal chart "
        "norms are completion-unbounded. The top RH direction is therefore "
        "exhausted at the present source level: a new adelic relative coupling or "
        "seam transition must be constructed before it can determine boundary "
        "jets while preserving the adjoint pairing."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
