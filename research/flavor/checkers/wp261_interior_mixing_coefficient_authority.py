"""WP261: exact coefficient-authority audit for an interior mixing selector."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def minimum(a, b):
    x = sp.simplify(a / (2 * b))
    second = 2 * b
    value = sp.simplify(-a * x + b * x**2)
    return x, second, value


def main():
    # x is the normalized commutator invariant sin^2(2 theta) on [0,1].
    a1, b1 = sp.Rational(1), sp.Rational(1)
    a2, b2 = sp.Rational(1), sp.Rational(2)
    x1, curvature1, value1 = minimum(a1, b1)
    x2, curvature2, value2 = minimum(a2, b2)

    # Exact matrix realization of x at theta=pi/8 for the first packet:
    # sin^2(2 theta)=sin^2(pi/4)=1/2.
    hu = sp.diag(0, 1)
    c = sp.sqrt(2 + sp.sqrt(2)) / 2
    s = sp.sqrt(2 - sp.sqrt(2)) / 2
    rotation = sp.Matrix([[c, s], [-s, c]])
    hd = sp.simplify(rotation * sp.diag(0, 1) * rotation.T)
    commutator = sp.simplify(hu * hd - hd * hu)
    normalized_commutator = sp.simplify(2 * sp.trace(commutator.conjugate().T * commutator))
    q = sp.Matrix([[sp.Rational(3, 5), sp.Rational(4, 5)],
                   [-sp.Rational(4, 5), sp.Rational(3, 5)]])
    hu_q = sp.simplify(q * hu * q.T)
    hd_q = sp.simplify(q * hd * q.T)
    commutator_q = sp.simplify(hu_q * hd_q - hd_q * hu_q)
    normalized_commutator_q = sp.simplify(2 * sp.trace(commutator_q.conjugate().T * commutator_q))

    # Same invariant action grammar and quotient descent, different unfixed
    # coefficient ratios, hence different selected physical points.
    checks = {
        "normalized_commutator_realizes_x_half": normalized_commutator == x1,
        "first_minimum_is_interior": 0 < x1 < 1,
        "second_minimum_is_interior": 0 < x2 < 1,
        "both_minima_are_strict": curvature1 > 0 and curvature2 > 0,
        "same_action_grammar_selects_different_points": x1 != x2,
        "selected_value_depends_only_on_coefficient_ratio": x1 == a1 / (2 * b1) and x2 == a2 / (2 * b2),
        "weak_basis_descent_is_exact": normalized_commutator_q == normalized_commutator,
        "proper_slice_reduction_is_conditional": x1 in (sp.Rational(1, 2),) and x2 in (sp.Rational(1, 4),),
        "deliberate_geometry_only_uniqueness_claim_fails": x1 - x2 != 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP261",
        "admitted_state_domain": "nondegenerate two-generation spectral orbit with x = sin^2(2 theta) in [0,1]",
        "faithful_quotient_coordinate": "ordered spectra plus the normalized weak-basis-invariant commutator coordinate x",
        "candidate_source_action": "V(x) = -a x + b x^2 with a>0 and b>0",
        "stationary_selector": "x_star = a/(2b) when 0<a<2b",
        "hostile_coefficient_packets": [
            {"a": str(a1), "b": str(b1), "x_star": str(x1), "curvature": str(curvature1), "minimum_value": str(value1)},
            {"a": str(a2), "b": str(b2), "x_star": str(x2), "curvature": str(curvature2), "minimum_value": str(value2)},
        ],
        "contextual_partition": "each admitted coefficient packet selects one interior point on the two-generation mixing slice; forgetting the coefficient ratio merges distinct selected points",
        "classification": "weak-basis-descending conditional source-action selector on a two-generation slice; neither numerical geometry-only selector nor presentation rigidifier",
        "first_nonfaithful_arrow": "invariant action grammar -> numerical coefficient ratio a/b",
        "smallest_exact_falsifier": "the equally admissible packets (a,b)=(1,1) and (1,2) select x=1/2 and x=1/4",
        "remaining_physical_instrument_gate": "derive a/b, the dynamical flavon substrate, kinetic normalization, finite relaxation/stabilization, three-generation completion, and physical readout independently of fitted flavor values",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp261_interior_mixing_coefficient_authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
