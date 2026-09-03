from __future__ import annotations

import json
from pathlib import Path


CONTRACT = Path("research/voevodsky/mellin-stokes-two-locus-interchange-v1.json")
THETA = Path("research/grothendieck/theta-modular-sewing-derivative-square-audit.md")
AFFINE = Path("research/voevodsky/results/affine_simplex_naturality.json")


def identity(size: int) -> list[list[int]]:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def kron(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[left[i // len(right)][j // len(right[0])] * right[i % len(right)][j % len(right[0])] for j in range(len(left[0]) * len(right[0]))] for i in range(len(left) * len(right))]


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]


def main() -> None:
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    theta = THETA.read_text(encoding="utf-8")
    affine = json.loads(AFFINE.read_text(encoding="utf-8"))
    assert affine["reciprocal_negation_naturality"] is True
    assert "Stokes basis mutation" in theta
    assert "covariance of every Mellin jet under basis mutation" in theta
    assert set(contract["loci"]) == {"spectral_affine", "integration_cycle"}

    rho = [[-1, 0], [0, -1]]
    T = [[1, 1], [0, 1]]
    spectral_action = kron(rho, identity(2))
    cycle_action = kron(identity(2), T)
    assert multiply(spectral_action, cycle_action) == multiply(cycle_action, spectral_action)

    status = contract["actual_status"]
    assert status["spectral_reciprocal_action"] == "constructed"
    assert status["cycle_level_stokes_covariance"] == "asserted"
    assert status["chain_model_for_stokes_action"] == "not supplied"
    assert status["period_pairing_interchange_cell"] == "not supplied"

    result = {
        "schema": "marici.voevodsky.mellin-stokes-two-locus-interchange-check.v1",
        "status": "action_locus_factorization_verified",
        "spectral_and_cycle_loci_distinct": True,
        "strict_product_actions_commute": True,
        "stokes_is_spectral_chain_endomorphism": False,
        "stokes_cycle_level_covariance_asserted": True,
        "actual_cycle_chain_map_supplied": False,
        "actual_pairing_interchange_cell_supplied": False,
        "cutoff_interchange_supplied": False,
        "first_missing_datum": contract["first_missing_datum"],
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
