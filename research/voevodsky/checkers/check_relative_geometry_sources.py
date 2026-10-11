"""Independent target comparison and input-sensitivity tests for the constructor.

Only this checker reads stored target cells. The constructor and its source
records contain no target imports, face lists, cell lists or particle switches.
"""
from copy import deepcopy
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path
import hashlib
import json

from assemble_relative_geometry import assemble, dot_metric, subtract
from check_common_assembly_symmetry import BASE, load_targets, vertex, cell


def match_target(output, target):
    distances, cells, marks = target
    actual_distances = [[Q(x) for x in row] for row in output['squared_distances']]
    n = len(actual_distances)
    if n != len(distances):
        return None
    coarse_target = {tuple(i for i in range(n) if any(v[i] for v in c)) for c in cells}
    target_marks = {tuple(sorted(mark)) for mark in marks}
    for p in permutations(range(n)):
        if any(actual_distances[i][j] != distances[p[i]][p[j]] for i in range(n) for j in range(n)):
            continue
        mapped = {tuple(sorted(p[i] for i in f)) for f in output['carrier_facets']}
        if mapped != coarse_target:
            continue
        mapped_marks = {tuple(sorted(p[i] for i in f)) for f in
                        output['external_interfaces']+output['retained_attachment_interfaces']}
        if mapped_marks != target_marks:
            continue
        # Optional centroid-edge subdivision is common to triangular facets;
        # compare the entire stored fine cell list, not just its cardinality.
        fine = set()
        for f in mapped:
            if len(f) == 3:
                centre = tuple(Q(i in f, 3) for i in range(n))
                for a, b in zip(f, f[1:]+f[:1]):
                    fine.add(cell((centre, vertex(n, a), vertex(n, b))))
            else:
                fine.add(cell(vertex(n, i) for i in f))
        if fine != set(cells):
            continue
        # The constructed center must also have the correct distances to every
        # matched target vertex; equal outer-edge metrics alone aren't enough.
        points = [tuple(map(Q, v)) for v in output['vertices']]
        center = tuple(map(Q, output['center']))
        G = [[Q(x) for x in row] for row in output['metric']]
        correction = sum(sum(row) for row in distances)/(2*n*n)
        assert all(dot_metric(subtract(points[i], center), subtract(points[i], center), G)
                   == sum(distances[p[i]])/n-correction for i in range(n))
        return {'vertex_correspondence': list(p), 'all_squared_distances_match': True,
                'all_coarse_facets_match': True, 'all_fine_cells_match': True,
                'fine_cells': len(fine), 'attachment_interfaces_match': True,
                'center_distances_match': True}
    return None


def expect_failure(source, text):
    try:
        assemble(source)
    except ValueError as error:
        assert text in str(error), str(error)
    else:
        raise AssertionError('Invalid/insufficient source was silently repaired')


def main():
    targets, target_hashes = load_targets()
    cases = [('proton', 'proton'), ('neutron', 'neutron_belt'), ('electron', 'electron_pentachoron')]
    results, sources = {}, {}
    constructor = BASE/'checkers/assemble_relative_geometry.py'
    for file_name, target_name in cases:
        path = BASE/'inputs'/f'relative-{file_name}.json'
        raw = path.read_bytes()
        source = json.loads(raw)
        sources[file_name] = source
        output = assemble(source)
        match = match_target(output, targets[target_name])
        assert match is not None, f'{file_name} did not match its stored target'
        output['source_sha256'] = hashlib.sha256(raw).hexdigest()
        output['constructor_sha256'] = hashlib.sha256(constructor.read_bytes()).hexdigest()
        (BASE/'results'/f'relative-{file_name}.json').write_text(json.dumps(output, indent=2)+'\n')
        # Every generator retained in these records is necessary for this input.
        for i in range(len(source['generators'])):
            reduced = deepcopy(source)
            reduced['generators'].pop(i)
            expect_failure(reduced, 'do not span')
        injected = deepcopy(source)
        injected['target_cells'] = output['carrier_facets']
        expect_failure(injected, 'exactly metric, generators and seeds')
        results[file_name] = {'source_sha256': output['source_sha256'], 'counts': output['counts'],
                              'seed_points': len(source['seeds']), 'generators': len(source['generators']),
                              'comparison': match, 'each_generator_deletion_detected': True,
                              'target_cell_injection_rejected': True}
    neutron = sources['neutron']
    for i in range(len(neutron['seeds'])):
        reduced = deepcopy(neutron)
        reduced['seeds'].pop(i)
        expect_failure(reduced, 'do not span')
    unprotected = deepcopy(neutron)
    for seed in unprotected['seeds']:
        seed['role'] = 'carrier'
    capped = assemble(unprotected)
    assert capped['counts']['carrier_facets'] == 8
    assert match_target(capped, targets['neutron_belt']) is None
    altered_gap = deepcopy(neutron)
    altered_gap['seeds'][0]['point'][1] = '1/4'
    altered_gap['seeds'][1]['point'][1] = '-1/4'
    altered = assemble(altered_gap)
    assert altered['counts']['carrier_facets'] == 6
    assert match_target(altered, targets['neutron_belt']) is None
    no_attachment = deepcopy(sources['electron'])
    no_attachment['seeds'][0]['role'] = 'carrier'
    unmarked = assemble(no_attachment)
    assert unmarked['counts'] == results['electron']['counts']
    assert match_target(unmarked, targets['electron_pentachoron']) is None
    report = {'status': 'passed', 'sources': results,
              'controls': {'removing_a_neutron_seed_rejected': True,
                           'unprotected_neutron_cones': capped['counts']['cone_cells'],
                           'changed_gap_keeps_incidence_but_fails_metric_match': True,
                           'erasing_electron_attachment_keeps_shape_but_fails_marked_match': True},
              'target_sha256': target_hashes,
              'constructor_sha256': hashlib.sha256(constructor.read_bytes()).hexdigest(),
              'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'target_loader_sha256': hashlib.sha256((BASE/'checkers/check_common_assembly_symmetry.py').read_bytes()).hexdigest(),
              'scope': 'Three proposed compact geometric source presentations, not proven minimal or derived from common primitive arrows. Metrics, symmetries, roles and neutron gap are explicit inputs. No shared coefficient operator or new particle arrow count.'}
    (BASE/'results/relative_geometry_sources.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
