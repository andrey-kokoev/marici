"""Actual seed histories lifted through the existing cyclic-mode processor.

Reuse the checked pair packet/rung adapter unchanged. Bind each moving arrow
correspondence to its unique supplied affine generator, apply the backend's
encode/advance/decode to labelled centroids, and test phase-sensitive descent.
This does NOT derive a pair interaction, phase-dependent admission or SI clock.
"""
from collections import Counter, deque
from contextlib import redirect_stdout
from fractions import Fraction as Q
from functools import cache
import hashlib
import io
import json
from pathlib import Path
import runpy
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
NATIVE = ROOT / 'research/voevodsky/checkers'
DEPENDENCIES = (
    'research/nima/checkers/check_actual_pair_endpoint_rung_bridge.py',
    'research/voevodsky/checkers/assemble_relative_geometry.py',
    'research/voevodsky/checkers/evolve_relative_geometry_modes.py',
)


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def rational_tree(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, (tuple, list)):
        return [rational_tree(x) for x in value]
    if isinstance(value, dict):
        return {k: rational_tree(v) for k, v in value.items()}
    return value


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    source_hashes = {path: sha(path) for path in DEPENDENCIES}
    sys.path.insert(0, str(NATIVE))
    with redirect_stdout(io.StringIO()):
        old = runpy.run_path(str(ROOT / DEPENDENCIES[0]))
        bridge = old['main']()  # fresh full endpoint/rung verification first
        native = runpy.run_path(str(ROOT / DEPENDENCIES[2]))
    source_hashes.update(bridge['source_hashes'])
    packet = bridge['packet']
    extend = bridge['extend']
    registry, context_edges = bridge['registry'], bridge['frame']
    models = {m['label']: m for m in json.loads((ROOT /
              'research/strominger/results/arrow_particle_collection.json').read_text())['models']}
    owners = ('proton', 'electron')
    sources = {owner: json.loads((ROOT / models[owner]['source_path']).read_text()) for owner in owners}
    prepared = {owner: native['evolve'](sources[owner]) for owner in owners}
    matrices, rings, coordinates, generators = {}, {}, {}, {}
    initial = []
    for owner, labels in (('proton', 'ABCD'), ('electron', 'ABCDE')):
        source = sources[owner]
        d = len(source['metric'])
        coordinates[owner] = {labels[0]: (Q(0),) * d}
        coordinates[owner].update({label: tuple(Q(j == i) for j in range(d))
                                   for i, label in enumerate(labels[1:])})
        matrices[owner] = tuple(tuple(tuple(Q(x) for x in row) for row in raw['matrix'])
                                for raw in source['generators'])
        generators[owner] = tuple((A, tuple(Q(x) for x in raw['translation']))
                                  for A, raw in zip(matrices[owner], source['generators']))
        rings[owner] = tuple(native['Cyclotomic'](native['matrix_order'](A)) for A in matrices[owner])
        initial.append(tuple(tuple(Q(x) for x in record['centered_centroid'])
                             for record in prepared[owner]['facet_states']))
        check('native/fixed-modes-retained/' + owner, prepared[owner]['fixed_modes_retained'])
        check('native/reverse-history/' + owner, prepared[owner]['reverse_history_recovers_every_centroid'])
    initial = tuple(initial)
    assembler = runpy.run_path(str(ROOT / DEPENDENCIES[1]))
    action_for = {}
    for primitive in registry:
        owner, _, a, b = primitive
        matches = [i for i, generator in enumerate(generators[owner])
                   if assembler['apply'](generator, coordinates[owner][a]) == coordinates[owner][b]]
        check('binding/unique-source-generator/' + repr(primitive), len(matches) == 1)
        action_for[primitive] = matches[0]

    def norm(state):
        return tuple(sum(native['dot_metric'](v, v, sources[owner]['metric'])
                         for v in field) for owner, field in zip(owners, state))
    baseline_norm = norm(initial)

    @cache
    def mode_step(state, primitive):
        owner = primitive[0]
        slot = owners.index(owner)
        index = action_for[primitive]
        A, ring = matrices[owner][index], rings[owner][index]
        following = []
        for v in state[slot]:
            modes = native['encode'](v, A, ring)
            advanced = native['advance'](modes, ring)
            decoded = native['decode'](advanced, ring)
            check('native-step/exact-decoding', decoded == native['mv'](A, v))
            check('native-step/phase-inverse', native['advance'](advanced, ring, -1) == modes)
            check('native-step/full-mode-decoding', native['decode'](modes, ring) == v)
            following.append(decoded)
        result = list(state)
        result[slot] = tuple(following)
        result = tuple(result)
        check('native-step/inherited-metric-norm', norm(result) == baseline_norm)
        return result

    @cache
    def path_state(path):
        previous = initial if len(path) == 1 else path_state(path[:-1])
        return mode_step(previous, path[-1][2])

    def phase_profile(x):
        return Counter((path[-1][1], path_state(path)) for path in x.paths)

    def step_phase_profile(current):
        following = Counter()
        for (endpoint, state), multiplicity in current.items():
            for (s, t, primitive), in context_edges:
                if s == endpoint:
                    following[t, mode_step(state, primitive)] += multiplicity
        return following

    def at_four_profile(y):
        # Original retained packet and decoder, no new phase payload in rows.
        return phase_profile(bridge['decode'](y))

    # Identify the actual generated ABC centroid by coordinates, not facet slot.
    pg = prepared['proton']['geometry']
    vertex_positions = [tuple(Q(x) for x in v) for v in pg['vertices']]
    abc_ids = {vertex_positions.index(coordinates['proton'][label]) for label in 'ABC'}
    abc = next(i for i, record in enumerate(prepared['proton']['facet_states'])
               if set(record['facet']) == abc_ids)
    def marked_y(path):
        return path_state(path)[0][abc][1]

    root_paths = tuple(path for path in context_edges if path[0][0] == ('A', 'E'))
    current = packet(root_paths)
    tested, trajectory = {}, []
    for depth in range(1, 6):
        next_x = extend(current)
        check(f'phase-square/full-frontier/{depth}',
              step_phase_profile(phase_profile(current)) == phase_profile(next_x))
        for policy in ('inherited', 'common'):
            y = bridge['encode'](current, policy)
            next_y = bridge['encode'](next_x, policy)
            check(f'phase-rung-square/{policy}/{depth}',
                  step_phase_profile(at_four_profile(y)) == at_four_profile(next_y))
            check(f'packet-unchanged/{policy}/{depth}', bridge['decode'](y) == current)
        for path in current.paths:
            # Binding control: generator motion of the tracked point really
            # realizes each recorded source/target correspondence.
            tracked = [coordinates['proton']['A'], coordinates['electron']['E']]
            for s, t, primitive in path:
                owner = primitive[0]
                slot = owners.index(owner)
                check('tracked-point/source-label', tracked[slot] == coordinates[owner][s[slot]])
                tracked[slot] = assembler['apply'](generators[owner][action_for[primitive]], tracked[slot])
                check('tracked-point/target-label', tracked[slot] == coordinates[owner][t[slot]])
            single = packet([path])
            key = (path[-1][1], path_state(path))
            next_profile = phase_profile(extend(single))
            if key in tested:
                check('phase-state/congruent-successor', tested[key] == next_profile)
            tested[key] = next_profile
        trajectory.append({'word_depth': depth, 'paths': len(current.paths),
                           'endpoint_classes': len(bridge['profile'](current)),
                           'endpoint_phase_classes': len(phase_profile(current))})
        current = next_x

    def word(path):
        return tuple((edge[2][0], edge[2][2] + edge[2][3]) for edge in path)
    depth_five = packet(root_paths)
    for _ in range(4):
        depth_five = extend(depth_five)
    lookup = {word(path): path for path in depth_five.paths}
    proton_word = (('proton', 'AB'), ('proton', 'BA'), ('proton', 'AB'),
                   ('proton', 'BC'), ('proton', 'CA'))
    electron_word = tuple(('electron', label) for label in ('EA', 'AB', 'BC', 'CD', 'DE'))
    xp, xe = packet([lookup[proton_word]]), packet([lookup[electron_word]])
    def small(x):
        return (len(x.registry), x.depth, tuple(sorted(bridge['profile'](x).items())),
                bridge['future'](x, 1), marked_y(x.paths[0]))
    check('witness/same-present-endpoint-count-and-marked-scalar', small(xp) == small(xe))
    check('witness/current-scalar-exact', marked_y(xp.paths[0]) == Q(1, 12))
    check('witness/different-retained-phase-frames', phase_profile(xp) != phase_profile(xe))
    check('witness/same-current-geometry-norm', norm(path_state(xp.paths[0])) == norm(path_state(xe.paths[0])))
    request = next(primitive for primitive in registry
                   if primitive[0] == 'proton' and primitive[2:] == ('A', 'B'))
    def requested_step(x):
        matches = [path for path in extend(x).paths if path[-1][2] == request]
        if len(matches) != 1:
            raise ValueError('Request must have one compatible continuation')
        return packet(matches)
    np, ne = requested_step(xp), requested_step(xe)
    check('witness/same-request-next-endpoint', bridge['profile'](np) == bridge['profile'](ne))
    check('witness/next-scalar-diverges', marked_y(np.paths[0]) == Q(-1, 4)
          and marked_y(ne.paths[0]) == Q(1, 12))
    check('witness/request-predicted-from-phase-state',
          mode_step(path_state(xp.paths[0]), request) == path_state(np.paths[0])
          and mode_step(path_state(xe.paths[0]), request) == path_state(ne.paths[0]))
    for policy in ('inherited', 'common'):
        for label, x, nx in (('p-history', xp, np), ('e-history', xe, ne)):
            y = bridge['encode'](x, policy)
            next_y = bridge['encode'](nx, policy)
            check(f'witness/retained-request-square/{policy}/{label}',
                  bridge['encode'](requested_step(bridge['decode'](y)), policy) == next_y)
            check(f'witness/source-phase-state-survives/{policy}/{label}',
                  at_four_profile(y) == phase_profile(x))

    # Close the finite endpoint/phase-state graph, rather than infer all-time
    # prediction from agreement on a bounded prefix. Retain one actual word as
    # a witness for each state; the complete original history is not quotiented.
    reachable = {}
    queue = deque()
    for path in root_paths:
        key = (path[-1][1], path_state(path))
        if key not in reachable:
            reachable[key] = path
            queue.append(key)
    transitions = {}
    while queue:
        key = queue.popleft()
        endpoint, state = key
        witness = packet([reachable[key]])
        children = extend(witness)
        check('closed-graph/independent-next-profile',
              step_phase_profile(Counter({key: 1})) == phase_profile(children))
        actions = {}
        for path in children.paths:
            child = (path[-1][1], path_state(path))
            actions[path[-1][2]] = child
            if child not in reachable:
                reachable[child] = path
                queue.append(child)
                if len(reachable) > 512:
                    raise ValueError('Phase-state exploration exceeded the finite bound')
        transitions[key] = actions
        for policy in ('inherited', 'common'):
            y = bridge['encode'](witness, policy)
            next_y = bridge['encode'](children, policy)
            check('closed-graph/rung-square/' + policy,
                  step_phase_profile(at_four_profile(y)) == at_four_profile(next_y))
    check('closed-graph/no-unexplored-successors',
          set(transitions) == set(reachable)
          and all(child in reachable for actions in transitions.values() for child in actions.values()))
    states = tuple(reachable)
    outputs = {key: (key[0], key[1][0][abc][1]) for key in states}
    def partition(signatures):
        labels = {}
        return {key: labels.setdefault(signatures[key], len(labels)) for key in states}
    classes = partition(outputs)
    refinement_sizes = [len(set(classes.values()))]
    while True:
        signatures = {key: (outputs[key], tuple((primitive, classes[child])
                       for primitive, child in sorted(transitions[key].items()))) for key in states}
        following = partition(signatures)
        if following == classes:
            break
        classes = following
        refinement_sizes.append(len(set(classes.values())))
    for i, key in enumerate(states):
        for other in states[:i]:
            if classes[key] == classes[other]:
                check('stable-partition/current-output', outputs[key] == outputs[other])
                check('stable-partition/admitted-request-labels',
                      set(transitions[key]) == set(transitions[other]))
                check('stable-partition/successor-congruence', all(
                      classes[child] == classes[transitions[other][primitive]]
                      for primitive, child in transitions[key].items()))
    # Important control: one generator is advanced per actual correspondence.
    # Three g arrows then three h arrows give g^3=h^3=I; do not substitute hg.
    six = extend(depth_five)
    six_lookup = {word(path): path for path in six.paths}
    for labels in (('AB', 'BC', 'CA', 'AD', 'DB', 'BA'),
                   ('AD', 'DB', 'BA', 'AB', 'BC', 'CA')):
        path = six_lookup[tuple(('proton', label) for label in labels)]
        check('control/full-triangle-traversals-return-native-frame', path_state(path) == initial)
    check('source-inputs-stable', source_hashes == {path: sha(path) for path in source_hashes})
    receipt = {
        'schema': 'marici.nima.actual-pair-phase-rung-bridge.v1', 'status': 'pass',
        'checks': checks, 'source_hashes': source_hashes,
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'previous_receipt_sha256': sha('research/nima/results/actual-pair-endpoint-rung-bridge.json'),
        'native_generator_orders': {owner: prepared[owner]['generator_orders'] for owner in owners},
        'baseline_centroid_norms': rational_tree(baseline_norm),
        'primitive_counts': {'proton': 6, 'electron': 5}, 'trajectory': trajectory,
        'closed_phase_graph': {'states': len(reachable),
                               'labelled_transitions': sum(map(len, transitions.values())),
                               'observable': 'joint endpoint plus proton ABC centroid coordinate 1',
                               'partition_refinement_sizes': refinement_sizes,
                               'stable_classes': len(set(classes.values()))},
        'witness': {'proton_history': proton_word, 'electron_history': electron_word,
                    'common_depth': 5, 'common_endpoint': ['A', 'E'], 'common_future_q1': 3,
                    'marked_facet': 'proton ABC', 'marked_coordinate': 1,
                    'present_scalar': '1/12', 'request': request,
                    'next_endpoint': ['B', 'E'], 'next_scalars': ['-1/4', '1/12']},
        'scope': ['existing native encode/advance/decode reused without a fitted Hamiltonian',
                  'unique source-generator/arrow-correspondence binding checked exactly',
                  'same original packet and both rung transport policies',
                  'generator choice along a path is an explicit schedule adapter',
                  'phase-sensitive response, not new phase-dependent admission',
                  'independent source operations, not a proton/electron interaction',
                  'full phase endpoint omits winding; histories remain retained',
                  'no physical clock, energy normalization, spinor transport or SI conversion'],
    }
    output = HERE.parent / 'results/actual-pair-phase-rung-bridge.json'
    output.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(checks)} exact actual-source mode/rung checks')
    print('Same endpoint and present marked scalar 1/12; same AB request gives -1/4 versus 1/12.')
    print('Labelled phase-frame profile closes and survives both original rung transports.')
    print('Control: complete triangle traversal is three native phase steps, not one generator application.')
    print('Scope: source phase lift, not a pair interaction/admission law or physical clock.')
    return {'bridge': bridge, 'states': states, 'transitions': transitions,
            'outputs': outputs, 'witnesses': reachable, 'path_state': path_state,
            'mode_step': mode_step, 'initial': initial, 'root_paths': root_paths}


if __name__ == '__main__':
    main()
