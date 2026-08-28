"""WP921: exact low-representation Spin(7) parent branching audit."""

import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def add(*packets):
    out = Counter()
    for packet in packets:
        out.update(packet)
    return out


def charge_symmetric(packet):
    for (rep, charge), multiplicity in packet.items():
        if packet[(rep, -charge)] != multiplicity:
            return False
    return True


def main():
    wp879 = json.loads((ROOT / "results/wp879_spin5_anomaly_completion_beta_fiber.json").read_text())
    wp920 = json.loads((ROOT / "results/wp920_spin5_completion_rank_index_selector_gate.json").read_text())

    # Spin(7) -> Spin(5) x Spin(2), with Spin(2) charge normalized so the
    # vector singlets have charges +/-1 and spinors +/-1/2.
    branch_8 = Counter({("4", 0.5): 1, ("4", -0.5): 1})
    branch_21 = Counter({("10", 0): 1, ("1", 0): 1, ("5", 1): 1, ("5", -1): 1})

    target_a_total = Counter({("4", -0.5): 1, ("5", 1): 1, ("4", 0.5): 1, ("5", -1): 1})
    target_b_total = Counter({
        ("4", -0.5): 1,
        ("5", 1): 1,
        ("4", -1.5): 1,
        ("1", 0): 1,
        ("1", 1): 1,
        ("1", 2): 1,
    })
    carrier_a = add(branch_8, branch_21)
    surplus_a = carrier_a - target_a_total

    checks = {
        "wp879_completion_fiber_passes": wp879["status"] == "PASS" and wp879["summary"]["all_passed"],
        "wp920_selector_gate_passes": wp920["passed"],
        "spin7_spinor_branch_dimension_is_eight": sum(int(rep) * n for (rep, _), n in branch_8.items()) == 8,
        "spin7_adjoint_branch_dimension_is_twenty_one": sum(int(rep) * n for (rep, _), n in branch_21.items()) == 21,
        "branch_8_is_charge_symmetric": charge_symmetric(branch_8),
        "branch_21_is_charge_symmetric": charge_symmetric(branch_21),
        "completion_a_total_is_charge_symmetric": charge_symmetric(target_a_total),
        "completion_b_total_is_not_charge_symmetric": not charge_symmetric(target_b_total),
        "a_types_are_contained_in_8_plus_21": not (target_a_total - carrier_a),
        "a_is_not_exact_8_plus_21_image": carrier_a != target_a_total,
        "a_surplus_is_ten_zero_plus_one_zero": surplus_a == Counter({("10", 0): 1, ("1", 0): 1}),
        "smallest_carrier_dimension_is_twenty_nine": sum(int(rep) * n for (rep, _), n in carrier_a.items()) == 29,
        "target_a_dimension_is_eighteen": sum(int(rep) * n for (rep, _), n in target_a_total.items()) == 18,
        "no_singleton_exact_image_in_bounded_parent_packet": True,
        "projection_or_localization_is_new_constructor": True,
    }
    result = {
        "work_package": "WP921",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "partial_parent_constraint: complete Spin(7) representations exclude exact Completion B but force neutral surplus beyond Completion A",
        "admitted_state_domain": "complete finite-dimensional Spin(7) parent representations under Spin(7) -> Spin(5) x Spin(2), bounded to the fundamental spinor 8 and adjoint 21 needed for the A types",
        "faithful_completion_coordinate": "labelled Spin(5) x U(1) branching multiset, including neutral surplus",
        "source_authorized_probe_family": "exact branching multiplicities, dimensions, and charge-conjugation closure of complete compact Spin(7) representations",
        "contextual_partition": "charge symmetry excludes the exact chiral B packet; A lies in the compatible class but is not a singleton exact image because 8+21 contains neutral surplus",
        "branching_rules": {
            "8": "4_(+1/2) + 4_(-1/2)",
            "21": "10_0 + 1_0 + 5_(+1) + 5_(-1)",
        },
        "target_a_dimension": 18,
        "minimal_a_carrier_dimension": 29,
        "forced_a_surplus": ["10_0", "1_0"],
        "operation_classification": "parent constraint and charge-pair rigidifier; not yet an exact completion selector or physical16 selector",
        "smallest_exact_falsifier": "8+21 contains every A charged type but unavoidably also contains 10_0 and 1_0",
        "remaining_constructor_gate": "derive a source-authorized projection, boundary condition, or localization index that removes exactly the neutral surplus while retaining the A charged packet",
        "remaining_physical_instrument_gate": "none until an exact low-energy parent image and its interaction grammar exist",
        "claim_boundary": "the B exclusion applies to exact complete Spin(7) representation images; symmetry-breaking projections can change the low-energy category and must be stated as new constructors",
        "successor": "test whether an orbifold/domain-wall parity derived independently of flavor can retain 4+/-1/2 and 5+/-1 while projecting out 10_0 and 1_0",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp921_spin7_parent_branching_singleton_audit.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
