import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
RESULT = ROOT / "research/nima/results/cross_sector_constructor_instrument_theorem.json"


def main() -> None:
    packet = json.loads(RESULT.read_text(encoding="utf-8"))
    gates = {
        "schema": packet["schema"] == "marici.cross-sector-constructor-instrument.v1",
        "six_vocabulary_types": set(packet["vocabulary"]) == {
            "substrate", "operation", "readout", "instrument", "constructor", "source_authority"
        },
        "joint_faithfulness_is_categorical": packet["categorical"]["joint_faithfulness"] == "joint_monicity_after_descent",
        "repeatability_is_idempotent": packet["categorical"]["repeatability"] == "idempotent_task",
        "stabilization_is_split": packet["categorical"]["stabilization"] == "split_idempotent_with_resource_return",
        "faithfulness_separation": packet["separation_theorems"]["faithful_readout_implies_constructibility"] is False,
        "controllability_separation": packet["separation_theorems"]["algebraic_controllability_implies_instrument"] is False,
        "four_sectors": set(packet["sectors"]) == {"qed_scattering", "flavor", "d_s3_topology", "radiative_string"},
        "qed_positive": packet["sectors"]["qed_scattering"]["positive_source_instrument"] is True,
        "three_distinct_failures": len({packet["sectors"][s]["first_failed_arrow"] for s in ("flavor", "d_s3_topology", "radiative_string")}) == 3,
        "four_hostile_tests": set(packet["hostile_tests"]) == {"fitted_selector", "undeclared_reference", "arbitrary_dilation", "type_erased_projection"},
        "hostile_tests_rejected": all(v == "rejected" for v in packet["hostile_tests"].values()),
        "common_lift_not_common_instrument": packet["categorical"]["common_higher_operation"] == "authority_indexed_realization_and_lift" and packet["universal_physical_instrument"] == "not_established",
    }
    failed = [name for name, passed in gates.items() if not passed]
    print(json.dumps({"gates": gates, "passed": len(gates) - len(failed), "total": len(gates), "failed": failed}, indent=2))
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
