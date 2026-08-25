import json
from pathlib import Path
import sympy as sp


def main():
    z, s = sp.symbols("z s")
    gaussian_mellin = sp.pi**(-z) * sp.gamma(z)
    exponential_mellin = sp.gamma(z)
    gaussian_residue = sp.residue(gaussian_mellin, z, 0)
    exponential_residue = sp.residue(exponential_mellin, z, 0)
    assert gaussian_residue == exponential_residue == 1

    alpha = (1 - s) / 2
    gaussian_boundary_coefficient = sp.simplify(sp.Rational(1, 2) *
                                                gaussian_mellin.subs(z, alpha))
    exponential_boundary_coefficient = sp.simplify(sp.Rational(1, 2) *
                                                   exponential_mellin.subs(z, alpha))
    boundary_ratio = sp.simplify(gaussian_boundary_coefficient /
                                 exponential_boundary_coefficient)
    assert boundary_ratio == sp.pi**(s / 2 - sp.Rational(1, 2))

    c = sp.symbols("c")
    scaled_residue = sp.residue(c * sp.gamma(z), z, 0)
    assert scaled_residue == c

    result = {
        "owner": "marici.Kitaev",
        "claim_strength": "conditional_normalized_mellin_regulator_universality",
        "gaussian_mellin_residue_at_zero": str(gaussian_residue),
        "exponential_mellin_residue_at_zero": str(exponential_residue),
        "boundary_coefficient_ratio_gaussian_to_exponential": str(boundary_ratio),
        "normalized_finite_part": "zeta(s)",
        "wrong_normalization_finite_part": "c*zeta(s)",
        "finite_counterterm_changes_divisor": True,
        "off_seam_divisor_avoidance": "unproved",
    }
    out = Path(__file__).parents[1] / "results" / "theta-regulator-universality.json"
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
