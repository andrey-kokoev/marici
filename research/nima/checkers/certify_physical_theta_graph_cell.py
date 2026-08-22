"""Certify the corrected disposition of the proposed P_02 filler.

The v1 packet conflated raw free rows with literal equation-(58) graph
generators. This aggregator preserves the valid rank observations but checks
the source typing before asserting a totalization.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RESULTS = ROOT / "research" / "nima" / "results"
OUT = RESULTS / "physical_theta_graph_cell_certificate.json"
DESIGNS = ((32003, 12, 6), (32003, 12, 7), (32009, 12, 6))


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    designs = []
    for prime, ambient, cutoff in DESIGNS:
        audit_path = RESULTS / (
            f"physical_theta_graph_typing_audit_p{prime}_a{ambient}_c{cutoff}.json"
        )
        connection_path = RESULTS / (
            f"physical_graph_cell_horizontality_p{prime}_a{ambient}_c{cutoff}.json"
        )
        audit = json.loads(audit_path.read_text(encoding="utf-8"))
        connection = json.loads(connection_path.read_text(encoding="utf-8"))
        assert audit["passed"] and connection["passed"]
        axis_signature = [
            {
                "axis": item["axis"],
                "equation58_simple_image_rank": item["equation58_simple_image_rank"],
                "actual_graph_boundary_rank": item["graph_boundary_rank"],
                "graph_projection_factorization_residual_rank": (
                    item["graph_projection_factorization_residual_rank"]
                ),
            }
            for item in audit["theta_image_comparison"]
        ]
        designs.append({
            "prime": prime,
            "ambient": ambient,
            "cutoff": cutoff,
            "sources": [
                {"path": str(audit_path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(audit_path)},
                {"path": str(connection_path.relative_to(ROOT)).replace("\\", "/"), "sha256": sha256(connection_path)},
            ],
            "raw_parity_block_rank": audit["raw_parity_block_rank"],
            "supported_graph_block_rank": audit["supported_graph_block_rank"],
            "raw_graph_combined_rank": audit["combined_rank"],
            "raw_graph_intersection_dimension": audit["intersection_dimension"],
            "actual_graph_is_single_parity_eigenspace": audit["graph_block_is_single_parity_eigenspace"],
            "axis_signature": axis_signature,
            "raw_projection_p02_is_horizontal": connection["p02_projection_is_horizontal"],
            "full_j3_projection_is_horizontal": connection["j3_projection_is_horizontal"],
            "raw_modular_covector_is_horizontal": connection["modular_line_is_horizontal"],
            "raw_p02_invariant_closure_dimension": connection[
                "minimal_invariant_source_closure_of_p02_dimension"
            ],
            "raw_projection_kernel_invariant_closure_dimension": connection[
                "invariant_closure_of_projection_kernel_dimension"
            ],
            "raw_modular_covector_dual_closure_dimension": connection[
                "minimal_dual_connection_closure_of_modular_covector_dimension"
            ],
        })

    signatures = {
        (
            item["raw_parity_block_rank"],
            item["supported_graph_block_rank"],
            item["raw_graph_combined_rank"],
            item["raw_graph_intersection_dimension"],
            tuple(
                (
                    axis["equation58_simple_image_rank"],
                    axis["actual_graph_boundary_rank"],
                    axis["graph_projection_factorization_residual_rank"],
                )
                for axis in item["axis_signature"]
            ),
            item["raw_projection_p02_is_horizontal"],
            item["full_j3_projection_is_horizontal"],
            item["raw_modular_covector_is_horizontal"],
            item["raw_p02_invariant_closure_dimension"],
            item["raw_projection_kernel_invariant_closure_dimension"],
            item["raw_modular_covector_dual_closure_dimension"],
        )
        for item in designs
    }
    assert len(signatures) == 1
    assert next(iter(signatures)) == (
        2, 2, 4, 0,
        ((1, 1, 1), (1, 1, 1)),
        False, False, False, 6, 9, 6,
    )

    packet = {
        "schema": "marici.physical-theta-graph-cell-certificate.v2",
        "supersedes_schema": "marici.physical-theta-graph-cell-certificate.v1",
        "designs": designs,
        "stable_typing_signature": {
            "raw_parity_and_supported_graph_blocks_are_disjoint": True,
            "raw_parity_and_supported_graph_blocks_have_same_rank_but_are_not_equal": True,
            "equation58_simple_sector_has_nonzero_theta_rank": 1,
            "actual_graph_projection_factorization_residual_rank_per_axis": [1, 1],
            "raw_projection_kernel_closes_to_all_of_a9": True,
            "raw_modular_line_is_nonhorizontal": True,
        },
        "surviving_observations": {
            "raw_free_basis_theta_support": [6, 8],
            "raw_free_basis_covector": [3, 0, 121],
            "bundled_raw_theta_rank": 1,
            "coefficient_target_rank_across_axes": 2,
            "warning": "these are raw-basis facts, not a graph-cell factorization",
        },
        "rejected_claims": [
            "the moving checker kernel rows are the literal equation-(58) graph generators",
            "the supported graph pair P_02 is the raw (1,0) parity eigenspace",
            "Theta=(Theta composed with i) composed with pi_J",
            "the displayed first-jet P_02 totalization has square zero",
            "the covector (3,0,121) defines a horizontal graph line",
        ],
        "corrected_disposition": (
            "The proposed P_02 filler is mistyped already at first jet. Its h_02 and pi_02 "
            "do not define the claimed source-derived bicomplex, so canonical mixed second "
            "derivatives and a dx wedge dy square cannot be formed from this candidate."
        ),
        "no_fit_rule": (
            "No higher cell is introduced to repair a candidate whose first vertical/horizontal typing fails."
        ),
        "scope": (
            "finite-field finite-cutoff no-go for this P_02 construction; it does not rule out "
            "a different independently derived relative-support complex"
        ),
        "passed": True,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
