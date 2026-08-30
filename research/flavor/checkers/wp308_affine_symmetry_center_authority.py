"""WP308: exact authority audit for a nonzero affine-symmetry fixed point."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    x, center = sp.symbols("x center", real=True)
    reflection = 2 * center - x
    potential = (x - center) ** 2
    transformed_potential = sp.expand(potential.subs(x, reflection))
    stationary = sp.solve(sp.diff(potential, x), x)
    selected = stationary[0]
    response = sp.diff(selected, center)

    center_one = sp.Rational(1)
    center_two = sp.Rational(2)
    point_one = selected.subs(center, center_one)
    point_two = selected.subs(center, center_two)
    centered_coordinate = sp.symbols("centered_coordinate", real=True)
    translated_potential = sp.expand(potential.subs(x, centered_coordinate + center))

    checks = {
        "affine_reflection_is_involution": sp.simplify(reflection.subs(x, reflection) - x) == 0,
        "potential_is_affine_reflection_invariant": sp.simplify(transformed_potential - potential) == 0,
        "fixed_locus_is_unique_center": sp.solve(sp.Eq(x, reflection), x) == [center],
        "potential_has_unique_stationary_point_at_center": stationary == [center],
        "hessian_is_strictly_positive": sp.diff(potential, x, 2) == 2,
        "selected_point_responds_to_center": response == 1,
        "same_abstract_z2_different_centers_select_different_points": point_one == 1 and point_two == 2,
        "translation_moves_center_to_zero_but_retains_physical_offset": translated_potential == centered_coordinate**2,
        "linear_reflection_center_zero_selects_origin": selected.subs(center, 0) == 0,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP308",
        "theorem_domain": "one weak-basis-invariant physical coordinate x with affine Z2 action r_a(x)=2a-x and invariant potential V_a(x)=(x-a)^2",
        "symmetry_fixed_point": "x_star=a",
        "source_response": "d x_star/d a=1",
        "rival_embeddings": [
            {"abstract_group": "Z2", "center": "1", "selected_point": str(point_one)},
            {"abstract_group": "Z2", "center": "2", "selected_point": str(point_two)},
        ],
        "coordinate_translation": "y=x-a turns the action into y->-y and V=y^2, but recovering physical x requires the offset a",
        "descent": "conditional on the affine action being defined directly on a declared weak-basis-invariant coordinate",
        "classification": "an affine symmetry can be an exact nonzero point selector only when its center has independent source authority; the abstract symmetry alone rigidifies around an unspecified reference",
        "smallest_exact_falsifier": "two affine realizations of the same abstract Z2, centered at 1 and 2, select different physical points",
        "reference_rule": "treating a as a reference port changes the relational experiment and stabilizer groupoid; it does not make a an absolute value of the original source",
        "remaining_physical_instrument_gate": "derive the affine center from source geometry with physical units and calibration, prove its weak-basis descent, and show that it is fixed rather than a surviving modulus",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp308_affine_symmetry_center_authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
