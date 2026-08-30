"""Direct completed-Mellin audit of the fifth-jet positivity reserve."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np
from scipy.integrate import quad
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
import deutschean_cumulant_gevrey_descent as descent


ROOT = Path(__file__).resolve().parents[3]
PACKET = ROOT / "research/strominger/deutschean-primitive-cumulant-completion-explanation.md"
RESULT = ROOT / "research/strominger/results/deutschean_completed_mellin_reserve.json"
T = 1.0 / 60.0
Q_VALUES = [4.0 + 0.5 * i for i in range(13)]


def source_log_carrier(x: float) -> float:
    exponential = np.exp(T * x) if T * x < 700 else np.inf
    if not np.isfinite(exponential):
        return -np.inf
    return (
        np.log(exponential - 1.5 * T)
        + 1.25 * T * x
        - (exponential - 1.0 - T * x) / T
    )


def log_mellin_cumulants(shape_minus_one: float, tolerance: float) -> tuple[float, float, float]:
    integrals = []
    for power in range(4):
        def integrand(x: float) -> float:
            if x == 0.0:
                return 0.0
            log_carrier = source_log_carrier(x)
            if not np.isfinite(log_carrier):
                return 0.0
            return float(
                np.exp(shape_minus_one * np.log(x) - x + log_carrier)
                * np.log(x) ** power
            )

        integrals.append(
            quad(
                integrand,
                0.0,
                np.inf,
                epsabs=tolerance,
                epsrel=tolerance,
                limit=400,
            )[0]
        )
    raw = np.asarray(integrals) / integrals[0]
    return (
        float(raw[1]),
        float(raw[2] - raw[1] ** 2),
        float(raw[3] - 3 * raw[2] * raw[1] + 2 * raw[1] ** 3),
    )


def completed_margin(q: float, cumulants: dict[float, tuple[float, float, float]]) -> tuple[float, float]:
    upper = cumulants[q]
    lower = cumulants[q - 1.0]
    adjacent = upper[0] - lower[0]
    variance = -(upper[1] - lower[1])
    skew = upper[2] - lower[2]
    affine = 1.0 - q * adjacent
    margin = (
        3.0 * affine * variance
        + adjacent**2 * (2.0 + affine)
        - q * skew
    ) / adjacent**2
    return margin, adjacent


def reconstruction_polynomials() -> dict[int, sp.Expr]:
    q_symbol = sp.symbols("q")
    carrier = descent.build_carrier()
    samples = {q: descent.margin_at_grade(carrier, q) for q in range(1, 7)}
    return {
        n: sp.interpolate(
            [
                (
                    q,
                    sp.Rational(samples[q][n].numerator, samples[q][n].denominator),
                )
                for q in range(1, n + 2)
            ],
            q_symbol,
        )
        for n in range(3, 6)
    }


def evaluate(tolerance: float) -> tuple[list[float], list[float]]:
    shapes = [3.0 + 0.5 * i for i in range(15)]
    cumulants = {shape: log_mellin_cumulants(shape, tolerance) for shape in shapes}
    polynomials = reconstruction_polynomials()
    q_symbol = sp.symbols("q")
    ratios = []
    adjacent_responses = []
    for q in Q_VALUES:
        margin, adjacent = completed_margin(q, cumulants)
        q_exact = sp.Rational(round(2 * q), 2)
        partial = sum(
            float(polynomials[n].subs(q_symbol, q_exact)) * T**n
            for n in range(3, 6)
        )
        reserve = 2.5 * q**3 * T**3
        ratios.append((margin - partial) / reserve)
        adjacent_responses.append(adjacent)
    return ratios, adjacent_responses


def main() -> None:
    coarse_ratios, coarse_adjacent = evaluate(2e-10)
    fine_ratios, fine_adjacent = evaluate(2e-12)
    convergence = max(
        abs(coarse - fine) for coarse, fine in zip(coarse_ratios, fine_ratios)
    )
    checks = {
        "completed_adjacent_response_stays_positive": all(
            value > 0 for value in fine_adjacent
        ),
        "completed_defect_has_expected_negative_orientation": all(
            value < 0 for value in fine_ratios
        ),
        "completed_defect_uses_less_than_two_fifths_reserve": all(
            abs(value) < 0.4 for value in fine_ratios
        ),
        "defect_ratio_is_monotone_on_half_step_shape_grid": all(
            fine_ratios[i + 1] < fine_ratios[i]
            for i in range(len(fine_ratios) - 1)
        ),
        "independent_tolerance_replay_agrees": convergence < 1e-6,
    }
    payload = {
        "artifact_sha256": sha256(PACKET.read_bytes()).hexdigest().upper(),
        "checks": checks,
        "observed": {
            "wall_parameter": "1/60",
            "shape_grid": Q_VALUES,
            "fine_defect_to_reserve_ratios": fine_ratios,
            "maximum_absolute_defect_ratio": max(abs(value) for value in fine_ratios),
            "maximum_tolerance_replay_difference": convergence,
            "minimum_adjacent_response": min(fine_adjacent),
        },
        "passed": all(checks.values()),
        "semantic_boundary": (
            "Direct source-integral evidence on the half-step q grid at t=1/60. "
            "It evaluates the completed Mellin readout rather than a long jet truncation, "
            "but it is not interval arithmetic and does not prove the continuous q or t bounds."
        ),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not payload["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
