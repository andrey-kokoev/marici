import itertools
import json
from pathlib import Path


def solutions(edge_parities, anchor=None):
    found = []
    for assignment in itertools.product((0, 1), repeat=3):
        if anchor is not None and assignment[0] != anchor:
            continue
        a, b, c = assignment
        constraints = (
            (a ^ b) == edge_parities[0],
            (b ^ c) == edge_parities[1],
            (c ^ a) == edge_parities[2],
        )
        if all(constraints):
            found.append(list(assignment))
    return found


trivial = (0, 0, 0)
hostile = (0, 0, 1)

trivial_solutions = solutions(trivial)
anchored_solutions = solutions(trivial, anchor=0)
hostile_solutions = solutions(hostile)

assert trivial_solutions == [[0, 0, 0], [1, 1, 1]]
assert anchored_solutions == [[0, 0, 0]]
assert hostile_solutions == []
assert hostile[0] ^ hostile[1] ^ hostile[2] == 1

# Every proper two-edge subsystem of the hostile is satisfiable.
proper_subsystems_satisfiable = []
for omitted in range(3):
    count = 0
    for assignment in itertools.product((0, 1), repeat=3):
        a, b, c = assignment
        checks = [
            (a ^ b) == hostile[0],
            (b ^ c) == hostile[1],
            (c ^ a) == hostile[2],
        ]
        if all(check for i, check in enumerate(checks) if i != omitted):
            count += 1
    proper_subsystems_satisfiable.append(count > 0)

assert all(proper_subsystems_satisfiable)

result = {
    "status": "pass",
    "claim": "objective records require source-anchored descent, not pairwise agreement alone",
    "trivial_holonomy": {
        "global_sections": trivial_solutions,
        "source_anchored_sections": anchored_solutions,
    },
    "nontrivial_holonomy_hostile": {
        "edge_parities": list(hostile),
        "every_two_edge_subsystem_satisfiable": all(proper_subsystems_satisfiable),
        "global_sections": hostile_solutions,
        "residual": "nontrivial_descent_holonomy",
    },
    "coherence_implies_fault_survival": False,
}

out = Path(__file__).parents[1] / "results" / "objective-record-descent.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))

