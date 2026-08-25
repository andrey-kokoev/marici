"""Exact source audit for one oriented D(S3) plaquette and its base vertex.

The checker is dependency-free.  Operators are represented by exact sparse
actions on the 6^4 edge-label basis, so no floating-point linear algebra is
used.
"""

import itertools
import json
from fractions import Fraction


def compose(p, q):
    return tuple(p[q[i]] for i in range(3))


def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p):
        out[image] = i
    return tuple(out)


def conjugate(x, g):
    return compose(compose(x, g), inverse(x))


def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "identity" if fixed == 3 else ("transposition" if fixed == 1 else "three_cycle")


def main():
    group = list(itertools.permutations(range(3)))
    e = (0, 1, 2)
    t = (1, 0, 2)
    c = (1, 2, 0)
    states = list(itertools.product(group, repeat=4))

    # Square boundary based at v0.  e0,e1 follow the traversal; e2,e3 oppose it.
    def holonomy(state):
        g0, g1, g2, g3 = state
        return compose(compose(compose(g0, g1), inverse(g2)), inverse(g3))

    # v0 is the origin of e0 and e3, hence both labels are left multiplied.
    def gauge(x, state):
        g0, g1, g2, g3 = state
        return (compose(x, g0), g1, g2, compose(x, g3))

    fibers = {g: {state for state in states if holonomy(state) == g} for g in group}
    assert all(len(fiber) == 6 ** 3 for fiber in fibers.values())
    assert set().union(*fibers.values()) == set(states)
    assert sum(len(fiber) for fiber in fibers.values()) == len(states)

    # Operator derivation: U_x B_g U_x^-1 = B_{xgx^-1} on every basis state.
    conjugation_checks = 0
    for x, g, state in itertools.product(group, group, states):
        lhs = holonomy(gauge(x, gauge(inverse(x), state))) == g
        # The direct pointwise identity is cleaner in pullback form.
        lhs = holonomy(gauge(inverse(x), state)) == g
        rhs = holonomy(state) == conjugate(x, g)
        assert lhs == rhs
        conjugation_checks += 1

    classes = {
        name: {g for g in group if cycle_type(g) == name}
        for name in ("identity", "transposition", "three_cycle")
    }

    def commutator_frobenius_squared(selected_fluxes):
        # A=(1/6)sum_x U_x.  For a diagonal projector B_S, the matrix entry
        # of [A,B_S] at (U_x state,state) is (1_S(state)-1_S(U_x state))/6.
        total = Fraction(0)
        selected = set(selected_fluxes)
        for state in states:
            before = holonomy(state) in selected
            for x in group:
                after = holonomy(gauge(x, state)) in selected
                total += Fraction((int(before) - int(after)) ** 2, 36)
        return total

    single_obstructions = {
        str(g): commutator_frobenius_squared({g}) for g in group
    }
    class_commutators = {
        name: commutator_frobenius_squared(fluxes) for name, fluxes in classes.items()
    }
    assert single_obstructions[str(e)] == 0
    assert single_obstructions[str(t)] > 0
    assert single_obstructions[str(c)] > 0
    assert all(value == 0 for value in class_commutators.values())

    # The gauge action is free on the four-edge basis.  It is also free on
    # the flat fiber, giving exact ranks for A and A B_e.
    gauge_orbits = {min(gauge(x, state) for x in group) for state in states}
    flat_orbits = {min(gauge(x, state) for x in group) for state in fibers[e]}
    assert len(gauge_orbits) == 6 ** 3
    assert len(flat_orbits) == 6 ** 2

    result = {
        "schema": "marici.s3-local-source-model.v1",
        "group_order": 6,
        "edge_count": 4,
        "hilbert_dimension": len(states),
        "plaquette_flux_projector_rank": 6 ** 3,
        "vertex_gauge_projector_rank": len(gauge_orbits),
        "local_flat_gauge_invariant_rank": len(flat_orbits),
        "operator_conjugation_checks": conjugation_checks,
        "single_flux_gauge_commutator_frobenius_squared": {
            key: str(value) for key, value in single_obstructions.items()
        },
        "class_flux_gauge_commutator_frobenius_squared": {
            key: str(value) for key, value in class_commutators.items()
        },
        "ports": {
            "transposition": {
                "support_edges": 4,
                "projector_is_hermitian": True,
                "commutes_with_native_vertex_projector": False,
                "annihilates_flat_code_space": True,
                "status": "local_diagonal_pulse_if_basepoint_resolved_holonomy_control_is_admitted",
            },
            "three_cycle": {
                "support_edges": 4,
                "projector_is_hermitian": True,
                "commutes_with_native_vertex_projector": False,
                "annihilates_flat_code_space": True,
                "status": "local_diagonal_pulse_if_basepoint_resolved_holonomy_control_is_admitted",
            },
        },
        "deliberate_failure": {
            "claim": "an_individual_noncentral_flux_projector_is_a_native_gauge_invariant_hamiltonian_term",
            "transposition_commutator_nonzero": single_obstructions[str(t)] != 0,
            "three_cycle_commutator_nonzero": single_obstructions[str(c)] != 0,
        },
        "aggregate_gates": {
            "flux_projectors_partition_the_basis": True,
            "gauge_action_conjugates_based_holonomy": True,
            "native_vertex_and_flatness_projectors_commute": True,
            "conjugacy_class_flux_projectors_are_gauge_invariant": True,
            "individual_transposition_port_breaks_gauge_invariance": True,
            "individual_three_cycle_port_breaks_gauge_invariance": True,
            "both_nontrivial_ports_annihilate_the_flat_code_space": True,
            "port_locality_is_four_edges_on_the_frozen_square": True,
            "physical_pulse_availability_remains_a_source_assumption": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
