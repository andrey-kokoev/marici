"""Verify history -> predictive state -> observation as one reusable contract."""
from collections import deque
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path

from check_actual_pair_phase_rung_bridge import main as build
from predictive_pair_quotient import PredictivePairQuotient

HERE = Path(__file__).resolve().parent


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    def rejects(name, operation):
        try:
            operation()
        except ValueError:
            checks.append(name)
        else:
            raise AssertionError(name)

    with redirect_stdout(io.StringIO()):
        binding = build()  # fresh source, mode and rung checks; no cached receipt
    q = PredictivePairQuotient(binding)
    check('carrier/60-states', len(q.states) == 60)
    check('carrier/150-transitions', sum(map(len, q.transitions)) == 150)
    bridge = binding['bridge']
    # A valid nonempty loop at the preparation, returning the whole phase frame.
    loop = ()
    endpoint = ('A', 'E')
    for label in ('AB', 'BC', 'CA'):
        edge = next(edge for (edge,) in bridge['frame']
                    if edge[0] == endpoint and edge[2][0] == 'proton'
                    and ''.join(edge[2][2:]) == label)
        loop += (edge,)
        endpoint = edge[1]
    check('provenance/loop-returns-preparation', endpoint == ('A', 'E')
          and binding['path_state'](loop) == binding['initial'])

    for state, witness in enumerate(q.witnesses):
        alternate = loop + witness
        check(f'projection/witness/{state}', q.project(witness) == state)
        check(f'projection/distinct-history-same-state/{state}',
              alternate != witness and q.project(alternate) == state)
        check(f'observation/factorization/{state}', q.observe(state) ==
              (witness[-1][1], binding['outputs'][q.states[state]][1]))
        for action in q.actions:
            tag = f'{state}/{action}'
            if action not in q.admitted(state):
                rejects('rejection/state/' + tag, lambda: q.step(state, action))
                for history in (witness, alternate):
                    rejects('rejection/history/' + tag, lambda: q.advance_history(history, action))
                for policy in ('inherited', 'common'):
                    y = q.retain(witness, policy)
                    rejects('rejection/rung/' + policy + '/' + tag,
                            lambda: q.advance_rung(y, action, policy))
                continue
            target = q.step(state, action)
            endpoint, frame = q.states[state]
            edge = next(edge for (edge,) in bridge['frame']
                        if edge[0] == endpoint and edge[2] == action)
            check('descent/native-recurrence/' + tag,
                  q.states[target] == (edge[1], binding['mode_step'](frame, action)))
            for history in (witness, alternate):
                advanced = q.advance_history(history, action)
                check('descent/history-square/' + tag, q.project(advanced) == target)
                for policy in ('inherited', 'common'):
                    y = q.retain(history, policy)
                    ny = q.advance_rung(y, action, policy)
                    check('transport/exact-provenance/' + policy + '/' + tag,
                          q.restore(y) == history and q.restore(ny) == advanced)
                    check('transport/operation-square/' + policy + '/' + tag,
                          ny == q.retain(advanced, policy) and q.project_rung(ny) == target)
                    check('transport/observation-square/' + policy + '/' + tag,
                          q.observe_rung(y) == q.observe(state)
                          and q.observe_rung(ny) == q.observe(target))
        for policy in ('inherited', 'common'):
            first, second = q.retain(witness, policy), q.retain(alternate, policy)
            check(f'provenance/not-identified/{policy}/{state}', first != second
                  and q.restore(first) == witness and q.restore(second) == alternate
                  and q.project_rung(first) == q.project_rung(second))

    # Explicit distinguishing continuations, not just a partition-size claim.
    def separator(a, b):
        pending = deque([(a, b, ())])
        visited = set()
        while pending:
            left, right, word = pending.popleft()
            if (left, right) in visited:
                continue
            visited.add((left, right))
            if q.observe(left) != q.observe(right):
                return word
            # Same endpoint output implies the same endpoint-admitted labels.
            check('separator/same-output-same-admission',
                  set(q.admitted(left)) == set(q.admitted(right)))
            for action in q.admitted(left):
                pending.append((q.step(left, action), q.step(right, action), word + (action,)))
        raise AssertionError('Indistinguishable distinct predictive states')

    separators = []
    for left in range(len(q.states)):
        for right in range(left):
            word = separator(left, right)
            a, b = left, right
            for action in word:
                a, b = q.step(a, action), q.step(b, action)
            check(f'minimality/separator/{left}/{right}', q.observe(a) != q.observe(b))
            separators.append({'states': [left, right], 'requests': word})
    for bad in (-1, 60, True, '0'):
        rejects('negative/invalid-state', lambda: q.observe(bad))
    rejects('negative/empty-history', lambda: q.project(()))
    rejects('negative/unknown-request', lambda: q.step(0, ('unknown',)))
    rejects('negative/unknown-policy', lambda: q.retain(q.witnesses[0], 'unknown'))
    rejects('negative/broken-history', lambda: q.project((loop[1],)))
    # Serializable finite contract: transition IDs are receipt-local only.
    def serialize(value):
        if isinstance(value, (tuple, list)):
            return [serialize(x) for x in value]
        if isinstance(value, dict):
            return {k: serialize(v) for k, v in value.items()}
        if isinstance(value, (str, int)):
            return value
        return str(value)
    paths = [Path(__file__), HERE / 'predictive_pair_quotient.py',
             HERE / 'check_actual_pair_phase_rung_bridge.py',
             HERE.parent / 'results/actual-pair-phase-rung-bridge.json']
    result = {
        'schema': 'marici.nima.predictive-pair-quotient.v1', 'status': 'pass',
        'checks': checks, 'states': len(q.states),
        'transitions': sum(map(len, q.transitions)),
        'distinguishable_pairs': len(separators),
        'maximum_separator_length': max(len(s['requests']) for s in separators),
        'provenance_loop': loop,
        'table': [{'id': i, 'state': state, 'output': q.observe(i),
                   'witness': q.witnesses[i],
                   'requests': [{'action': a, 'target': t} for a, t in q.transitions[i].items()]}
                  for i, state in enumerate(q.states)],
        'separators': separators,
        'input_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
        'scope': 'Nonempty single histories from (A,E); endpoint-admitted source-generator requests; '
                 'marked centroid observable. No interaction or physical calibration. '
                 'Quotient IDs do not reconstruct history; original rung records do.',
    }
    output = HERE.parent / 'results/predictive-pair-quotient.json'
    output.write_text(json.dumps(serialize(result), indent=2) + '\n', encoding='utf-8')
    print(f'PASS: {len(checks)} predictive quotient contract checks')
    print(f'60 states, 150 transitions, {len(separators)} distinguishing continuations; '
          f'maximum length {result["maximum_separator_length"]}.')
    print('All registered requests tested for descent/rejection; both rung policies preserve provenance.')


if __name__ == '__main__':
    main()
