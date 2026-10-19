"""Compare one triangle and both orientations through existing assembly rules."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/voevodsky/checkers'))
sys.path.insert(0, str(ROOT / 'research/nima/checkers'))
from assemble_relative_geometry import assemble as geometry
from evolve_relative_geometry_modes import evolve
from assemble_triangle_arrow_source import assemble as coefficients
from build_neutrino_seed_candidates import simplex_source
from check_neutrino_arrow_seed_science import rank


def main():
    forward = [('A', 'B'), ('B', 'C'), ('C', 'A')]
    reverse = [(b, a) for a, b in forward]
    cases, geometries, networks, checks = {}, [], [], {}
    # Same declared regular triangle metric in both runs. The coordinate
    # frontend uses an offset 3D frame so its centroid-edge matrix is invertible.
    points = {'A': [1, 1, 1], 'B': [1, -1, -1], 'C': [-1, 1, -1]}
    for label, arrows, cycles in [('single', forward, [[0, 1, 2]]),
                                  ('paired', forward + reverse, [[0, 1, 2], [0, 2, 1]])]:
        source, _ = simplex_source(3, cycles)
        geo = geometry(source)
        motion = evolve(source)
        report, transfers = coefficients({'vertices': points, 'arrows': arrows})
        boundary = [[Q(v == b) - Q(v == a) for a, b in arrows] for v in points]
        K = [[Q(a[1] == b[0]) for a in arrows] for b in arrows]
        # Branch count is intrinsic to the raw continuation; no phase filter.
        checks[label + '_uniform_continuation'] = len({sum(row) for row in K}) == 1
        cases[label] = {
            'arrows': arrows, 'source': source, 'geometry': geo,
            'occurrence_count': len(arrows), 'incidence_rank': rank(boundary),
            'occurrence_kernel_dimension': len(arrows) - rank(boundary),
            'continuation_rank': rank(K), 'continuation_outdegree': str(sum(K[0])),
            'cycle_steps': motion['scheduled_atomic_steps_to_word_return'],
            'generator_orders': motion['generator_orders'],
            'inverse_recovery': motion['reverse_history_recovers_every_centroid'],
            'coefficient_report': report,
        }
        geometries.append(geo)
        networks.append(transfers)
    checks['geometry_identical'] = geometries[0] == geometries[1]
    checks['primitive_records_distinct'] = cases['single']['occurrence_count'] == 3 and cases['paired']['occurrence_count'] == 6
    checks['occurrence_kernels_distinct'] = cases['single']['occurrence_kernel_dimension'] == 1 and cases['paired']['occurrence_kernel_dimension'] == 4
    checks['coefficient_manifest_identical'] = networks[0] == networks[1]
    checks['cycle_schedule_changes'] = cases['single']['cycle_steps'] == 3 and cases['paired']['cycle_steps'] == 2
    checks['both_spectral_recoveries_pass'] = all(c['inverse_recovery'] for c in cases.values())
    checks['generated_group_same'] = all(c['coefficient_report']['proper_rotations'] == 3 for c in cases.values())
    # Adding the inverse generator changes the declared schedule to R then
    # R^-1. It does not introduce an exchange of triangle face records.
    # Four edge-link candidate outputs from Voevodsky's retained note.
    outputs = [('ACE', 'BDF'), ('ACF', 'BDE'), ('ADE', 'BCF'), ('ADF', 'BCE')]
    checks['recombination_outputs_are_disjoint_not_opposite_same_triangle'] = all(
        not set(a) & set(b) and len(set(a) | set(b)) == 6 for a, b in outputs)
    # A chosen oriented simplex boundary has three signed edges, not six
    # independent directed occurrences. Reversal negates that chain.
    d2 = [Q(1), Q(1), Q(1)]
    incidence = [[Q(v == b) - Q(v == a) for a, b in forward] for v in points]
    checks['one_triangle_boundary_closes_without_reverse_occurrences'] = all(
        sum(x*y for x, y in zip(row, d2)) == 0 for row in incidence)
    report = {'status': 'passed' if all(checks.values()) else 'failed', 'checks': checks,
        'question': 'Does adding the opposite directed triangle define a filled photon distinct from a one-cycle neutrino candidate?',
        'cases': cases,
        'recombination_output_supports': outputs,
        'disposition': 'Different primitive occurrence records and raw continuation; identical assembled geometry and coefficient transfer manifest. Paired schedule returns in two applications because generators are inverses, not because filled and unfilled faces swap. Existing recombination outputs are disjoint triangles on six vertices, not two orientations on one three-vertex support.',
        'boundary': 'Metric and affine cycle interpretation explicitly supplied as in existing seed tests. No photon/neutrino identity or filling rule is inferred.',
        'source_hashes': {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in [
            Path(__file__).resolve(), ROOT/'research/strominger/checkers/build_neutrino_seed_candidates.py',
            ROOT/'research/voevodsky/checkers/assemble_relative_geometry.py',
            ROOT/'research/voevodsky/checkers/evolve_relative_geometry_modes.py',
            ROOT/'research/nima/checkers/assemble_triangle_arrow_source.py',
            ROOT/'research/voevodsky/edge-link-recombination-exchange-symmetry-and-polarization-correlations.md']}}
    dest = ROOT/'research/strominger/results/opposite_triangle_pair.json'
    dest.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': report['status'], 'checks': checks, 'measures': {
        key: {k: value[k] for k in ('occurrence_count','occurrence_kernel_dimension','cycle_steps')} |
        {'coefficient_transfers': value['coefficient_report']['unique_directed_arrows']} for key, value in cases.items()}}, indent=2))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
