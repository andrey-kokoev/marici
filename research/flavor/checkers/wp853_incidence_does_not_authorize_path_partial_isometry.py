"""Exact WP853 nonfaithfulness audit from finite path to incidence packet."""

import json
from pathlib import Path
import sympy as sp


def weighted_shift(a, b, c):
    matrix = sp.zeros(4)
    matrix[1, 0], matrix[2, 1], matrix[3, 2] = a, b, c
    return matrix


def main() -> None:
    N = sp.diag(0, 1, 2, 3)
    q = sp.Matrix([1, 2, 3])
    B = sp.Matrix([[2, -1, 0], [3, 0, -1]])
    P3 = sp.diag(0, 0, 0, 1)
    I = sp.eye(4)
    canonical = weighted_shift(1, 1, 1)
    hostile = weighted_shift(1, 2, 1)
    a, b, c = sp.symbols("a b c", positive=True)
    general = weighted_shift(a, b, c)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("path_number_spectrum_generates_wp820_charge_ray",
          sp.Matrix([N[j, j] for j in range(1, 4)]) == q, q)
    check("wp820_incidence_annihilates_path_charge_ray", B*q == sp.zeros(2, 1), B*q)
    check("path_charge_ray_has_wp820_cubic_record", sum(x**3 for x in q) == 36,
          sum(x**3 for x in q))
    check("all_positive_weighted_shifts_have_degree_one",
          N*general-general*N == general, N*general-general*N)
    check("weighted_shift_family_has_same_cyclic_support",
          sp.Matrix.hstack(*[(general**j)*sp.Matrix([1, 0, 0, 0]) for j in range(4)]).det()
          == a**3*b**2*c, a**3*b**2*c)
    check("incidence_and_inflow_are_independent_of_path_weights",
          not ({a, b, c} & (set(B.free_symbols) | set(q.free_symbols))),
          {"incidence": B, "charges": q, "inflow": 36})
    canonical_gram = canonical.T*canonical
    hostile_gram = hostile.T*hostile
    check("hostile_pair_has_distinct_singular_value_records",
          canonical_gram.eigenvals() != hostile_gram.eigenvals(),
          {"canonical": canonical_gram.eigenvals(), "hostile": hostile_gram.eigenvals()})
    check("canonical_shift_satisfies_partial_isometry_relation",
          canonical_gram == I-P3, canonical_gram)
    check("hostile_shift_fails_partial_isometry_relation",
          hostile_gram != I-P3, hostile_gram)
    check("number_preserving_unitaries_cannot_remove_weight_hostile",
          sorted(canonical_gram.eigenvals().keys())
          != sorted(hostile_gram.eigenvals().keys()),
          {"canonical_spectrum": sorted(canonical_gram.eigenvals().keys()),
           "hostile_spectrum": sorted(hostile_gram.eigenvals().keys())})

    result = {
        "work_package": "WP853",
        "title": "Incidence does not authorize the path partial isometry",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_domain": "positive weighted degree-one shifts on the four-vertex charged path",
        "faithful_coordinate": "three path singular values modulo number-preserving unitaries",
        "authorized_probe_family": ["primitive charge ray", "integer incidence", "cubic inflow"],
        "contextual_partition": "one class containing the full positive three-weight fiber",
        "first_nonfaithful_arrow": "(N,T,e0) -> (q,B,k=36)",
        "smallest_hostile_pair": ["T(1,1,1)", "T(1,2,1)"],
        "classification": "WP852 is a selector only after adding the partial-isometry source relation",
        "remaining_gate": "derive T^*T=I-P3 microscopically or instrument T^*T in the physical16 frame",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp853_incidence_does_not_authorize_path_partial_isometry.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
