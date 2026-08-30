"""Exact WP860 reducing-subspace threshold survival audit."""

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    root2 = sp.sqrt(2)
    c, s = sp.symbols("c s", real=True)
    rotation = sp.Matrix([[c, 0, -s], [0, 1, 0], [s, 0, c]])
    A = rotation[:2, :2]
    C = rotation[2:, :2]
    light_projector = sp.diag(1, 1, 0)
    hostile = rotation.subs({c: sp.Rational(3, 4), s: sp.sqrt(7)/4})
    hostile_A = hostile[:2, :2]
    hostile_C = hostile[2:, :2]
    dark = sp.Matrix([-1, 1])/root2
    common = sp.Matrix([[1, 1]])/root2
    difference = sp.Matrix([[-1, 1]])/root2
    junction = sp.Matrix.vstack(common, difference)
    q = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)],
                   [sp.Rational(4, 5), sp.Rational(3, 5)]])
    safe = sp.diag(1, 1, 1)
    safe[:2, :2] = q
    transported_dark = q*dark
    transported_common = common*q.T
    transported_difference = difference*q.T
    transported_junction = junction*q.T
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition), "evidence": str(evidence)})

    check("unitary_block_identity_localizes_light_defect",
          sp.simplify((A.T*A+C.T*C).subs(c**2, 1-s**2)) == sp.eye(2),
          A.T*A+C.T*C)
    check("light_compression_is_isometric_only_without_heavy_leakage",
          sp.solve(list(A.T*A-sp.eye(2)), [c], dict=True) == [{c: -1}, {c: 1}],
          A.T*A)
    check("reducing_projector_commutes_only_when_mixing_vanishes",
          (rotation*light_projector-light_projector*rotation).subs(s, 0) == sp.zeros(3)
          and rotation*light_projector-light_projector*rotation != sp.zeros(3),
          rotation*light_projector-light_projector*rotation)
    check("hostile_full_threshold_is_exactly_unitary", hostile.T*hostile == sp.eye(3),
          hostile.T*hostile)
    check("hostile_compression_defect_equals_heavy_leakage_gram",
          sp.eye(2)-hostile_A.T*hostile_A == hostile_C.T*hostile_C,
          hostile_C.T*hostile_C)
    hostile_dark = hostile_A*dark
    check("hostile_changes_dark_component_ratio_and_norm",
          hostile_dark[0]/hostile_dark[1] == -sp.Rational(3, 4)
          and sp.simplify(hostile_dark.dot(hostile_dark)) == sp.Rational(25, 32),
          hostile_dark)
    check("safe_threshold_has_reducing_light_sector",
          safe*light_projector == light_projector*safe and q.T*q == sp.eye(2), safe)
    check("covariant_state_and_common_probe_transport_preserves_dark_record",
          transported_common*transported_dark == common*dark,
          transported_common*transported_dark)
    check("covariant_state_and_difference_probe_transport_preserves_readout",
          transported_difference*transported_dark == difference*dark,
          transported_difference*transported_dark)
    check("full_transported_two_port_instrument_remains_unitary",
          transported_junction*transported_junction.T == sp.eye(2),
          transported_junction*transported_junction.T)

    result = {
        "work_package": "WP860",
        "title": "Reducing-subspace threshold survival theorem",
        "summary": {"passed": sum(t["passed"] for t in tests), "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "necessary_and_sufficient_condition": "the WP859 two-port subspace is reducing for the full threshold unitary",
        "source_form": "P_L commutes with the complete microscopic threshold interaction algebra",
        "transport_rule": "d->Ad, M->MA*, D->DA* with A unitary",
        "smallest_hostile": "one heavy state mixed with one light port at cosine 3/4",
        "classification": "exact conditional threshold-survival theorem; source superselection authority open",
        "remaining_gates": ["derive central light-sector projector", "prove full threshold-algebra commutation",
                            "identify RG semigroup", "calibrate transported physical16 detector"],
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp860_reducing_subspace_threshold_survival_theorem.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
