from fractions import Fraction
import json
from pathlib import Path


def add(left, right):
    return left[0] + right[0], left[1] + right[1]


def multiply(left, right):
    return (
        left[0] * right[0] - left[1] * right[1],
        left[0] * right[1] + left[1] * right[0],
    )


def power(value, exponent):
    result = (Fraction(1), Fraction(0))
    for _ in range(exponent):
        result = multiply(result, value)
    return result


def conjugate(value):
    return value[0], -value[1]


def scale(value, scalar):
    return value[0] * scalar, value[1] * scalar


def norm_squared(value):
    return value[0] * value[0] + value[1] * value[1]


rotor = (Fraction(3, 5), Fraction(4, 5))
rotor_conjugate = conjugate(rotor)
records = []

for prime_proxy in [2, 3, 5, 7, 11]:
    radial = Fraction(1, prime_proxy)
    q_plus = scale(rotor, radial)
    q_minus = scale(rotor_conjugate, radial)

    for grade in range(1, 7):
        shell_plus = (
            Fraction(prime_proxy + grade, prime_proxy + 2),
            Fraction(grade, prime_proxy + 3),
        )
        shell_minus = conjugate(shell_plus)
        u_plus = multiply(power(q_plus, grade), shell_plus)
        u_minus = multiply(power(q_minus, grade), shell_minus)
        assert u_minus == conjugate(u_plus)
        assert norm_squared(u_minus) == norm_squared(u_plus)

        off_scale = Fraction(2)
        off_plus = scale(u_plus, off_scale)
        off_minus = scale(u_minus, Fraction(1, 2))
        assert norm_squared(off_plus) != norm_squared(off_minus)

    records.append(
        {
            "prime_proxy": prime_proxy,
            "conjugate_matching_through_grade": 6,
            "centered_exchange_isometric": True,
            "off_center_exchange_isometric": False,
        }
    )

sample = multiply(q_plus, (Fraction(2), Fraction(1)))
good_counterterm_plus = (Fraction(1, 3), Fraction(2, 7))
good_counterterm_minus = conjugate(good_counterterm_plus)
renormalized_plus = add(sample, scale(good_counterterm_plus, Fraction(-1)))
renormalized_minus = add(
    conjugate(sample), scale(good_counterterm_minus, Fraction(-1))
)
assert renormalized_minus == conjugate(renormalized_plus)

bad_counterterm_minus = (Fraction(1, 3), Fraction(2, 7))
bad_renormalized_minus = add(
    conjugate(sample), scale(bad_counterterm_minus, Fraction(-1))
)
assert bad_renormalized_minus != conjugate(renormalized_plus)

result = {
    "schema": "marici.nima.reciprocal-real-markov-gluing.v1",
    "records": records,
    "paired_counterterm_preserves_real_structure": True,
    "independent_counterterm_preserves_real_structure": False,
    "verdict": "low grades must be reciprocally paired before relative completion",
}

out = Path(__file__).parents[1] / "results" / "reciprocal-real-markov-gluing.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
