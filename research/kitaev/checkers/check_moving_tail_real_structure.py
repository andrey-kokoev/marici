#!/usr/bin/env python3
"""Exact finite witnesses for strong but nonuniform real-structure transport."""

import hashlib
import json
from pathlib import Path

from sympy import Matrix


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/moving-tail-real-structure.json"


def structure(dimension, flipped_index=None):
    diagonal = [1] * dimension
    if flipped_index is not None:
        diagonal[flipped_index] = -1
    return Matrix.diag(*diagonal)


def main():
    fixtures = []
    for dimension in [3, 5, 8, 13]:
        flipped = dimension - 1
        standard = structure(dimension)
        moving = structure(dimension, flipped)
        residual = standard - moving
        witness = Matrix.eye(dimension)[:, flipped]
        unit = Matrix.eye(dimension)[:, 0]

        assert residual.rank() == 1
        assert residual * witness == 2 * witness
        assert residual * unit == Matrix.zeros(dimension, 1)
        # All fixed-prefix probes are blind to the last-coordinate residual.
        prefix_width = dimension - 1
        prefix_probe = Matrix.eye(dimension)[:prefix_width, :]
        assert prefix_probe * residual * witness == Matrix.zeros(prefix_width, 1)

        # Real-linear projection gap on the flipped complex coordinate is one.
        projection_gap = 1
        fixtures.append({
            "dimension": dimension,
            "flipped_coordinate": dimension,
            "residual_rank": residual.rank(),
            "moving_witness_residual_norm": 2,
            "vacuum_residual": 0,
            "fixed_prefix_blind": True,
            "real_subspace_gap": projection_gap,
        })

    # For any fixed prefix k, every later flip is exactly invisible there.
    fixed_prefix = 4
    ambient = 10
    prefix_probe = Matrix.eye(ambient)[:fixed_prefix, :]
    eventual_zero = []
    for flipped in range(fixed_prefix, ambient):
        residual = structure(ambient) - structure(ambient, flipped)
        eventual_zero.append(prefix_probe * residual == Matrix.zeros(fixed_prefix, ambient))
    assert all(eventual_zero)

    payload = {
        "schema": "marici.kitaev.moving_tail_real_structure.v1",
        "status": "pass",
        "strong_limit": "J_N -> J pointwise because 2|x_N| -> 0 for every x in l2",
        "operator_norm_residual": 2,
        "fixed_real_subspace_gap": 1,
        "finite_fixtures": fixtures,
        "fixed_prefix_test": {
            "prefix_dimension": fixed_prefix,
            "later_flips_all_invisible": all(eventual_zero),
        },
        "completion_gate": [
            "uniform intertwiner norm",
            "fixed-real-subspace gap convergence",
            "source topology kills every moving witness",
            "authorized rows uniformly observe every moving witness",
        ],
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope_exclusions": ["theta/Tate topology", "witness operativity", "source conjugation", "RH"],
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
