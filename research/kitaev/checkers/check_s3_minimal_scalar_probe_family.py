"""Exact minimal scalar probe family for the eight D(S3) anyon labels."""

import itertools
import json
from fractions import Fraction


def q(value):
    return Fraction(value)


def rational_text(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main():
    labels = ("A", "B", "C", "D", "E", "F", "G", "H")
    # Rows and columns use the same frozen label order. Entries are exact rationals.
    s_matrix = [
        [q(1)/6, q(1)/6, q(1)/3, q(1)/2, q(1)/2, q(1)/3, q(1)/3, q(1)/3],
        [q(1)/6, q(1)/6, q(1)/3, -q(1)/2, -q(1)/2, q(1)/3, q(1)/3, q(1)/3],
        [q(1)/3, q(1)/3, q(2)/3, 0, 0, -q(1)/3, -q(1)/3, -q(1)/3],
        [q(1)/2, -q(1)/2, 0, q(1)/2, -q(1)/2, 0, 0, 0],
        [q(1)/2, -q(1)/2, 0, -q(1)/2, q(1)/2, 0, 0, 0],
        [q(1)/3, q(1)/3, -q(1)/3, 0, 0, q(2)/3, -q(1)/3, -q(1)/3],
        [q(1)/3, q(1)/3, -q(1)/3, 0, 0, -q(1)/3, -q(1)/3, q(2)/3],
        [q(1)/3, q(1)/3, -q(1)/3, 0, 0, -q(1)/3, q(2)/3, -q(1)/3],
    ]
    twists = ("1", "1", "1", "1", "-1", "1", "omega", "omega2")
    probes = {"twist": twists}
    for row, reference in zip(s_matrix, labels):
        probes["S_" + reference] = tuple(row)

    def signature(label_index, probe_names):
        return tuple(probes[name][label_index] for name in probe_names)

    def faithful(probe_names):
        signatures = [signature(i, probe_names) for i in range(len(labels))]
        return len(set(signatures)) == len(labels)

    probe_names = tuple(probes)
    faithful_by_size = {}
    minimum_size = None
    minimum_families = []
    for size in range(1, len(probe_names) + 1):
        families = [family for family in itertools.combinations(probe_names, size) if faithful(family)]
        faithful_by_size[size] = families
        if families:
            minimum_size = size
            minimum_families = families
            break
    assert minimum_size == 3
    assert not faithful_by_size[1] and not faithful_by_size[2]
    witness = ("twist", "S_D", "S_F")
    assert witness in minimum_families and faithful(witness)

    witness_signatures = {
        label: [rational_text(value) if isinstance(value, (Fraction, int)) else value
                for value in signature(i, witness)]
        for i, label in enumerate(labels)
    }
    assert len({tuple(values) for values in witness_signatures.values()}) == 8

    # Exact two-probe obstructions explain the lower bound for the witness architecture.
    assert signature(labels.index("A"), ("twist", "S_F")) == signature(labels.index("B"), ("twist", "S_F"))
    assert signature(labels.index("C"), ("twist", "S_D")) == signature(labels.index("F"), ("twist", "S_D"))
    assert signature(labels.index("G"), ("S_D", "S_F")) == signature(labels.index("H"), ("S_D", "S_F"))

    # Twist resolves the centralizer-irrep kernel inside both nontrivial flux families.
    twist_resolves_transposition_irreps = twists[labels.index("D")] != twists[labels.index("E")]
    twist_resolves_cycle_irreps = len({twists[labels.index(x)] for x in ("F", "G", "H")}) == 3
    assert twist_resolves_transposition_irreps and twist_resolves_cycle_irreps

    result = {
        "schema": "marici.s3-minimal-scalar-probe-family.v1",
        "candidate_probe_surface": ["twist"] + ["S_" + label for label in labels],
        "anyon_label_order": list(labels),
        "minimum_probe_count": minimum_size,
        "minimum_family_count": len(minimum_families),
        "minimum_families": [list(family) for family in minimum_families],
        "selected_minimum_family": list(witness),
        "selected_family_signatures": witness_signatures,
        "two_probe_falsifiers": {
            "twist_plus_S_F_collides": ["A", "B"],
            "twist_plus_S_D_collides": ["C", "F"],
            "S_D_plus_S_F_collides": ["G", "H"],
        },
        "twist_resolves_D_E": twist_resolves_transposition_irreps,
        "twist_resolves_F_G_H": twist_resolves_cycle_irreps,
        "aggregate_gates": {
            "selected_three_probe_family_is_jointly_faithful": True,
            "no_one_probe_family_is_faithful": True,
            "no_two_probe_family_is_faithful": True,
            "minimum_is_exhaustive_over_frozen_surface": True,
            "twist_closes_pure_charge_centralizer_irrep_kernel": True,
            "reference_Hopf_link_probes_separate_remaining_charge_flux_collisions": True,
            "probe_minimality_is_surface_relative_not_absolute": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
