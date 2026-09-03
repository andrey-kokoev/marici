from __future__ import annotations

import json
from fractions import Fraction

Vector3 = tuple[Fraction, Fraction, Fraction]
Vector2 = tuple[Fraction, Fraction]


def q(x: Vector3) -> Vector2:
    return x[1], x[2]


def good_f(x: Vector3) -> Fraction:
    return 2 * x[1] - x[2]


def descended(y: Vector2) -> Fraction:
    return 2 * y[0] - y[1]


def bad_f(x: Vector3) -> Fraction:
    return x[0] + 2 * x[1] - x[2]


def shear(x: Vector3) -> Vector3:
    return x[0] + x[1], x[1], x[2]


def render_vector(x: tuple[Fraction, ...]) -> list[str]:
    return [f"{entry.numerator}/{entry.denominator}" for entry in x]


def main() -> None:
    samples: list[Vector3] = [
        (Fraction(0), Fraction(0), Fraction(0)),
        (Fraction(3), Fraction(2), Fraction(-1)),
        (Fraction(-4), Fraction(5, 2), Fraction(7, 3)),
    ]
    assert all(good_f(x) == descended(q(x)) for x in samples)

    gauge = (Fraction(1), Fraction(0), Fraction(0))
    assert good_f(gauge) == 0
    representative = (Fraction(0), Fraction(2), Fraction(-1))
    shifted = tuple(representative[i] + gauge[i] for i in range(3))
    assert q(representative) == q(shifted)
    assert bad_f(representative) != bad_f(shifted)

    witness = (Fraction(0), Fraction(1), Fraction(0))
    assert shear(witness) != witness
    assert q(shear(witness)) == q(witness)

    result = {
        "schema": "marici.voevodsky.gauge-quotient-descent-univalence.v1",
        "status": "descent_verified_naive_displayed_univalence_falsified",
        "kernel_generator": render_vector(gauge),
        "good_observable_annihilates_kernel": True,
        "good_observable_descends": True,
        "hostile_representatives": [render_vector(representative), render_vector(shifted)],
        "hostile_values_differ": True,
        "vertical_automorphism": "h(x1,x2,x3)=(x1+x2,x2,x3)",
        "vertical_automorphism_nonidentity": True,
        "vertical_automorphism_over_quotient": True,
        "naive_set_level_displayed_univalence": False,
        "repair_gate": "univalent or Rezk completion, higher quotient, or source-authorized rigidification",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
