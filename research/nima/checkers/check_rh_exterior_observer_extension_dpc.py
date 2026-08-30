#!/usr/bin/env python3
"""Finite DPC for interior energy versus exterior observer extension."""

import json
from pathlib import Path


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def main() -> None:
    # Interior state coordinates: vacuum and one nonvacuum label.
    q = ((0, 0), (0, 2))
    observer = (1, 1)
    cancelling_state = (1, -1)
    energy = sum(cancelling_state[i] * q[i][j] * cancelling_state[j] for i in range(2) for j in range(2))
    assert dot(observer, cancelling_state) == 0
    assert energy == 2

    # Adjoin one exterior boundary coordinate.  Both extensions agree on the
    # entire interior embedding x -> (x, 0), but differ on the boundary unit.
    beta_zero = (1, 1, 0)
    beta_one = (1, 1, 1)
    interior_basis = ((1, 0, 0), (0, 1, 0))
    boundary_unit = (0, 0, 1)
    assert all(dot(beta_zero, x) == dot(beta_one, x) for x in interior_basis)
    assert dot(beta_zero, boundary_unit) != dot(beta_one, boundary_unit)

    result = {
        "schema": "marici.rh-exterior-observer-extension-dpc.v1",
        "positive_energy_zero_readout_witness": {
            "state": cancelling_state,
            "readout": 0,
            "energy": energy
        },
        "interior_agreement_does_not_fix_boundary_extension": True,
        "boundary_extension_values": [dot(beta_zero, boundary_unit), dot(beta_one, boundary_unit)],
        "finite_vacuum_transversality": "already_closed",
        "first_order_tail_closed_range": "already_closed",
        "remaining_gate": "source_authorized_path_independent_exterior_boundary_morphism"
    }
    out = Path(__file__).parents[1] / "results" / "rh-exterior-observer-extension-dpc.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
