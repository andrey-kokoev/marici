"""Exact typing audit for primitive and square reciprocal grades."""

from fractions import Fraction
import json


def grades(c, sigma, incidence):
    a1 = sigma * c
    a2 = 1 - c * c / 2
    return incidence * a1, incidence * a2


c = Fraction(5, 2)
cases = {
    "negative_root_numerator": grades(c, 1, 1),
    "positive_root_numerator": grades(c, -1, 1),
    "negative_root_denominator": grades(c, 1, -1),
    "positive_root_denominator": grades(c, -1, -1),
}
discriminant = c * c - 4

checks = {
    "square_grade_forgets_phase": cases["negative_root_numerator"][1]
    == cases["positive_root_numerator"][1],
    "primitive_grade_reverses_with_phase": cases["negative_root_numerator"][0]
    == -cases["positive_root_numerator"][0],
    "denominator_reverses_both_grades": all(
        cases[name.replace("denominator", "numerator")][i] == -values[i]
        for name, values in cases.items()
        if "denominator" in name
        for i in (0, 1)
    ),
    "square_encodes_common_discriminant": discriminant
    == -2 * (cases["negative_root_numerator"][1] + 1),
    "off_unit_regime": discriminant > 0,
    "square_grade_nonexceptional": cases["negative_root_numerator"][1] != 0,
}

result = {
    "schema": "marici.grothendieck.primitive-square-split-typing.v1",
    "passed": all(checks.values()),
    "checks": checks,
    "witness": {
        "c": str(c),
        "discriminant": str(discriminant),
        "grades": {name: [str(x) for x in values] for name, values in cases.items()},
    },
}

print(json.dumps(result, indent=2, sort_keys=True))
