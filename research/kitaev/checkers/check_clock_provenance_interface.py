"""Exact clock/noise unit transport and saved scope checks; no physical execution."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/clock-provenance-interface.v1.json'
NOTE = BASE+'clock-provenance-interface-v1.md'
SELF = BASE+'checkers/check_clock_provenance_interface.py'
OUT = ROOT/(BASE+'results/clock-provenance-interface-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def mul(A, B):
    return [[sum(x*y for x, y in zip(row, column)) for column in zip(*B)] for row in A]


def transpose(A):
    return [list(row) for row in zip(*A)]


def scale(A, a):
    return [[a*x for x in row] for row in A]


def add(A, B):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(A, B)]


def report():
    c = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    require(all(v is False for v in c['boundary'].values()), 'no physical or audit-review promotion')
    counts = {}
    n = 0
    for a, m in product([F(1, 2), F(1), F(2), F(4)], [F(1), F(2), F(8)]):
        frequencies, masses = [m, 2*m], [F(1, 4), F(3, 4)]
        changed_frequencies = [E/a for E in frequencies]
        require(changed_frequencies[0] == m/a > 0 and all(Ep*a == E for E, Ep in zip(frequencies, changed_frequencies)), 'clock parameter rescales frequencies and the whole source gap')
        require(sum(masses) == 1 and sum(Ep*w for Ep, w in zip(changed_frequencies, masses)) == sum(E*w for E, w in zip(frequencies, masses))/a, 'atomic spectral masses do not acquire a density Jacobian')
        n += 1
    counts['clock_frequency_gap_packets'] = n
    S1, S2 = [[F(1), F(1, 2)], [F(1, 2), F(1)]], [[F(2), F(0)], [F(0), F(1)]]
    Bs = [[[F(2), F(0)], [F(0), F(1)]], [[F(0), F(1)], [F(1), F(0)]], [[F(1), F(1)], [F(0), F(1)]]]
    original_variance = add(S1, scale(S2, 2))  # widths1 and2
    n = 0
    for a, B in product([F(1, 2), F(1), F(2), F(4)], Bs):
        expected = mul(mul(B, original_variance), transpose(B))
        result = [[F(0), F(0)], [F(0), F(0)]]
        for density, width in [(S1, F(1)), (S2, F(2))]:
            transformed_density = scale(mul(mul(B, density), transpose(B)), a)
            result = add(result, scale(transformed_density, width/a))
        require(result == expected, 'PSD density Jacobian and frequency width preserve readout-conjugated noise variance')
        require(result[0][0] >= 0 and result[1][1] >= 0 and result[0][0]*result[1][1]-result[0][1]**2 >= 0, 'full correlated positive covariance remains positive')
        n += 1
    counts['matrix_PSD_band_variance_packets'] = n
    correct_trace = S1[0][0]+S1[1][1]
    wrong_trace = correct_trace/2
    require(correct_trace-wrong_trace == 1, 'omitting PSD Jacobian at a2 changes integrated variance,not merely labels')
    counts['missing_Jacobian_hostile'] = 1
    n = 0
    for N in [2, 4, 8, 16]:
        h, a = F(1, N), F(N)
        original_gap = 1/h
        fixed_time_correlation = F(1, 2**N)
        retimed_correlation = F(1, 2)
        require(original_gap/a == 1 and retimed_correlation-fixed_time_correlation > 0, 'the same printed time argument is not the same physical separation after a cutoff-dependent retiming')
        n += 1
    counts['fixed_vs_retimed_gap_packets'] = n
    kappa = 1-F(6, 121)-F(6, 23)-F(11, 16)
    require(kappa == F(91, 44528), 'cosmological arithmetic residual is distinct from Hamiltonian kappa')
    n = 0
    for delta in [F(0), F(1, 1000), F(1, 100)]:
        readings = [kappa-delta, kappa+delta]
        mean = sum(readings)/2
        variance = sum((x-mean)**2 for x in readings)/2
        require(mean == kappa and variance == delta*delta, 'one closure mean does not select a noise variance or physical readout')
        n += 1
    counts['equal_mean_different_noise_packets'] = n
    n = 0
    for h, g_squared in product([F(1, 4), F(1, 16)], [F(512), F(1024)]):
        kappa_H = g_squared/(2*h)
        old_lambda, once_lambda = 2/(h*g_squared), 4/(h*g_squared)
        require(once_lambda/kappa_H == 2*old_lambda/kappa_H == 8/g_squared**2 < F(27, 262144), 'old and once-counted matching are different premises')
        lower_energy = F(5, 64)*kappa_H
        require((h*lower_energy)**2 > F(3200, 27) == 2*F(1600, 27), 'retain the corrected once-counted conditional coefficient without rewriting the frozen old note')
        n += 1
    counts['matching_convention_packets'] = n
    checkpoint_path = BASE+'yang-mills-checkpoint-index.v1.json'
    checkpoint = json.loads((ROOT/checkpoint_path).read_text(encoding='utf-8'))
    completed = checkpoint['post_audit_completion']
    require(completed['status'] == 'declared_R3_R4_obligations_supplied_at_written_conditional_scope' and not completed['independent_analytic_review_complete'] and not completed['parent_physical_continuum_or_reviewed_root_discharged'], 'completed written audits stay completed without claiming independent acceptance')
    rf_path = BASE+'contracts/krakensdr-physical-composition.v1.json'
    rf = json.loads((ROOT/rf_path).read_text(encoding='utf-8'))
    require(not rf['evidence_boundary']['physical_data_collected_or_validated'] and not rf['evidence_boundary']['hardware_energization_authorized'], 'RF design did not produce a native physical clock/noise map')
    central_path = c['inspected_central_snapshot']['contract']
    central = json.loads((ROOT/central_path).read_text(encoding='utf-8'))
    require(central['selected_physical_targets'] == c['inspected_central_snapshot']['selected_targets'], 'generic RF draft is not an admitted replacement target set')
    counts['saved_scope_status_audit'] = 1
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 37, 'exact control coverage')
    paths = [CONTRACT, NOTE, SELF, checkpoint_path, rf_path, central_path,
             BASE+'yang-mills-physical-scaling-obstruction-v1.md', BASE+'yang-mills-arbitrary-clock-locality-v1.md']
    return {'schema': 'marici.clock-provenance-interface.result.v1', 'passed': True,
            'new_exact_controls': 37, 'coverage': counts,
            'acted_on_message': c['instruction']['entity_id'],
            'missing_PSD_Jacobian_integrated_trace_defect': '1',
            'source_clock_and_physical_clock_identified': False,
            'completed_audits_reopened': False, 'R3_R4_proof_suites_replayed': False,
            'independent_review_or_physical_binding_certified': False,
            'physical_noise_or_curvature_RF_prediction_derived': False,
            'instrument_io_executed': False, 'hardware_execution_authorized': False,
            'other_owner_source_modified': False,
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in r.items() if k != 'input_sha256'}, indent=2))
