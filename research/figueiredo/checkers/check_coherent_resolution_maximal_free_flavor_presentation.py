import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
source_checker = ROOT / "research/nima/checkers/check_a3_coherent_resolution.py"
transport_path = ROOT / "research/nima/results/n8-boundary-completed-cluster-transport.json"
out_path = ROOT / "research/figueiredo/results/coherent-resolution-maximal-free-flavor-presentation.json"

source_text = source_checker.read_text(encoding="utf-8")
source_body = source_text.rsplit("raise SystemExit", 1)[0]
ns = {"__file__": str(source_checker), "__name__": "a3_source_checker"}
exec(compile(source_body, str(source_checker), "exec"), ns)
D1, D2, D3, AUG = ns["D1"], ns["D2"], ns["D3"], ns["AUG"]
transport = json.loads(transport_path.read_text(encoding="utf-8"))

I0 = sp.eye(D1.rows)
I1 = sp.eye(D1.cols)
I2 = sp.eye(D2.cols)
I3 = sp.eye(D3.cols)

chain_residuals = {
    "edges": D1 * I1 - I0 * D1,
    "faces": D2 * I2 - I1 * D2,
    "top_cell": D3 * I3 - I2 * D3,
}

false_I1 = sp.eye(D1.cols)
false_I1[0, 0] = 2
false_residual = D1 * false_I1 - I0 * D1
false_nonzero = [(i, j, int(false_residual[i, j]))
                 for i in range(false_residual.rows)
                 for j in range(false_residual.cols)
                 if false_residual[i, j] != 0]

checks = {
    "all_14_vertices_mapped": I0.rank() == 14,
    "all_21_edges_mapped": I1.rank() == 21,
    "all_9_faces_mapped": I2.rank() == 9,
    "top_cell_mapped": I3.rank() == 1,
    "edge_chain_identity": chain_residuals["edges"].is_zero_matrix,
    "face_chain_identity": chain_residuals["faces"].is_zero_matrix,
    "top_chain_identity": chain_residuals["top_cell"].is_zero_matrix,
    "augmentation_preserved": AUG * I0 == AUG,
    "kernel_zero_all_degrees": all(m.nullspace() == [] for m in (I0, I1, I2, I3)),
    "image_full_all_degrees": [m.rank() for m in (I0, I1, I2, I3)] == [14, 21, 9, 1],
    "completed_transport_all_edges": transport["checks"]["all_twenty_one_edge_ratios_defined"],
    "completed_transport_flat": transport["checks"]["all_face_holonomies_one"],
    "false_descent_has_two_endpoint_residuals": len(false_nonzero) == 2,
}

result = {
    "schema": "marici.figueiredo.coherent-resolution-maximal-free-flavor-presentation.v1",
    "finite_stage": "A3 at selected n=8 coefficient completion",
    "target": {
        "groups": {"F0": 14, "F1": 21, "F2": 9, "F3": 1},
        "generators": "one relabeled free generator f_x for every CR cell x",
        "differential": "the CR signed cellular differential under relabeling",
        "admissible_equivalences": "cellular boundary relations only",
        "augmentation": "every F0 generator maps to 1",
    },
    "map": "degreewise identity after x -> f_x",
    "kernel_ranks": [0, 0, 0, 0],
    "image_ranks": [14, 21, 9, 1],
    "augmented_homology_effect": "isomorphism 0 -> 0 in every degree",
    "coefficient_transport": "gauge-trivial rank-one coboundary on the free presentation",
    "false_descent": {
        "operation": "double the first edge while fixing vertices",
        "nonzero_residual_entries": false_nonzero,
    },
    "physical_comparison": {
        "status": "undefined",
        "missing_map": "A3 Carrier vertices to weak-basis Yukawa orbits",
        "physical16_faithfulness": "not composable with this presentation",
        "physical10_fibers": "not enumerable on this presentation",
    },
    "checks": checks,
    "passed": all(checks.values()),
    "claim_boundary": "Finite A3 free presentation only; no Carrier-to-Yukawa comparison map is asserted.",
}

out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["passed"]:
    raise SystemExit(1)
