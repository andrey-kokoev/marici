"""Dependency-free exact synthetic controls. Never connects to instruments."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
import json
import re
from math import isfinite

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/krakensdr-physical-composition.v1.json'
TEMPLATE = BASE+'contracts/krakensdr-physical-composition-run.template.json'
NOTE = BASE+'krakensdr-physical-composition-v1.md'
SELF = BASE+'checkers/check_krakensdr_physical_composition.py'
OUT = ROOT/(BASE+'results/krakensdr-physical-composition-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def cmul(z, w):
    return (z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0])


def norm2(z):
    return sum(x*x for x in z)


def cdiv(z, w):
    return tuple(x/norm2(w) for x in cmul(z, (w[0], -w[1])))


def matvec(a, v):
    return [sum(x*y for x, y in zip(row, v)) for row in a]


def quadratic(v, a):
    return sum(x*y for x, y in zip(v, matvec(a, v)))


def finite_number(value):
    if type(value) not in (int, float):
        return False
    try:
        return isfinite(value)
    except OverflowError:
        return False


def specification_errors(m):
    """Lexical/consistency preflight only; does not verify evidence contents."""
    errors = []
    if m.get('status') != 'specification_frozen' or not m.get('run_id'):
        errors.append('unfrozen_or_unnamed')
    for key in ['inventory', 'manual_port_limits', 'safe_link_budget', 'component_receiver_calibration',
                'joint_noise_drift', 'power_loss', 'loaded_topology', 'model_and_code']:
        item = m.get('evidence', {}).get(key)
        if not isinstance(item, dict) or not item.get('path') or not re.fullmatch('[0-9a-f]{64}', str(item.get('sha256', ''))):
            errors.append('missing_reference:'+key)
    configurations = m.get('configuration_ids', [])
    if set(configurations) != {'A0B0', 'A0B1', 'A1B0', 'A1B1'} or len(configurations) != 4:
        errors.append('factorial_context_unavailable')
    partitions = m.get('partitions', {})
    lists = [partitions.get(k, []) for k in ['pilot', 'calibration', 'evaluation']]
    if any(not x for x in lists) or any(len(set(x)) != len(x) for x in lists):
        errors.append('empty_or_duplicate_partition')
    if any(set(lists[i]) & set(lists[j]) for i in range(3) for j in range(i)):
        errors.append('partition_leakage')
    capture = m.get('capture', {})
    if not capture.get('verified_alias_safe') or not capture.get('verified_linear'):
        errors.append('capture_domain_unverified')
    for k in ['center_frequency_hz', 'sample_rate_hz', 'source_level']:
        value = capture.get(k)
        if not finite_number(value) or (k != 'source_level' and value <= 0):
            errors.append('missing_capture:'+k)
    if not capture.get('source_level_units'):
        errors.append('missing_capture_units')
    a = m.get('analysis', {})
    for k in ['per_setting_refit', 'program_target_responses', 'labels_as_signal_features']:
        if a.get(k) is not False:
            errors.append('forbidden_analysis:'+k)
    for k in ['common_phase_reference', 'covariance_rule', 'singular_range_rule']:
        if not a.get(k):
            errors.append('missing_analysis:'+k)
    acceptance = m.get('acceptance', {})
    for k in ['absolute_error_tolerance', 'drift_limit']:
        value = acceptance.get(k)
        if not finite_number(value) or value <= 0:
            errors.append('missing_numeric_acceptance:'+k)
    confidence = acceptance.get('confidence')
    if not finite_number(confidence) or not 0 < confidence < 1:
        errors.append('missing_confidence')
    for k in ['error_units', 'coverage_rule', 'multiplicity_rule']:
        if not acceptance.get(k):
            errors.append('missing_acceptance:'+k)
    acquisition = m.get('acquisition', {})
    if type(acquisition.get('repetitions')) is not int or acquisition['repetitions'] < 2:
        errors.append('missing_repetition_count')
    for k in ['settling_reset_rule', 'randomization_rule', 'raw_storage']:
        if not acquisition.get(k):
            errors.append('missing_acquisition:'+k)
    return errors


def report():
    c = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    draft = json.loads((ROOT/TEMPLATE).read_text(encoding='utf-8'))
    require(all(v is False for v in c['evidence_boundary'].values()), 'software is not physical evidence')
    counts = {}
    n = 0
    for a, b in product([F(1, 2), F(2, 3), F(3, 4)], [F(1, 3), F(1, 2), F(4, 5)]):
        records = [F(1), b, a, a*b]  # 00,01,10,11
        delta = records[3]-records[2]-records[1]+records[0]
        require(delta == (b-1)*(a-1) != 0 and a*b-b*a == 0, 'mixed contrast does not certify noncommutativity or nonlinearity')
        n += 1
    counts['commuting_mixed_contrast'] = n
    A, B, x = [[F(1), 0], [0, F(1, 2)]], [[0, F(1)], [F(1), 0]], [F(1), 0]
    BA, AB = matvec(B, matvec(A, x)), matvec(A, matvec(B, x))
    require(norm2([u-v for u, v in zip(BA, AB)]) == F(1, 4), 'hypothetical two-mode order contrast is distinct,not attributed to the owned splitter')
    counts['hypothetical_two_mode_order_contrast'] = 1
    for S in [[[F(0), F(1, 2)], [F(1, 2), F(1, 2)]], [[F(1, 3), F(1, 2)], [F(1, 2), F(0)]]]:
        # I-S^T S is PSD by exact two-by-two principal minors.
        P = [[F(i == j)-sum(S[k][i]*S[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
        require(P[0][0] >= 0 and P[1][1] >= 0 and P[0][0]*P[1][1]-P[0][1]**2 >= 0, 'loading hostile uses passive reciprocal component fixtures')
    forward, reverse = F(1, 4)/(1-F(1, 2)*F(1, 3)), F(1, 4)
    require(forward-reverse == F(1, 20), 'classical internal reflections alone give an order effect')
    counts['passive_mismatch_order_effect'] = 1
    n = 0
    for r in [F(1, 2), F(2, 3), F(1)]:
        z, w = (3*r/5, 4*r/5), (3*r/5, -4*r/5)
        require(norm2(z) == norm2(w) == r*r and z[0] == w[0] and norm2([a-b for a, b in zip(z, w)]) == F(64, 25)*r*r, 'joint quadratures resolve the declared coarse collision')
        n += 1
    counts['conjugate_quadrature_blindness'] = n
    z = (F(6, 5), F(8, 5))
    reciprocal = cdiv((F(1), F(0)), z)
    require(norm2(z) == 4 and norm2(reciprocal) == F(1, 4), 'swapping unequal-loss paths does not create an intensity-blind conjugate pair')
    counts['unequal_loss_reciprocal_guard'] = 1
    delta = [1, -1, -1, 1]
    require(sum(delta) == 0 and sum(a*b for a, b in zip(delta, [0, 0, 1, 1])) == 0 and sum(a*b for a, b in zip(delta, [0, 1, 0, 1])) == 0 and delta[3] == 1, 'native optional four-record contrast is invisible to either bit,not a physical RF amplitude')
    counts['joint_record_marginal_blindness'] = 1
    endpoint_0, endpoint_1 = (1, 0), (1, 0)
    interior_0, interior_1 = (1, 0), (0, -1)
    require(endpoint_0 == endpoint_1 and norm2([a-b for a, b in zip(interior_0, interior_1)]) == 2, 'one carrier-period delay ambiguity is resolved off the endpoint frequency')
    counts['endpoint_delay_alias'] = 1
    calibration_gain, heldout_input, heldout_observation = F(2), F(3), F(9)
    require(heldout_observation-calibration_gain*heldout_input == 3 and heldout_observation/heldout_input == 3 != calibration_gain, 'free per-row gain fits the adversarial holdout but does not validate the common calibration model')
    counts['held_out_common_gain_failure'] = 1
    n = 0
    for error, upper_margin, tolerance, expected in [(F(1, 10), F(1, 100), F(1, 20), False), (F(1, 100), F(1, 200), F(1, 20), True)]:
        equivalent = error+upper_margin <= tolerance
        require(equivalent == expected, 'equivalence uses an upper error bound,not failure to reject')
        n += 1
    require(F(1, 10)**2/100 < F(1, 1000), 'a large noise covariance can hide a physically excessive residual')
    counts['equivalence_not_nonrejection'] = n
    n = 0
    contrast = [F(1), F(-1), F(-1), F(1)]
    for drift, full in [([F(1)]*4, F(4)), (contrast, F(20))]:
        covariance = [[F(i == j)+drift[i]*drift[j] for j in range(4)] for i in range(4)]
        diagonal_only = sum(contrast[i]**2*covariance[i][i] for i in range(4))
        require(quadratic(contrast, covariance) == full and diagonal_only == 8 != full, 'joint contrast covariance must preserve shared drift')
        n += 1
    counts['correlated_contrast_covariance'] = n
    n = 0
    z = (F(3, 5), F(4, 5))
    for common in [(F(1), F(0)), (F(0), F(1)), (F(-1), F(0))]:
        require(cdiv(cmul(z, common), common) == z, 'a calibrated simultaneous common reference removes only the common phase')
        n += 1
    counts['common_reference_phase_transport'] = n
    errors = specification_errors(draft)
    require(errors and not draft['physical_evidence_verified'] and not draft['hardware_energization_authorized'], 'production draft remains blocked')
    counts['draft_preflight_blocked'] = 1
    complete = deepcopy(draft)
    complete.update(status='specification_frozen', run_id='SYNTHETIC-NOT-A-RUN', data_origin='synthetic_fixture')
    complete['evidence'] = {k: {'path': 'synthetic://not-measured/'+k, 'sha256': '0'*64} for k in draft['evidence']}
    complete['configuration_ids'] = ['A0B0', 'A0B1', 'A1B0', 'A1B1']
    complete['partitions'] = {'pilot': ['p0'], 'calibration': ['c0'], 'evaluation': ['e0']}
    complete['capture'] = {'verified_alias_safe': True, 'verified_linear': True, 'center_frequency_hz': 1, 'sample_rate_hz': 1, 'source_level': -1, 'source_level_units': 'synthetic units,not an instrument setting'}
    complete['analysis'].update(common_phase_reference='synthetic reference', covariance_rule='full joint synthetic covariance', singular_range_rule='reject unresolved range')
    complete['acceptance'] = {'absolute_error_tolerance': 1, 'error_units': 'synthetic', 'confidence': 0.95, 'coverage_rule': 'synthetic simultaneous', 'multiplicity_rule': 'synthetic fixed family', 'drift_limit': 1}
    complete['acquisition'] = {'repetitions': 2, 'settling_reset_rule': 'synthetic', 'randomization_rule': 'synthetic fixed seed', 'raw_storage': 'synthetic://no-files'}
    require(not specification_errors(complete) and not complete['hardware_energization_authorized'] and not complete['physical_evidence_verified'], 'specification completeness does not verify references or authorize hardware')
    counts['synthetic_complete_specification_only'] = 1
    mutations = [
        ('evidence', 'manual_port_limits', None), ('acceptance', 'absolute_error_tolerance', None),
        ('analysis', 'covariance_rule', None), ('partitions', 'evaluation', ['c0']),
        ('analysis', 'per_setting_refit', True), ('analysis', 'program_target_responses', True),
        (None, 'configuration_ids', ['A0B0']), ('capture', 'verified_alias_safe', False),
        ('analysis', 'labels_as_signal_features', True), ('analysis', 'common_phase_reference', None),
        ('evidence', 'power_loss', None), ('acquisition', 'settling_reset_rule', None),
        ('capture', 'source_level', float('nan'))]
    for section, key, value in mutations:
        bad = deepcopy(complete)
        (bad if section is None else bad[section])[key] = value
        require(specification_errors(bad), 'fail closed on missing or circular prerequisite:'+key)
    counts['fail_closed_specification_mutations'] = len(mutations)
    require(counts == c['frozen_synthetic_coverage'] and sum(counts.values()) == 40, 'frozen exact fixture coverage')
    inputs = [CONTRACT, TEMPLATE, NOTE, SELF, c['predecessor_protocol'],
              'research/nima/seed-joint-parity-response.md', 'research/nima/tick-unitary-image-nonuniqueness.md',
              'research/voevodsky/route_residue_metaphysical_premise_correction.md']
    return {'schema': 'marici.krakensdr.physical-composition.result.v1', 'passed': True,
            'new_exact_synthetic_controls': 40, 'coverage': counts,
            'commuting_mixed_contrast_can_be_nonzero': True,
            'passive_loading_order_defect': '1/20', 'heldout_common_gain_residual': '3',
            'joint_contrast_covariances': ['4', '20'], 'incorrect_diagonal_only_variance': '8',
            'production_template_errors': errors,
            'software_only': True, 'instrument_io_executed': False, 'physical_evidence_verified': False,
            'acquisition_preregistration_complete': False, 'hardware_energization_authorized': False,
            'historical_protocol_modified': False,
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}}


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in r.items() if k not in ('input_sha256', 'production_template_errors')}, indent=2))
