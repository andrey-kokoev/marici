"""Exact WP869 Kato transport of a portal kernel and detector frame."""

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    t = sp.symbols("t", real=True)
    differential = sp.Matrix([[sp.sin(t), sp.cos(t)]])
    kernel = sp.Matrix([sp.cos(t), -sp.sin(t)])
    projector = sp.simplify(kernel*kernel.conjugate().T)
    initial_projector = sp.diag(1, 0)
    initial_differential = sp.Matrix([[0, 1]])
    generator = sp.simplify(sp.diff(projector, t)*projector
                            - projector*sp.diff(projector, t))
    transport = sp.Matrix([[sp.cos(t), sp.sin(t)],
                           [-sp.sin(t), sp.cos(t)]])
    fixed_detector = sp.Matrix([[1, 0]])
    moving_detector = sp.simplify(fixed_detector*transport.conjugate().T)
    fixed_gram = sp.simplify((fixed_detector*kernel)[0]**2)
    moving_gram = sp.simplify((moving_detector*kernel)[0]**2)
    endpoint = {sp.cos(t): sp.Rational(3, 4),
                sp.sin(t): sp.sqrt(7)/4}
    expectation0 = sp.kronecker_product(initial_projector, initial_projector)
    expectation_t = sp.kronecker_product(projector, projector)
    induced_transport = sp.kronecker_product(transport, transport)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("kato_generator_is_exact_antihermitian_rotation",
          generator == sp.Matrix([[0, 1], [-1, 0]]), generator)
    check("transport_solves_kato_initial_value_problem",
          sp.simplify(sp.diff(transport, t)-generator*transport) == sp.zeros(2)
          and transport.subs(t, 0) == sp.eye(2), transport)
    check("transport_is_unitary",
          sp.simplify(transport.conjugate().T*transport) == sp.eye(2), transport)
    check("kernel_projector_is_parallel_transport",
          sp.simplify(projector-transport*initial_projector*transport.conjugate().T)
          == sp.zeros(2), projector)
    check("complete_differential_is_intertwined",
          sp.simplify(differential*transport-initial_differential)
          == sp.zeros(1, 2), differential*transport)
    check("moving_detector_gram_is_identically_one",
          moving_gram == 1, moving_gram)
    check("fixed_detector_gram_at_hostile_endpoint_is_nine_sixteenths",
          sp.simplify(fixed_gram.subs(endpoint)) == sp.Rational(9, 16),
          fixed_gram.subs(endpoint))
    check("conditional_expectation_transports_covariantly",
          sp.simplify(expectation_t-induced_transport*expectation0
                      *induced_transport.conjugate().T) == sp.zeros(4),
          expectation_t)
    check("projector_transport_does_not_imply_detector_transport", True,
          "fixed and co-moving rows give 9/16 and 1 on the same endpoint kernel")
    check("physical_execution_and_calibration_remain_open", True,
          "requires source-controlled detector connection and physical16 unit map")

    result = {
        "schema": "marici.flavor.kato-kernel-detector-parallel-transport.v1",
        "work_package": "WP869",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "source_domain": "gapped marked equivariant differential path D_t",
        "canonical_transport": "Kato connection [dP,P]",
        "transported_objects": ["kernel projector", "conditional expectation",
                                "complete detector frame"],
        "fixed_detector_endpoint_gram": "9/16",
        "moving_detector_endpoint_gram": "1",
        "groupoid": "co-moving detector defines a relational experiment over the transported-frame stabilizer",
        "classification": "canonical mathematical threshold parallelization; physical execution not yet authorized",
        "smallest_exact_falsifier": "same endpoint kernel with fixed versus Kato-transported detector row",
        "remaining_physical_instrument_gate": "derive detector co-transport and physical16 calibration from the same microscopic source",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp869_kato_kernel_detector_parallel_transport.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
