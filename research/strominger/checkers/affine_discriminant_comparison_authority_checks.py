"""Exact duality and torsion-free no-go for the affine discriminant object."""
import json
from fractions import Fraction
from pathlib import Path


# F^{-1} for F=[[2,7],[3,7]].
F_inv = ((Fraction(-1), Fraction(1)), (Fraction(3, 7), Fraction(-2, 7)))


def pairing(x, y):
    # y^T F^{-1} x modulo one.
    fx = (
        F_inv[0][0] * x[0] + F_inv[0][1] * x[1],
        F_inv[1][0] * x[0] + F_inv[1][1] * x[1],
    )
    value = y[0] * fx[0] + y[1] * fx[1]
    return value - value.numerator // value.denominator


generator_value = pairing((1, 0), (0, 1))
phase_exponents = [[(3 * a * b) % 7 for b in range(7)] for a in range(7)]
character_rows = {tuple(row) for row in phase_exponents}

tests = {
    "inverse_has_denominator_seven": generator_value == Fraction(3, 7),
    "generator_pairing_is_primitive": generator_value.numerator % 7 != 0,
    "seven_distinct_character_rows": len(character_rows) == 7,
    "pairing_is_nondegenerate_left": all(
        any(phase_exponents[a][b] != 0 for b in range(7)) for a in range(1, 7)
    ),
    "pairing_is_nondegenerate_right": all(
        any(phase_exponents[a][b] != 0 for a in range(7)) for b in range(1, 7)
    ),
    "torsion_free_target_has_no_nonzero_Z7_image": all(
        # In a rational additive target, 7*y=0 implies y=0.  Replay over a
        # bounded rational grid to accompany the general algebraic proof.
        not (7 * Fraction(n, d) == 0) or Fraction(n, d) == 0
        for d in range(1, 9)
        for n in range(-16, 17)
    ),
}

result = {
    "schema": "marici.checker_results.v1",
    "checker": "affine_discriminant_comparison_authority_checks.py",
    "passed": all(tests.values()),
    "tests": tests,
    "generator_linking_value": str(generator_value),
    "phase_exponent_table_mod_7": phase_exponents,
    "associated_constructor": "coker(F) tensor reduced reflection orbit",
    "ordinary_physical_additive_comparison": "proved_zero_into_any torsion-free carrier",
    "smallest_missing_physical_constructor": "discriminant phase port or reflection-equivariant mod-seven physical lattice",
}

out = Path(__file__).resolve().parents[1] / "results" / "affine_discriminant_comparison_authority_checks.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
