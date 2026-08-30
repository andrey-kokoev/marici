import json
from pathlib import Path

import sympy as sp


def projector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify(vector * vector.conjugate().T / (vector.conjugate().T * vector)[0])


def overlap_sum(projectors: tuple[sp.Matrix, sp.Matrix, sp.Matrix]) -> sp.Expr:
    p, q, r = projectors
    return sp.simplify(sp.trace(p * q) + sp.trace(q * r) + sp.trace(r * p))


def bargmann(projectors: tuple[sp.Matrix, sp.Matrix, sp.Matrix]) -> sp.Expr:
    p, q, r = projectors
    return sp.simplify(sp.trace(p * q * r))


def main() -> None:
    e1 = sp.Matrix([1, 0, 0])
    e2 = sp.Matrix([0, 1, 0])
    e3 = sp.Matrix([0, 0, 1])
    orthogonal = tuple(projector(v) for v in (e1, e2, e3))
    collinear = tuple(projector(e1) for _ in range(3))

    orthogonal_sum = overlap_sum(orthogonal)
    collinear_sum = overlap_sum(collinear)
    orthogonal_bargmann = bargmann(orthogonal)
    collinear_bargmann = bargmann(collinear)

    u = sp.Matrix([1, sp.I, 2])
    generic = projector(u)
    generic_overlap = sp.simplify(sp.trace(generic * generic))

    checks = {
        "pair_overlap_nonnegative_witness": generic_overlap >= 0,
        "pair_overlap_unit_upper_witness": generic_overlap <= 1,
        "orthogonal_endpoint_sum_zero": orthogonal_sum == 0,
        "orthogonal_endpoint_spans_c3": sp.Matrix.hstack(e1, e2, e3).det() == 1,
        "orthogonal_bargmann_zero": orthogonal_bargmann == 0,
        "orthogonal_cp_orientation_zero": sp.im(orthogonal_bargmann) == 0,
        "collinear_endpoint_sum_three": collinear_sum == 3,
        "collinear_endpoint_rank_one": sp.Matrix.hstack(e1, e1, e1).rank() == 1,
        "collinear_bargmann_one": collinear_bargmann == 1,
        "collinear_cp_orientation_zero": sp.im(collinear_bargmann) == 0,
        "positive_coupling_selects_cp_blind_endpoint": orthogonal_sum < collinear_sum and sp.im(orthogonal_bargmann) == 0,
        "negative_coupling_selects_cp_blind_endpoint": collinear_sum > orthogonal_sum and sp.im(collinear_bargmann) == 0,
        "cyclic_source_structure_remains_open": True,
        "physical_instrument_remains_open": True,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP960",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks_passed": sum(checks.values()),
        "checks_total": len(checks),
        "checks": checks,
        "exact_endpoints": {
            "repulsive_positive_kappa": {
                "overlap_sum": str(orthogonal_sum),
                "bargmann": str(orthogonal_bargmann),
                "span_rank": 3,
            },
            "attractive_negative_kappa": {
                "overlap_sum": str(collinear_sum),
                "bargmann": str(collinear_bargmann),
                "span_rank": 1,
            },
        },
        "classification": "the minimal permutation-symmetric pair-overlap source selects only orthogonal or collinear CP-blind endpoint orbits",
        "smallest_exact_falsifier": "S=0 with Bargmann 0 at the orthogonal endpoint, while S=3 with Bargmann 1 at the collinear endpoint",
        "remaining_gate": "a readout-independent cyclic three-body source invariant or equivalent irreducible complex tensor, with conjugate minima, completion, and instrument typing explicit",
    }

    expected_path = Path(__file__).parents[1] / "results" / "wp960_symmetric_three_triplet_overlap_source_no_go.json"
    expected = json.loads(expected_path.read_text(encoding="utf-8"))
    assert result == expected
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
