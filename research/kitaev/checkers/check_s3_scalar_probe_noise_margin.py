"""Exact adversarial separation margins for minimum D(S3) scalar probes."""

import itertools
import json
from fractions import Fraction


class Zeta3:
    """a+b*omega with |a+b*omega|^2=a^2-a*b+b^2."""

    def __init__(self, a=0, b=0):
        self.a, self.b = Fraction(a), Fraction(b)

    def __sub__(self, other):
        return Zeta3(self.a - other.a, self.b - other.b)

    def midpoint(self, other):
        return Zeta3((self.a + other.a) / 2, (self.b + other.b) / 2)

    def norm_squared(self):
        return self.a * self.a - self.a * self.b + self.b * self.b

    def text(self):
        if self.b == 0:
            return fraction_text(self.a)
        return f"({fraction_text(self.a)},{fraction_text(self.b)})_in_basis_1_omega"


def fraction_text(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main():
    labels = ("A", "B", "C", "D", "E", "F", "G", "H")
    twists = {
        "A": Zeta3(1), "B": Zeta3(1), "C": Zeta3(1), "D": Zeta3(1),
        "E": Zeta3(-1), "F": Zeta3(1), "G": Zeta3(0, 1), "H": Zeta3(-1, -1),
    }
    s_rows = {
        "C": dict(zip(labels, map(lambda x: Zeta3(x),
            [Fraction(1, 3), Fraction(1, 3), Fraction(2, 3), 0, 0,
             -Fraction(1, 3), -Fraction(1, 3), -Fraction(1, 3)]))),
        "D": dict(zip(labels, map(lambda x: Zeta3(x),
            [Fraction(1, 2), -Fraction(1, 2), 0, Fraction(1, 2),
             -Fraction(1, 2), 0, 0, 0]))),
        "E": dict(zip(labels, map(lambda x: Zeta3(x),
            [Fraction(1, 2), -Fraction(1, 2), 0, -Fraction(1, 2),
             Fraction(1, 2), 0, 0, 0]))),
        "F": dict(zip(labels, map(lambda x: Zeta3(x),
            [Fraction(1, 3), Fraction(1, 3), -Fraction(1, 3), 0, 0,
             Fraction(2, 3), -Fraction(1, 3), -Fraction(1, 3)]))),
    }
    families = (
        ("twist", "S_C", "S_D"),
        ("twist", "S_C", "S_E"),
        ("twist", "S_D", "S_F"),
        ("twist", "S_E", "S_F"),
    )

    def value(probe, label):
        return twists[label] if probe == "twist" else s_rows[probe[2:]][label]

    def distance_squared(family, left, right):
        return max((value(probe, left) - value(probe, right)).norm_squared() for probe in family)

    audits = {}
    global_best_squared = Fraction(0)
    for family in families:
        pair_distances = {
            left + "-" + right: distance_squared(family, left, right)
            for left, right in itertools.combinations(labels, 2)
        }
        minimum_squared = min(pair_distances.values())
        closest_pairs = [pair for pair, distance in pair_distances.items() if distance == minimum_squared]
        assert minimum_squared > 0
        global_best_squared = max(global_best_squared, minimum_squared)
        audits["+".join(family)] = {
            "minimum_L_infinity_complex_distance_squared": fraction_text(minimum_squared),
            "minimum_distance": "1/3" if minimum_squared == Fraction(1, 9) else "unexpected",
            "unique_decoding_open_error_radius": "1/6" if minimum_squared == Fraction(1, 9) else "unexpected",
            "closest_pairs": closest_pairs,
        }
    assert all(audit["minimum_distance"] == "1/3" for audit in audits.values())

    selected = families[2]
    selected_key = "+".join(selected)
    closest_pair_name = audits[selected_key]["closest_pairs"][0]
    left, right = closest_pair_name.split("-")
    midpoint = [value(probe, left).midpoint(value(probe, right)) for probe in selected]
    midpoint_left_distances = [(midpoint[i] - value(probe, left)).norm_squared() for i, probe in enumerate(selected)]
    midpoint_right_distances = [(midpoint[i] - value(probe, right)).norm_squared() for i, probe in enumerate(selected)]
    assert max(midpoint_left_distances) == Fraction(1, 36)
    assert max(midpoint_right_distances) == Fraction(1, 36)

    result = {
        "schema": "marici.s3-scalar-probe-noise-margin.v1",
        "metric": "L_infinity_over_probe_coordinates_using_complex_modulus",
        "minimum_family_audits": audits,
        "all_four_minimum_families_have_same_margin": True,
        "optimal_minimum_distance_over_minimum_families": "1/3",
        "sharp_unique_nearest_signature_condition": "per_probe_error_strictly_less_than_1/6",
        "boundary_falsifier": {
            "selected_family": list(selected),
            "closest_pair": [left, right],
            "midpoint_signature": [entry.text() for entry in midpoint],
            "distance_to_each_endpoint": "1/6",
            "closed_error_balls_intersect_at_boundary": True,
        },
        "aggregate_gates": {
            "every_minimum_family_has_positive_separation": True,
            "all_minimum_families_have_distance_one_third": True,
            "errors_below_one_sixth_preserve_unique_label": True,
            "one_sixth_boundary_is_sharp": True,
            "margin_uses_complex_modulus_not_formal_symbol_equality": True,
            "deterministic_margin_does_not_supply_noise_probabilities": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
