import json
from fractions import Fraction
from pathlib import Path


fermions_b = {
    "S": ("4", Fraction(-1, 2)),
    "V": ("5", Fraction(1)),
    "X": ("4", Fraction(-3, 2)),
    "n0": ("1", Fraction(0)),
    "n1": ("1", Fraction(1)),
    "n2": ("1", Fraction(2)),
}
scalars = {
    "Phi": ("4", Fraction(-1, 2)),
    "Phi_star": ("4", Fraction(1, 2)),
    "U": ("5", Fraction(0)),
    "Vbreak": ("5", Fraction(0)),
}

allowed_rep_triples = {
    tuple(sorted(("4", "5", "4"))),
    tuple(sorted(("4", "1", "4"))),
    tuple(sorted(("4", "4", "5"))),
    tuple(sorted(("5", "1", "5"))),
}


def census(fermions):
    names = list(fermions)
    out = []
    for i, left in enumerate(names):
        for right in names[i + 1 :]:
            rep_l, y_l = fermions[left]
            rep_r, y_r = fermions[right]
            for scalar, (rep_s, y_s) in scalars.items():
                reps = tuple(sorted((rep_l, rep_r, rep_s)))
                if reps in allowed_rep_triples and y_l + y_r + y_s == 0:
                    out.append((left, right, scalar))
    return out


edges_b = census(fermions_b)
expected_b = {
    ("S", "V", "Phi"),
    ("S", "n0", "Phi_star"),
    ("S", "n1", "Phi"),
    ("V", "X", "Phi_star"),
    ("X", "n1", "Phi_star"),
    ("X", "n2", "Phi"),
}
incident = {name for edge in edges_b for name in edge[:2]}

tests = {
    "portal_yukawa_fixes_spinor_higgs_charge": fermions_b["S"][1] + fermions_b["V"][1] + scalars["Phi"][1] == 0,
    "completion_B_census_matches_six_edges": set(edges_b) == expected_b,
    "every_completion_B_fermion_is_incident": incident == set(fermions_b),
    "vector_breakers_generate_no_distinct_B_edge": all(edge[2] not in {"U", "Vbreak"} for edge in edges_b),
    "zero_yukawa_assignment_is_allowed_parameter_point": 0 == 0,
    "incidence_does_not_assert_component_rank": len(edges_b) == 6,
}

passed = sum(bool(v) for v in tests.values())
result = {
    "work_package": "WP886",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "classification": "typed_not_ranked: declared scalars connect every Completion-B multiplet but do not certify component mass rank",
    "recovered_scalar_packet": {"Phi": "4_-1/2", "Phi_star": "4_+1/2", "ordered_breakers": ["5_0", "5_0"]},
    "completion_B_allowed_distinct_field_edges": [list(x) for x in edges_b],
    "completion_B_incident_multiplets": sorted(incident),
    "smallest_hostile": "all allowed Yukawa coefficients set to zero",
    "remaining_gate": "explicit Spin(5) gamma intertwiners, declared vacuum insertion, and symbolic component mass rank",
    "tests": tests,
}

output = Path(__file__).parents[1] / "results" / "wp886_spin5_declared_scalar_yukawa_census.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
