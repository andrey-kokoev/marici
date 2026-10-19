"""Finite realization of the existing normalization-coordinate coherence law.

Tests C_target U_request = C_source as equality of permutations on the entire
reachable frame orbit. Does not instantiate the Agda compiler or select a
physical admission policy. Coordinates are transported from identity.
"""
from contextlib import redirect_stdout
from collections import Counter
import hashlib
import io
import json
from pathlib import Path

from check_actual_pair_phase_rung_bridge import main as build, rational_tree
from predictive_pair_quotient import PredictivePairQuotient

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FORMAL = ROOT / 'research/nima/agda/DependentNormalizationCoherence.agda'


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    with redirect_stdout(io.StringIO()):
        binding = build()
    q = PredictivePairQuotient(binding)
    frames = tuple(dict.fromkeys(state[1] for state in q.states))
    ids = {frame: i for i, frame in enumerate(frames)}
    identity = tuple(range(len(frames)))
    def compose(left, right):
        return tuple(left[i] for i in right)
    def inverse(p):
        return tuple(p.index(i) for i in identity)
    actions = {}
    for action in q.actions:
        images = tuple(binding['mode_step'](frame, action) for frame in frames)
        check('native-action/orbit-closed/' + repr(action), all(v in ids for v in images))
        actions[action] = tuple(ids[v] for v in images)
        check('native-action/equivalence/' + repr(action),
              sorted(actions[action]) == list(identity))
    def history_action(history):
        result = identity
        for edge in history:
            result = compose(actions[edge[2]], result)
        return result

    lifts = tuple(history_action(history) for history in q.witnesses)
    coordinates = tuple(inverse(lift) for lift in lifts)
    check('carrier/60-frames', len(frames) == 60)
    check('carrier/60-distinct-action-lifts', len(set(lifts)) == 60)
    initial = ids[binding['initial']]
    for state, lift in enumerate(lifts):
        check(f'lift/recovers-frame/{state}', frames[lift[initial]] == q.states[state][1])
        check(f'coordinates/equivalence/{state}',
              compose(coordinates[state], lift) == identity
              and compose(lift, coordinates[state]) == identity)
    # Every root action agrees with its state's lift, and every reachable
    # transition does too: induction gives history independence for all words.
    for history in binding['root_paths']:
        check('lift/root', history_action(history) == lifts[q.project(history)])
    admitted = rejected = 0
    for source in range(len(q.states)):
        for action in q.admitted(source):
            target = q.step(source, action)
            check(f'lift/transition/{source}/{action}',
                  compose(actions[action], lifts[source]) == lifts[target])
            # Native CoherentMap condition on the whole finite carrier, not
            # merely on the currently prepared frame or a scalar probe.
            for candidate in range(len(q.states)):
                if q.states[candidate][0] != q.states[target][0]:
                    continue
                coherent = compose(coordinates[candidate], actions[action]) == coordinates[source]
                check(f'gate/target-uniqueness/{source}/{action}/{candidate}',
                      coherent == (candidate == target))
                if coherent:
                    admitted += 1
                else:
                    rejected += 1
            for policy in ('inherited', 'common'):
                retained = q.retain(q.witnesses[source], policy)
                following = q.advance_rung(retained, action, policy)
                recovered = q.project_rung(following)
                check(f'gate/rung/{policy}/{source}/{action}',
                      compose(coordinates[recovered], actions[action]) == coordinates[source])

    # An actual valid closed endpoint word with nontrivial frame holonomy.
    def path_for(labels, owner):
        endpoint = ('A', 'E')
        path = ()
        for label in labels:
            edge = next(edge for (edge,) in q.bridge['frame']
                        if edge[0] == endpoint and edge[2][0] == owner
                        and ''.join(edge[2][2:]) == label)
            path += (edge,)
            endpoint = edge[1]
        return path
    nontrivial = path_for(('AB', 'BA', 'AB', 'BC', 'CA'), 'proton')
    trivial = path_for(('EA', 'AB', 'BC', 'CD', 'DE'), 'electron')
    p, e = q.project(nontrivial), q.project(trivial)
    check('obstruction/same-endpoint', q.states[p][0] == q.states[e][0] == ('A', 'E'))
    check('obstruction/nonidentity-loop', history_action(nontrivial) != identity)
    check('control/electron-full-cycle-identity', history_action(trivial) == identity)
    check('obstruction/coordinates-distinct', coordinates[p] != coordinates[e])
    # Any injective C_endpoint satisfying C_endpoint U_loop=C_endpoint would
    # imply U_loop=I. Exhibit a concrete unequal pair to certify the obstruction.
    holonomy = history_action(nontrivial)
    moved = next(i for i in identity if holonomy[i] != i)
    check('obstruction/moved-frame', frames[moved] != frames[holonomy[moved]])
    loop = path_for(('AB', 'BC', 'CA'), 'proton')
    check('provenance/triangle-loop-trivial-action', history_action(loop) == identity)
    for state, history in enumerate(q.witnesses):
        other = loop + history
        check(f'descent/distinct-history-same-coordinates/{state}',
              other != history and q.project(other) == state
              and inverse(history_action(other)) == coordinates[state])
    fibers = Counter(state[0] for state in q.states)
    check('carrier/three-states-per-endpoint', len(fibers) == 20 and set(fibers.values()) == {3})

    paths = [Path(__file__), HERE / 'predictive_pair_quotient.py',
             HERE / 'check_actual_pair_phase_rung_bridge.py', FORMAL,
             ROOT / 'research/nima/agda/NativeNormalizationRouteCompiler.agda',
             ROOT / 'research/nima/agda/ThreeRecordTriangleRegression.agda',
             HERE.parent / 'results/actual-pair-phase-rung-bridge.json']
    receipt = {
        'schema': 'marici.nima.predictive-pair-coherence-descent.v1',
        'status': 'pass', 'checks': checks,
        'formal_condition': 'C_target composed with U_request equals C_source',
        'formal_source': str(FORMAL.relative_to(ROOT)),
        'verification_kind': 'Exact finite permutation realization; not an Agda compiler instantiation',
        'frames': len(frames), 'states_per_joint_endpoint': 3,
        'coherent_candidate_targets': admitted, 'incoherent_candidate_targets': rejected,
        'frame_carrier': rational_tree(frames),
        'presentations': [{'state': i, 'endpoint': state[0],
                           'frame_id': ids[state[1]], 'witness': q.witnesses[i]}
                          for i, state in enumerate(q.states)],
        'coordinates': [list(c) for c in coordinates],
        'requests': [{'action': a, 'permutation': u} for a, u in actions.items()],
        'endpoint_obstruction': {'word': nontrivial, 'state': p,
                                 'identity_loop_state': e, 'moved_frame_id': moved,
                                 'image_frame_id': holonomy[moved]},
        'input_sha256': {str(path.relative_to(ROOT)): hashlib.sha256(path.read_bytes()).hexdigest()
                         for path in paths},
        'scope': ['transported normalization coordinates descend to the 60-state quotient',
                  'endpoint-only faithful fixed coordinates are obstructed by nontrivial holonomy',
                  'all currently admitted requests remain coherent with their actual targets',
                  'rejecting wrong target presentations is not selecting a physical interaction',
                  'formal source supplies law shape; no Agda proof or native seed binding added'],
    }
    output = HERE.parent / 'results/predictive-pair-coherence-descent.json'
    output.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(checks)} exact normalization-coherence descent checks')
    print(f'Candidate target gate: {admitted} coherent, {rejected} incoherent.')
    print('Transported coordinates descend to 60 states; endpoint-only coordinates are obstructed.')
    print('Scope: finite realization of native condition, not physical admission or Agda instantiation.')


if __name__ == '__main__':
    main()
