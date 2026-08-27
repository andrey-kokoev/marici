"""Finite falsifier: one local square boundary, four global attachments."""
import json
from pathlib import Path


boundary_vertices = [0, 1, 2, 3]
boundary_edges = [(0, 1), (1, 2), (2, 3), (3, 0)]

attachments = [
    {
        "id": "unfilled",
        "vertices": boundary_vertices,
        "edges": boundary_edges,
        "faces": [],
        "beta_1": 1,
        "new_probe": None,
    },
    {
        "id": "cubical_filler",
        "vertices": boundary_vertices,
        "edges": boundary_edges,
        "faces": [[0, 1, 2, 3]],
        "beta_1": 0,
        "new_probe": "square_interior",
    },
    {
        "id": "diagonal_02",
        "vertices": boundary_vertices,
        "edges": boundary_edges + [(0, 2)],
        "faces": [[0, 1, 2], [0, 2, 3]],
        "beta_1": 0,
        "new_probe": "diagonal_02",
    },
    {
        "id": "diagonal_13",
        "vertices": boundary_vertices,
        "edges": boundary_edges + [(1, 3)],
        "faces": [[0, 1, 3], [1, 2, 3]],
        "beta_1": 0,
        "new_probe": "diagonal_13",
    },
]


def restricted_boundary(packet):
    return {
        "vertices": packet["vertices"],
        "edges": [edge for edge in packet["edges"] if edge in boundary_edges],
    }


boundary_packets = [restricted_boundary(packet) for packet in attachments]
tests = {
    "all_local_boundaries_identical": all(packet == boundary_packets[0] for packet in boundary_packets),
    "global_homology_not_determined": {packet["beta_1"] for packet in attachments} == {0, 1},
    "filler_shape_not_determined": {len(packet["faces"]) for packet in attachments} == {0, 1, 2},
    "internal_probe_not_determined": len({packet["new_probe"] for packet in attachments}) == 4,
    "opposite_triangulations_have_same_counts_but_different_ports": attachments[2]["beta_1"]
    == attachments[3]["beta_1"]
    and len(attachments[2]["edges"]) == len(attachments[3]["edges"])
    and attachments[2]["new_probe"] != attachments[3]["new_probe"],
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "deutschian_source_incidence_nerve_falsifier.py",
    "passed": all(tests.values()),
    "tests": tests,
    "attachments": attachments,
    "verdict": "local source incidence does not determine global attachment geometry",
    "missing_constructor": "source-authorized global attachment grammar",
}

out = Path(__file__).resolve().parents[1] / "results" / "deutschian_source_incidence_nerve_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
