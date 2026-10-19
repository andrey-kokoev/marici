# /// script
# dependencies = ["numpy>=2,<3", "sympy"]
# ///
"""Compare existing rung and instrument contracts; do not construct a new adapter."""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
from contextlib import redirect_stdout
from fractions import Fraction as F
from pathlib import Path
import hashlib
import io
import json
import runpy
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE.parent / 'results/seed-instrument-binding-comparison.json'


def main():
    OUT.unlink(missing_ok=True)
    checks = []
    fresh = {}

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    def execute(name, entry=False):
        path = HERE / name
        with redirect_stdout(io.StringIO()):
            data = runpy.run_path(str(path), run_name='__main__' if entry else '<run_path>')
        fresh[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        return data

    tower = execute('check_rung_transport_diagram.py')
    instrument = execute('check_source_exchange_end_to_end.py')
    check('existing-instrument-check-passed', instrument['result']['status'] == 'passed')
    execute('check_rung_descent_endpoint_binding.py', entry=True)
    endpoint = json.loads((HERE.parent / 'results/rung-descent-endpoint-binding.json').read_text())
    check('existing-actual-path-endpoint-check-passed', endpoint['verification_status'] == 'pass')

    # Exact interface agreement for the EXISTING 137-row fixture only.
    check('same-native-values', tower['m']['values'] == instrument['native']['values'])
    check('same-fixed-reference', tower['physical_reference'].value == instrument['native']['values']['d'])
    expected_labels = tuple(
        [('a', a, b) for a in tower['E'] for b in tower['E']]
        + [('s', a, b) for a in range(4) for b in range(4)])
    check('same-labelled-port-order', instrument['ex'].labels == expected_labels)
    residuals = []
    for row in tower['source']:
        residual = tower['add'](row.value, tower['scale'](-1, tower['physical_reference'].value))
        residuals.append(residual[0][0] + residual[1][1])
    check('all137-preparation-traces-match-in-order', residuals == instrument['raw'])
    readers = {}
    for policy in ('inherited', 'common'):
        rows = tower['incoming_promotion'](tower['source'], 1, policy)
        rows = tower['incoming_promotion'](rows, 2, policy)
        view = tower['indexed'](rows, 'target')
        readers[policy] = tower['read_at_four'](view)
    check('both-rung-policies-same-aggregate', readers['inherited'] == readers['common'])
    J = readers['inherited']
    trace = J[0][0] + J[1][1]
    check('trace-of-J4-is-mean-native-response', trace == sum(residuals, F(0))/137)
    check('mean-prepared-X-is-gain-times-trace-J4',
          abs(float(instrument['gamma']*trace) - np.mean(instrument['seed'])) < 1e-10)

    # The implemented instrument retains native preparation as provenance and
    # adds independent current corrections. Projection onto that provenance
    # is NOT an asserted native time evolution. Test that projection explicitly.
    ex = instrument['ex']
    echo = instrument['echo']
    rectangle = instrument['rectangle']
    check('same-preparation-id', echo.preparation_id == rectangle.preparation_id)
    check('different-retained-event-histories', echo.history != rectangle.history)
    check('echo-restores-full-current-state', np.max(np.abs(instrument['state_echo']-instrument['state0'])) < 1e-10)
    check('rectangle-needs-current-memory', np.linalg.norm(instrument['corrections']) > 1e-10)
    check('faithful-packet-reconstructs-current-memory',
          np.max(np.abs(instrument['seed'] + instrument['corrections'] - ex.state(rectangle)[16:])) < 1e-10)
    ratios = instrument['ratios']
    check('same-native-preparation-different-detector-response',
          abs(ratios['exchange_echo']-1) < 1e-10 and abs(ratios['exchange_rectangle']) < 1e-10)

    support = instrument['result']['fresh_support_checks']
    for name in ('matrix-leg-exchange-closure', 'witness-record-memory-gate', 'exchange-shared-leg-composition'):
        receipt = json.loads((HERE.parent / 'results' / (name+'.json')).read_text())
        check('fresh-negative-control/'+name, receipt['status'] == 'passed')
    result = {
        'schema': 'marici.nima.seed-instrument-binding-comparison.v1',
        'verification_status': 'pass', 'source_selected_descent_complete': False,
        'checks': checks, 'fresh_top_level_sha256': fresh, 'fresh_instrument_support': support,
        'exact_common_fixture_interface': {
            'J4': [[str(x) for x in row] for row in J],
            'trace_J4': str(trace), 'preparation_gain': str(instrument['gamma']),
            'mean_prepared_X': str(instrument['gamma']*trace),
            'scope': 'Existing shared-leg fixture only; not a six-arrow-seed realization.'},
        'projection_collision': {
            'projection': 'Forget event history and attached current memory; retain original matrix preparation.',
            'same_projected_J4': True,
            'echo_detector_ratio': float(ratios['exchange_echo']),
            'rectangle_detector_ratio': float(ratios['exchange_rectangle']),
            'conclusion': 'Detector response does not factor through J4 of retained preparation.',
            'scope': 'No native evolution of matrix legs is supplied or inferred by this projection.'},
        'gates': {
            'seed_to_fixture': 'Not supplied: amplitudes, state branch, reference, and DG witness interpretation.',
            'fixture_to_preparation': 'Exact declared trace/gain interface matches all137 existing rung leaves.',
            'operation': 'Labelled event compiler passes; shared-leg closure and strict invertible factorization fail in their tested scopes.',
            'memory': 'Current corrections reconstruct; existing fixed-boundary witness reader cannot encode independent corrections.',
            'observation': 'Initial mean agrees with trace J4; addressed detector response needs current memory and event execution.',
            'physical_selection': 'Preparation, pulse, memory attachment, detector, and intended T9 remain unselected.'},
        'actual_path_endpoint_receipt': endpoint['schema'],
        'scope': 'Fresh comparison of existing constructions; no new source map, pulse, reader, or physical calibration.'}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(f'PASS: {len(checks)} existing-chain binding comparison checks')
    print('Exact preparation interface found; source-selected operation and observation binding remain open.')


if __name__ == '__main__':
    main()
