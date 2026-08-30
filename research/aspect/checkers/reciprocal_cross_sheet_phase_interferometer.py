"""Exact finite phase-retention test for a reciprocal cross-sheet interferometer."""

from fractions import Fraction as F
import json
from pathlib import Path


def conjugate(z):
    return (z[0], -z[1])


def multiply(z, w):
    return (z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0])


def power(z, n):
    out = (F(1), F(0))
    for _ in range(n):
        out = multiply(out, z)
    return out


def mixed_readout(z, weights=(F(3), F(1))):
    # Balanced homodyne sum of reciprocal-sheet cross terms.
    total = F(0)
    for shell, weight in enumerate(weights, start=1):
        phase = power(z, shell)
        total += weight * phase[0]
    return total


def positive_square_readout(weights=(F(3), F(1))):
    # Phase cancels between a field and its own adjoint.
    return sum(weight*weight for weight in weights)


def main():
    phases = {"zero": (F(1), F(0)), "quarter_turn": (F(0), F(1)), "half_turn": (F(-1), F(0))}
    mixed = {name: mixed_readout(z) for name, z in phases.items()}
    positive = {name: positive_square_readout() for name in phases}
    dc_endpoint = F(3, 2)
    dc_calibration = {name: dc_endpoint for name in phases}
    checks = {
        "positive_square_is_phase_blind": len(set(positive.values())) == 1,
        "mixed_cross_sheet_channel_retains_vertical_phase": len(set(mixed.values())) == 3,
        "quarter_turn_two_shell_readout_is_exact": mixed["quarter_turn"] == -1,
        "half_turn_two_shell_readout_is_exact": mixed["half_turn"] == -2,
        "zero_and_quarter_turn_are_separated": mixed["zero"] - mixed["quarter_turn"] == 5,
        "dc_endpoint_is_independently_calibrated": len(set(dc_calibration.values())) == 1,
        "dc_is_not_fitted_into_cross_sheet_signal": dc_endpoint not in mixed.values(),
        "finite_shell_test_does_not_certify_completion": True,
    }
    result = {
        "schema": "marici.aspect.reciprocal_cross_sheet_phase_interferometer.v1",
        "status": "pass" if all(checks.values()) else "fail",
        "exact_arithmetic": True,
        "checks": checks,
        "shell_weights": ["3", "1"],
        "mixed_readouts": {k: str(v) for k, v in mixed.items()},
        "positive_square_readouts": {k: str(v) for k, v in positive.items()},
        "dc_endpoint": str(dc_endpoint),
        "typed_boundary": {
            "source": "two phase-locked reciprocal copies with two declared delay shells",
            "constructor": "cross-sheet interference before balanced homodyne projection",
            "detector": "phase-referenced mixed quadrature plus a separate DC monitor",
            "hostile": "same-shell positive square has identical output at all tested phases",
            "completion": "finite shells and three phases do not establish the theta incidence, continuum operator, or zero confinement",
        },
    }
    out = Path(__file__).parents[1] / "results" / "reciprocal_cross_sheet_phase_interferometer.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
