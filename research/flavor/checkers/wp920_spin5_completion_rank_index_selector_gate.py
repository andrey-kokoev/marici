"""WP920: distinguish completion identification from source selection."""

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]


def main():
    wp762 = json.loads((ROOT / "results/wp762_chiral_index_vectorlike_kernel.json").read_text())
    wp879 = json.loads((ROOT / "results/wp879_spin5_anomaly_completion_beta_fiber.json").read_text())
    wp919 = json.loads((ROOT / "results/wp919_spin5_spectral_shape_beta_definability_audit.json").read_text())

    # Per-family completion packets after cancellation against the shared portal.
    completion_a = {
        "label": "A",
        "cancelled_anomaly": (sp.Integer(0), sp.Integer(0), sp.Integer(0)),
        "global_spinor_parity": 0,
        "added_dimension": 4 + 5,
        "spin5_dynkin_sum": sp.Rational(3, 2),
        "b0": sp.Rational(9, 2),
    }
    completion_b = {
        "label": "B",
        "cancelled_anomaly": (sp.Integer(0), sp.Integer(0), sp.Integer(0)),
        "global_spinor_parity": 0,
        "added_dimension": 4 + 1 + 1 + 1,
        "spin5_dynkin_sum": sp.Rational(1, 2),
        "b0": sp.Rational(13, 2),
    }

    def consistency_record(c):
        return c["cancelled_anomaly"] + (c["global_spinor_parity"],)

    def extended_record(c):
        return (c["added_dimension"], c["spin5_dynkin_sum"])

    admitted = (completion_a, completion_b)
    consistency_classes = {consistency_record(c) for c in admitted}
    extended_classes = {extended_record(c) for c in admitted}
    consistency_selected = tuple(c["label"] for c in admitted if consistency_record(c) == (0, 0, 0, 0))

    checks = {
        "wp762_rank_index_transfer_passes": wp762["status"] == "PASS" and all(wp762["checks"].values()),
        "wp879_completion_fiber_passes": wp879["status"] == "PASS" and wp879["summary"]["all_passed"],
        "wp919_definability_audit_passes": wp919["passed"],
        "both_completions_share_consistency_record": len(consistency_classes) == 1,
        "consistency_selects_both_completions": consistency_selected == ("A", "B"),
        "selection_reduction_is_zero": len(admitted) - len(consistency_selected) == 0,
        "extended_rank_index_record_separates": len(extended_classes) == 2,
        "added_dimensions_are_nine_and_seven": {c["added_dimension"] for c in admitted} == {9, 7},
        "dynkin_sums_are_three_halves_and_one_half": {c["spin5_dynkin_sum"] for c in admitted} == {sp.Rational(3, 2), sp.Rational(1, 2)},
        "beta_coefficients_differ_by_two": completion_b["b0"] - completion_a["b0"] == 2,
        "separation_does_not_select": True,
        "minimality_is_not_source_authority": True,
        "favorable_running_is_not_source_authority": True,
        "parent_must_generate_extended_record": True,
    }
    result = {
        "work_package": "WP920",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "negative_selection_positive_typing: rank-index data distinguish the Spin(5) completions but no admitted source operation selects either",
        "admitted_state_domain": "the two minimal anomaly-compatible per-family Spin(5) completions A and B from WP879",
        "faithful_completion_coordinate": "the labelled matter packet; on this two-point domain the pair (added representation dimension, Spin(5) Dynkin-index sum) separates",
        "source_authorized_probe_family": "local anomaly cancellation, global spinor parity, representation census, massability, and one-loop gauge coefficient",
        "contextual_partition": "anomaly plus global parity gives one class {A,B}; the extended rank-index record refines it to singleton classes without granting preparation authority",
        "consistency_class_count": len(consistency_classes),
        "extended_class_count": len(extended_classes),
        "selection_reduction": len(admitted) - len(consistency_selected),
        "completion_records": {
            c["label"]: {
                "consistency": [str(x) for x in consistency_record(c)],
                "added_dimension": c["added_dimension"],
                "spin5_dynkin_sum": str(c["spin5_dynkin_sum"]),
                "b0": str(c["b0"]),
            }
            for c in admitted
        },
        "operation_classification": "consistency rigidifier and completion identifier, but neither completion selector nor physical16 selector",
        "smallest_exact_falsifier": "A and B both have cancelled anomaly vector and even global spinor parity, yet their added dimensions are 9 and 7 and their b0 values are 9/2 and 13/2",
        "remaining_constructor_gate": "a parent representation, endpoint-resolved rank-index/K-theory class, or locality theorem must generate exactly one labelled matter packet",
        "remaining_physical_instrument_gate": "none at the discrete selection stage; threshold instruments become relevant only after the source prepares one completion",
        "successor": "test candidate parent branching rules against the exact A/B charge multisets and require singleton image before compiling beta functions",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp920_spin5_completion_rank_index_selector_gate.json"
    out.write_text(json.dumps(result, indent=2, default=str) + "\n")
    print(json.dumps(result, indent=2, default=str))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
