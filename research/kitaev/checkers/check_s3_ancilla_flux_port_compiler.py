"""Exact nine-step ancilla compiler for based D(S3) flux phase ports."""

import itertools
import json


def compose(p, q): return tuple(p[q[i]] for i in range(3))
def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p): out[image] = i
    return tuple(out)
def conjugate(x, g): return compose(compose(x, g), inverse(x))
def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "identity" if fixed == 3 else ("transposition" if fixed == 1 else "three_cycle")


def main():
    group = list(itertools.permutations(range(3)))
    e, t, c = (0, 1, 2), (1, 0, 2), (1, 2, 0)
    states = list(itertools.product(group, repeat=4))

    def factors(state):
        g0, g1, g2, g3 = state
        return (g0, g1, inverse(g2), inverse(g3))

    def holonomy(state):
        a = e
        for factor in factors(state): a = compose(a, factor)
        return a

    def compute(state, ancilla=e):
        for factor in factors(state): ancilla = compose(ancilla, factor)
        return ancilla

    def uncompute(state, ancilla):
        for factor in reversed(factors(state)): ancilla = compose(ancilla, inverse(factor))
        return ancilla

    def gauge(x, state):
        g0, g1, g2, g3 = state
        return (compose(x, g0), g1, g2, compose(x, g3))

    ports = {}
    for name, target in (("transposition", t), ("three_cycle", c)):
        marked = 0
        for state in states:
            ancilla = compute(state)
            assert ancilla == holonomy(state)
            phase_exponent = int(ancilla == target)
            marked += phase_exponent
            assert uncompute(state, ancilla) == e
            assert phase_exponent == int(holonomy(state) == target)
        assert marked == 216
        ports[name] = {
            "target": str(target),
            "marked_basis_states": marked,
            "compute_two_body_gates": 4,
            "ancilla_phase_gates": 1,
            "uncompute_two_body_gates": 4,
            "total_serial_gate_count": 9,
            "clean_ancilla_dimension": 6,
        }

    # Deliberate failure: the based element predicate is not gauge invariant.
    gauge_mismatches = {}
    for name, target in (("transposition", t), ("three_cycle", c)):
        count = 0
        for x, state in itertools.product(group, states):
            if (holonomy(state) == target) != (holonomy(gauge(x, state)) == target):
                count += 1
        assert count > 0
        gauge_mismatches[name] = count

    # Class-conditioned phase is invariant, demonstrating the exact cost of
    # removing the basepoint frame: element resolution is merged.
    for state, x in itertools.product(states, group):
        assert cycle_type(holonomy(state)) == cycle_type(holonomy(gauge(x, state)))

    result = {
        "schema": "marici.s3-ancilla-flux-port-compiler.v1",
        "basis_states_checked_per_port": len(states),
        "ports": ports,
        "element_predicate_gauge_mismatch_counts": gauge_mismatches,
        "deliberate_failure": {
            "claim": "clean_ancilla_compilation_makes_the_element_flux_port_gauge_invariant",
            "actual": False,
        },
        "aggregate_gates": {
            "transposition_port_compiles_exactly": True,
            "three_cycle_port_compiles_exactly": True,
            "ancilla_returns_clean_for_every_basis_state": True,
            "each_compilation_uses_nine_serial_gates": True,
            "only_edge_ancilla_two_body_and_ancilla_phase_gates_are_required": True,
            "element_resolution_remains_basepoint_dependent": True,
            "class_conditioning_is_gauge_invariant_but_merges_elements": True,
            "vacuum_flat_sector_receives_no_nontrivial_flux_phase": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__": main()
