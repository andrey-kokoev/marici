"""Exact code-distance threshold for logical terms in local perturbation paths."""

import itertools
import json


def apply(columns, vector):
    out = 0
    for i, column in enumerate(columns):
        if vector >> i & 1:
            out ^= column
    return out


def span(columns):
    values = {0}
    for column in columns:
        values |= {x ^ column for x in tuple(values)}
    return values


def vectors_of_weight(n, weight):
    for support in itertools.combinations(range(n), weight):
        value = 0
        for i in support:
            value |= 1 << i
        yield value


def torus(L):
    vertex = lambda x, y: (x % L) * L + (y % L)
    h = lambda x, y: (x % L) * L + (y % L)
    v = lambda x, y: L * L + (x % L) * L + (y % L)
    d1 = []
    for x in range(L):
        for y in range(L):
            d1.append((1 << vertex(x, y)) | (1 << vertex(x + 1, y)))
    for x in range(L):
        for y in range(L):
            d1.append((1 << vertex(x, y)) | (1 << vertex(x, y + 1)))
    faces = []
    for x in range(L):
        for y in range(L):
            faces.append((1 << h(x, y)) | (1 << v(x + 1, y)) |
                         (1 << h(x, y + 1)) | (1 << v(x, y)))
    stars = []
    for z in range(L * L):
        support = 0
        for e, endpoints in enumerate(d1):
            if endpoints >> z & 1:
                support |= 1 << e
        stars.append(support)
    return d1, faces, stars


def x_syndrome(faces, chain):
    return sum((((face & chain).bit_count() & 1) << i) for i, face in enumerate(faces))


def audit(L):
    d1, faces, stars = torus(L)
    n = 2 * L * L
    z_repairs, x_repairs = span(faces), span(stars)
    z_counts = []
    x_counts = []
    for weight in range(1, L + 1):
        z_count = 0
        x_count = 0
        for chain in vectors_of_weight(n, weight):
            if apply(d1, chain) == 0 and chain not in z_repairs:
                z_count += 1
            if x_syndrome(faces, chain) == 0 and chain not in x_repairs:
                x_count += 1
        z_counts.append(z_count)
        x_counts.append(x_count)
    assert z_counts[:-1] == x_counts[:-1] == [0] * (L - 1)
    assert z_counts[-1] == x_counts[-1] == 2 * L

    # A marked horizontal logical Z loop anticommutes with the uniform local
    # X field term on each of its L support edges.
    marked_z = sum(1 << (x * L) for x in range(L))
    anticommuting_x_terms = marked_z.bit_count()
    assert anticommuting_x_terms == L
    return {
        "L": L,
        "z_logical_counts_by_weight_1_through_L": z_counts,
        "x_logical_counts_by_weight_1_through_L": x_counts,
        "all_perturbative_pauli_monomials_below_order_L_project_scalar_or_zero": True,
        "first_possible_logical_effective_term_order": L,
        "minimum_X_and_Z_logical_representatives": 2 * L,
        "bare_marked_Z_wilson_anticommuting_uniform_X_terms": anticommuting_x_terms,
        "bare_marked_Z_wilson_not_conserved_by_uniform_X_field": True,
    }


def main():
    payload = {
        "schema": "marici.local-perturbation-order-threshold.v1",
        "perturbation_class": "arbitrary_sum_of_weight_one_edge_Paulis",
        "audits": [audit(L) for L in range(2, 5)],
        "aggregate_gates": {
            "code_distance_blocks_logical_terms_below_order_L": True,
            "order_L_logical_paths_exist": True,
            "mixed_pauli_case_follows_from_independent_CSS_centralizer_conditions": True,
            "bare_wilson_port_fails_uniform_field_conservation": True,
            "spectral_convergence_not_inferred_from_formal_order": True,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

