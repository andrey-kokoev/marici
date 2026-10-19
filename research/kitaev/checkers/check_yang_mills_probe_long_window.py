"""Exact source separation budgets and nonergodic/finite-prefix controls."""
from fractions import Fraction as F
from itertools import product
from math import comb
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_path_density import report as predecessor_report, log_one_plus_bounds
from check_yang_mills_probe_pressure import require

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-long-window.v1.json'
NOTE = BASE+'yang-mills-probe-long-window-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_long_window.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-long-window-v1.json')


def separation_plan(m, delta, a, b, tolerance):
    m, delta, a, b, tolerance = map(F, [m, delta, a, b, tolerance])
    if m <= 0 or not 0 <= delta <= m/8 or not 0 < tolerance < 1:
        raise ValueError('source gap/probe/tolerance envelope')
    if not (0 <= a <= 2*delta and 0 <= b <= 2*delta):
        raise ValueError('source entropy-rate envelope')
    if a == b == 0:
        return {'case': 'identical_constant', 'horizon': None}
    if a == 0 or b == 0:
        raise ValueError('one zero rate is inconsistent with the source dichotomy')
    g = m-2*delta
    C = 2*delta**2*(1/(m*b*b)+1/(g*a*a))
    target = C/tolerance
    horizon = max(1, (target.numerator+target.denominator-1)//target.denominator)
    return {'case': 'nonconstant_separation', 'horizon': horizon, 'C': C,
            'original_error': 2*delta**2/(m*horizon*b*b),
            'tilted_error': 2*delta**2/(g*horizon*a*a)}


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 13 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'scope')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['small-probe-pointwise-generator-core'], 'pointwise-generator frontier')
    require('obstructed' in contract['classification']['density_extension'], 'global-density negative boundary retained')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-path-density-v1.json')).read_text()), 'fresh path-density receipt')
    source_packets = 0
    horizon_example = None
    for n, kappa, tolerance in product([1, 2, 4, 8, 16, 32], [F(1, 2), F(1), F(2)], [F(1, 10), F(1, 100)]):
        t = F(1, 256*n)
        epsilon = t/(1+t*t)
        J = 1+3*t*t+t**4
        a, b = 3*kappa*t*t/J, 3*kappa*t*t
        delta, m = 6*kappa*epsilon/(1-2*epsilon), kappa/2
        require(0 < a and 0 < b and delta < m/8, 'actual nonconstant free-SU2 plaquette source')
        require(b/(3*kappa/F(256**2)) == F(1, n*n), 'fixed-gap probe rates have no uniform positive floor')
        plan = separation_plan(m, delta, a, b, tolerance)
        total_error = plan['original_error']+plan['tilted_error']
        require(plan['case'] == 'nonconstant_separation' and total_error <= tolerance, 'source discrimination budget')
        require(total_error == plan['C']/plan['horizon'], 'two actual mean margins retained')
        if plan['horizon'] > 1:
            require(plan['C']/(plan['horizon']-1) > tolerance, 'least sufficient positive integer source horizon')
        # Endpoint-free expected likelihood signs for E=0: means are b,-a.
        require(-b < 0 < a and b-(-a) == a+b, 'signed likelihood and occupation separation')
        if n == 1 and kappa == 1 and tolerance == F(1, 10):
            horizon_example = {'source_horizon': plan['horizon'], 'error_sum_bound': str(total_error), 'forward_rate': str(a), 'reverse_rate': str(b)}
        source_packets += 1
    constant_packets = 0
    for kappa, coefficient, tolerance in product([F(1, 2), F(1), F(2)], [F(-1, 256), F(0), F(1, 256)], [F(1, 10), F(1, 100)]):
        U = E = kappa*coefficient
        plan = separation_plan(kappa/2, abs(U), 0, 0, tolerance)
        require(plan == {'case': 'identical_constant', 'horizon': None} and E-U == 0, 'constant probes leave the whole path law unchanged')
        constant_packets += 1
    prefix_packets = flag_packets = 0
    fair, biased = F(1, 2), F(3, 4)
    for n in [1, 2, 4, 8, 12, 16]:
        p = [F(comb(n, k))*fair**k*(1-fair)**(n-k) for k in range(n+1)]
        q = [F(comb(n, k))*biased**k*(1-biased)**(n-k) for k in range(n+1)]
        d = [(biased/fair)**k*((1-biased)/(1-fair))**(n-k) for k in range(n+1)]
        require(sum(p) == sum(q) == sum(x*y for x, y in zip(p, d)) == 1 and min(d) > 0, 'finite prefix densities positive with exact mean1')
        for k in range(n+1):
            next_up = (biased/fair)**(k+1)*((1-biased)/(1-fair))**(n-k)
            next_down = (biased/fair)**k*((1-biased)/(1-fair))**(n+1-k)
            require(fair*next_up+(1-fair)*next_down == d[k], 'density prefix martingale')
        require(sum(k*x for k, x in enumerate(p)) == F(n, 2) and sum(k*x for k, x in enumerate(q)) == 3*F(n, 4), 'exact likelihood entropy coefficients')
        tv = sum(abs(x-y) for x, y in zip(p, q))/2
        require(0 < tv < 1, 'finite-word measures remain equivalent')
        prefix_packets += 1
        p_flag = [x/2 for x in p]+[x/2 for x in p]
        q_flag = [x/2 for x in p]+[x/2 for x in q]
        tv_flag = sum(abs(x-y) for x, y in zip(p_flag, q_flag))/2
        require(tv_flag == tv/2 < F(1, 2) and sum(p_flag) == sum(q_flag) == 1, 'positive entropy does not remove common invariant-flag mass')
        flag_packets += 1
    forward_entropy_low, _ = log_one_plus_bounds(F(27, 16)-1)
    reverse_entropy_low, _ = log_one_plus_bounds(F(4, 3)-1)
    require(forward_entropy_low/8 > 0 and reverse_entropy_low/4 > 0, 'both flag-mixture entropy rates strictly positive')
    transition = [[F(1, 2), F(1, 2), F(0), F(0)]]*2+[[F(0), F(0), F(1, 2), F(1, 2)]]*2
    invariant_flag = [F(-1), F(-1), F(1), F(1)]
    require([sum(x*y for x, y in zip(row, invariant_flag)) for row in transition] == invariant_flag and sum(invariant_flag) == 0, 'hidden flag violates the one-dimensional source kernel')
    covariance_packets = 0
    for gamma, S in product([F(1, 2), F(1), F(2)], [F(1, 2), F(1), F(2)]):
        # r=e^(-gamma*S) needs only1-gamma*S<=r<=1 for this envelope.
        low = max(F(0), 1-gamma*S)
        for r in [low, (1+low)/2, F(1)]:
            integral = S/gamma-(1-r)/(gamma*gamma)
            require(0 <= integral <= S/gamma, 'integrated covariance kernel bound')
            require(2*integral/(S*S) <= 2/(gamma*S), 'stationary time-average variance envelope')
        covariance_packets += 1
    require((source_packets, constant_packets, prefix_packets, flag_packets, covariance_packets) == (36, 18, 6, 6, 9), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-path-density', 'probe-diffusion-path', 'probe-gradient-core', 'probe-pressure']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md', BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-long-window.result.v1', 'passed': True,
            'strength': 'written constant/nonconstant infinite-horizon path dichotomy and source discrimination; independent analytic review open',
            'actual_free_SU2_budget_packets': source_packets, 'constant_exception_packets': constant_packets,
            'normalized_prefix_packets': prefix_packets, 'shared_flag_packets': flag_packets, 'covariance_kernel_envelopes': covariance_packets,
            'horizon_example_R0_kappa1_t1_256_error_1_10': horizon_example,
            'nonergodic_positive_entropy_common_path_mass': '1/2', 'actual_free_SU2_rate_decay': 'b_n/b_1=1/n^2',
            'written_nonconstant_density_limit_mass_defect': '1',
            'closed_obstruction': contract['subnet']['closed_obstruction'], 'nonconstant_infinite_horizon_density_constructed': False,
            'pointwise_weak_drift_or_Feller_cylinder_core_proved': False, 'independent_analytic_review': False,
            'physical_clock_or_continuum_Yang_Mills': False, 'ready_frontier': contract['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'actual_free_SU2_budget_packets', 'constant_exception_packets',
                     'normalized_prefix_packets', 'shared_flag_packets', 'covariance_kernel_envelopes',
                     'nonergodic_positive_entropy_common_path_mass', 'horizon_example_R0_kappa1_t1_256_error_1_10']}, indent=2))
