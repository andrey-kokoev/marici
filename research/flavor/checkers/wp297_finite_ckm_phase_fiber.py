"""WP297: exact twofold CKM phase fiber after a lower-sector modulus probe."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def ckm_packet(cos_delta):
    sin_delta = sp.Rational(4, 5)
    phase = cos_delta + sp.I * sin_delta
    s12, c12 = sp.Rational(3, 5), sp.Rational(4, 5)
    s23, c23 = sp.Rational(5, 13), sp.Rational(12, 13)
    s13, c13 = sp.Rational(5, 13), sp.Rational(12, 13)
    matrix = sp.Matrix(
        [
            [c12 * c13, s12 * c13, s13 * sp.conjugate(phase)],
            [-s12 * c23 - c12 * s23 * s13 * phase, c12 * c23 - s12 * s23 * s13 * phase, s23 * c13],
            [s12 * s23 - c12 * c23 * s13 * phase, -c12 * s23 - s12 * c23 * s13 * phase, c23 * c13],
        ]
    )
    squared_moduli = [sp.simplify(sp.expand_complex(value * sp.conjugate(value))) for value in matrix]
    signed_j = sp.simplify(c12 * c23 * c13**2 * s12 * s23 * s13 * sin_delta)
    masses = [sp.Rational(value) for value in (1, 2, 3, 5, 7, 11)]
    readout = masses + squared_moduli[:3] + [squared_moduli[5], signed_j]
    physical = masses + squared_moduli + [signed_j]
    return matrix, squared_moduli, signed_j, readout, physical


def main():
    first = ckm_packet(sp.Rational(3, 5))
    second = ckm_packet(sp.Rational(-3, 5))
    first_matrix, first_moduli, first_j, first_readout, first_physical = first
    second_matrix, second_moduli, second_j, second_readout, second_physical = second
    difference = [sp.simplify(a - b) for a, b in zip(first_physical, second_physical)]
    interference_indices = [3, 4, 6, 7]

    checks = {
        "first_ckm_is_exactly_unitary": sp.simplify(first_matrix * first_matrix.conjugate().T) == sp.eye(3),
        "second_ckm_is_exactly_unitary": sp.simplify(second_matrix * second_matrix.conjugate().T) == sp.eye(3),
        "masses_first_row_vcb_and_signed_j_match": first_readout == second_readout,
        "signed_j_is_positive_and_equal": first_j == second_j and first_j > 0,
        "cosines_have_opposite_sign": sp.Rational(3, 5) == -sp.Rational(-3, 5),
        "interference_sensitive_moduli_differ": all(first_moduli[index] != second_moduli[index] for index in interference_indices),
        "physical16_embeddings_are_distinct": any(value != 0 for value in difference),
        "row_and_column_normalization_hold": all(
            sum(moduli[3 * row : 3 * row + 3]) == 1 and sum(moduli[row::3]) == 1
            for moduli in (first_moduli, second_moduli)
            for row in range(3)
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP297",
        "admitted_state_domain": "standard ordered-angle CKM domain with nonzero angles, positive sin(delta), and exact unitary matrices",
        "faithful_quotient_coordinate": "physical16 represented by six masses, nine squared CKM moduli, and signed J",
        "probe_family": "six masses, complete first-row moduli, |V_cb|, and signed J",
        "shared_probe_readout": [str(value) for value in first_readout],
        "hostile_pair": {
            "cos_delta_values": ["3/5", "-3/5"],
            "shared_sin_delta": "4/5",
            "first_physical16_squared_embedding": [str(value) for value in first_physical],
            "second_physical16_squared_embedding": [str(value) for value in second_physical],
            "difference": [str(value) for value in difference],
        },
        "contextual_partition": "the admitted probes fix the mixing-angle sines and sin(delta) but retain the generic delta versus pi-delta interference pair",
        "descent": "all probe coordinates are weak-basis-invariant physical16 functions",
        "classification": "near-faithful physical readout with an exact twofold phase fiber on the declared generic standard domain; neither selector nor rigidifier",
        "smallest_exact_falsifier": "cos(delta)=3/5 and -3/5 at shared sin(delta)=4/5 preserve the admitted readout but change four interference-sensitive CKM moduli",
        "durable_rule": "finite fiber is not singleton fiber",
        "remaining_physical_instrument_gate": "add one independently calibrated cos(delta)-sensitive modulus to separate the pair, while keeping readout faithfulness distinct from source selection",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp297_finite_ckm_phase_fiber.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
