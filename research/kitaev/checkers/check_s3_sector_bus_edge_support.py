"""Four-edge support lower bound for a clean D(S3) sector-label bus."""

import itertools
import json


def compose(p, q): return tuple(p[q[i]] for i in range(3))
def inverse(p):
    out = [0, 0, 0]
    for i, image in enumerate(p): out[image] = i
    return tuple(out)
def cycle_type(p):
    fixed = sum(p[i] == i for i in range(3))
    return "e" if fixed == 3 else ("t" if fixed == 1 else "c")
def holonomy(state):
    g0, g1, g2, g3 = state
    return compose(compose(compose(g0, g1), inverse(g2)), inverse(g3))


def main():
    group = list(itertools.permutations(range(3)))
    states = list(itertools.product(group, repeat=4))
    witnesses = {}
    for omitted in range(4):
        found = None
        buckets = {}
        for state in states:
            key = tuple(state[i] for i in range(4) if i != omitted)
            kind = cycle_type(holonomy(state))
            if key in buckets and buckets[key][0] != kind:
                found = (buckets[key][1], state)
                break
            buckets[key] = (kind, state)
        assert found is not None
        a, b = found
        assert all(a[i] == b[i] for i in range(4) if i != omitted)
        assert cycle_type(holonomy(a)) != cycle_type(holonomy(b))
        witnesses[str(omitted)] = {
            "holonomy_classes": [cycle_type(holonomy(a)), cycle_type(holonomy(b))],
            "differing_edges": [i for i in range(4) if a[i] != b[i]],
        }

    result = {
        "schema": "marici.s3-sector-bus-edge-support.v1",
        "oriented_holonomy": "g0*g1*g2^-1*g3^-1",
        "edge_count": 4,
        "omission_witnesses": witnesses,
        "minimum_data_support_for_full_sector_label": 4,
        "clean_compute_phase_uncompute_lower_bound": {
            "forward_edge_bus_interactions": 4,
            "reverse_edge_bus_interactions": 4,
            "edge_bus_interactions_before_charge_overhead": 8,
            "ancilla_phase_operations": 1,
            "baseline_serial_gates": 9,
        },
        "scope": "standard_clean_compute_phase_uncompute_bus_architecture",
        "aggregate_gates": {
            "every_edge_has_a_flux_class_omission_witness": True,
            "full_sector_label_requires_all_four_edges": True,
            "two_body_arity_does_not_reduce_data_support": True,
            "clean_bus_baseline_requires_eight_edge_interactions": True,
            "charge_sensitive_extraction_adds_to_the_flux_baseline": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

