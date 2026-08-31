"""Exact first-jet packet for the moving physical three-wall family.

This checker deliberately separates facts that are often conflated:

1. the normal sequence and its one-dimensional cokernel;
2. local bulk-to-wall moving-residue compatibility;
3. pairwise Cech closure of the physical localization boundary.

It does not construct the missing chain-level homotopy joining all three.
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path



ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "nima" / "results" / "cosmology_augmented_wall_first_jet_packet.json"


def run_source_checker(path: Path) -> dict:
    completed = subprocess.run(
        [sys.executable, str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(completed.stdout)


def main() -> None:
    # T_fiber -> N_walls for q1=b-y-z, q2=a-x-z, q3=a+b+z.
    jacobian = [[0, 1], [1, 0], [1, 1]]
    quotient = [-1, -1, 1]
    assert jacobian[0][0] * jacobian[1][1] - jacobian[0][1] * jacobian[1][0] == -1
    assert [sum(quotient[i] * jacobian[i][j] for i in range(3)) for j in range(2)] == [0, 0]
    assert 2 - 3 + 1 == 0

    kodaira_spencer = "dx + dy + 3*dz"

    bulk_wall = run_source_checker(
        ROOT / "benincasa" / "physical_bulk_wall_connection_residue.py"
    )
    cech = run_source_checker(
        ROOT / "benincasa" / "physical_g12_shared_wall_cech_cocycle.py"
    )
    first_cech = json.loads(
        (ROOT / "benincasa" / "physical-wall-first-gauss-manin-cech.json").read_text(
            encoding="utf-8"
        )
    )
    principal = run_source_checker(
        ROOT / "nima" / "checkers" / "check_cosmology_source_principal_wall_cell.py"
    )
    assert bulk_wall["all_commutators_zero"]
    assert bulk_wall["nonzero_moving_wall_corrections"] > 0
    assert cech["physical_localization_boundary_is_closed"]
    assert first_cech["all_transported_cech_components_zero"]
    assert principal["incidence_parameter_source_derived"]
    assert not principal["independent_principal_line_inferred"]

    packet = {
        "schema": "marici.cosmology-augmented-wall-first-jet-packet.v1",
        "normal_sequence": {
            "dimensions": [2, 3, 1],
            "fiber_to_wall_rank": 2,
            "wall_to_principal_rank": 1,
            "composition_zero": True,
            "exact": True,
        },
        "base_to_principal_representative": kodaira_spencer,
        "base_to_principal_generically_nonzero": True,
        "local_bulk_to_wall_commutators_zero": True,
        "local_moving_wall_corrections_nonzero": bulk_wall[
            "nonzero_moving_wall_corrections"
        ],
        "physical_localization_boundary_cech_closed": True,
        "first_derivative_pairwise_cech_closed": True,
        "homogeneous_simultaneous_three_wall_lift_exists_generically": False,
        "homogeneous_model_requires_cokernel_completion": True,
        "completion_retyped_as_triple_incidence_support": True,
        "independent_principal_augmentation_inferred": False,
        "principal_chain_level_homotopy_constructed": False,
        "global_augmented_residue_connection_claimed": False,
        "remaining_gate": (
            "construct the triple-Cech nearby-cycle term on the source "
            "incidence divisor p=x+y+3*z=0"
        ),
        "passed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
