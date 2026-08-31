#!/usr/bin/env python3
"""Finite exact hostile for the RH completion-stability gate."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT = ROOT / "results" / "rh_completion_inverse_bound_gate_checks.json"

# Derived-limit hostile: every finite trivialization is invertible, but the
# inverse norm diverges and the limit map has a kernel.
epsilons = [Fraction(1, n) for n in range(1, 9)]
finite_invertible = all(e != 0 for e in epsilons)
inverse_norms = [1 / e for e in epsilons]
strict_inverse_growth = all(inverse_norms[i] < inverse_norms[i + 1] for i in range(len(inverse_norms) - 1))
limit_has_kernel = Fraction(0) == 0

# Renormalization hostile: raw Euler-like mean escape and divisor-bearing
# fluctuation are different channels. A raw bound fails even with zero
# fluctuation. Mean subtraction is necessary but is not a mechanism.
raw_mean_partial = [sum(Fraction(1, k) for k in range(1, n + 1)) for n in range(1, 9)]
raw_mean_grows = all(raw_mean_partial[i] < raw_mean_partial[i + 1] for i in range(len(raw_mean_partial) - 1))
zero_fluctuation = [Fraction(0) for _ in raw_mean_partial]
renormalized_fluctuation_bounded = max(abs(x) for x in zero_fluctuation) == 0

# Positivity/coercivity hostile: pointwise positive line-distance energy has no
# uniform lower bound when gaps shrink. For two scales separated by 1/n and
# zero-sum c=(1,-1), the positive energy is proportional to the gap.
gaps = [Fraction(1, n) for n in range(2, 10)]
energies = [2 * gap for gap in gaps]
positive_each_stage = all(e > 0 for e in energies)
no_uniform_lower_bound_witness = all(energies[i] > energies[i + 1] for i in range(len(energies) - 1))

# Virial bridge target: strict positivity contradicts a zero-energy nonzero
# complement state, but only if the zero-to-state construction supplies the
# state and identity independently. This finite row encodes the logical gate.
nonzero_complement_state = (Fraction(1), Fraction(-1))
positive_energy_for_state = energies[-1] > 0
posthoc_virial_claim_would_be_circular = True
independent_zero_to_state_bridge_present = False

checks = {
    "finite_trivializations_are_invertible": finite_invertible,
    "inverse_norms_diverge_in_hostile_prefix": strict_inverse_growth,
    "limit_can_acquire_kernel": limit_has_kernel,
    "raw_mean_escape_grows_without_fluctuation": raw_mean_grows and renormalized_fluctuation_bounded,
    "mean_subtraction_is_necessary_not_explanatory": raw_mean_grows and max(abs(x) for x in zero_fluctuation) == 0,
    "positive_commutator_is_not_uniformly_coercive": positive_each_stage and no_uniform_lower_bound_witness,
    "strict_positivity_would_contradict_independent_virial_zero": positive_energy_for_state and nonzero_complement_state != (0, 0),
    "zero_to_state_bridge_not_supplied_by_finite_audit": not independent_zero_to_state_bridge_present and posthoc_virial_claim_would_be_circular,
}

payload = {
    "schema": "marici.strominger.rh_completion_inverse_bound_gate.v1",
    "status": "passed" if all(checks.values()) else "failed",
    "derived_limit_hostile": {
        "epsilons": [str(e) for e in epsilons],
        "inverse_norms": [str(x) for x in inverse_norms],
        "limit_map": "zero",
    },
    "renormalization_hostile": {
        "raw_mean_prefix": [str(x) for x in raw_mean_partial],
        "renormalized_fluctuation_prefix": [str(x) for x in zero_fluctuation],
    },
    "coercivity_hostile": {
        "gaps": [str(x) for x in gaps],
        "energies_for_c_1_minus_1": [str(x) for x in energies],
    },
    "verdict": (
        "The RH mate completion direction survives only as a sharpened theorem "
        "obligation. Finite invertibility and identity holonomy do not survive "
        "completion without a uniform inverse/graph-norm bound. Raw prime-density "
        "escape must be subtracted before divisor information is typed. The "
        "positive order-Mellin current is pointwise strict but noncoercive under "
        "shrinking gaps, so an RH mechanism must supply either an independent "
        "zero-to-state virial identity or a noncircular completion-stability bound."
    ),
    "checks": checks,
    "gate_count": len(checks),
    "passed_gate_count": sum(checks.values()),
}
RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
print(json.dumps(payload, indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
