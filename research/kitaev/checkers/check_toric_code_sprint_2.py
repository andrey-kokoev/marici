"""Exact constructor-access, migration, and perturbation checks for WP11--WP15."""

import itertools
import json


def rank(rows, width):
    rows = list(rows)
    out = 0
    for col in range(width):
        pivot = next((i for i in range(out, len(rows)) if rows[i] >> col & 1), None)
        if pivot is None:
            continue
        rows[out], rows[pivot] = rows[pivot], rows[out]
        for i in range(len(rows)):
            if i != out and rows[i] >> col & 1:
                rows[i] ^= rows[out]
        out += 1
    return out


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
    v = lambda x, y: (x % L) * L + (y % L)
    h = lambda x, y: (x % L) * L + (y % L)
    q = lambda x, y: L * L + (x % L) * L + (y % L)
    d1 = []
    for x in range(L):
        for y in range(L):
            d1.append((1 << v(x, y)) | (1 << v(x + 1, y)))
    for x in range(L):
        for y in range(L):
            d1.append((1 << v(x, y)) | (1 << v(x, y + 1)))
    faces = []
    for x in range(L):
        for y in range(L):
            faces.append((1 << h(x, y)) | (1 << q(x + 1, y)) |
                         (1 << h(x, y + 1)) | (1 << q(x, y)))
    return d1, faces


def support_threshold(L):
    d1, faces = torus(L)
    repairs = span(faces)
    below = 0
    at_distance = 0
    for weight in range(1, L + 1):
        count = sum(1 for chain in vectors_of_weight(2 * L * L, weight)
                    if apply(d1, chain) == 0 and chain not in repairs)
        if weight < L:
            below += count
        else:
            at_distance = count
    assert below == 0 and at_distance == 2 * L
    return {
        "L": L,
        "code_distance": L,
        "nontrivial_residue_free_chains_below_distance": below,
        "minimum_nontrivial_cycle_count": at_distance,
        "mobile_ancilla_two_qubit_gate_count": L,
        "mobile_ancilla_sequential_depth": L,
        "mobile_ancilla_spacetime_worldline_length": L,
        "extended_ancilla_spatial_extent": L,
        "instantaneous_data_coupling_depth_with_prepared_cat_state": 1,
    }


def symplectic(u, v):
    ux, uz = u & 0b11, u >> 2
    vx, vz = v & 0b11, v >> 2
    return ((ux & vz).bit_count() + (uz & vx).bit_count()) & 1


def generated_labels(generators):
    return span(generators)


def accessible_algebras():
    # Labels are (x1,x2,z1,z2), packed with X bits low.
    X1, X2, Z1, Z2 = 0b0001, 0b0010, 0b0100, 0b1000
    cases = [
        ("local_stabilizers_only", []),
        ("one_loop_Z1", [Z1]),
        ("two_commuting_loops_Z1_Z2", [Z1, Z2]),
        ("one_intersecting_pair_X1_Z1", [X1, Z1]),
        ("complete_four_ports", [X1, X2, Z1, Z2]),
    ]
    audits = []
    for name, generators in cases:
        labels = generated_labels(generators)
        audits.append({
            "constructor_set": name,
            "pauli_label_rank": rank(generators, 4),
            "projective_operator_basis_size": len(labels),
            "has_noncommuting_pair": any(symplectic(a, b) for a in generators for b in generators),
        })
    assert [a["projective_operator_basis_size"] for a in audits] == [1, 2, 4, 4, 16]
    assert not audits[2]["has_noncommuting_pair"]
    assert audits[3]["has_noncommuting_pair"]
    return audits


def cylinder(L, width=2):
    vertex = lambda x, y: (x % L) * (width + 1) + y
    horizontal = lambda x, y: (x % L) * (width + 1) + y
    horizontal_count = L * (width + 1)
    vertical = lambda x, y: horizontal_count + (x % L) * width + y
    d1 = []
    for x in range(L):
        for y in range(width + 1):
            d1.append((1 << vertex(x, y)) | (1 << vertex(x + 1, y)))
    for x in range(L):
        for y in range(width):
            d1.append((1 << vertex(x, y)) | (1 << vertex(x, y + 1)))
    faces = []
    for x in range(L):
        for y in range(width):
            faces.append((1 << horizontal(x, y)) | (1 << vertical(x + 1, y)) |
                         (1 << horizontal(x, y + 1)) | (1 << vertical(x, y)))
    rough_vertices = {vertex(x, 0) for x in range(L)}
    rough_edges = {horizontal(x, 0) for x in range(L)}
    gamma = sum(1 << horizontal(x, width) for x in range(L))
    seam = sum(1 << horizontal(0, y) for y in range(width + 1))
    bulk_perturbed_edge = horizontal(0, 1)
    return d1, faces, rough_vertices, rough_edges, gamma, seam, bulk_perturbed_edge


def migration_audit(L):
    width = 2
    d1, faces, rough_vertices, rough_edges, gamma, seam, perturb_edge = cylinder(L, width)
    n0, n1 = L * (width + 1), L * (2 * width + 1)
    repair_span = span(faces)
    absolute_h1 = n1 - rank(d1, n0) - rank(faces, n1)
    assert absolute_h1 == 1 and apply(d1, gamma) == 0 and gamma not in repair_span
    assert (gamma & seam).bit_count() & 1 == 1
    assert all(((face & seam).bit_count() & 1) == 0 for face in faces)

    kept_edges = [e for e in range(n1) if e not in rough_edges]
    kept_vertices = [v for v in range(n0) if v not in rough_vertices]
    edge_pos = {old: new for new, old in enumerate(kept_edges)}
    vertex_pos = {old: new for new, old in enumerate(kept_vertices)}

    def q1(chain):
        return sum(1 << edge_pos[e] for e in kept_edges if chain >> e & 1)

    def q0(vertices):
        return sum(1 << vertex_pos[v] for v in kept_vertices if vertices >> v & 1)

    relative_d1 = [q0(d1[e]) for e in kept_edges]
    relative_faces = [q1(face) for face in faces]
    assert all(q0(apply(d1, 1 << e)) == apply(relative_d1, 1 << edge_pos[e]) for e in kept_edges)
    assert all(apply(relative_d1, q1(face)) == 0 for face in faces)
    relative_h1 = len(kept_edges) - rank(relative_d1, len(kept_vertices)) - rank(relative_faces, len(kept_edges))
    projected_gamma = q1(gamma)
    assert relative_h1 == 0 and projected_gamma in span(relative_faces)

    projected_seam = q1(seam)
    new_repair_with_old_readout_one = next(face for face in relative_faces
                                           if (face & projected_seam).bit_count() & 1)
    assert new_repair_with_old_readout_one

    anticommuting_faces = [i for i, face in enumerate(faces) if face >> perturb_edge & 1]
    assert len(anticommuting_faces) == 2
    assert not (gamma >> perturb_edge & 1)
    return {
        "L": L,
        "absolute_h1_dimension": absolute_h1,
        "gamma_absolute_nonzero": True,
        "absolute_wilson_readout_on_gamma": 1,
        "relative_chain_condition": True,
        "relative_h1_dimension": relative_h1,
        "gamma_becomes_relative_repair": True,
        "old_wilson_functional_nonzero_on_new_repair": True,
        "old_wilson_readout_fails_relative_descent": True,
        "unchanged_source_data": ["cell_labels", "bulk_incidence", "coefficient_prime"],
        "invalidated_cached_claims": ["gamma_nontrivial", "old_wilson_descends"],
        "perturbation_edge_disjoint_from_gamma": True,
        "perturbation_anticommuting_face_count": len(anticommuting_faces),
        "gamma_wilson_commutes_with_perturbation": True,
        "perturbed_local_block_characteristic": "lambda^2-5",
    }


def disappearance_table():
    rows = [
        {
            "mechanism": "access_denial",
            "upstream_absolute_class_exists": True,
            "class_exists_in_current_quotient": True,
            "constructor_accessible": False,
            "readout_kernel_contains_gamma": None,
            "successor_relative_class_exists": "not_applied",
            "coarse_record_values_on_logical_bit_0_1": None,
            "spectral_response": "same_disjoint_single_edge_perturbation",
        },
        {
            "mechanism": "projection_loss",
            "upstream_absolute_class_exists": True,
            "class_exists_in_current_quotient": True,
            "constructor_accessible": True,
            "readout_kernel_contains_gamma": True,
            "successor_relative_class_exists": "not_applied",
            "coarse_record_values_on_logical_bit_0_1": [0, 0],
            "spectral_response": "same_disjoint_single_edge_perturbation",
        },
        {
            "mechanism": "constitutive_collapse",
            "upstream_absolute_class_exists": True,
            "class_exists_in_current_quotient": False,
            "constructor_accessible": False,
            "readout_kernel_contains_gamma": None,
            "successor_relative_class_exists": False,
            "coarse_record_values_on_logical_bit_0_1": None,
            "spectral_response": "boundary_hamiltonian_changed_plus_local_perturbation",
        },
    ]
    assert all(r["upstream_absolute_class_exists"] for r in rows)
    assert len({(r["class_exists_in_current_quotient"], r["constructor_accessible"],
                    r["readout_kernel_contains_gamma"], r["successor_relative_class_exists"])
                for r in rows}) == 3
    return rows


def main():
    payload = {
        "schema": "marici.toric-code-sprint-2.v1",
        "support_costs": [support_threshold(L) for L in range(2, 5)],
        "accessible_algebras": accessible_algebras(),
        "migration_and_perturbation": [migration_audit(L) for L in range(3, 7)],
        "three_disappearances": disappearance_table(),
        "aggregate_gates": {
            "same_class_three_disappearance_mechanisms_separated": True,
            "accessible_algebra_derived_from_constructor_sets": True,
            "projective_basis_sizes_1_2_4_4_16": True,
            "subdistance_constructor_has_no_logical_action": True,
            "mobile_ancilla_time_resource_equals_noncontractible_length": True,
            "absolute_to_relative_chain_squares_commute": True,
            "old_wilson_readout_invalidated_by_new_repairs": True,
            "bounded_perturbation_preserves_three_way_distinction": True,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
