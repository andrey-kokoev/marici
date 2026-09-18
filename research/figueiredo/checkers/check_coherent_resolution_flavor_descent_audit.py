import json
from pathlib import Path

root = Path(__file__).resolve().parents[3]
cr_path = root / "research/nima/results/a3-coherent-resolution.json"
wt_path = root / "research/nima/results/a3-physical-weight-transport.json"
out_path = root / "research/figueiredo/results/coherent-resolution-flavor-descent-audit.json"

cr = json.loads(cr_path.read_text(encoding="utf-8"))
wt = json.loads(wt_path.read_text(encoding="utf-8"))

basis = cr["basis"]
ranks = cr["ranks"]
total = wt["mutation_edges_total"]
determined = wt["edges_determined_by_positive_root_weights"]
residual = wt["edges_requiring_missing_coordinates"]

checks = {
    "source_complex_passed": cr["passed"] is True,
    "a3_basis_matches": basis == {
        "C0_clusters": 14,
        "C1_mutations": 21,
        "C2_faces": 9,
        "C3_polytope": 1,
    },
    "a3_ranks_match": ranks == {"d1": 13, "d2": 8, "d3": 1},
    "edge_partition_exact": determined + residual == total,
    "all_edges_not_determined": determined < total,
    "predicted_obstruction_nonzero": residual != 0,
    "predicted_obstruction_equals_fourteen": residual == 14,
    "three_boundary_coordinates_missing": len(wt["missing_negative_simple_diagonals"]) == 3,
}

result = {
    "schema": "marici.figueiredo.coherent-resolution-flavor-descent-audit.v1",
    "source_results": [str(cr_path.relative_to(root)), str(wt_path.relative_to(root))],
    "finite_stage": "A3",
    "source_basis": basis,
    "source_ranks": ranks,
    "edge_transport": {
        "total": total,
        "source_determined": determined,
        "undetermined": residual,
    },
    "deliberate_failure_test": {
        "proposition": "the six admitted positive-root weights determine all mutation edges",
        "predicted_nonzero_obstruction": "undetermined edge count",
        "observed_obstruction": residual,
        "failed_as_predicted": residual != 0,
    },
    "checks": checks,
    "passed": all(checks.values()),
    "claim_boundary": "Audits the admitted finite A3 source and coefficient coverage; no flavor target complex or Carrier-to-flavor chain map is supplied by these sources.",
    "first_missing_typed_object": "A labeled chain map from A3 triangulations/flips/cells to a declared flavor target complex with quotient and readout authority.",
}

out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
if not result["passed"]:
    raise SystemExit(1)
