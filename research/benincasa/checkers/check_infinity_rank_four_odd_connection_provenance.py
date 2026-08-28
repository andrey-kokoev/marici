import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "results" / "infinity-rank-four-odd-connection-provenance.json"


def main() -> None:
    data = json.loads(PACKET.read_text(encoding="utf-8"))
    checks = {
        "basis_is_full_odd_relative_basis": data["ordered_basis"]
        == ["qS0", "qSinf", "h1", "h2"],
        "joint_covector_is_primitive": data["source_joint_covector"]
        == [-1, 1, 1, 1],
        "endpoint_splitter_is_available": data["available_source_data"][
            "principal_endpoint_splitter"
        ],
        "elliptic_block_is_available": data["available_source_data"][
            "elliptic_gauss_manin_block"
        ],
        "both_base_connection_matrices_are_missing": all(
            data["missing_common_frame_data"][key]
            for key in ("rank_four_connection_x", "rank_four_connection_y")
        ),
        "mixed_blocks_are_missing": all(
            data["missing_common_frame_data"][key]
            for key in ("endpoint_to_elliptic_block", "elliptic_to_endpoint_block")
        ),
        "horizontality_is_not_claimed": data["typed_conclusion"][
            "static_joint_covector_is_horizontal"
        ]
        == "not_established",
        "quartic_is_not_inferred": data["typed_conclusion"]["quartic_support"]
        == "not_testable_from_static_joint_covector",
    }
    failed = [name for name, passed in checks.items() if not passed]
    print(json.dumps({"checks": checks, "passed": len(checks) - len(failed), "total": len(checks)}, indent=2))
    if failed:
        raise SystemExit("failed: " + ", ".join(failed))


if __name__ == "__main__":
    main()
