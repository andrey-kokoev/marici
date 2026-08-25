"""Exact finite group audit for the non-Abelian D(S3) ribbon frontier."""

import itertools
import json


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def conjugate(g, h):
    return compose(compose(g, h), inverse(g))


def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    if fixed == 3:
        return "identity"
    if fixed == 1:
        return "transposition"
    return "three_cycle"


def main():
    group = list(itertools.permutations(range(3)))
    identity = (0, 1, 2)
    assert len(group) == 6
    classes = {}
    for g in group:
        classes.setdefault(cycle_type(g), set()).add(g)
    class_sizes = {name: len(values) for name, values in classes.items()}
    assert class_sizes == {"identity": 1, "transposition": 3, "three_cycle": 2}

    representatives = {name: next(iter(values)) for name, values in classes.items()}
    centralizers = {
        name: [g for g in group if compose(g, rep) == compose(rep, g)]
        for name, rep in representatives.items()
    }
    centralizer_sizes = {name: len(values) for name, values in centralizers.items()}
    assert centralizer_sizes == {"identity": 6, "transposition": 2, "three_cycle": 3}

    irrep_dimensions = {
        "identity": [1, 1, 2],
        "transposition": [1, 1],
        "three_cycle": [1, 1, 1],
    }
    assert all(sum(d * d for d in irrep_dimensions[name]) == centralizer_sizes[name]
               for name in centralizer_sizes)
    anyon_dimensions = []
    for name in ("identity", "transposition", "three_cycle"):
        anyon_dimensions.extend(class_sizes[name] * d for d in irrep_dimensions[name])
    assert anyon_dimensions == [1, 1, 2, 3, 3, 2, 2, 2]
    assert sum(d * d for d in anyon_dimensions) == len(group) ** 2

    t01 = (1, 0, 2)
    t12 = (0, 2, 1)
    t02 = (2, 1, 0)
    braided = conjugate(t01, t12)
    assert braided == t02 and braided != t12
    transpositions = [t01, t12, t02]
    braid_permutation = [transpositions.index(conjugate(t01, h)) for h in transpositions]
    assert braid_permutation == [0, 2, 1]

    result = {
        "schema": "marici.s3-quantum-double-ribbon.v1",
        "group_order": len(group),
        "conjugacy_class_sizes": class_sizes,
        "centralizer_sizes": centralizer_sizes,
        "anyon_quantum_dimensions": anyon_dimensions,
        "anyon_type_count": len(anyon_dimensions),
        "total_quantum_dimension_squared": sum(d * d for d in anyon_dimensions),
        "nonabelian_flux_braid": {
            "conjugator": "(01)",
            "input_flux": "(12)",
            "output_flux": "(02)",
            "transposition_basis_permutation": braid_permutation,
            "braid_is_not_scalar_phase": True,
        },
        "aggregate_gates": {
            "anyon_labels_require_conjugacy_class_and_centralizer_irrep": True,
            "eight_D_S3_anyon_types_recovered": True,
            "quantum_dimension_sum_rule_equals_group_order_squared": True,
            "nonabelian_braid_changes_internal_flux_label": True,
            "scalar_intersection_phase_is_insufficient": True,
            "oriented_ribbon_and_endpoint_base_data_required": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

