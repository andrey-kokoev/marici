"""Replay and verify the consolidated stateful proton operation interface."""
from contextlib import redirect_stdout
from dataclasses import replace
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import sympy as S

from check_predictive_pair_exchange_residual import main as build
from retained_proton_operation import RetainedProtonOperation
from check_proton_electron_contact_binding import ONE, ZERO, act, norm

HERE = Path(__file__).resolve().parent


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    def rejects(name, f):
        try:
            f()
        except ValueError:
            checks.append(name)
        else:
            raise AssertionError(name)
    with redirect_stdout(io.StringIO()):
        binding = build()
    q = binding['quotient']
    old = binding['exchange']
    actions = {''.join(a[2:]): a for a in q.actions if a[0] == 'proton'}
    words = [()]
    frontier = [(('A','E'), ())]
    for _ in range(6):
        following = []
        for endpoint, word in frontier:
            for (s,t,a), in q.bridge['frame']:
                if a[0] == 'proton' and s == endpoint:
                    following.append((t,word+(a,)))
        words.extend(word for _,word in following)
        frontier = following
    for signs in product(('+I','-I'),repeat=2):
        api = RetainedProtonOperation(binding, signs)
        initial = api.prepare((ONE,ZERO), tuple(old['excited']))
        for word in words:
            execution = api.execute(initial,word)
            check('history/inverse', api.recover(execution) == initial)
            check('state/exchange-budget',
                  (S.Matrix(api.exchange_state(execution.final)).T*old['metric']*
                   S.Matrix(api.exchange_state(execution.final)))[0] == 1)
            check('state/spin-norm', norm(execution.final.spin) == ONE)
            # Independent full 22-row update, not merely reduced-state replay.
            full = old['excited']
            for a in word:
                full = old['operators'][''.join(a[2:])]*full
            check('state/full-exchange-reading', api.exchange_state(execution.final) == tuple(full))
            for cut in range(len(word)+1):
                prefix = api.execute(initial,word[:cut])
                suffix = api.execute(prefix.final,word[cut:])
                check('history/composition', suffix.final == execution.final)
            if word:
                for policy in ('inherited','common'):
                    retained = api.retain(execution,policy)
                    check('rung/recovery/'+policy, api.restore(retained) == execution)
                    check('rung/reading/'+policy,
                          api.observe(api.restore(retained).final) == api.observe(execution.final))
                    for a in q.admitted(execution.final.geometric):
                        if a[0] == 'proton':
                            advanced = api.advance_rung(retained,a,policy)
                            check('rung/operation/'+policy,
                                  api.restore(advanced).final == api.step(execution.final,a))
        first = tuple(actions[x] for x in ('AB','BC','CA')*2)
        second = first*2
        x,y = api.execute(initial,first),api.execute(initial,second)
        check('collision/same-geometry-and-spin', x.final.geometric == y.final.geometric
              and x.final.spin == y.final.spin)
        check('collision/different-mismatch', x.final.mismatch != y.final.mismatch)
        check('collision/same-anchor', x.final.anchor == y.final.anchor)
        rejects('negative/altered-execution', lambda: api.recover(replace(x,final=initial)))
        electron = next(a for a in q.admitted(initial.geometric) if a[0] == 'electron')
        rejects('negative/unbound-electron', lambda: api.step(initial,electron))
        rejects('negative/bad-seam', lambda: api.step(initial,actions['BC']))
        rejects('negative/empty-rung', lambda: api.retain(api.execute(initial,()),'common'))
        other = RetainedProtonOperation(binding, ('-I' if signs[0] == '+I' else '+I', signs[1]))
        rejects('negative/foreign-lift-policy', lambda: other.restore(api.retain(x,'common')))
    files = [Path(__file__),HERE/'retained_proton_operation.py',
             HERE/'check_predictive_pair_exchange_residual.py',
             HERE.parent/'results/predictive-pair-exchange-residual.json']
    report = {'schema':'marici.nima.retained-proton-operation.v1','status':'pass',
              'checks':checks,'lift_policies':4,'words_through_depth_six':len(words),
              'scope':'Six bound proton requests; geometry, spin and exchange are separate readings. '
                      'Exact per-port exchange identities and native bindings are rebuilt. '
                      'History tests are bounded; composition extends by the supplied deterministic '
                      'step recurrence. Rung wrapper retains initial preparation and lift policy '
                      'alongside the unchanged original path record; it is not the old scalar aggregate. '
                      'No electron exchange, physical event IDs, contact law or clock supplied.',
              'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    output = HERE.parent/'results/retained-proton-operation.json'
    output.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} retained proton-operation checks')
    print(f'Four lift policies, {len(words)} words through depth six, both rung policies.')
    print('Geometric/spin return retains nontrivial exchange mismatch; electron exchange rejected.')


if __name__ == '__main__':
    main()
