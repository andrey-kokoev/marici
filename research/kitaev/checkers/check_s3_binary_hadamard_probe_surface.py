"""Exact formal binary-effect surface and sampling margin for D(S3)."""

import itertools
import json
import sympy as sp


def text(value):
    return str(sp.simplify(value)).replace("sqrt(3)", "sqrt3")


def main():
    labels = ("A", "B", "C", "D", "E", "F", "G", "H")
    sqrt3 = sp.sqrt(3)
    probes = {
        "twist_Re": (1, 1, 1, 1, -1, 1, -sp.Rational(1, 2), -sp.Rational(1, 2)),
        "twist_Im": (0, 0, 0, 0, 0, 0, sqrt3 / 2, -sqrt3 / 2),
        "S_A": (sp.Rational(1, 6), sp.Rational(1, 6), sp.Rational(1, 3), sp.Rational(1, 2), sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3)),
        "S_B": (sp.Rational(1, 6), sp.Rational(1, 6), sp.Rational(1, 3), -sp.Rational(1, 2), -sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3)),
        "S_C": (sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(2, 3), 0, 0, -sp.Rational(1, 3), -sp.Rational(1, 3), -sp.Rational(1, 3)),
        "S_D": (sp.Rational(1, 2), -sp.Rational(1, 2), 0, sp.Rational(1, 2), -sp.Rational(1, 2), 0, 0, 0),
        "S_E": (sp.Rational(1, 2), -sp.Rational(1, 2), 0, -sp.Rational(1, 2), sp.Rational(1, 2), 0, 0, 0),
        "S_F": (sp.Rational(1, 3), sp.Rational(1, 3), -sp.Rational(1, 3), 0, 0, sp.Rational(2, 3), -sp.Rational(1, 3), -sp.Rational(1, 3)),
        "S_G": (sp.Rational(1, 3), sp.Rational(1, 3), -sp.Rational(1, 3), 0, 0, -sp.Rational(1, 3), -sp.Rational(1, 3), sp.Rational(2, 3)),
        "S_H": (sp.Rational(1, 3), sp.Rational(1, 3), -sp.Rational(1, 3), 0, 0, -sp.Rational(1, 3), sp.Rational(2, 3), -sp.Rational(1, 3)),
    }

    def signature(index, family):
        return tuple(probes[name][index] for name in family)

    def faithful(family):
        return len({signature(i, family) for i in range(8)}) == 8

    names = tuple(probes)
    minimum_size = None
    minimum_families = []
    for size in range(1, len(names) + 1):
        families = [family for family in itertools.combinations(names, size) if faithful(family)]
        if families:
            minimum_size, minimum_families = size, families
            break
    assert minimum_size == 3
    selected = ("twist_Im", "S_D", "S_F")
    assert selected in minimum_families

    selected_signatures = {label: [text(value) for value in signature(i, selected)] for i, label in enumerate(labels)}
    pair_distances = {}
    for i, j in itertools.combinations(range(8), 2):
        distance = max(abs(sp.simplify(a - b)) for a, b in zip(signature(i, selected), signature(j, selected)))
        pair_distances[labels[i] + "-" + labels[j]] = distance
    minimum_expectation_distance = min(pair_distances.values())
    closest_pairs = [pair for pair, value in pair_distances.items() if value == minimum_expectation_distance]
    assert minimum_expectation_distance == sp.Rational(1, 3)

    # Formal Bernoulli completion of a bounded scalar m: p(+)=(1+m)/2.
    plus_probabilities = {
        label: [text((sp.sympify(value) + sp.Integer(1)) / 2) for value in signature(i, selected)]
        for i, label in enumerate(labels)
    }
    minimum_probability_distance = minimum_expectation_distance / 2
    unique_frequency_radius = minimum_probability_distance / 2
    assert minimum_probability_distance == sp.Rational(1, 6)
    assert unique_frequency_radius == sp.Rational(1, 12)

    # Hoeffding + union bound: 3 settings, two tails per setting.
    # P(any |p_hat-p| >= 1/12) <= 6 exp(-n/72).
    result = {
        "schema": "marici.s3-formal-binary-effect-surface.v2",
        "candidate_atomic_settings": list(names),
        "minimum_atomic_setting_count": minimum_size,
        "minimum_family_count": len(minimum_families),
        "minimum_families": [list(family) for family in minimum_families],
        "selected_family": list(selected),
        "selected_expectation_signatures": selected_signatures,
        "selected_plus_probabilities": plus_probabilities,
        "minimum_expectation_distance": text(minimum_expectation_distance),
        "closest_pairs": closest_pairs,
        "minimum_probability_distance": text(minimum_probability_distance),
        "sharp_unique_empirical_frequency_error": "strictly_less_than_1/12",
        "iid_bernoulli_sufficient_bound": {
            "failure_probability_upper_bound": "6*exp(-n/72)",
            "shots_per_setting_for_target_alpha": "ceiling(72*ln(6/alpha))",
            "assumptions": ["independent_repetitions", "stationary_binary_effects", "exact_calibration", "nearest_signature_decision"],
        },
        "aggregate_gates": {
            "three_atomic_binary_settings_are_sufficient": True,
            "no_one_or_two_atomic_setting_family_is_faithful": True,
            "imaginary_twist_quadrature_alone_resolves_G_H": True,
            "selected_expectation_margin_is_one_third": True,
            "binary_probability_margin_is_one_sixth": True,
            "empirical_frequency_radius_is_one_twelfth": True,
            "hoeffding_bound_is_conditional_not_source_noise_model": True,
            "raw_S_binary_effects_require_an_unresolved_apparatus_realization": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
