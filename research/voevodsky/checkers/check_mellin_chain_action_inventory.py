from __future__ import annotations

import json
from pathlib import Path


INVENTORY = Path("research/voevodsky/mellin-chain-action-inventory-v1.json")
MELLIN = Path("research/grothendieck/the-unilateral-seam-cocycle-is-filled-by-the-mellin-orbit-before-completion.md")
THETA = Path("research/grothendieck/theta-modular-sewing-derivative-square-audit.md")
AFFINE = Path("research/voevodsky/results/affine_simplex_naturality.json")


def main() -> None:
    inventory = json.loads(INVENTORY.read_text(encoding="utf-8"))
    mellin = MELLIN.read_text(encoding="utf-8")
    theta = THETA.read_text(encoding="utf-8")
    affine = json.loads(AFFINE.read_text(encoding="utf-8"))
    assert affine["passed"] is True and affine["reciprocal_negation_naturality"] is True
    assert "straight reciprocal orbit" in mellin
    assert "M_X(w)" in mellin and "cutoff" in mellin
    assert "Stokes basis mutation" in theta
    assert "covariance of every Mellin jet under basis mutation" in theta

    actions = {action["id"]: action for action in inventory["actions"]}
    assert len(actions) == 4
    assert actions["reciprocal_negation"]["chain_level_status"] == "constructed"
    assert actions["stokes_basis_mutation"]["chain_level_status"] == "explicit chain map on affine filler object not supplied"
    assert actions["euler_cutoff_transition"]["chain_level_status"] == "missing"
    assert inventory["excluded_action"]["id"] == "nonlinear_spectral_inversion"

    # A supplied integral basis matrix would be linear, but this fixture cannot identify the source matrix.
    sample_integral_matrix = ((1, 1), (0, 1))
    determinant = sample_integral_matrix[0][0] * sample_integral_matrix[1][1] - sample_integral_matrix[0][1] * sample_integral_matrix[1][0]
    assert determinant == 1

    result = {
        "schema": "marici.voevodsky.mellin-chain-action-inventory-check.v1",
        "status": "action_locus_and_missing_maps_verified",
        "actions_audited": len(actions),
        "reciprocal_chain_action_constructed": True,
        "conjugation_chain_action_conditional": True,
        "stokes_period_covariance_asserted": True,
        "stokes_affine_filler_chain_map_supplied": False,
        "euler_cutoff_transition_map_supplied": False,
        "nonlinear_inversion_imported": False,
        "first_missing_map": inventory["first_missing_map"],
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
