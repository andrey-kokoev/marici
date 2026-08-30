"""Exact WP855 boundary-current contextual readout hierarchy."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    root2 = sp.sqrt(2)
    plus = sp.Matrix([1, -1])/root2
    minus = -plus
    absent = sp.zeros(2, 1)
    symmetric = sp.Matrix([1, 1])/root2
    sum_port = sp.Matrix([[1, 1]])
    difference_port = sp.Matrix([[1, -1]])
    reference = sp.Integer(1)
    states = {"plus": plus, "minus": minus, "absent": absent}
    sum_records = {name: sp.simplify((sum_port*state)[0]) for name, state in states.items()}
    difference_records = {
        name: sp.simplify((difference_port*state)[0]) for name, state in states.items()}
    difference_intensities = {name: sp.simplify(value**2)
                              for name, value in difference_records.items()}
    referenced_pairs = {
        name: (sp.simplify((reference+value)**2),
               sp.simplify((reference-value)**2))
        for name, value in difference_records.items()
    }
    loop_records = {
        name: sp.simplify(state[0]*state[1])
        for name, state in {**states, "symmetric": symmetric}.items()
    }
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("ordinary_sum_port_collapses_both_orientations_and_absence",
          len(set(sum_records.values())) == 1, sum_records)
    check("downstream_contact_cannot_repair_sum_port_kernel",
          all(value**2 == 0 for value in sum_records.values()), sum_records)
    check("loop_product_separates_symmetric_from_antisymmetric",
          loop_records["symmetric"] != loop_records["plus"], loop_records)
    check("loop_product_erases_boundary_orientation",
          loop_records["plus"] == loop_records["minus"], loop_records)
    check("difference_amplitude_separates_three_declared_states",
          len(set(difference_records.values())) == 3, difference_records)
    check("difference_intensity_erases_orientation_but_detects_presence",
          difference_intensities["plus"] == difference_intensities["minus"]
          and difference_intensities["plus"] != difference_intensities["absent"],
          difference_intensities)
    check("two_referenced_difference_settings_are_jointly_faithful",
          len(set(referenced_pairs.values())) == 3, referenced_pairs)
    check("referenced_pair_has_orientation_odd_difference",
          referenced_pairs["plus"][0]-referenced_pairs["plus"][1]
          == -(referenced_pairs["minus"][0]-referenced_pairs["minus"][1]),
          referenced_pairs)

    result = {
        "work_package": "WP855",
        "title": "Boundary-current readout hierarchy",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "state_domain": ["positive boundary orientation", "negative boundary orientation",
                         "absent boundary source"],
        "probe_partition": {
            "sum_contact": "one class containing all three states",
            "loop_product": "relative-parity classes; boundary orientations identified",
            "difference_intensity": "presence class plus absence; orientations identified",
            "referenced_difference_pair": "three singleton classes",
        },
        "first_nonfaithful_arrow": "two charged paths -> ordinary sum port",
        "smallest_exact_falsifier": "p=(1,-1)/sqrt(2) and p=0 both give zero sum-contact response",
        "groupoid_change": "coherent reference reduces the experiment to its phase stabilizer",
        "instrument_gate": "source-derived pre-projection difference channel and calibrated coherent reference",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp855_boundary_current_readout_hierarchy.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
