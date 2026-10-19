"""Compare actual proton words in the phase/spin and existing exchange actions.

Exact exchange decomposition into conserved anchor and six evolving mismatch
coordinates. This binds no exchange operation to electron requests and selects
no new interaction or preparation law.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S

from check_actual_pair_phase_rung_bridge import main as phase_main
from check_predictive_pair_proton_spin_binding import main as spin_main
from predictive_pair_quotient import PredictivePairQuotient

HERE = Path(__file__).resolve().parent


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    with redirect_stdout(io.StringIO()):
        old = runpy.run_path(str(HERE / 'check_seed_port_exchange_binding.py'))
        phase = phase_main()
        spin_main()
    q = PredictivePairQuotient(phase)
    labels, F, H = old['labels'], old['features'], old['H']
    operators, metric = old['operators'], old['metric']
    anchor, B, K = old['anchor'], old['B'], old['K']
    # r=K^-1(delta+F^T H a), y=a-F r. This is reconstruction,
    # not deletion of the six hidden mismatch channels.
    inverse_K = K.inv()
    decoder_r = (inverse_K*F.T*H).row_join(inverse_K)
    decoder_y = (S.eye(16)-F*inverse_K*F.T*H).row_join(-F*inverse_K)
    decoder = decoder_y.col_join(decoder_r)
    encoder = anchor.col_join(B)
    check('decomposition/two-sided-inverse', encoder*decoder == S.eye(22)
          and decoder*encoder == S.eye(22))
    check('decomposition/six-independent-mismatches', B.rank() == 6)
    # Induced positive metric on mismatch at fixed zero anchor.
    mismatch_metric = decoder[:,16:].T*metric*decoder[:,16:]
    check('decomposition/mismatch-metric', mismatch_metric == inverse_K)
    reduced = {}
    for i, label in enumerate(labels):
        T = S.eye(6)-K[:,i]*S.eye(6)[i,:]
        reduced[label] = T
        check('port/mismatch-intertwiner/' + label, B*operators[label] == T*B)
        check('port/anchor-fixed/' + label, anchor*operators[label] == anchor)
        check('port/full-conjugacy/' + label,
              encoder*operators[label]*decoder == S.diag(S.eye(16), T))
        check('port/mismatch-metric-preserved/' + label, T.T*inverse_K*T == inverse_K)
        check('port/reduced-involution/' + label, T*T == S.eye(6))

    def word_action(word, actions, dimension):
        result = S.eye(dimension)
        for label in word:
            result = actions[label]*result
        return result
    def path_for(word):
        endpoint = ('A', 'E')
        path = ()
        for label in word:
            edge = next(edge for (edge,) in q.bridge['frame'] if edge[0] == endpoint
                        and edge[2][0] == 'proton' and ''.join(edge[2][2:]) == label)
            path += (edge,)
            endpoint = edge[1]
        return path
    first_word = ('AB', 'BC', 'CA')*2
    second_word = first_word*2
    first_path, second_path = path_for(first_word), path_for(second_word)
    check('collision/same-geometric-predictive-state', q.project(first_path) == q.project(second_path))
    # Both lift signs return after six applications of the first generator.
    from check_proton_electron_contact_binding import decode_matrix, I
    from check_pentachoron_cycle_transport import power
    spin_receipt = HERE.parent / 'results/predictive-pair-proton-spin-binding.json'
    spin = json.loads(spin_receipt.read_text())
    for variant in spin['variants']:
        if set(variant['arrows']) == {'AB', 'BC', 'CA'}:
            u = decode_matrix(variant['logical_action'])
            check('collision/both-spin-signs-return', power(u,6) == power(u,12) == I)
    first = word_action(first_word, operators, 22)
    second = word_action(second_word, operators, 22)
    residual = second-first
    check('collision/exchange-actions-differ', residual != S.zeros(22))
    check('collision/residual-invisible-to-anchor', anchor*residual == S.zeros(16,22))
    check('collision/residual-visible-to-mismatch', B*residual != S.zeros(6,22))
    excited = old['excited']  # unchanged unit AB-record preparation
    z1, z2 = first*excited, second*excited
    check('collision/old-preparation-witnesses-difference', z1 != z2)
    check('collision/same-anchor', anchor*z1 == anchor*z2)
    check('collision/same-budget', (z1.T*metric*z1)[0] == (z2.T*metric*z2)[0] == 1)
    for name, word, path, output in (('first',first_word,first_path,z1),
                                      ('second',second_word,second_path,z2)):
        delta = word_action(word,reduced,6)*B*excited
        check('history/reduced-prediction/' + name, delta == B*output)
        check('history/exact-reconstruction/' + name,
              decoder*(anchor*excited).col_join(delta) == output)
        for policy in ('inherited','common'):
            retained = q.retain(path,policy)
            restored = q.restore(retained)
            restored_word = tuple(''.join(edge[2][2:]) for edge in restored)
            check('rung/exchange-reading/' + name + '/' + policy,
                  word_action(restored_word,operators,22)*excited == output)
            check('rung/mismatch-reading/' + name + '/' + policy,
                  word_action(restored_word,reduced,6)*B*excited == delta)
    # Prove failure on the whole input domain, not only an excited sample.
    kernel = residual.nullspace()
    check('residual/kernel-exact', all(residual*v == S.zeros(22,1) for v in kernel)
          and len(kernel)+residual.rank() == 22)
    mismatch_residual = word_action(second_word,reduced,6)-word_action(first_word,reduced,6)
    check('residual/reduced-rank-agrees', mismatch_residual.rank() == residual.rank())
    nonzero = next((i,str(x)) for i,x in enumerate(z2-z1) if x)
    def matrix(m):
        return [[str(x) for x in row] for row in m.tolist()]
    files = [Path(__file__), HERE/'check_seed_port_exchange_binding.py',
             HERE/'check_actual_pair_phase_rung_bridge.py', spin_receipt,
             HERE.parent/'results/seed-port-exchange-binding.json']
    result = {'schema':'marici.nima.predictive-pair-exchange-residual.v1',
              'status':'pass','checks':checks,
              'collision':{'first_word':first_word,'second_word':second_word,
                           'same_geometric_state':q.project(first_path),
                           'both_spin_actions':'identity for either lift sign',
                           'exchange_residual_rank':residual.rank(),
                           'exchange_residual_kernel_dimension':len(kernel),
                           'old_AB_preparation_nonzero_residual':nonzero},
              'decomposition':{'anchor_dimensions':16,'mismatch_dimensions':6,
                               'encoder':matrix(encoder),'decoder':matrix(decoder),
                               'mismatch_metric':matrix(inverse_K),
                               'port_updates':{a:matrix(t) for a,t in reduced.items()}},
              'scope':'Existing conditional proton-port exchange only. No electron exchange '
                      'assigned. Six mismatch coordinates suffice for this exchange; minimality '
                      'for a chosen observation not asserted. Conserved anchor is needed for '
                      'full reconstruction, and initial preparation is external. '
                      'No physical contact, charge law, event duration or spin coupling inferred.',
              'input_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    output_path = HERE.parent/'results/predictive-pair-exchange-residual.json'
    output_path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact source-word exchange comparison checks')
    print(f'Same geometric/spin return, different exchange: residual rank {residual.rank()}.')
    print('Six mismatch coordinates close; anchor plus mismatch recovers all 22 exchange coordinates.')
    return {'phase': phase, 'quotient': q, 'exchange': old,
            'encoder': encoder, 'decoder': decoder, 'updates': reduced,
            'spin_variants': spin['variants']}


if __name__ == '__main__':
    main()
