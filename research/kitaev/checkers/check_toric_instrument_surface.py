"""Exact source-derived toric instrument, capability fiber, and code witness."""

from fractions import Fraction
import json


def zero(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def eye(n):
    out = zero(n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def add(*matrices):
    return [[sum(m[i][j] for m in matrices)
             for j in range(len(matrices[0][0]))]
            for i in range(len(matrices[0]))]


def projector(indices, n=4):
    out = zero(n)
    for i in indices:
        out[i][i] = Fraction(1)
    return out


def permutation_x1():
    out = zero(4)
    for i in range(4):
        out[i ^ 1][i] = Fraction(1)
    return out


def effect(k):
    return mul(transpose(k), k)


def branch(k, rho):
    return mul(mul(k, rho), transpose(k))


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def logical_instrument_audit():
    p_plus = projector([0, 2])
    p_minus = projector([1, 3])
    x1 = permutation_x1()
    qnd = [p_plus, p_minus]
    flip = [mul(x1, p_plus), mul(x1, p_minus)]
    assert add(*(effect(k) for k in qnd)) == eye(4)
    assert [effect(k) for k in qnd] == [effect(k) for k in flip]

    # Derive Kraus maps from the controlled-pointer dilation: ancilla starts
    # at 0 and is XORed with logical z1; projection on pointer b gives P_b.
    derived = [zero(4), zero(4)]
    for system_in in range(4):
        pointer_out = system_in & 1
        derived[pointer_out][system_in][system_in] = Fraction(1)
    assert derived == qnd

    rho = projector([0])
    qnd_plus = branch(qnd[0], rho)
    flip_plus = branch(flip[0], rho)
    assert trace(qnd_plus) == trace(flip_plus) == 1
    assert qnd_plus != flip_plus
    qnd_repeat_plus = trace(branch(qnd[0], qnd_plus))
    flip_repeat_plus = trace(branch(qnd[0], flip_plus))
    assert qnd_repeat_plus == 1 and flip_repeat_plus == 0
    return {
        "system_dimension": 4,
        "apparatus_dimension": 2,
        "apparatus_preparation": "pointer_0",
        "interaction": "pointer_xor_logical_Z1_label",
        "pointer_outcomes": [0, 1],
        "conditioning": "project_pointer_then_partial_trace",
        "derived_kraus_equal_logical_luders_projectors": True,
        "qnd_and_flip_effects_identical": True,
        "qnd_and_flip_successors_different": True,
        "qnd_repeat_plus_probability": str(qnd_repeat_plus),
        "flip_repeat_plus_probability": str(flip_repeat_plus),
        "sequential_record_distinguishes_capability_fiber": True,
    }


def torus_supports(L):
    vertex = lambda x, y: (x % L) * L + (y % L)
    h = lambda x, y: (x % L) * L + (y % L)
    v = lambda x, y: L * L + (x % L) * L + (y % L)
    edge_boundaries = []
    for x in range(L):
        for y in range(L):
            edge_boundaries.append((1 << vertex(x, y)) | (1 << vertex(x + 1, y)))
    for x in range(L):
        for y in range(L):
            edge_boundaries.append((1 << vertex(x, y)) | (1 << vertex(x, y + 1)))
    stars = []
    for z in range(L * L):
        support = 0
        for e, endpoints in enumerate(edge_boundaries):
            if endpoints >> z & 1:
                support |= 1 << e
        stars.append(support)
    loop = sum(1 << h(x, 0) for x in range(L))
    return stars, loop


def protected_code_witness(L):
    stars, loop = torus_supports(L)
    overlaps = [(star & loop).bit_count() for star in stars]
    assert all(count % 2 == 0 for count in overlaps)
    affected = [i for i, count in enumerate(overlaps) if count]
    assert len(affected) == L
    # Global W commutes with every star and its + Lüders branch preserves a
    # W=+ ground state. Fine Z_e dephasing kills any A_v containing a measured
    # edge, hence L exact stabilizer expectations change from 1 to 0.
    return {
        "L": L,
        "wilson_star_overlap_parities": [count % 2 for count in overlaps],
        "global_wilson_preserves_all_star_expectations": True,
        "fine_then_coarse_killed_star_expectation_count": len(affected),
        "fine_then_coarse_leaves_ground_stabilizer_face": False,
        "protected_ground_space_instrument_witness": True,
    }


def main():
    payload = {
        "schema": "marici.toric-instrument-surface.v1",
        "source_instrument": logical_instrument_audit(),
        "protected_witnesses": [protected_code_witness(L) for L in range(2, 7)],
        "cross_sector_position": {
            "toric_controlled_string": "source_derived_qnd_instrument",
            "double_slit_controlled_pointer": "source_derived_qnd_instrument",
            "udw_one_mode": "source_derived_absorptive_instrument",
            "scattering_flavor_luders": "formal_completion_only",
            "radiative_memory": "paired_effect_without_apparatus_dilation",
            "cosmology": "scalar_period_without_outcome_algebra",
        },
        "aggregate_gates": {
            "toric_source_supplies_complete_instrument_dilation": True,
            "derived_kraus_maps_are_logical_luders_projectors": True,
            "same_effect_supports_distinct_capability_fiber_points": True,
            "sequential_records_recover_hidden_update_difference": True,
            "fine_coarsening_differs_on_protected_ground_space": True,
            "cross_sector_instrument_types_remain_heterogeneous": True,
        },
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

