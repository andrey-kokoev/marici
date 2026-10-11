"""H3: quotient disjoint oriented cells by labelled interface matches.

The gluer uses no particle name or position. Geometry supplies the test fixtures'
orientations; endpoint labels determine the identification maps. Separate tests
show how much choice remains when cell inventories or interface labels are not
supplied. No automatic higher-cell completion is hidden in the gluer.
"""
from collections import defaultdict
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json

from check_common_assembly_symmetry import BASE, load_targets, affine_coordinates, determinant, vertex, cell
from check_common_assembly_cones import closure, invariants


def permutation_sign(sequence):
    return (-1)**sum(a > b for i, a in enumerate(sequence) for b in sequence[i+1:])


def orient(distances, cells):
    _, coordinates = affine_coordinates(distances)
    d = len(coordinates[0])
    center = tuple(sum(p[k] for p in coordinates)/len(coordinates) for k in range(d))
    out = []
    for c in sorted(cells):
        c = list(c)
        points = [tuple(sum(w*coordinates[i][k] for i, w in enumerate(v)) for k in range(d)) for v in c]
        value = determinant([[p[k]-center[k] for p in points] for k in range(d)])
        assert value != 0
        if value < 0:
            c[0], c[1] = c[1], c[0]
        out.append(tuple(c))
    return out


def glue(oriented_cells, protected=()):
    """Glue opposite-oriented facets by equal vertex labels; retain unpaired ones."""
    protected = {tuple(sorted(f)) for f in protected}
    assert len({tuple(sorted(c)) for c in oriented_cells}) == len(oriented_cells), 'Repeated top-cell records need a separate cellular, not simplicial, quotient'
    facets = defaultdict(list)
    parents = {}
    for ci, c in enumerate(oriented_cells):
        assert len(set(c)) == len(c)
        for v in c:
            parents[(ci, v)] = (ci, v)
        for i in range(len(c)):
            face = c[:i]+c[i+1:]
            key = tuple(sorted(face))
            sign = (-1)**i * permutation_sign(face)
            facets[key].append((ci, sign))
    def root(x):
        while parents[x] != x:
            parents[x] = parents[parents[x]]
            x = parents[x]
        return x
    def identify(a, b):
        parents[root(a)] = root(b)
    conflicts, blocked, seams, exposed = [], [], [], []
    for f, uses in sorted(facets.items()):
        if len(uses) > 2:
            conflicts.append('more than two cells incident to one facet')
        elif len(uses) == 2:
            (a, sa), (b, sb) = uses
            if sa != -sb:
                conflicts.append('equal induced orientations')
            elif f in protected:
                blocked.append(f)
            else:
                seams.append((a, b, f))
                for v in f:
                    identify((a, v), (b, v))
        else:
            exposed.append(f)
    if conflicts or blocked:
        return {'accepted': False, 'orientation_conflicts': len(conflicts),
                'protected_interface_conflicts': len(blocked)}
    # The quotient is formed from local occurrences, not by preidentifying all
    # equal labels before gluing. Disconnected vertex stars would be detected.
    classes = defaultdict(set)
    for occurrence in parents:
        classes[root(occurrence)].add(occurrence)
    class_labels = []
    for occurrences in classes.values():
        labels = {v for _, v in occurrences}
        assert len(labels) == 1
        class_labels.append(next(iter(labels)))
    expected_labels = {v for c in oriented_cells for v in c}
    assert set(class_labels) == expected_labels
    assert len(class_labels) == len(expected_labels), 'Facet gluing did not identify every occurrence of a vertex'
    # Relabel the quotient by its uniquely retained labels for exact comparison.
    label_of_class = {r: next(iter({v for _, v in occurrences})) for r, occurrences in classes.items()}
    quotient = {tuple(sorted(label_of_class[root((ci, x))] for x in c))
                for ci, c in enumerate(oriented_cells)}
    expected = {tuple(sorted(c)) for c in oriented_cells}
    assert quotient == expected
    stats = invariants(closure(quotient))
    adjacency = {(a, b) for a, b, _ in seams}
    seen = {0}
    while True:
        expanded = seen | {b for a, b in adjacency if a in seen} | {a for a, b in adjacency if b in seen}
        if expanded == seen:
            break
        seen = expanded
    return {'accepted': True, 'cell_count': len(quotient), 'quotient_vertices': len(classes),
            'identified_interfaces': len(seams), 'exposed_interfaces': len(exposed),
            'exact_quotient_matches_input_cells': True, 'topology': stats,
            'dual_graph_connected': len(seen) == len(oriented_cells),
            'orientation_solutions_for_fixed_inventory': 2 if len(seen) == len(oriented_cells) else None}


def barycentric_distance(a, b, distances):
    difference = [x-y for x, y in zip(a, b)]
    assert sum(difference) == 0
    return -sum(difference[i]*difference[j]*distances[i][j]
                for i in range(len(a)) for j in range(len(a)))/2


def interface_metric_choices(distances, cells):
    occurrences = []
    for ci, c in enumerate(cells):
        for face in combinations(c, len(c)-1):
            # A full distance-matrix canonicalization works in every facet size.
            key = min(tuple(barycentric_distance(order[i], order[j], distances)
                            for i in range(len(order)) for j in range(len(order)))
                      for order in permutations(face))
            occurrences.append((ci, tuple(sorted(face)), key))
    compatible = [(a, b) for a, b in combinations(occurrences, 2) if a[0] != b[0] and a[2] == b[2]]
    exact = sum(a[1] == b[1] for a, b in compatible)
    return {'metric_compatible_facet_occurrence_pairs': len(compatible),
            'same_label_facet_pairs': exact,
            'extra_local_candidates_after_erasing_labels': len(compatible)-exact,
            'scope': 'Local interface compatibility only, not an enumeration of globally valid quotients'}


def missing_cell_control(distances, full_cells):
    full = orient(distances, full_cells)
    opened = full[1:]
    assert {s for s in closure(full) if len(s) < len(full[0])} == {
        s for s in closure(opened) if len(s) < len(full[0])}
    closed_result, open_result = glue(full), glue(opened)
    assert closed_result['accepted'] and open_result['accepted']
    assert closed_result['exposed_interfaces'] == 0
    assert open_result['exposed_interfaces'] == len(full[0])
    return {'same_entire_lower_skeleton': True,
            'full': closed_result, 'one_cell_omitted': open_result,
            'finding': 'Labelled oriented gluing accepts both inventories; lower-dimensional incidence does not force the missing cell.'}


def main():
    targets, evidence = load_targets()
    results = {}
    for name, (distances, cells, marks) in targets.items():
        oriented = orient(distances, cells)
        reconstruction = glue(oriented)
        assert reconstruction['accepted']
        flipped = list(oriented)
        c = flipped[0]
        flipped[0] = (c[1], c[0], *c[2:])
        flip_result = glue(flipped)
        assert not flip_result['accepted'] and flip_result['orientation_conflicts'] > 0
        choices = interface_metric_choices(distances, cells)
        assert choices['same_label_facet_pairs'] == reconstruction['identified_interfaces']
        assert choices['extra_local_candidates_after_erasing_labels'] > 0
        results[name] = {'labelled_oriented_reconstruction': reconstruction,
                         'single_cell_orientation_flip': flip_result,
                         'label_erasure': choices}
    # Coarse cell lists are recovered from the already explicit centroids.
    pd, pc, _ = targets['proton']
    proton_faces = {cell(vertex(4, i) for i in range(4) if any(v[i] for v in c)) for c in pc}
    pd_control = missing_cell_control(pd, proton_faces)
    ed, ec, _ = targets['electron_pentachoron']
    ed_control = missing_cell_control(ed, ec)
    nd, nc, marks = targets['neutron_belt']
    belt_faces = {cell(vertex(6, i) for i in range(6) if any(v[i] for v in c)) for c in nc}
    cap_faces = [cell(vertex(6, i) for i in mark) for mark in marks]
    protected = {tuple(sorted(e)) for cap in cap_faces for e in combinations(cap, 2)}
    initial_skeleton = {s for s in closure(belt_faces) if len(s) <= 2}
    cap_tests = []
    for mask in range(4):
        candidate = belt_faces | {cap for i, cap in enumerate(cap_faces) if mask & (1 << i)}
        assert {s for s in closure(candidate) if len(s) <= 2} == initial_skeleton
        oriented = orient(nd, candidate)
        free, guarded = glue(oriented), glue(oriented, protected)
        assert free['accepted']
        assert guarded['accepted'] == (mask == 0)
        assert free['exposed_interfaces'] == 6-3*mask.bit_count()
        cap_tests.append({'added_caps': mask.bit_count(), 'which_caps_mask': mask,
                          'same_vertices_and_edges': True, 'unprotected': free, 'protected_rims': guarded})
    report = {'hypothesis': 3, 'status': 'tested', 'target_reconstructions': results,
              'proton_inventory_control': pd_control, 'electron_inventory_control': ed_control,
              'neutron_cap_inventory_controls': cap_tests, 'sources': evidence,
              'implementation_sha256': {name: hashlib.sha256((BASE/'checkers'/name).read_bytes()).hexdigest()
                  for name in ('check_common_assembly_gluing.py', 'check_common_assembly_symmetry.py', 'check_common_assembly_cones.py')},
              'conclusion': 'One labelled oriented gluer recovers exact quotients for all targets and rejects orientation errors. Its uniqueness depends on supplied cell inventory and labels. Identical lower skeletons admit different locally valid cell inventories. Protecting the two neutron rims excludes all three cap additions in the tested four-way family.',
              'scope': 'Exact gluing and bounded alternative-inventory tests; does not derive the inventory or enumerate every unlabelled quotient. No coefficient count.'}
    (BASE/'results/common_assembly_gluing.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
