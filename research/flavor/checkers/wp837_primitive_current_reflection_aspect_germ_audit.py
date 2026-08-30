"""Exact WP837 Aspect-germ audit of primitive-current reflection selection."""

import json
from pathlib import Path
import sympy as sp


def spectral_shape(matrix: sp.Matrix):
    gram = matrix.T * matrix
    n = matrix.rows
    return sp.simplify(sp.trace(gram) / gram.det() ** sp.Rational(1, n))


def main() -> None:
    q = sp.Matrix([1, 2, 3])
    projector = q * q.T / (q.dot(q))
    reflection = sp.eye(3) - 2 * projector
    one = sp.ones(3, 1)
    alternative = sp.eye(3) - sp.Rational(2, 3) * one * one.T
    mass = sp.symbols("mass", positive=True, real=True)
    tests = []

    def check(name, condition, evidence):
        tests.append({"name": name, "passed": bool(condition),
                      "evidence": str(evidence)})

    check("primitive_current_norm_is_fourteen", q.dot(q) == 14, q.dot(q))
    check("current_projector_is_rank_one_orthoprojector",
          projector.T == projector and projector * projector == projector
          and projector.rank() == 1 and sp.trace(projector) == 1,
          projector)
    check("reflection_is_self_adjoint_involution",
          reflection.T == reflection and reflection * reflection == sp.eye(3),
          reflection)
    check("reflection_has_one_negative_line",
          sp.trace(reflection) == 1 and reflection.det() == -1,
          (sp.trace(reflection), reflection.det()))
    check("reflection_reverses_exactly_the_current_line",
          reflection * q == -q
          and reflection * sp.Matrix([2, -1, 0]) == sp.Matrix([2, -1, 0])
          and reflection * sp.Matrix([3, 0, -1]) == sp.Matrix([3, 0, -1]),
          reflection * q)
    negative_projector = (sp.eye(3) - reflection) / 2
    check("negative_projector_reconstructs_unique_reflection",
          negative_projector == projector
          and sp.eye(3) - 2 * negative_projector == reflection,
          negative_projector)
    check("current_reflection_saturates_wp836_shape_bound",
          spectral_shape(reflection) == 3, spectral_shape(reflection))
    check("alternative_wp836_minimizer_fails_current_attachment",
          spectral_shape(alternative) == 3 and alternative * q != -q,
          alternative * q)

    U = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
    transported_q = U * q
    transported_projector = transported_q * transported_q.T / transported_q.dot(transported_q)
    transported_reflection = sp.eye(3) - 2 * transported_projector
    check("projector_is_equivariant_under_simultaneous_frame_transport",
          transported_projector == U * projector * U.T,
          transported_projector - U * projector * U.T)
    check("reflection_is_equivariant_under_simultaneous_frame_transport",
          transported_reflection == U * reflection * U.T,
          transported_reflection - U * reflection * U.T)
    check("positive_scale_fiber_survives",
          spectral_shape(mass * reflection) == spectral_shape(reflection),
          spectral_shape(mass * reflection))
    check("smallest_scale_hostile_is_exact",
          spectral_shape(reflection) == spectral_shape(2 * reflection)
          and reflection != 2 * reflection,
          (spectral_shape(reflection), spectral_shape(2 * reflection)))

    result = {
        "work_package": "WP837",
        "title": "Primitive-current reflection under Aspect's germ tester",
        "summary": {"passed": sum(t["passed"] for t in tests),
                    "total": len(tests),
                    "all_passed": all(t["passed"] for t in tests)},
        "marked_carrier": "attached pair (primitive Ward current q, spectral operator D), with current provenance and completion-family comparison port retained",
        "native_relation": "family-relative Phi minimization followed by equality of the normalized negative spectral line with span(q)",
        "aspect_gates": {
            "fiber": "passes simultaneous real orthogonal frame transport; fails if the q attachment is forgotten; full complex weak-basis descent is not yet derived",
            "arity": "passes only when the full admitted completion family and q-to-D attachment remain arguments",
            "authority": "fails: neither Phi minimization nor the current-reflection law is derived from an admitted source action",
            "realization": "fails: no RG preparation, threshold-survival map, or calibrated physical16 instrument",
        },
        "classification": "conditional mixing rigidifier attached to the WP836 finite-completion selector; not a physical16 source selector",
        "smallest_exact_falsifier": "D=H_q and D=2 H_q obey the same germ law and score but have different absolute spectral thresholds",
        "remaining_gate": "derive the comparison functional and current-reflection attachment from one source action, extend covariance to the full weak-basis groupoid, fix or predict the scale, and supply matched physical16 instrumentation",
        "tests": tests,
    }
    output = Path(__file__).parents[1] / "results" / "wp837_primitive_current_reflection_aspect_germ_audit.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result["summary"], indent=2))
    if not result["summary"]["all_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
