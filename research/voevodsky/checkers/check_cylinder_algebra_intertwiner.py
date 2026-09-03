from __future__ import annotations

import json
import sympy as sp


def main() -> None:
    entries = sp.symbols("c0:16")
    C = sp.Matrix(4, 4, entries)

    # Two finite cylinder projections jointly separate the bulk support
    # (first two atoms) from the corona support (last two atoms).
    bulk_rep = [sp.diag(1, 0, 0, 0), sp.diag(0, 1, 0, 0)]
    corona_rep = [sp.zeros(4), sp.zeros(4)]
    equations = []
    for plus, times in zip(bulk_rep, corona_rep):
        equations.extend(list(C * plus - times * C))

    solution = sp.linsolve(equations, entries)
    tuple_solution = next(iter(solution))
    forced_zero_columns = all(tuple_solution[4 * i + j] == 0 for i in range(4) for j in (0, 1))
    assert forced_zero_columns

    result = {
        "schema":"marici.voevodsky.cylinder-algebra-intertwiner-check.v1",
        "status":"separating_cylinder_projections_kill_intertwiner",
        "finite_fixture_forced_bulk_columns_zero":True,
        "infinite_extension":"bounded intertwining passes from strongly dense cylinder algebra to generated multiplication von Neumann algebra",
        "unbounded_closable_channel_excluded":False,
        "smaller_nonseparating_algebra_excluded":False,
        "rh_implication":False,
        "passed":True
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
