"""Audit actual endpoint contracts, without renaming retention as physical descent.

Freshly evaluate the unchanged rung-4 reader on a retained source-word collision.
No new source adapter or observation is substituted to make the gate pass.
"""
from contextlib import redirect_stdout
from pathlib import Path
from fractions import Fraction as F
import hashlib
import io
import json
import sympy as S
from check_predictive_pair_exchange_residual import main as build

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    checks = []
    def check(name, condition):
        if not condition: raise AssertionError(name)
        checks.append(name)
    with redirect_stdout(io.StringIO()):
        binding = build()
    q = binding['quotient']
    bridge = q.bridge
    tower = bridge['tower']
    old = binding['exchange']
    words = [('AB','BC','CA')*2,('AB','BC','CA')*4]
    outputs = []
    def history(word):
        endpoint = ('A','E')
        path = ()
        for label in word:
            edge = next(edge for (edge,) in bridge['frame'] if edge[0] == endpoint
                        and edge[2][0] == 'proton' and ''.join(edge[2][2:]) == label)
            path += (edge,)
            endpoint = edge[1]
        return path
    ref = tower['physical_reference']
    check('reader/original-fixed-reference', ref.rung == 4 and ref.value == tower['scale'](2,tower['I']))
    check('source/original-fixture-has-137-leaves', len(tower['source']) == 137)
    for word in words:
        path = history(word)
        state = old['excited']
        for label in word:
            state = old['operators'][label]*state
        readings = {}
        for policy in ('inherited','common'):
            retained = q.retain(path,policy)
            check('transport/actual-word-recovery/'+policy+str(len(word)),q.restore(retained)==path)
            leaves = tower['leaves'](tower['unindex'](retained.view))
            check('adapter/one-identity-valued-path-leaf/'+policy+str(len(word)),
                  len(leaves)==1 and leaves[0].value==tower['I'])
            value = tower['read_at_four'](retained.view)
            check('reader/unchanged-aggregate-blind/'+policy+str(len(word)),
                  value==tower['scale'](F(-1),tower['I']))
            readings[policy] = [[str(x) for x in row] for row in value]
        outputs.append({'word':word,'readings':readings,
                        'mismatch':list(map(str,old['B']*state))})
    check('factorization/same-current-rung-reader', outputs[0]['readings']==outputs[1]['readings'])
    check('factorization/different-required-exchange-reading', outputs[0]['mismatch']!=outputs[1]['mismatch'])
    # Equal inputs to any postprocessing function must give equal outputs.
    # This concrete collision rules out deriving the mismatch from J4 alone
    # for this adapter, not from the full retained rung object.
    files = [Path(__file__),HERE/'check_rung_transport_diagram.py',
             HERE/'check_actual_pair_endpoint_rung_bridge.py',
             HERE/'check_predictive_pair_exchange_residual.py',
             HERE.parent/'results/predictive-pair-exchange-residual.json',
             HERE.parent/'rung-transport-diagram-and-fixed-reference.md',
             HERE.parent/'joint-seam-fixed-reader-closure.md']
    result = {'schema':'marici.nima.rung-descent-endpoint-binding.v1',
              'verification_status':'pass','full_source_selected_descent':'not-established',
              'checks':checks,'witnesses':outputs,
              'endpoint_gates':{
                  'rung12_source':'Original 137-row shared-leg fixture and actual path adapter '
                                  'are distinct inputs; no operation-preserving identification supplied.',
                  'horizontal_transport':'Both retained grouping candidates pass; neither '
                                         'is selected as the intended physical T9 generator.',
                  'rung4_reader':'Original weighted matrix mean minus fixed 2I evaluated unchanged. '
                                 'It cannot recover the exhibited exchange mismatch from its output.',
                  'conditional_seam_reader':'Three-row seam observer belongs to a conditional '
                                            'deleted-edge completion and covariant orphan extension. '
                                            'No supplied map identifies it with the original J4.'},
              'positive_result':'Full retained rung object recovers both histories; separate '
                                'source-bound exchange evaluation recovers their different responses.',
              'negative_result':'No function of the unchanged aggregate J4 alone can reproduce '
                                'the mismatch reading on this witness pair.',
              'next_required_data':['A source operation-preserving binding into the intended rung12 domain',
                                    'An explicit intended T9 construction, not merely coherent regrouping',
                                    'An authorized rung4 observable and source/target reader comparison'],
              'scope':'No claim that all rung4 readers fail or all physical completions are impossible. '
                      'No new readout, reference, coefficient adapter or physical policy introduced.',
              'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    output = HERE.parent/'results/rung-descent-endpoint-binding.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact rung endpoint-binding audit checks')
    print('GATE FAIL: unchanged J4 reads -I for both histories; required mismatch readings differ.')
    print('Retention succeeds; original-source identification and physical observer binding remain absent.')


if __name__ == '__main__':
    main()
