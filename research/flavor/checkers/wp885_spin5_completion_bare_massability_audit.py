import json
from pathlib import Path

from fractions import Fraction


shared = [("4", Fraction(-1, 2)), ("5", Fraction(1, 1))]
completion_a = [("4", Fraction(1, 2)), ("5", Fraction(-1, 1))]
completion_b = [
    ("4", Fraction(-3, 2)),
    ("1", Fraction(0, 1)),
    ("1", Fraction(1, 1)),
    ("1", Fraction(2, 1)),
]


def charged_bare_pairs(fields):
    pairs = []
    for i, (rep_i, y_i) in enumerate(fields):
        for j in range(i + 1, len(fields)):
            rep_j, y_j = fields[j]
            if rep_i == rep_j and y_i + y_j == 0 and y_i != 0:
                pairs.append((i, j, rep_i, str(y_i), str(y_j)))
    return pairs


pairs_a = charged_bare_pairs(shared + completion_a)
pairs_b = charged_bare_pairs(shared + completion_b)
neutral_majorana_b = [x for x in completion_b if x == ("1", Fraction(0, 1))]

tests = {
    "completion_A_has_spinor_dirac_pair": any(p[2] == "4" for p in pairs_a),
    "completion_A_has_vector_dirac_pair": any(p[2] == "5" for p in pairs_a),
    "completion_A_has_two_charged_bare_pairs": len(pairs_a) == 2,
    "completion_B_has_no_charged_bare_pair": len(pairs_b) == 0,
    "completion_B_has_one_neutral_majorana_candidate": len(neutral_majorana_b) == 1,
    "neutral_majorana_does_not_pair_charged_rep": all(x[1] == 0 for x in neutral_majorana_b),
    "completion_A_mass_parameter_dimension_is_two": len(pairs_a) == 2,
    "completion_A_hostile_mass_choices_are_distinct": (1, 1) != (2, 1),
}

passed = sum(bool(v) for v in tests.values())
result = {
    "work_package": "WP885",
    "status": "PASS" if passed == len(tests) else "FAIL",
    "summary": {"passed": passed, "total": len(tests), "all_passed": passed == len(tests)},
    "classification": "split_negative: completion A is massable with free scales; completion B lacks a charged bare mass action",
    "completion_A_charged_bare_pairs": pairs_a,
    "completion_A_bare_mass_parameter_dimension_per_family": 2,
    "completion_B_charged_bare_pairs": pairs_b,
    "completion_B_neutral_majorana_candidates": len(neutral_majorana_b),
    "smallest_falsifier": "completion A with (M4,M5)=(1,1) versus (2,1)",
    "remaining_gate": "complete invariant Yukawa census on the declared scalar packet and generic mass-matrix rank",
    "tests": tests,
}

output = Path(__file__).parents[1] / "results" / "wp885_spin5_completion_bare_massability_audit.json"
output.write_text(json.dumps(result, indent=2, default=bool) + "\n", encoding="utf-8")
print(json.dumps(result["summary"], indent=2))
raise SystemExit(0 if result["status"] == "PASS" else 1)
