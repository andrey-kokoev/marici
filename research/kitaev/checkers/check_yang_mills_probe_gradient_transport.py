"""Based module and eigen-energy controls, not SU2 gradient computations."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_gradient_core import report as predecessor_report, derivative, inner
from check_yang_mills_probe_pressure import require

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-gradient-transport.v1.json'
NOTE = BASE+'yang-mills-probe-gradient-transport-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_gradient_transport.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-gradient-transport-v1.json')


def module_inner(law, v, w):
    return sum((p*sum(x*y for x, y in zip(a, b)) for p, a, b in zip(law, v, w)), F(0))


def difference(v, w):
    return [tuple(x-y for x, y in zip(a, b)) for a, b in zip(v, w)]


def multiply(a, v):
    return [tuple(c*x for x in row) for c, row in zip(a, v)]


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 10 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'scope')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['small-probe-diffusion-path-transport'], 'path-law frontier')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-gradient-core-v1.json')).read_text()), 'fresh gradient-core receipt')
    ns = [1, 2, 4, 8, 16, 32]
    module_packets = 0
    u = [(F(1), F(0)), (F(0), F(1)), (F(1), F(-1))]
    d = [(F(1), F(1)), (F(-2), F(1)), (F(1), F(-2))]
    rows = [(F(1), F(-1)), (F(2), F(0)), (F(0), F(1))]
    basis = [[tuple(F(int(i == j and a == b)) for b in range(2)) for j in range(3)] for i, a in product(range(3), range(2))]
    for n in ns:
        t = F(1, 8*n)
        nu = [(2-t)/8, (2+t)/8, F(1, 2)]
        psi = [1+t, 1-t, F(1)]
        rho = [p*x*x for p, x in zip(nu, psi)]
        require(min(nu+rho+psi) > 0 and sum(nu) == sum(rho) == 1, 'actual normalized positive source multiplier')
        v = [tuple(x+t*y for x, y in zip(a, b)) for a, b in zip(u, d)]
        r = multiply([1/x for x in psi], v)
        err_v, err_r = difference(v, u), difference(r, u)
        require(module_inner(nu, err_v, err_v) <= 5*t*t, 'original common-section recovery bound')
        rhs = difference(v, multiply(psi, u))
        require(module_inner(rho, err_r, err_r) == module_inner(nu, rhs, rhs) <= 8*t*t, 'within-source vector unitary and state-change recovery')
        contraction_error = [(sum(a*b for a, b in zip(row, er)),) for row, er in zip(rows, err_r)]
        require(module_inner(rho, contraction_error, contraction_error) <= 4*module_inner(rho, err_r, err_r) <= 32*t*t, 'finite continuous row contraction')
        for eta in basis:
            err = difference(v, eta)
            require(module_inner(nu, err, err) == module_inner(nu, v, v)+module_inner(nu, eta, eta)-2*module_inner(nu, eta, v), 'weak plus norms recovery identity')
        module_packets += 1
    energy_packets = 0
    for n, kappa in product(ns, [F(1, 2), F(1), F(2)]):
        epsilon = F(1, 128*n)
        psi = {-1: epsilon/2, 0: F(1), 1: epsilon/2}
        dp = derivative(psi)
        ddp = derivative(dp)
        normalizer = inner(psi, psi)
        gradient_norm2 = inner(dp, dp)/normalizer
        tilted_potential_mean = -kappa*inner(psi, ddp)/normalizer
        require(kappa*gradient_norm2 == -tilted_potential_mean, 'actual normalized E=0 kinetic/eigen-energy identity')
        require(gradient_norm2 == F(1, 32768*n*n+1), 'strong gradient norm decay in the continuous-circle family')
        require(kappa*epsilon/(1-epsilon) < 5*kappa/512, 'potential below even the whole-window source small-probe cap')
        require(gradient_norm2 <= (epsilon/(1-epsilon))**2, 'tilted log-gradient norm envelope')
        energy_packets += 1
    ripple_packets = []
    for n in [2, 4, 8, 16, 32, 64]:
        psi = {-n: F(1, 2*n), 0: F(1), n: F(1, 2*n)}
        dp = derivative(psi)
        normalizer = inner(psi, psi)
        gradient_norm2 = inner(dp, dp)/normalizer
        require(normalizer == 1+F(1, 2*n*n) and gradient_norm2 >= F(4, 9), 'uniform functions and bounded gradients do not give gradient norm convergence')
        require(F(1)/(1-F(1, n)) <= 2, 'ripple log-gradient uniformly bounded')
        for k in range(-min(n-1, 3), min(n-1, 3)+1):
            require(inner({k: F(1)}, dp) == 0, 'every fixed low-mode weak test eventually misses the ripple')
        require(F(n)/(1-F(1, n)) > F(1, 8), 'ripple potential violates fixed norm-small source hypotheses')
        ripple_packets.append({'n': n, 'gradient_squared_norm': str(gradient_norm2), 'raw_uniform_error': str(F(1, n))})
    target = [(F(1), F(0))]*3
    rival = [(F(0), F(1))]*3
    law = [F(1, 4), F(1, 4), F(1, 2)]
    require(module_inner(law, target, target) == module_inner(law, rival, rival) == 1, 'norm-only rotated rival has the same norm')
    weak_defect = module_inner(law, target, target)-module_inner(law, target, rival)
    err = difference(target, rival)
    recovery_defect = module_inner(law, err, err)
    require(weak_defect == 1 and recovery_defect == 2, 'weak identification cannot be replaced by norm matching')
    require((module_packets, energy_packets, len(ripple_packets)) == (6, 18, 6), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-gradient-core', 'probe-quasilocal', 'probe-eigenstate', 'propagator-comparison']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md', BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-gradient-transport.result.v1', 'passed': True,
            'strength': 'written based gradient norm, localized weak-drift and operator-graph transport; independent analytic review open',
            'changing_module_packets': module_packets, 'circle_eigen_energy_packets': energy_packets, 'normalized_ripple_packets': ripple_packets,
            'weak_only_gradient_norm_floor': '4/9', 'norm_only_weak_test_defect': str(weak_defect), 'norm_only_squared_recovery_defect': str(recovery_defect),
            'stationary_continuous_path_law_transport_proved': False, 'cross_source_L2_gradient_difference_defined': False,
            'pointwise_gradient_convergence_proved': False, 'operator_unit_ball_norm_convergence_proved': False,
            'classical_smooth_log_drift_proved': False, 'independent_analytic_review': False, 'continuum_Yang_Mills': False,
            'ready_frontier': contract['subnet']['ready_frontier'], 'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'changing_module_packets', 'circle_eigen_energy_packets',
                     'weak_only_gradient_norm_floor', 'norm_only_weak_test_defect', 'norm_only_squared_recovery_defect']}, indent=2))
