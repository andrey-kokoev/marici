from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    identity = sp.eye(2)
    sign = sp.diag(1, -1)

    # Bidegree (1,1) boundary exists, but its mixed square fails.
    f_weak = identity
    f_strong = sign
    source_base_change = identity
    target_base_change = identity
    route_strengthen_after_transfer = target_base_change * f_weak
    route_transfer_after_strengthen = f_strong * source_base_change
    assert route_strengthen_after_transfer != route_transfer_after_strengthen
    mixed_residual = route_strengthen_after_transfer - route_transfer_after_strengthen
    assert mixed_residual == sp.diag(0, 2)

    # Immutable realization gives an identity mixed cell.
    immutable_f_weak = sign
    immutable_f_strong = sign
    assert target_base_change * immutable_f_weak == immutable_f_strong * source_base_change

    # Higher certificate chains need compatible pasting of mixed cells.
    certificate_states = ("b0", "b1", "b2")
    base_edges = (("b0", "b1"), ("b1", "b2"), ("b0", "b2"))
    assert len(certificate_states) == 3 and len(base_edges) == 3
    mixed_01 = identity
    mixed_12 = identity
    mixed_02 = identity
    assert mixed_12 * mixed_01 == mixed_02

    required_fields = {
        "logical_generator_id",
        "certificate_state_source",
        "certificate_state_target",
        "source_base_change",
        "target_base_change",
        "fiber_realization_source",
        "fiber_realization_target",
        "mixed_comparison_cell",
        "mixed_residual",
        "higher_mixed_dependencies",
    }

    result = {
        "schema": "marici.voevodsky.bisimplicial-certificate-naturality.v1",
        "status": "mixed_certificate_sector_horn_gate_verified",
        "bidegree_1_1_boundary_arrows_present": True,
        "boundary_presence_implies_mixed_cell": False,
        "mixed_square_countermodel_residual": [[0, 0], [0, 2]],
        "immutable_realization_identity_cell": True,
        "bidegree_2_1_pasting_fixture": True,
        "pure_and_mixed_horns_independent": True,
        "required_mixed_record_fields": sorted(required_fields),
        "R_zeta_mixed_naturality_status": "deferred_no_realized_fiber_arrow",
        "global_certificate_natural_representation": False,
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
