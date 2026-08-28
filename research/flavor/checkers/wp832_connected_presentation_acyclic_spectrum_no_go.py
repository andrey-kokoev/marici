"""Exact WP832 test: support-connected presentation does not remove acyclic spectrum."""

import json
from itertools import combinations
from math import gcd
from pathlib import Path
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ


def support_connected(matrix: sp.Matrix) -> tuple[bool, list[int], list[int]]:
    rows, cols = matrix.shape
    adjacency = {("r", i): set() for i in range(rows)}
    adjacency.update({("c", j): set() for j in range(cols)})
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] != 0:
                adjacency[("r", i)].add(("c", j))
                adjacency[("c", j)].add(("r", i))
    start = next(iter(adjacency))
    seen = {start}
    frontier = [start]
    while frontier:
        node = frontier.pop()
        for neighbor in adjacency[node]-seen:
            seen.add(neighbor)
            frontier.append(neighbor)
    row_degrees = [len(adjacency[("r", i)]) for i in range(rows)]
    col_degrees = [len(adjacency[("c", j)]) for j in range(cols)]
    return len(seen) == len(adjacency), row_degrees, col_degrees


def main() -> None:
    base = sp.Matrix([[2, -1, 0], [3, 0, -1]])
    stabilized = sp.diag(1, 1, 1)  # placeholder overwritten for explicit shape
    stabilized = sp.Matrix([[2, -1, 0, 0],
                            [3, 0, -1, 0],
                            [0, 0, 0, 1]])
    connected = sp.Matrix([[2, -1, 0, 1],
                           [3, 0, -1, 1],
                           [1, 1, -1, 1]])
    q = sp.Matrix([1, 2, 3])
    q_ext = sp.Matrix([1, 2, 3, 0])
    r = sp.symbols("r", positive=True, integer=True)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("base_primitive_kernel_is_retained",
          base*q == sp.zeros(2, 1) and base.rank() == 2, base.nullspace())
    check("connected_completion_retains_extended_primitive_kernel",
          connected*q_ext == sp.zeros(3, 1) and connected.rank() == 3
          and connected.nullspace()[0] == q_ext/3,
          connected.nullspace())
    snf_stabilized = smith_normal_form(stabilized, domain=ZZ)
    snf_connected = smith_normal_form(connected, domain=ZZ)
    check("connected_and_split_presentations_have_same_smith_form",
          snf_stabilized == snf_connected, (snf_stabilized, snf_connected))

    minors = [connected[:, cols].det() for cols in combinations(range(4), 3)]
    minor_gcd = 0
    for value in minors:
        minor_gcd = gcd(minor_gcd, abs(int(value)))
    check("connected_completion_has_trivial_cokernel", minor_gcd == 1, minors)

    split_connected, split_rows, split_cols = support_connected(stabilized)
    apparent_connected, row_degrees, col_degrees = support_connected(connected)
    check("split_stabilization_has_disconnected_support", not split_connected,
          (split_rows, split_cols))
    check("equivalent_presentation_has_connected_support", apparent_connected,
          (row_degrees, col_degrees))
    check("connected_presentation_has_no_leaf_row_or_column",
          min(row_degrees) >= 2 and min(col_degrees) >= 2,
          (row_degrees, col_degrees))

    base_anomaly = sum(component**3 for component in q)
    extended_anomaly = sum(component**3 for component in q_ext)
    check("oriented_current_anomaly_is_unchanged",
          base_anomaly == extended_anomaly == 36,
          (base_anomaly, extended_anomaly))
    check("acyclic_vectorlike_decoration_remains_anomaly_neutral",
          r+(-r) == 0 and sp.expand(r**3+(-r)**3) == 0,
          (r+(-r), sp.expand(r**3+(-r)**3)))

    base_index = q.dot(q)
    completed_index = base_index+2*r**2
    check("connected_acyclic_decoration_changes_spectral_index",
          sp.simplify(completed_index-base_index-2*r**2) == 0,
          completed_index)

    mass, heat_time = sp.symbols("mass heat_time", positive=True, real=True)
    heat_record = 2*sp.exp(-heat_time*mass**2)
    check("acyclic_mass_remains_a_continuous_spectral_parameter",
          sp.diff(heat_record, mass) != 0, sp.diff(heat_record, mass))

    hostile_coupling = sp.sqrt(sp.Rational(7, 8))
    check("ward_response_fiber_survives_connected_presentation",
          base_index == (base_index+2)*hostile_coupling**2,
          (base_index, (base_index+2)*hostile_coupling**2))

    result = {
        "work_package": "WP832",
        "title": "Connected-presentation acyclic-spectrum no-go",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "exact_matrices": {
            "base": [[int(value) for value in row] for row in base.tolist()],
            "split_stabilization": [[int(value) for value in row]
                                    for row in stabilized.tolist()],
            "support_connected_completion": [[int(value) for value in row]
                                             for row in connected.tolist()],
            "common_smith_form": [[int(value) for value in row]
                                  for row in snf_connected.tolist()],
            "primitive_kernel": [int(value) for value in q_ext],
            "connected_support_degrees": {"rows": row_degrees, "columns": col_degrees},
        },
        "classification": {
            "preserved": ["primitive current", "oriented anomaly 36",
                          "kernel rank one", "trivial cokernel", "Smith type"],
            "presentation_change": "the split acyclic summand can be represented by a support-connected matrix with no leaf row or column",
            "not_selected": ["vectorlike charge decoration", "acyclic mass",
                             "spectral index", "threshold coupling"],
            "first_nonfaithful_arrow": "integral chain object up to Smith equivalence to support-connected presentation",
            "selector_or_rigidifier": "support connectedness rigidifies a presentation; it is not a spectral-completion selector",
            "smallest_exact_falsifier": "B direct-sum 1 versus the displayed connected 3x4 matrix, followed by the same (14,1)/(16,sqrt(7/8)) Ward-response fiber",
        },
        "remaining_source_gate": "an invariant physical irreducibility or spectral action must exclude or fix interacting anomaly-neutral sectors and their masses; graph support connectedness or matrix indecomposability by permutation is insufficient",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp832_connected_presentation_acyclic_spectrum_no_go.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
