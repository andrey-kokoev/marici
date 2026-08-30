#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

from sympy import Matrix, Rational

ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/kitaev/results/effective-resistance-unit.json"


def grounded_resistance(reduced_laplacian, target_index):
    voltage = reduced_laplacian.inv() * Matrix.eye(reduced_laplacian.rows)[:, target_index]
    return voltage[target_index]


def main():
    chain_reduced = Matrix([[2, -1], [-1, 1]])
    seam_reduced = Matrix([[2, -1], [-1, 2]])
    chain_r = grounded_resistance(chain_reduced, 1)
    seam_r = grounded_resistance(seam_reduced, 1)
    assert chain_r == 2
    assert seam_r == Rational(2, 3)
    assert seam_r < chain_r

    u = [1, Rational(3, 4), Rational(1, 2)]
    chain_energy = (u[0] - u[1]) ** 2 + (u[1] - u[2]) ** 2
    seam_energy = chain_energy + (u[0] - u[2]) ** 2
    endpoint_defect = (u[2] - u[0]) ** 2
    assert chain_energy == Rational(1, 8)
    assert seam_energy == Rational(3, 8)
    assert chain_r * chain_energy == endpoint_defect == Rational(1, 4)
    assert seam_r * seam_energy == endpoint_defect

    disconnected_reduced = Matrix([[1, 0], [0, 0]])
    assert disconnected_reduced.det() == 0

    payload = {
        "schema": "marici.kitaev.effective_resistance_unit.v1",
        "status": "pass",
        "chain": {"effective_resistance_anchor_to_target": str(chain_r),
                  "energy": str(chain_energy), "sharp_product": str(endpoint_defect)},
        "seam_augmented": {"effective_resistance_anchor_to_target": str(seam_r),
                           "energy": str(seam_energy), "sharp_product": str(endpoint_defect)},
        "rayleigh_monotonicity": True,
        "disconnected_hostile": {"grounded_laplacian_singular": True,
                                 "effective_resistance": "infinity"},
        "shared_geometry": ["incidence", "conductance", "anchor", "effective_resistance"],
        "coefficient_lens": ["edge_norm", "normalization_interpretation", "root_sheet_meaning"],
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
