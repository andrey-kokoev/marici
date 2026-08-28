import json
from pathlib import Path

import sympy as sp


def projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.conjugate().T / (vector.conjugate().T * vector)[0])


def main() -> None:
    p = sp.Matrix([1, 0, 0])
    q = sp.Matrix([1, 1, 0])
    r = sp.Matrix([1, sp.I, 1])
    p_projector = projector(p)
    q_projector = projector(q)
    r_projector = projector(r)

    common_line = sp.Matrix([0, 0, 1])
    two_word_a = sp.eye(3) + 2 * p_projector + 3 * q_projector
    two_word_d = 2 * sp.eye(3) + 5 * p_projector - q_projector
    two_commutator = sp.simplify(two_word_a * two_word_d - two_word_d * two_word_a)

    bargmann = sp.simplify(sp.trace(p_projector * q_projector * r_projector))
    conjugate_bargmann = sp.simplify(
        sp.trace(p_projector.conjugate() * q_projector.conjugate() * r_projector.conjugate())
    )
    span_matrix = sp.Matrix.hstack(p, q, r)

    checks = {
        "projectors_rank_one": all(x.rank() == 1 for x in (p_projector, q_projector, r_projector)),
        "projectors_idempotent": all(sp.simplify(x**2) == x for x in (p_projector, q_projector, r_projector)),
        "projector_rescaling_invariant": projector((2 + 3 * sp.I) * r) == r_projector,
        "two_projectors_share_line": p_projector * common_line == sp.zeros(3, 1) and q_projector * common_line == sp.zeros(3, 1),
        "two_projector_commutator_rank_at_most_two": two_commutator.det() == 0,
        "two_projector_cp_cubic_zero": sp.factor(sp.trace(two_commutator**3)) == 0,
        "three_rays_span_family_space": span_matrix.det() == 1,
        "bargmann_exact": bargmann == (1 + sp.I) / 6,
        "bargmann_imaginary_nonzero": sp.im(bargmann) == sp.Rational(1, 6),
        "conjugation_reverses_orientation": conjugate_bargmann == sp.conjugate(bargmann),
        "source_action_remains_open": True,
        "physical_instrument_remains_open": True,
    }

    result = {
        "work_package": "WP959",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact": {
            "span_determinant": str(span_matrix.det()),
            "bargmann": str(bargmann),
            "bargmann_imaginary_part": str(sp.im(bargmann)),
            "two_projector_commutator_rank": two_commutator.rank(),
            "two_projector_cp_cubic": str(sp.factor(sp.trace(two_commutator**3))),
        },
        "classification": "the canonical complex-triplet projector interface exists, but the first CP-sensitive relational source packet has arity three",
        "smallest_exact_falsifier": "two projectors share a common line and force zero commutator cubic",
        "remaining_gate": "a readout-independent source action deriving an ordered spanning triple or equivalent irreducible complex tensor, plus completion and instrument transport",
    }
    expected_path = Path(__file__).parents[1] / "results" / "wp959_projective_source_arity_threshold.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
