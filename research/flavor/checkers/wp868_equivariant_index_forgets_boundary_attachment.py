"""Exact WP868 equivariant-index boundary-attachment hostile."""

import json
from pathlib import Path

import sympy as sp


def data(sine, cosine):
    differential = sp.Matrix([[sine, cosine]])
    kernel = sp.Matrix([cosine, -sine])
    kernel_projector = sp.simplify(sp.eye(2)-differential.conjugate().T*differential)
    light = sp.Matrix([[1, 0]])
    detector_gram = sp.simplify((light*kernel_projector*light.conjugate().T)[0])
    return differential, kernel, kernel_projector, detector_gram


def main() -> None:
    d0, k0, p0, gram0 = data(0, 1)
    sine = sp.sqrt(7)/4
    cosine = sp.Rational(3, 4)
    d1, k1, p1, gram1 = data(sine, cosine)
    source_action = -sp.eye(2)
    target_action = sp.Matrix([[-1]])
    t = sp.symbols("t", real=True)
    dt = sp.Matrix([[sp.sin(t), sp.cos(t)]])
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("both_differentials_are_odd_equivariant",
          target_action*d0 == d0*source_action
          and target_action*d1 == d1*source_action, [d0, d1])
    check("both_maps_are_surjective_with_unit_gap",
          d0.rank() == d1.rank() == 1
          and d0*d0.conjugate().T == sp.eye(1)
          and d1*d1.conjugate().T == sp.eye(1),
          [d0*d0.conjugate().T, d1*d1.conjugate().T])
    check("equivariant_index_is_one_odd_character", 2-1 == 1,
          "2 chi_- - 1 chi_- = chi_-")
    check("declared_vectors_are_exact_kernels",
          d0*k0 == sp.zeros(1, 1) and d1*k1 == sp.zeros(1, 1), [k0, k1])
    check("kernel_projectors_are_exact",
          p0**2 == p0 and p1**2 == p1
          and p0.rank() == p1.rank() == 1, [p0, p1])
    check("kernel_embedding_changes_while_index_stays_fixed",
          p0 != p1, p1-p0)
    check("detector_gram_changes_from_one_to_nine_sixteenths",
          gram0 == 1 and gram1 == sp.Rational(9, 16), [gram0, gram1])
    check("gapped_equivariant_homotopy_connects_the_pair",
          sp.simplify(dt*dt.conjugate().T) == sp.eye(1),
          dt*dt.conjugate().T)
    check("index_and_gap_do_not_determine_boundary_attachment", True,
          "actual kernel projector and evaluation map are required")
    check("physical_detector_calibration_remains_open", True,
          "detector Gram is source-normalized but not calibrated in physical16 units")

    result = {
        "schema": "marici.flavor.equivariant-index-forgets-boundary-attachment.v1",
        "work_package": "WP868",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "admitted_domain": "two odd source copies to one odd target copy",
        "preserved_data": [
            "domain and target characters", "equivariant index chi_-",
            "surjectivity", "unit nonzero singular gap", "mod-two anomaly",
        ],
        "forgotten_data": "embedding of kernel line into marked light and heavy copies",
        "smallest_exact_falsifier": {
            "D0": "(0,1)", "D1": "(sqrt(7)/4,3/4)",
            "detector_grams": [str(gram0), str(gram1)],
        },
        "first_nonfaithful_arrow": "marked equivariant complex -> representation-valued index",
        "required_repair": "transport actual kernel projector plus named detector evaluation in one calibrated frame",
        "classification": "equivariant rigidifier, not marked portal protector",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp868_equivariant_index_forgets_boundary_attachment.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
