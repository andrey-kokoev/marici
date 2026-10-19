"""Exact joint-characteristic/initial-coupling/scope controls, not a limit prover."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_strong_noise import report as predecessor_report
from check_yang_mills_probe_pressure import require

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-coupled-transport.v1.json'
NOTE = BASE+'yang-mills-probe-coupled-transport-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_coupled_transport.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-coupled-transport-v1.json')


def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), F(0))


def qmul(a, b):
    w, x, y, z = a
    s, u, v, t = b
    return [w*s-x*u-y*v-z*t, w*u+x*s+y*t-z*v,
            w*v-x*t+y*s+z*u, w*t+x*v-y*u+z*s]


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 16 and c['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in c['boundary'].values()) and not c['parent_net']['discharges_parent'], 'scope')
    require(c['subnet']['parent_outcome'] is None and c['subnet']['ready_frontier'] == [], 'no invented successor')
    require(c['subnet']['bounded_source_construction_complete_at_written_scope'] and c['subnet']['no_nonredundant_executable_successor_in_retained_envelope'], 'bounded written completion,not reviewed root assembly')
    require(len(c['subnet']['reopening_conditions']) == 3, 'typed reopening conditions')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'continuum parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-strong-noise-v1.json')).read_text()), 'fresh predecessor receipt')
    require(previous['written_strong_marked_noise_realization'], 'pathwise uniqueness constructor retained at written scope')
    source_packets = 0
    opposite_defect = independent_defect = None
    for kappa, z, correlation in product([F(1, 8), F(1, 2), F(2)], map(F, [-2, -1, 0, 1, 2]), map(F, [-1, 0, 1])):
        gradient_squared = 4-z*z
        marginal_bracket = 2*kappa*gradient_squared
        mixed_generator = correlation*marginal_bracket
        determinant = marginal_bracket**2-mixed_generator**2
        require(marginal_bracket >= 0 and determinant >= 0, 'actual free-SU2 pair covariance')
        require(2*marginal_bracket-2*mixed_generator == 4*kappa*gradient_squared*(1-correlation), 'diagonal-distance quadratic reader')
        # Delta(character)=-3character; the marginal action ignores the marking.
        casimir = 4*F(1, 2)*(F(1, 2)+1)
        marginal_generator = -kappa*casimir*z
        require(casimir == 3 and marginal_generator == -3*kappa*z, 'four actual link Casimirs fix the marginal source action')
        if kappa == F(1, 8) and z == 0:
            if correlation == -1:
                opposite_defect = marginal_bracket-mixed_generator
                require(opposite_defect == 2, 'actual gauge-invariant opposite-noise reader')
            if correlation == 0:
                independent_defect = marginal_bracket-mixed_generator
                require(independent_defect == 1, 'actual independent-noise reader')
        source_packets += 1
    joint_packets = 0
    for effective_sigma, correlation in product([F(1, 2), F(1), F(2)], map(F, [-1, 0, 1])):
        # Character0: |Dcharacter|=2,so effective_sigma^2=8kappa.
        kappa = effective_sigma**2/8
        require(8*kappa == effective_sigma**2, 'projected marked source normalization')
        independent = F(correlation == 0)
        coefficients = [[effective_sigma, F(0)],
                        [correlation*effective_sigma, independent*effective_sigma], [F(1), F(0)]]
        covariance = [[dot(a, b) for b in coefficients] for a in coefficients]
        residual = covariance[1][1]+effective_sigma**2*covariance[2][2]-2*effective_sigma*covariance[1][2]
        require(residual == 2*effective_sigma**2*(1-correlation), 'self and mixed-with-W brackets determine residual')
        require((residual == 0) == (correlation == 1), 'only the marked joint arrow has zero residual')
        joint_packets += 1
    quaternions = [list(map(F, row)) for row in [
        [1, 0, 0, 0], [0, 1, 0, 0], [F(3, 5), F(4, 5), 0, 0],
        [F(1, 2), F(1, 2), F(1, 2), F(1, 2)], [0, 0, F(3, 5), F(4, 5)]]]
    initial_packets = 0
    for q, increment in product(quaternions, repeat=2):
        require(dot(q, q) == dot(increment, increment) == 1, 'actual unit-SU2 quaternion data')
        path_value = qmul(q, increment)
        antipodal_path = qmul([-x for x in q], increment)
        require(antipodal_path == [-x for x in path_value] and dot(path_value, path_value) == 1, 'same right noise preserves the antipodal coupling')
        difference = [a-b for a, b in zip(path_value, antipodal_path)]
        bounded_chord_squared = dot(difference, difference)/4
        first_link_metric_squared = F(1, 2)**2*bounded_chord_squared
        require(bounded_chord_squared == 1 and first_link_metric_squared == F(1, 4), 'first-link bounded product-path defect1/2')
        initial_packets += 1
    tail_packets = 0
    for N, coordinate_error in product([1, 2, 4, 8, 16, 32], [F(0), F(1, 16), F(1, 4)]):
        weights = [F(1, 2**n) for n in range(1, N+1)]
        tail = F(1, 2**N)
        require(sum(weights)+tail == 1, 'exact product metric tail')
        controlled = sum(w*coordinate_error for w in weights)+tail
        require(controlled <= coordinate_error+tail, 'finite-coordinate control plus summable tail')
        tail_packets += 1
    scope_packets = 0
    for N in [2, 4, 8, 16, 32, 64]:
        spikes = [[F(i == omega) for omega in range(N)] for i in range(N)]
        sup_expectation = max(sum(row)/N for row in spikes)
        expectation_sup = sum(max(row[omega] for row in spikes) for omega in range(N))/N
        require(sup_expectation == F(1, N) and expectation_sup == 1, 'uniform mean is not expectation of the supremum')
        if N == 8:
            require(expectation_sup-sup_expectation == F(7, 8), 'exact quantifier-scope gap')
        scope_packets += 1
    power_packets = 0
    for p, a, b in product([1, 2, 4], [F(0), F(1, 4), F(1, 2), F(1)], [F(0), F(1, 4), F(1, 2), F(1)]):
        require((a+b)**p <= 2**(p-1)*(a**p+b**p), 'Lp triangle/error-decomposition envelope')
        power_packets += 1
    require((source_packets, joint_packets, initial_packets, tail_packets, scope_packets, power_packets) == (45, 9, 25, 18, 6, 48), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, c['parent_net']['path']]
    for name in ['probe-strong-noise', 'probe-pointwise-core', 'probe-diffusion-path', 'probe-quasilocal']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md', BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-coupled-transport.result.v1', 'passed': True,
            'strength': 'written native common-noise map convergence with joint martingale closure; bounded fixed-lattice construction complete at written scope,independent analytic review open',
            'actual_free_SU2_mixed_generator_packets': source_packets, 'joint_covariance_residual_packets': joint_packets,
            'actual_free_SU2_antipodal_coupling_packets': initial_packets, 'product_tail_packets': tail_packets,
            'sup_expectation_scope_packets': scope_packets, 'Lp_envelope_packets': power_packets,
            'actual_opposite_marking_defect': str(opposite_defect), 'actual_independent_marking_defect': str(independent_defect),
            'actual_antipodal_initial_coupling_path_defect': '1/2', 'sup_expectation_scope_gap_N8': '7/8',
            'written_native_common_noise_map_transport': True, 'written_uniform_initial_mean_transport': True,
            'bounded_source_construction_complete_at_written_scope': True, 'ready_frontier': [],
            'independent_analytic_review': False, 'infinite_horizon_density_extension_reopened': False,
            'physical_clock_or_continuum_Yang_Mills': False,
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'actual_free_SU2_mixed_generator_packets', 'joint_covariance_residual_packets',
                     'actual_free_SU2_antipodal_coupling_packets', 'product_tail_packets', 'sup_expectation_scope_packets',
                     'Lp_envelope_packets', 'actual_opposite_marking_defect', 'actual_independent_marking_defect',
                     'actual_antipodal_initial_coupling_path_defect', 'sup_expectation_scope_gap_N8']}, indent=2))
