#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational, sqrt

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/resistance-vs-state-observability.json"


def grounded_star(m):
    # One anchored leaf is removed. Coordinates: center, then m-1 other leaves.
    laplacian = Matrix.zeros(m)
    laplacian[0, 0] = m
    for j in range(1, m):
        laplacian[j, j] = 1
        laplacian[0, j] = laplacian[j, 0] = -1
    return laplacian


def main():
    fixtures = []
    for m in (2, 3, 5, 8, 16):
        laplacian = grounded_star(m)
        inverse = laplacian.inv()
        resistance_radius = max(inverse[i, i] for i in range(m))
        expected_gap = (m + 1 - sqrt((m + 1) ** 2 - 4)) / 2
        actual_gap = min(laplacian.eigenvals(), key=lambda z: float(z))
        assert resistance_radius == 2
        assert actual_gap == expected_gap

        constant_state = Matrix([Rational(1, 2)] * m)
        energy = (constant_state.T * laplacian * constant_state)[0]
        norm_squared = (constant_state.T * constant_state)[0]
        assert energy == Rational(1, 4)
        assert norm_squared == Rational(m, 4)
        fixtures.append({"unanchored_dimension": m,
                         "resistance_radius": str(resistance_radius),
                         "grounded_spectral_gap": str(actual_gap),
                         "constant_state_energy": str(energy),
                         "constant_state_norm_squared": str(norm_squared)})

    payload = {
        "schema": "marici.kitaev.resistance_vs_state_observability.v1",
        "status": "pass",
        "star_family": fixtures,
        "uniform_pointwise_unit_threshold": "energy < 1/2",
        "uniform_state_observability": False,
        "separation": "bounded_resistance_radius_does_not_imply_grounded_spectral_gap",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
