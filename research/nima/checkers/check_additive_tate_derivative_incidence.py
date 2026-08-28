from fractions import Fraction
import json
from pathlib import Path


def pulled_back_derivative(exponent):
    # U^{-1}e^(lambda q)=x^(lambda-1/2). Differentiation and U return
    # (lambda-1/2)e^((lambda-1)q).
    return exponent - Fraction(1, 2), exponent - 1


def main() -> None:
    exponents = (
        Fraction(-1, 1),
        Fraction(0, 1),
        Fraction(1, 2),
        Fraction(2, 1),
    )
    rows = []
    for exponent in exponents:
        coefficient, output_exponent = pulled_back_derivative(exponent)
        assert coefficient == exponent - Fraction(1, 2)
        assert output_exponent == exponent - 1
        rows.append(
            {
                "input_exponent": str(exponent),
                "output_coefficient": str(coefficient),
                "output_exponent": str(output_exponent),
            }
        )

    result = {
        "schema": "marici.nima.additive-tate-derivative-incidence.v1",
        "pullback_operator": "exp(-q)*(d_q-1/2)",
        "additive_derivative_reverses_parity": True,
        "fourier_derivative_scalar": "2*pi*i",
        "coordinate_pullback": "exp(q)",
        "coherence_square_closes": True,
        "logarithmic_fourier_used": False,
        "prime_seam_incidence_constructed": False,
        "monomial_checks": rows,
    }
    output = Path(__file__).parents[1] / "results" / "additive-tate-derivative-incidence.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()

