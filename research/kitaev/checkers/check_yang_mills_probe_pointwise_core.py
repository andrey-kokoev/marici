"""Exact one-form, Banach-range and topology controls, not an analytic prover."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_long_window import report as predecessor_report
from check_yang_mills_probe_pressure import require
from check_yang_mills_thermodynamic_vacuum import invert

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-pointwise-core.v1.json'
NOTE = BASE+'yang-mills-probe-pointwise-core-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_pointwise_core.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-pointwise-core-v1.json')


def matvec(A, v):
    return [sum((a*b for a, b in zip(row, v)), F(0)) for row in A]


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 14 and c['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in c['boundary'].values()) and not c['parent_net']['discharges_parent'], 'scope')
    require(c['subnet']['parent_outcome'] is None and c['subnet']['ready_frontier'] == ['small-probe-strong-noise-realization'], 'new strong-noise realization cell')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-long-window-v1.json')).read_text()), 'fresh predecessor receipt')
    require(previous['nonconstant_infinite_horizon_density_constructed'] is False, 'closed global-density obstruction')
    source_packets = 0
    ricci_example = None
    for n, kappa, x in product([1, 2, 4, 8, 16, 32], [F(1, 2), F(1), F(2)], map(F, [-2, -1, 0, 1, 2])):
        t = F(1, 256*n)
        epsilon = t/(1+t*t)
        raw = 1+epsilon*x
        U = -3*kappa*epsilon*x/raw
        Uprime = -3*kappa*epsilon/(raw*raw)
        delta = 6*kappa*epsilon/(1-2*epsilon)
        require(raw > 0 and delta < kappa/16, 'actual smooth gauge-invariant free-plaquette source')
        lhs = (3*kappa+U)*epsilon
        rhs = -raw*Uprime
        require(lhs == rhs, 'actual pointwise one-form eigen-equation')
        # Four radius-two link derivatives of the holonomy character.
        gradient_character_squared = 4-x*x
        gradient_log_squared = epsilon*epsilon*gradient_character_squared/(raw*raw)
        require(0 <= gradient_log_squared <= (2*epsilon/(1-2*epsilon))**2, 'pointwise source drift norm')
        without_ricci = (F(5, 2)*kappa+U)*epsilon
        require(lhs-without_ricci == kappa*epsilon/2 > 0, 'omitted Ricci changes the differentiated source eigen-equation')
        if n == 1 and kappa == 1 and x == 0:
            ricci_example = lhs-without_ricci
            require(gradient_character_squared == 4 and ricci_example == F(128, 65537), 'actual nonzero source covector hostile')
        source_packets += 1
    resolvent_packets = 0
    weight = F(4, 3)
    for kappa, R, sign_U, sign_E in product([F(1, 2), F(1), F(2)], [F(0), F(1, 64), F(1, 16)], [-1, 1], [-1, 1]):
        m = kappa*(F(1, 2)-3*R)
        delta, g = m/8, 3*m/4
        h = [[R, R/4, F(0)], [R/4, R, R/4], [F(0), R/4, R]]
        require(all(sum(weight**abs(i-j)*h[i][j] for j in range(3)) <= 3*R for i in range(3)), 'weighted Hessian envelope')
        u, E = sign_U*delta, sign_E*delta
        B = [[(kappa/2+u-E if i == j else F(0))-kappa*h[i][j] for j in range(3)] for i in range(3)]
        inverse = invert(B)
        forcing = [F(1), F(0), F(0)]
        v = [-a for a in matvec(inverse, forcing)]
        require(matvec(B, v) == [-a for a in forcing] and min(a for row in inverse for a in row) >= 0, 'cooperative one-form resolvent')
        require(sum(weight**i*abs(v[i]) for i in range(3)) <= 1/g, 'coercive localized inverse bound')
        resolvent_packets += 1
    neumann_packets = 0
    for kappa, L in product([F(1, 2), F(1), F(2)], [F(0), F(1, 8), F(1, 2), F(1), F(2), F(4)]):
        alpha = 8*kappa*(1+4*L*L)
        # pi<4 in the ANALYTIC integral estimate, not an asserted rational pi.
        rational_squared_upper = 8*kappa*L*L/alpha
        require(rational_squared_upper == L*L/(1+4*L*L) < F(1, 4), 'Banach, not Hilbert, Neumann envelope')
        neumann_packets += 1
    huber_packets = 0
    for n in [1, 2, 4, 8, 16, 32]:
        x = F(1, 2*n)
        value_error_at_zero = F(1, 2*n)
        gradient_n, gradient_2n = n*x, 2*n*x
        require(gradient_2n-gradient_n == F(1, 2) and value_error_at_zero > 0, 'uniform values and bounded Lipschitz do not prove C1 convergence')
        for y in [F(0), x, F(1, n)]:
            error = n*y*y/2+F(1, 2*n)-y
            require(error == F(n, 2)*(y-F(1, n))**2 and 0 <= error <= value_error_at_zero, 'C1 Huber value approximation')
        huber_packets += 1
    topology_packets = 0
    for n in [2, 4, 8, 16]:
        size = n+1
        projection = [[F(i == j and i < n) for j in range(size)] for i in range(size)]
        localized = [F(i == 0) for i in range(size)]
        escaping = [F(i == n) for i in range(size)]
        require(matvec(projection, localized) == localized, 'strong convergence on localized vectors')
        image = matvec(projection, escaping)
        require(sum(abs(a-b) for a, b in zip(image, escaping)) == 1, 'operator-norm defect stays1')
        topology_packets += 1
    require((source_packets, resolvent_packets, neumann_packets, huber_packets, topology_packets) == (90, 36, 18, 6, 4), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, c['parent_net']['path']]
    for name in ['probe-long-window', 'propagator-comparison', 'probe-quasilocal', 'probe-gradient-core']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md', BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-pointwise-core.result.v1', 'passed': True,
            'strength': 'written continuous one-form transport, uniform gradient recovery, C(X) cylinder core and all-start-point weak drift; independent analytic review open',
            'actual_free_SU2_one_form_packets': source_packets, 'cooperative_resolvent_packets': resolvent_packets,
            'Banach_Neumann_packets': neumann_packets, 'Huber_topology_packets': huber_packets, 'strong_operator_topology_packets': topology_packets,
            'actual_free_SU2_missing_Ricci_coefficient': str(ricci_example), 'Huber_gradient_Cauchy_defect': '1/2', 'global_operator_norm_defect': '1',
            'written_CX_cylinder_core_identified': True, 'written_all_start_point_weak_drift_identified': True,
            'strong_tilted_SDE_or_pathwise_uniqueness_proved': False, 'independent_analytic_review': False,
            'infinite_horizon_density_extension_reopened': False, 'physical_clock_or_continuum_Yang_Mills': False,
            'ready_frontier': c['subnet']['ready_frontier'], 'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'actual_free_SU2_one_form_packets', 'cooperative_resolvent_packets',
                     'Banach_Neumann_packets', 'Huber_topology_packets', 'strong_operator_topology_packets',
                     'actual_free_SU2_missing_Ricci_coefficient', 'Huber_gradient_Cauchy_defect', 'global_operator_norm_defect']}, indent=2))
