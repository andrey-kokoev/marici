# /// script
# dependencies = ["sympy", "numpy>=2,<3"]
# ///
"""Audit existing native/field/reference operations without inventing adapters.

Fresh Agda closure is a separate prerequisite; the Python audits validate its
receipts. Exact period obstructions concern one source step per target step.
"""
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS', '1')
from contextlib import redirect_stdout
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import runpy
import sympy as S

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
OUT = HERE.parent/'results/native-memory-chain-compatibility.json'


def main():
    OUT.unlink(missing_ok=True)
    checks, fresh = [], {}

    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)

    def execute(name, entry=False, function=None):
        path = HERE/name
        with redirect_stdout(io.StringIO()):
            data = runpy.run_path(str(path), run_name='__main__' if entry else '<run_path>')
            if function:
                data[function]()
        fresh[name] = hashlib.sha256(path.read_bytes()).hexdigest()
        return data

    query = execute('check_native_transition_instrument.py')
    policy = execute('check_native_instrument_policy_classification.py')
    execute('check_twelve_triangle_positive_geometry.py', function='regression_main')
    phase = execute('check_phase_memory_first_moment.py', entry=True)
    history = execute('check_native_history_memory_realization.py')
    bank = execute('check_four_packet_record_feedback.py', entry=True)
    execute('check_retained_memory_reference.py', entry=True)
    execute('check_seed_instrument_binding_comparison.py', entry=True)
    check('native-policy-census-reproduced', policy['result']['admissible_count'] == 36)

    # No total equivariant map from this recorder to the ACTUAL changing
    # route-count orbit: fixed points must map to fixed points, but it has none.
    states = tuple(query['states'])
    record = query['record']
    index = {s: i for i, s in enumerate(states)}
    permutation = tuple(index[record(s)] for s in states)
    fixed = [s for s in states if record(s) == s]
    check('recorder-has-six-fixed-states', len(fixed) == 6)
    check('recorder-true-query-is-two-cycle', record((0,0)) == (0,1) and record((0,1)) == (0,0))
    actual = (history['initial_counts'], history['returned_counts'])
    check('actual-route-orbit-is-nonconstant-two-cycle', actual[0] != actual[1] and actual[0][::-1] == actual[1])
    possible = [f for f in product(range(2), repeat=8)
                if all(f[permutation[i]] == 1-f[i] for i in range(8))]
    check('no-total-recorder-to-actual-route-orbit-intertwiner', possible == [])
    orientations = [f for f in product(range(2), repeat=2) if f[1] == 1-f[0]]
    check('true-query-restriction-has-two-unselected-orientations', len(orientations) == 2)

    # The existing source-count-to-field encoding DOES intertwine.
    encode, step = history['encode'], history['step']
    first, second = encode(actual[0], F(1)), encode(actual[1], F(1))
    check('actual-history-field-intertwiner', step(*first) == second and step(*second) == first)
    check('fixed-decoded-payload', history['add'](*first) == history['add'](*second) == history['u'])
    check('nonempty-preparation-cost', history['total'](*first)-history['total'](history['u'], history['zero']) == F(80,3))
    check('coarse-history-encoding-not-injective', encode((1,2),F(1)) == encode((2,3),F(1)))

    # Compare actual existing linear laws, NOT dimensions alone.
    def history_update(v):
        a,b = step(tuple(v[:12]), tuple(v[12:]))
        return a+b
    U = S.Matrix(bank['matrix_of'](history_update,24))
    V = S.Matrix(bank['matrix_of'](bank['full_cycle'],20))
    Iu, Iv = S.eye(24), S.eye(20)
    check('history-law-is-involution', U*U == Iu and U != Iu)
    check('reference-law-has-order-six', V**6 == Iv and all(V**k != Iv for k in (1,2,3)))
    multiplicities = {
        'history_plus': 24-(U-Iu).rank(), 'history_minus': 24-(U+Iu).rank(),
        'reference_plus': 20-(V-Iv).rank(), 'reference_minus': 20-(V+Iv).rank(),
        'reference_two_periodic': 20-(V*V-Iv).rank()}
    check('exact-eigenspace-dimensions', multiplicities == {
        'history_plus':13, 'history_minus':11, 'reference_plus':6,
        'reference_minus':6, 'reference_two_periodic':12})
    # V M=M U implies (V^2-I)M=0, hence rank M<=12. This is not
    # merely the trivial 24-to20 dimension obstruction.
    check('one-step-linear-image-bound-is-twelve', multiplicities['reference_two_periodic'] == 12)
    empty = S.Matrix(bank['UNIT']+bank['ZERO16'])
    check('existing-empty-bank-reference-orbit-has-period-three',
          V**3*empty == empty and V*empty != empty and V**2*empty != empty)
    # Even a nonlinear equivariant map out of a two-cycle has a two-periodic
    # image, so it cannot hit this original empty-bank reference trajectory.
    check('actual-two-cycle-cannot-hit-empty-bank-return-orbit', V**2*empty != empty)
    # A rescheduling can remove that period obstruction; it is new policy,
    # not the existing one-step comparison under audit.
    check('three-reference-steps-form-a-nontrivial-involution', (V**3)**2 == Iv and V**3 != Iv)

    receipts = {}
    for module in ('NativeTransitionInstrument','NativeFeedbackRouteReadout'):
        path = HERE.parent/'results'/f'agda-{module}.json'
        receipt = json.loads(path.read_text(encoding='utf-8-sig'))
        check('formal-receipt-valid/'+module, receipt['passed'] and receipt['ignore_interfaces']
              and receipt['inputs_stable_during_check'])
        receipts[module] = {'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                            'finished_at':receipt['finished_at'],
                            'source_sha256':receipt['source_sha256']}
    result = {
        'schema':'marici.nima.native-memory-chain-compatibility.v1',
        'verification_status':'pass', 'source_selected_rung_descent_complete':False,
        'checks':checks, 'fresh_python_sha256':fresh, 'formal_receipts':receipts,
        'recorder_to_actual_route_orbit':{
            'total_equivariant_maps':len(possible),
            'true_query_restricted_orientations':len(orientations),
            'scope':'Fixed recorder states cannot map to the actual nonconstant two-cycle. Other route orbits or controlled laws are not excluded.'},
        'history_to_reference':{
            'eigenspace_dimensions':multiplicities, 'linear_one_step_intertwiner_rank_bound':12,
            'existing_empty_bank_orbit_period':3,
            'scope':'One update per update. Restriction, changed schedule, controller, or another preparation is additional data.'},
        'positive_result':'Existing route-count swap intertwines with the existing prepared twelve-mode memory law; decoded payload stays fixed and the extra80/3 budget remains explicit.',
        'rung_boundary':'The separately rerun137-record interface remains only a declared trace/gain preparation binding. None of these native or numerical mechanisms is identified with its current writable ports or intended T9.',
        'next_required_data':[
            'A common typed source task and state binding, rather than identifying distinct native fixtures.',
            'Protected observables, allowed changes, and memory preparation policy.',
            'A justified schedule or restricted invariant sector if relating the involution to the order-six reference law.',
            'An operation-and-observation binding into the actual137-record rung interface.'],
        'scope':'Exact rational and finite compatibility audit, with fresh existing numerical chain checks; no new physical adapter or instrument policy.'}
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} native-memory compatibility checks')
    print('Naive one-step chaining rejected: recorder fixed points and reference-return period are incompatible.')
    print('Existing history-to-field intertwiner survives with explicit preparation cost; rung binding remains open.')


if __name__ == '__main__':
    main()
