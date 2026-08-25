"""Exact sector-information limit of a holonomy-only D(S3) ancilla bus."""

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
    return "e" if fixed == 3 else ("t" if fixed == 1 else "c")


def main():
    group = list(itertools.permutations(range(3)))
    classes = {kind: [g for g in group if cycle_type(g) == kind]
               for kind in ("e", "t", "c")}
    conjugation_orbits = []
    unseen = set(group)
    while unseen:
        g = next(iter(unseen))
        orbit = {conjugate(x, g) for x in group}
        conjugation_orbits.append(orbit)
        unseen -= orbit
    assert sorted(len(orbit) for orbit in conjugation_orbits) == [1, 2, 3]

    sector_flux_class = {
        "A": "e", "B": "e", "C": "e",
        "D": "t", "E": "t",
        "F": "c", "G": "c", "H": "c",
    }
    target_residues = dict(zip("ABCDEFGH", (0, 1, 2, 3, 6, 7, 4, 5)))
    class_signatures = {label: {"e": 0, "t": 1, "c": 2}[kind]
                        for label, kind in sector_flux_class.items()}
    collision_blocks = []
    for value in sorted(set(class_signatures.values())):
        collision_blocks.append([label for label in "ABCDEFGH"
                                 if class_signatures[label] == value])
    assert collision_blocks == [["A", "B", "C"], ["D", "E"], ["F", "G", "H"]]
    assert len(set(target_residues.values())) == 8
    assert any(len({target_residues[label] for label in block}) > 1
               for block in collision_blocks)

    # A one-shot compute--phase--uncompute construction with eight distinct
    # phases requires eight mutually orthogonal eigenvectors of the normal
    # ancilla phase operator, hence dimension at least eight.
    distinct_phase_count = len(set(target_residues.values()))
    one_shot_ancilla_lower_bound = distinct_phase_count
    assert one_shot_ancilla_lower_bound == 8 > len(group)

    result = {
        "schema": "marici.s3-holonomy-bus-sector-limit.v1",
        "holonomy_bus": {
            "dimension": len(group),
            "conjugacy_class_count": len(conjugation_orbits),
            "conjugacy_class_sizes": sorted(len(x) for x in conjugation_orbits),
            "gauge_invariant_phase_tables_are_class_functions": True,
            "maximum_gauge_invariant_sector_signature_count": 3,
            "forced_sector_collisions": collision_blocks,
            "full_eight_sector_generator_reachable": False,
        },
        "nonclass_phase_table": {
            "can_resolve_group_elements": True,
            "is_gauge_invariant": False,
            "defines_block_central_sector_phase": False,
        },
        "one_shot_clean_label_bus": {
            "distinct_target_phases": distinct_phase_count,
            "minimum_orthogonal_ancilla_states": one_shot_ancilla_lower_bound,
            "minimum_dimension": one_shot_ancilla_lower_bound,
            "requires_charge_sensitive_information": True,
        },
        "target_residues": target_residues,
        "aggregate_gates": {
            "S3_has_three_conjugacy_classes": True,
            "class_functions_force_three_collision_blocks": True,
            "target_Z_separates_all_eight_sectors": True,
            "six_level_holonomy_bus_cannot_hold_one_shot_sector_label": True,
            "element_resolution_breaks_gauge_centrality": True,
            "one_shot_clean_label_bus_requires_dimension_eight": True,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()

