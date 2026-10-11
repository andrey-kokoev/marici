"""Independent exact tests for reversible complex-mode evolution."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

from evolve_relative_geometry_modes import evolve, Cyclotomic, decode, mm
from check_relative_geometry_sources import match_target
from check_relative_geometry_mode_selection import change_frame
from check_common_assembly_symmetry import BASE, load_targets


def main():
    # Exercise the cyclotomic arithmetic beyond the prime source orders.
    for m in range(1, 13):
        ring = Cyclotomic(m)
        assert ring.root(m) == ring.one
        for k in range(m):
            total = ring.zero
            for t in range(m):
                total = ring.add(total, ring.root(k*t))
            assert total == (ring.scalar(m) if k == 0 else ring.zero)
            assert ring.multiply(ring.root(k), ring.conjugate(ring.root(k))) == ring.one
    targets, target_hashes = load_targets()
    results = {}
    for name, target_name, source_file in [
        ('proton', 'proton', 'relative-proton.json'),
        ('neutron', 'neutron_belt', 'mode-neutron.json'),
        ('electron', 'electron_pentachoron', 'relative-electron.json'),
    ]:
        source_path = BASE/'inputs'/source_file
        raw = source_path.read_bytes()
        source = json.loads(raw)
        assert all(seed['role'] != 'external_interface' for seed in source['seeds'])
        evolved = evolve(source)
        comparison = match_target(evolved['geometry'], targets[target_name])
        assert comparison is not None
        # Changing coordinates, not the geometric motion, must preserve selection.
        d = len(source['metric'])
        transformed = change_frame(source, [Q(i+2) for i in range(d)], [Q(1, i+2) for i in range(d)])
        transformed_result = evolve(transformed)
        assert transformed_result['generator_orders'] == evolved['generator_orders']
        assert transformed_result['scheduled_atomic_steps_to_word_return'] == evolved['scheduled_atomic_steps_to_word_return']
        assert match_target(transformed_result['geometry'], targets[target_name]) is not None
        stationary = [f for f in evolved['facet_states'] if not f['moving_centroid']]
        dropped_fixed_failures = 0
        for facet in stationary:
            assert facet['some_corner_moves'], 'Centroid-only and full-cell motion were conflated'
            for record in facet['generator_modes']:
                ring = Cyclotomic(record['order'])
                modes = tuple(tuple(tuple(map(Q, c)) for c in v) for v in record['encoded_modes'])
                full = decode(modes, ring)
                erased = list(modes)
                erased[0] = tuple(ring.zero for _ in full)
                if decode(erased, ring) != full:
                    dropped_fixed_failures += 1
        evolved['source_sha256'] = hashlib.sha256(raw).hexdigest()
        evolved['constructor_sha256'] = hashlib.sha256((BASE/'checkers/evolve_relative_geometry_modes.py').read_bytes()).hexdigest()
        (BASE/'results'/f'mode-motion-{name}.json').write_text(json.dumps(evolved, indent=2)+'\n')
        results[name] = {'source_file': source_file, 'source_sha256': evolved['source_sha256'], 'exact_target_comparison': comparison,
                         'generator_orders': evolved['generator_orders'],
                         'scheduled_word_order': evolved['scheduled_word_order'],
                         'scheduled_atomic_steps': evolved['scheduled_atomic_steps_to_word_return'],
                         'all_labelled_centroid_return_steps': [i+1 for i, s in enumerate(evolved['centroid_motion_trace']) if s['all_labelled_centroids_returned']],
                         'moving_centroid_channels': sum(f['moving_centroid'] for f in evolved['facet_states']),
                         'stationary_centroid_channels': len(stationary),
                         'stationary_centroid_channels_with_moving_corners': sum(f['some_corner_moves'] for f in stationary),
                         'dropping_fixed_modes_breaks_reconstruction': dropped_fixed_failures,
                         'coordinate_change_control_passed': True,
                         'forward_and_stepwise_reverse_history_checked': True}
    assert results['neutron']['stationary_centroid_channels'] == 2
    assert results['neutron']['dropping_fixed_modes_breaks_reconstruction'] == 2
    assert [results[n]['moving_centroid_channels'] for n in ('proton', 'neutron', 'electron')] == [4, 6, 5]
    report = {'status': 'passed', 'results': results, 'target_sha256': target_hashes,
              'cyclotomic_root_tests': 'orders 1 through 12',
              'implementation_sha256': {name: hashlib.sha256((BASE/'checkers'/name).read_bytes()).hexdigest()
                  for name in ('evolve_relative_geometry_modes.py', 'check_relative_geometry_mode_motion.py',
                               'assemble_relative_geometry.py', 'check_relative_geometry_sources.py',
                               'check_relative_geometry_mode_selection.py', 'check_common_assembly_symmetry.py')},
              'scope': 'Exact encode/phase/decode dynamics and inverse on centroid channels. Returns depend on supplied source actions and schedule, not inferred particle periods. The choice of centroid channels and active-mode cell admission remains the model hypothesis.'}
    (BASE/'results/relative_geometry_mode_motion.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
