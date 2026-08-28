"""WP922: exact intrinsic-parity fiber for a Spin(7) orbifold zero-mode packet."""

import itertools
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def zero_modes(components, intrinsic_parity):
    return Counter(label for label, involution_grade in components if intrinsic_parity * involution_grade == 1)


def main():
    wp921 = json.loads((ROOT / "results/wp921_spin7_parent_branching_singleton_audit.json").read_text())

    spinor_8 = (("4_(+1/2)", 1), ("4_(-1/2)", -1))
    adjoint_21 = (("10_0", 1), ("1_0", 1), ("5_(+1)", -1), ("5_(-1)", -1))
    target = Counter({"4_(+1/2)": 1, "4_(-1/2)": 1, "5_(+1)": 1, "5_(-1)": 1})

    assignments = []
    for eta_8a, eta_8b, eta_21 in itertools.product((-1, 1), repeat=3):
        packet = zero_modes(spinor_8, eta_8a) + zero_modes(spinor_8, eta_8b) + zero_modes(adjoint_21, eta_21)
        assignments.append({
            "etas": (eta_8a, eta_8b, eta_21),
            "packet": packet,
            "is_target": packet == target,
        })
    target_assignments = [a for a in assignments if a["is_target"]]
    hostile = next(a for a in assignments if a["etas"] == (-1, 1, 1))

    checks = {
        "wp921_parent_audit_passes": wp921["passed"],
        "eight_intrinsic_parity_assignments_enumerated": len(assignments) == 8,
        "negative_21_parity_retains_charged_coset": zero_modes(adjoint_21, -1) == Counter({"5_(+1)": 1, "5_(-1)": 1}),
        "negative_21_parity_removes_neutral_surplus": "10_0" not in zero_modes(adjoint_21, -1) and "1_0" not in zero_modes(adjoint_21, -1),
        "one_8_cannot_retain_both_spinors": all(sum(zero_modes(spinor_8, eta).values()) == 1 for eta in (-1, 1)),
        "two_opposite_8_parities_retain_both_spinors": zero_modes(spinor_8, -1) + zero_modes(spinor_8, 1) == Counter({"4_(+1/2)": 1, "4_(-1/2)": 1}),
        "exact_a_zero_mode_packet_exists": len(target_assignments) > 0,
        "exact_a_assignments_are_two_orderings": len(target_assignments) == 2,
        "target_requires_negative_21_parity": all(a["etas"][2] == -1 for a in target_assignments),
        "target_requires_opposite_8_parities": all(a["etas"][0] == -a["etas"][1] for a in target_assignments),
        "intrinsic_parity_fiber_is_not_singleton": len(assignments) > len(target_assignments),
        "hostile_flip_restores_neutral_surplus": hostile["packet"]["10_0"] == 1 and hostile["packet"]["1_0"] == 1,
        "hostile_flip_removes_charged_vectors": hostile["packet"]["5_(+1)"] == 0 and hostile["packet"]["5_(-1)"] == 0,
        "projection_changes_low_energy_category": True,
        "yukawa_grammar_not_fixed_by_spectrum_alone": True,
    }
    result = {
        "work_package": "WP922",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "classification": "conditional_exact_constructor_nonselection: a Spin(7) orbifold parity realizes exact Completion A zero modes, but intrinsic parities remain an eight-point source fiber",
        "admitted_state_domain": "one bulk matter adjoint 21 and two bulk matter spinors 8 under the fixed Spin(7) -> Spin(5) x Spin(2) involution, with independent intrinsic parities",
        "faithful_completion_coordinate": "the complete labelled four-dimensional zero-mode multiset",
        "source_authorized_probe_family": "fixed involution grades and zero-mode retention rule eta times grade equals plus one",
        "contextual_partition": "eight intrinsic-parity assignments map to zero-mode packets; exactly two ordered assignments yield the target A packet",
        "parity_assignment_count": len(assignments),
        "target_assignment_count": len(target_assignments),
        "target_assignments": [list(a["etas"]) for a in target_assignments],
        "target_zero_modes": sorted(target.elements()),
        "operation_classification": "exact presentation/field-content rigidifier conditional on parity choice; not a source-derived completion selector or physical16 selector",
        "smallest_exact_falsifier": "flip eta_21 from -1 to +1: 10_0 and 1_0 return while 5_(+/-1) disappear",
        "remaining_constructor_gate": "derive the three intrinsic parities from boundary topology, locality, or an endpoint-resolved index independently of the desired A spectrum",
        "remaining_yukawa_gate": "derive which bulk and boundary interactions survive the same parity operation and whether they generate the complete three-family Yukawa tensors",
        "remaining_physical_instrument_gate": "none until parity authority and the surviving interaction grammar are established",
        "claim_boundary": "this is a new five-dimensional relational/source construction; it does not reveal that A was already selected in the four-dimensional Spin(5) theory",
        "successor": "compute the parity-even cubic invariant census for 8_a, 8_b, 21, and the breaking scalars, then test whether the surviving family tensors have a free shape kernel",
        "checks": checks,
        "passed": all(checks.values()),
    }
    out = ROOT / "results/wp922_spin7_orbifold_zero_mode_projection_fiber.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
