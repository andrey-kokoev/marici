"""Compose exact sector audits to separate geometry, dynamics, and access."""

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


kitaev = load(
    "kitaev_wp7_wp9",
    ROOT / "kitaev" / "checkers" / "check_toric_code_wp7_wp9.py",
)
access = load(
    "accessible_readout",
    ROOT / "nima" / "checkers" / "check_accessible_readout_algebra.py",
)


def main():
    boundary = kitaev.boundary_audit(3)
    perturbation = kitaev.perturbation_audit(3)
    restricted = access.audit("two_commuting_loop_ports", [0b0100, 0b1000])
    complete = access.audit(
        "full_primal_dual_loop_ports", [0b0100, 0b1000, 0b0001, 0b0010]
    )

    assert boundary["absolute_h1_dimension"] == 1
    assert boundary["relative_h1_dimension_after_rough_condensation"] == 0
    assert perturbation["chain_complex_unchanged"]
    assert perturbation["adjacent_plaquette_syndrome_not_conserved"]
    assert restricted["projective_pauli_basis_size"] == 4
    assert complete["projective_pauli_basis_size"] == 16

    payload = {
        "schema": "marici.geometry-dynamics-access-axes.v1",
        "geometry_axis": {
            "absolute_h1": boundary["absolute_h1_dimension"],
            "relative_h1_after_boundary_relation": boundary[
                "relative_h1_dimension_after_rough_condensation"
            ],
            "constitutive_change": True,
        },
        "dynamics_axis": {
            "chain_complex_unchanged": perturbation["chain_complex_unchanged"],
            "adjacent_syndrome_conservation_lost": perturbation[
                "adjacent_plaquette_syndrome_not_conserved"
            ],
            "local_spectral_polynomial": perturbation[
                "local_block_characteristic_polynomial"
            ],
        },
        "access_axis": {
            "commuting_port_basis_size": restricted["projective_pauli_basis_size"],
            "complete_port_basis_size": complete["projective_pauli_basis_size"],
            "geometry_change_required": False,
        },
        "gates": {
            "constitutive_geometry_differs_from_dynamical_conservation": True,
            "dynamical_conservation_differs_from_operational_access": True,
            "one_carrier_can_support_multiple_operational_realities": True,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
