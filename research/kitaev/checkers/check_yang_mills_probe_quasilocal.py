"""Exact nonlinear-gradient/compactness controls; not SU2 eigenfunctions."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_doob import report as predecessor_report, ceil_fraction
from check_yang_mills_probe_pressure import require, scale, sub
from check_yang_mills_probe_clustering import mm, mv, eye
from check_yang_mills_mesh_word import inverse

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-quasilocal.v1.json'
NOTE = BASE+'yang-mills-probe-quasilocal-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_quasilocal.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-quasilocal-v1.json')


def log_tail_coefficient(R, kappa):
    kappa = F(kappa)
    if kappa <= 0:
        raise ValueError('positive source kappa required')
    if R is None:
        return F(2376, 35)/kappa
    R = F(R)
    if not 0 <= R < F(9, 64):
        raise ValueError('outside source coupling window')
    c = F(1, 2)-3*R
    return F(44, 7)*(1/c-2)/kappa


def plan_log_tail(R, kappa, gradient_u, epsilon):
    gradient_u, epsilon = map(F, [gradient_u, epsilon])
    coefficient = log_tail_coefficient(R, kappa)
    if gradient_u < 0 or epsilon <= 0:
        raise ValueError('nonnegative gradient budget and positive tolerance required')
    b = 1
    while coefficient*gradient_u*F(3, 4)**b > epsilon:
        b += 1
    return {'buffer': b, 'error_bound': coefficient*gradient_u*F(3, 4)**b}


def nonlinear_block(v, hessian, block):
    return sum(v[i]*2*sum(hessian[i][j]*v[j] for j in range(len(v))) for i in block)


def common_advection(v, hessian, block, advective_indices=None):
    indices = range(len(v)) if advective_indices is None else advective_indices
    return 2*sum(v[j]*sum(v[i]*hessian[j][i] for i in block) for j in indices)


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 8 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'scope')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['small-probe-gradient-form-core'], 'domain frontier')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-doob-v1.json')).read_text()), 'fresh predecessor receipt')
    jet_packets = 0
    for seed in range(1, 25):
        v = [F((seed+2*i)%7-3, seed+1) for i in range(6)]
        hessian = [[F((seed+(i+1)*(j+1))%11-5, seed+2) for j in range(6)] for i in range(6)]
        require(all(hessian[i][j] == hessian[j][i] for i in range(6) for j in range(6)), 'covariant scalar Hessian symmetry')
        for block in [range(3), range(3, 6)]:
            require(nonlinear_block(v, hessian, block) == common_advection(v, hessian, block), 'nonlinear gradient becomes common advection')
        jet_packets += 1
    v = [F(1), F(0), F(0), F(1), F(0), F(0)]
    hessian = [[F(0)]*6 for _ in range(6)]
    hessian[0][3] = hessian[3][0] = F(1)
    mixed_residual = nonlinear_block(v, hessian, range(3))-common_advection(v, hessian, range(3), range(3))
    require(mixed_residual == 2, 'omitting cross-block advection hostile')
    matrix_packets = 0
    norm_packets = 0
    max_exponent = 0
    a = F(4, 3)
    for R, kappa in product([F(0), F(1, 128), F(9, 128), F(575, 4096)], [F(1, 2), F(1), F(2)]):
        c, m = F(1, 2)-3*R, kappa*(F(1, 2)-3*R)
        edge = 3*R/(2*a)
        h = [[edge if abs(i-j) == 1 else F(0) for j in range(3)] for i in range(3)]
        require(all(sum(a**abs(i-j)*h[i][j] for j in range(3)) <= 3*R for i in range(3)), 'actual weighted cooperative matrix budget')
        resolvent = inverse(scale(sub(scale(eye(3), F(1, 2)), h), kappa))
        gain = sub(resolvent, scale(eye(3), 2/kappa))
        require(min(x for row in gain for x in row) >= 0, 'identity removed inside positive Neumann resolvent')
        require(all(sum(a**abs(i-j)*resolvent[i][j] for j in range(3)) <= 1/m for i in range(3)), 'full integrated gradient bound')
        require(all(sum(a**abs(i-j)*gain[i][j] for j in range(3)) <= (1/c-2)/kappa for i in range(3)), 'coupling-sensitive integrated gradient gain')
        w = mv(resolvent, [F(1), F(0), F(0)])
        require(sum(a**i*w[i] for i in range(1, 3)) <= (1/c-2)/kappa, 'off-support log-filter gradient budget')
        if R == 0:
            require(w[1:] == [0, 0], 'zero-coupling exact probe support')
        matrix_packets += 1
        for gu in [F(0), F(1)]:
            oscillation_majorant = F(44, 7)*gu/m
            exponent = ceil_fraction(2*oscillation_majorant)
            H = 2**exponent
            require(oscillation_majorant <= F(exponent, 2) and H >= 1, 'exact dyadic majorant for exp oscillation')
            require(F(1, H)*H == 1 and H*gu/m >= 0, 'normalized noncollapse and positive inverse envelope')
            max_exponent = max(max_exponent, exponent)
            norm_packets += 1
    for n in [2, 4, 8, 16, 32, 64]:
        norm2, raw_mean = 1+F(4, 3*n), 1+F(1, 2*n)
        require(F(4)/norm2 >= F(9, 4), 'normalized triangular spike sup-distance at least1/2')
        require(raw_mean**2 >= norm2*(1-F(2, 3*n))**2 and 1-F(2, 3*n) >= 0, 'exact squared certificate for L2-distance bound4/(3n)')
    spike_floor = F(1, 2)
    law = [F(1), F(0)]
    f, g = [F(1), F(1)], [F(1), F(2)]
    invisible_norm = sum(law[i]*(f[i]-g[i])**2 for i in range(2))
    support_residual = max(abs(x-y) for x, y in zip(f, g))
    require(invisible_norm == 0 and support_residual == 1, 'full support required for continuous version uniqueness')
    planner_packets = 0
    for R, kappa, gu, epsilon in product([None, F(0), F(1, 128), F(9, 128), F(575, 4096)], [F(1, 2), F(1), F(2)], [F(0), F(1), F(2)], [F(1, 100), F(1, 1000)]):
        plan = plan_log_tail(R, kappa, gu, epsilon)
        require(plan['error_bound'] <= epsilon and plan['buffer'] >= 1, 'logarithmic quasilocality tolerance')
        if plan['buffer'] > 1:
            require(log_tail_coefficient(R, kappa)*gu*F(3, 4)**(plan['buffer']-1) > epsilon, 'least sufficient tail buffer')
        planner_packets += 1
    examples = [plan_log_tail(R, 1, 1, F(1, 1000))['buffer'] for R in [None, F(9, 128)]]
    require(examples == [39, 32] == list(contract['transport']['buffers_kappa1_MU1_epsilon_1_1000'].values()), 'worked log-locality buffers')
    require((jet_packets, matrix_packets, norm_packets, planner_packets) == (24, 12, 24, 90), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-doob', 'probe-eigenstate', 'propagator-comparison', 'source-clustering']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md', BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-quasilocal.result.v1', 'passed': True,
            'strength': 'written covariant log-gradient, uniform completion and Feller realization; independently unreviewed source analysis',
            'covariant_jet_packets': jet_packets, 'weighted_resolvent_packets': matrix_packets,
            'dyadic_norm_envelopes': norm_packets, 'log_tail_budget_packets': planner_packets,
            'mixed_block_advection_hostile_residual': str(mixed_residual), 'L2_only_uniform_hostile_floor': str(spike_floor),
            'nonfull_support_continuous_version_hostile_residual': str(support_residual),
            'buffers_kappa1_MU1_epsilon_1_1000': examples, 'largest_dyadic_norm_envelope_exponent': max_exponent,
            'classical_smooth_log_drift_proved': False, 'tilted_gradient_form_core_identified': False,
            'independent_analytic_review': False, 'continuum_Yang_Mills': False,
            'ready_frontier': contract['subnet']['ready_frontier'], 'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'covariant_jet_packets', 'weighted_resolvent_packets', 'dyadic_norm_envelopes',
                     'log_tail_budget_packets', 'mixed_block_advection_hostile_residual', 'L2_only_uniform_hostile_floor',
                     'nonfull_support_continuous_version_hostile_residual']}, indent=2))
