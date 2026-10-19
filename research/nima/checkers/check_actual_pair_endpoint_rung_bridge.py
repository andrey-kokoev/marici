"""Bounded actual-seed endpoint extension through the existing rung API.

Explicit adapter, not a selected physical processor: independent endpoint
extension, unit path-context coefficients, and the unchanged rung-4 reference.
Word depth is NOT elapsed time. Context edges reference 11 seed primitives;
they are not 50 new primitives. No energy or SI calibration is introduced.
"""
from collections import Counter
from contextlib import redirect_stdout
from dataclasses import dataclass, replace
from fractions import Fraction
import hashlib
import io
import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
DEPENDENCIES = (
    'research/strominger/results/arrow_particle_collection.json',
    'research/voevodsky/inputs/relative-proton.json',
    'research/voevodsky/inputs/relative-electron.json',
    'research/nima/inputs/proton-six-arrows.json',
    'research/nima/checkers/check_indexed_path_synthesis.py',
    'research/nima/checkers/check_rung_transport_diagram.py',
    'research/nima/checkers/check_shared_leg_dg_realization.py',
    'research/nima/checkers/biclique_complex.py',
)


def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8-sig'))


def moving_arrows(source, labels):
    """Derive labelled moving correspondences from the supplied affine maps.

    Convention: A is the affine origin, subsequent labels are coordinate axes.
    Fixed correspondences are not additional moving seed arrows.
    """
    dimension = len(source['metric'])
    points = {labels[0]: (Fraction(0),) * dimension}
    points.update({label: tuple(Fraction(j == i) for j in range(dimension))
                   for i, label in enumerate(labels[1:])})
    inverse = {point: label for label, point in points.items()}
    result = []
    for generator in source['generators']:
        for a, point in points.items():
            image = tuple(sum(Fraction(c) * x for c, x in zip(row, point))
                          + Fraction(t)
                          for row, t in zip(generator['matrix'], generator['translation']))
            b = inverse[image]
            if a != b:
                result.append((a, b))
    return tuple(result)


@dataclass(frozen=True)
class Packet:
    registry: tuple
    start: tuple
    depth: int
    paths: tuple


@dataclass(frozen=True)
class AtFour:
    registry: tuple
    start: tuple
    depth: int
    view: dict


def main():
    hashes = {path: digest(path) for path in DEPENDENCIES}
    checks = []

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    collection = load(DEPENDENCIES[0])
    models = {model['label']: model for model in collection['models']}
    check('collection/proton-and-electron-source-pins', all(
        digest(models[name]['source_path']) == models[name]['source_sha256']
        for name in ('proton', 'electron')))
    p = moving_arrows(load(DEPENDENCIES[1]), 'ABCD')
    e = moving_arrows(load(DEPENDENCIES[2]), 'ABCDE')
    manifest = tuple(map(tuple, load(DEPENDENCIES[3])['arrows']))
    check('proton/affine-moving-arrows-match-six-arrow-manifest',
          len(p) == 6 and set(p) == set(manifest))
    check('electron/affine-moving-arrows-form-original-five-cycle',
          e == tuple(zip('ABCDE', 'BCDEA')))
    # IDs refer to supplied moving correspondences; no simulated execution ID.
    registry = tuple((owner, i, a, b)
                     for owner, arrows in (('proton', p), ('electron', e))
                     for i, (a, b) in enumerate(arrows))
    primitives = set(registry)
    vertices = tuple((i, j) for i in 'ABCD' for j in 'ABCDE')
    frame = []
    for primitive in registry:
        owner, _, a, b = primitive
        held = 'ABCDE' if owner == 'proton' else 'ABCD'
        for h in held:
            s, t = ((a, h), (b, h)) if owner == 'proton' else ((h, a), (h, b))
            frame.append(((s, t, primitive),))
    frame = tuple(frame)
    check('registry/11-primitives-50-addressed-context-edges',
          len(registry) == 11 and len(frame) == 50)
    with redirect_stdout(io.StringIO()):
        composition = runpy.run_path(str(ROOT / DEPENDENCIES[4]))
        tower = runpy.run_path(str(ROOT / DEPENDENCIES[5]))
    compose = composition['compose']
    Row = tower['Row']
    indexed, unindex = tower['indexed'], tower['unindex']
    promote, leaves = tower['incoming_promotion'], tower['leaves']
    I = tower['I']

    def validate(packet):
        if packet.registry != registry or packet.start not in vertices:
            raise ValueError('Foreign primitive registry or starting state')
        if packet.depth < 1 or not packet.paths or tuple(sorted(set(packet.paths))) != packet.paths:
            raise ValueError('Expected nonempty unique ordered path frame')
        for path in packet.paths:
            if len(path) != packet.depth or path[0][0] != packet.start:
                raise ValueError('Wrong depth or root')
            for k, (s, t, primitive) in enumerate(path):
                if primitive not in primitives or ((s, t, primitive),) not in frame:
                    raise ValueError('Unknown primitive or incompatible held context')
                if k and path[k - 1][1] != s:
                    raise ValueError('Broken endpoint join')
        return packet

    def packet(paths, start=('A', 'E')):
        paths = tuple(sorted(paths))
        return validate(Packet(registry, start, len(paths[0]), paths))

    def extend(x):
        validate(x)
        return packet(compose(set(x.paths), set(frame)), x.start)

    def profile(x):
        return Counter(path[-1][1] for path in x.paths)

    def step_profile(current):
        result = Counter()
        for (s, t, _), in frame:
            result[t] += current[s]
        return +result

    def future(x, horizon):
        current = x
        for _ in range(horizon):
            current = extend(current)
        return horizon * len(current.paths)

    def rows(x):
        return tuple(Row(('pair-path', x.depth, i, path),
                         ('joint',) + path[0][0], ('joint',) + path[-1][1], I)
                     for i, path in enumerate(x.paths))

    def encode(x, policy):
        original = rows(validate(x))
        def T(rs):
            return promote(promote(rs, 1, policy), 2, policy)
        upper = indexed(unindex(indexed(T(original), 'source')), 'target')
        left = indexed(unindex(indexed(original, 'source')), 'target')
        lower = indexed(T(unindex(left)), 'target')
        check(f'transport/routes/{policy}/{x.depth}/{len(x.paths)}', upper == lower)
        return AtFour(x.registry, x.start, x.depth, upper)

    def decode(y):
        original = leaves(unindex(y.view))
        paths = []
        for row in original:
            tag, depth, _, path = row.label
            if (tag != 'pair-path' or depth != y.depth or row.value != I or row.mass != 1
                    or row.source != ('joint',) + path[0][0]
                    or row.target != ('joint',) + path[-1][1]):
                raise ValueError('Altered retained row or endpoint label')
            paths.append(path)
        return validate(Packet(y.registry, y.start, y.depth, tuple(sorted(paths))))

    def read_profile(y):
        # Read retained target-labelled leaves, not the fresh-label mean.
        return Counter(row.target[1:] for row in leaves(unindex(y.view)))

    frontier = packet(path for path in frame if path[0][0] == ('A', 'E'))
    trajectory = []
    for depth in range(1, 5):
        x = frontier
        next_x = extend(x)
        check(f'endpoint-square/depth-{depth}', step_profile(profile(x)) == profile(next_x))
        check(f'history-prefix-recovery/depth-{depth}',
              {path[:-1] for path in next_x.paths} == set(x.paths))
        check(f'horizon-one-count-law/depth-{depth}',
              future(next_x, 1) == 3 * future(x, 1) - len(x.paths))
        readings = {}
        for policy in ('inherited', 'common'):
            y = encode(x, policy)
            next_y = encode(next_x, policy)
            check(f'lossless-packet/{policy}/{depth}', decode(y) == x)
            check(f'induced-retained-square/{policy}/{depth}',
                  encode(extend(decode(y)), policy) == next_y)
            check(f'independent-profile-square/{policy}/{depth}',
                  step_profile(read_profile(y)) == read_profile(next_y))
            check(f'fixed-reference/{policy}/{depth}',
                  tower['physical_reference'].rung == 4
                  and tower['physical_reference'].value == tower['scale'](2, I))
            check(f'aggregate-blind/{policy}/{depth}',
                  tower['read_at_four'](y.view) == tower['scale'](-1, I))
            readings[policy] = read_profile(y)
        check(f'policy-independent-labelled-profile/{depth}',
              readings['inherited'] == readings['common'])
        trajectory.append({'word_depth': depth, 'path_contexts': len(x.paths),
                           'future_q1': future(x, 1), 'future_q3': future(x, 3),
                           'endpoint_profile': {''.join(k): v for k, v in sorted(profile(x).items())}})
        frontier = next_x

    # Explicit prepared subfamilies of valid length-two words. This preparation
    # is declared, NOT claimed to be selected by the native seed assembler.
    depth_two = extend(packet(path for path in frame if path[0][0] == ('A', 'E')))
    def identify(word):
        return tuple((edge[2][0], edge[2][2] + edge[2][3]) for edge in word)
    by_word = {identify(path): path for path in depth_two.paths}
    high = packet([by_word[(('proton', 'AB'), ('proton', 'BA'))],
                   by_word[(('proton', 'AD'), ('proton', 'DB'))]])
    low = packet([by_word[(('proton', 'AB'), ('proton', 'BC'))],
                  by_word[(('proton', 'AD'), ('electron', 'EA'))],
                  by_word[(('electron', 'EA'), ('proton', 'AD'))]])
    def coarse(x):
        return (len(x.registry), x.depth, future(x, 1))
    check('prepared-family/coarse-present-collision', coarse(high) == coarse(low) == (11, 2, 6))
    check('prepared-family/coarse-next-failure', future(extend(high), 1) == 16
          and future(extend(low), 1) == 15)
    for x in (high, low):
        check('prepared-family/count-plus-workload-closes',
              future(extend(x), 1) == 3 * future(x, 1) - len(x.paths))
        for policy in ('inherited', 'common'):
            y = encode(x, policy)
            check('prepared-family/profile-predicts-next/' + policy,
                  step_profile(read_profile(y)) == profile(extend(x)))
            check('prepared-family/full-recovery/' + policy, decode(y) == x)
    # Exhaust every nonempty unit-coefficient subfamily of this registered
    # eight-word depth-two frame. This proves only the finite prepared domain.
    profile_classes, count_classes = {}, {}
    for mask in range(1, 1 << len(depth_two.paths)):
        x = packet(path for i, path in enumerate(depth_two.paths) if mask & (1 << i))
        next_x = extend(x)
        key = tuple(sorted(profile(x).items()))
        next_key = tuple(sorted(profile(next_x).items()))
        check(f'all-subfamilies/profile-square/{mask}', step_profile(profile(x)) == profile(next_x))
        if key in profile_classes:
            check(f'all-subfamilies/profile-congruence/{mask}', profile_classes[key] == next_key)
        profile_classes[key] = next_key
        count_key = (len(x.paths), future(x, 1))
        next_count_key = (len(next_x.paths), future(next_x, 1))
        check(f'all-subfamilies/count-law/{mask}',
              next_count_key == (count_key[1], 3 * count_key[1] - count_key[0]))
        if count_key in count_classes:
            check(f'all-subfamilies/count-congruence/{mask}', count_classes[count_key] == next_count_key)
        count_classes[count_key] = next_count_key
    check('all-subfamilies/nonempty-domain-size', (1 << len(depth_two.paths)) - 1 == 255)
    # Same current endpoint, different order. Endpoint extension ignores order,
    # but the retained packet must not identify the histories.
    pe = packet([by_word[(('proton', 'AD'), ('electron', 'EA'))]])
    ep = packet([by_word[(('electron', 'EA'), ('proton', 'AD'))]])
    check('history-order/same-profile-different-records', profile(pe) == profile(ep) and pe != ep)
    check('history-order/endpoint-next-agrees-under-declared-rule',
          profile(extend(pe)) == profile(extend(ep)))
    for policy in ('inherited', 'common'):
        check('history-order/retained-after-transport/' + policy,
              decode(encode(pe, policy)) != decode(encode(ep, policy)))
    # An otherwise unchanged row with a wrong endpoint must not be decoded.
    good = rows(pe)
    bad_row = replace(good[0], target=('joint', 'A', 'A'))
    bad = AtFour(registry, pe.start, pe.depth, indexed((bad_row,), 'target'))
    try:
        decode(bad)
    except ValueError:
        rejected = True
    else:
        rejected = False
    check('hostile/altered-endpoint-rejected', rejected)
    check('dependency-inputs-stable', hashes == {path: digest(path) for path in DEPENDENCIES})

    result = {
        'schema': 'marici.nima.actual-pair-endpoint-rung-bridge.v1',
        'status': 'pass', 'checks': checks, 'source_hashes': hashes,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'primitive_counts': {'proton': len(p), 'electron': len(e), 'pair': len(registry)},
        'primitive_registry': registry, 'joint_context_edges': len(frame),
        'declared_start': ['A', 'E'], 'trajectory': trajectory,
        'coarse_collision': {'present_m_depth_q1': [11, 2, 6],
                             'path_counts': [len(high.paths), len(low.paths)],
                             'next_q1': [16, 15]},
        'count_closure': {'next_path_count': 'q1', 'next_q1': '3*q1-path_count'},
        'prepared_domain': {'word_depth': 2, 'frame_words': len(depth_two.paths),
                            'nonempty_unit_subfamilies': 255,
                            'endpoint_profile_classes': len(profile_classes),
                            'path_count_q1_classes': len(count_classes)},
        'scope': ['actual affine seed correspondences and original six-arrow manifest',
                  'existing endpoint composition and retained rung API reused',
                  'explicit independent extension, not source-selected physical evolution',
                  'prepared-subfamily hostile is conditional on that preparation interface',
                  'endpoint profile suffices for this successor, not every history-dependent law',
                  'member masses are path counts, not particle masses',
                  'word depth is not time or a processing cycle; no Hamiltonian/clock/SI bridge',
                  '20-component endpoint profile is not four-dimensional physical spacetime'],
    }
    output = HERE.parent / 'results/actual-pair-endpoint-rung-bridge.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(checks)} exact checks; actual seed pair endpoint/rung bridge')
    print('Counts alone collide: (m,depth,q1)=(11,2,6), but next q1 is 16 versus 15.')
    print('Labelled endpoint profile closes; both rung policies retain complete paths.')
    print('Scope: declared endpoint extension, not a physical pair-cycle or SI calibration.')
    # Expose the checked adapter for successor/readout comparisons without
    # duplicating its packet, endpoint registry or rung transport functions.
    return {'packet': packet, 'extend': extend, 'profile': profile,
            'future': future, 'encode': encode, 'decode': decode,
            'read_profile': read_profile, 'registry': registry, 'frame': frame,
            'vertices': vertices, 'tower': tower, 'source_hashes': hashes}


if __name__ == '__main__':
    main()
