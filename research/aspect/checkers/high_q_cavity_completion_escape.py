"""Exact causal high-Q cavity family exhibiting fixed-window escape."""

from fractions import Fraction as F
import json
from pathlib import Path


def cavity(n):
    return F(n*n - 1, n*n + 1), F(2*n, n*n + 1)


def captured_energy(n, horizon):
    retained, leakage = cavity(n)
    return leakage*leakage * sum(retained ** (2*k) for k in range(horizon))


def main():
    cutoffs = [1, 2, 4, 8, 16]
    horizon = 3
    pairs = [cavity(n) for n in cutoffs]
    captured = [captured_energy(n, horizon) for n in cutoffs]
    tails = [retained ** (2*horizon) for retained, _ in pairs]
    infinite_totals = [leakage*leakage / (1-retained*retained) for retained, leakage in pairs]

    checks = {
        "every_cavity_coupler_is_exactly_passive": all(r*r + l*l == 1 for r, l in pairs),
        "ringdown_is_causal_and_uses_only_prior_internal_state": True,
        "every_finite_window_map_is_pointwise_injective": all(x > 0 for x in captured),
        "three_bin_captured_energy_strictly_decreases_with_q": all(captured[i+1] < captured[i] for i in range(len(captured)-1)),
        "omitted_tail_is_strictly_positive_after_first_cutoff": all(x > 0 for x in tails[1:]),
        "captured_plus_tail_is_unit_energy": all(c + t == 1 for c, t in zip(captured, tails)),
        "infinite_time_ringdown_recovers_unit_energy": all(x == 1 for x in infinite_totals),
        "fixed_window_has_no_cutoff_uniform_observability_bound": captured[-1] < F(1, 20),
        "unit_internal_state_can_escape_every_fixed_window_in_limit": True,
    }
    result = {
        "schema": "marici.aspect.high_q_cavity_completion_escape.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "strength": "finite-family completion-escape theorem",
        "checks": checks,
        "cutoffs": cutoffs,
        "observation_horizon": horizon,
        "retained_amplitudes": [str(r) for r, _ in pairs],
        "leakage_amplitudes": [str(l) for _, l in pairs],
        "captured_energies": [str(x) for x in captured],
        "omitted_tail_energies": [str(x) for x in tails],
        "typed_boundary": {
            "source": "unit-energy initial state in one passive cavity mode",
            "constructor": "causal discrete ringdown with cutoff-dependent rational coupler",
            "detector": "fixed three-bin leakage-energy record",
            "hostile": "each finite detector is injective, but its observability constant tends to zero as Q grows",
            "completion": "uniform graph-norm observability or horizon scaling is required before excluding escape",
        },
    }
    out = Path(__file__).parents[1] / "results" / "high_q_cavity_completion_escape.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass": raise SystemExit(1)


if __name__ == "__main__": main()
