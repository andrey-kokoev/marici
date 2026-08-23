"""Exact linear compatibility gate for the three moving shared walls."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

OUT = Path(__file__).resolve().parents[1] / "results" / "cosmology_three_wall_moving_normal_obstruction.json"


def main():
    dx, dy, dz = sp.symbols("dx dy dz")
    jacobian = sp.Matrix(((0, 1), (1, 0), (1, 1)))
    external = sp.Matrix((-dy - dz, -dx - dz, dz))
    cokernel = sp.Matrix(((-1, -1, 1),))
    assert jacobian.rank() == 2
    assert cokernel * jacobian == sp.zeros(1, 2)
    obstruction = sp.expand((cokernel * external)[0])
    assert obstruction == dx + dy + 3 * dz

    # Verify sufficiency: when the obstruction vanishes, da=dx+dz and
    # db=dy+dz solves all three fixed-normal equations.
    da, db = dx + dz, dy + dz
    residual = sp.simplify(jacobian * sp.Matrix((da, db)) + external)
    assert list(residual) == [0, 0, dx + dy + 3 * dz]

    packet = {
        "schema": "marici.cosmology-three-wall-moving-normal-obstruction.v1",
        "fiber_normal_jacobian": [
            [int(value) for value in row] for row in jacobian.tolist()
        ],
        "rank": jacobian.rank(),
        "left_cokernel_generator": [-1, -1, 1],
        "external_normal_variation": ["-dy-dz", "-dx-dz", "dz"],
        "compatibility_obstruction": str(obstruction),
        "pure_total_energy_obstruction": "3*dE",
        "ordinary_simultaneous_fixed_normal_lift_exists_generically": False,
        "required_completion": "one-dimensional augmented principal wall-motion cell",
        "passed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
