"""Exact frame/force/range/noise controls; not a pathwise-uniqueness prover."""
from fractions import Fraction as F
from itertools import product
from math import factorial
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_pointwise_core import report as predecessor_report
from check_yang_mills_probe_pressure import require

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-strong-noise.v1.json'
NOTE = BASE+'yang-mills-probe-strong-noise-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_strong_noise.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-strong-noise-v1.json')


def levi(a, b, c):
    if len({a, b, c}) < 3:
        return 0
    return 1 if (a, b, c) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)] else -1


def connection(a, v):
    return [sum((F(levi(c, a, b), 2)*v[b] for b in range(3)), F(0)) for c in range(3)]


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 15 and c['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in c['boundary'].values()) and not c['parent_net']['discharges_parent'], 'scope')
    require(c['subnet']['parent_outcome'] is None and c['subnet']['ready_frontier'] == ['small-probe-coupled-source-transport'], 'remaining coupled-map arrow')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-pointwise-core-v1.json')).read_text()), 'fresh predecessor receipt')
    source_packets = 0
    missing_J = None
    force_example = None
    for n, kappa, z in product([1, 2, 4, 8, 16, 32], [F(1, 2), F(1), F(2)], map(F, [-2, -1, 0, 1, 2])):
        t = F(1, 256*n)
        epsilon = t/(1+t*t)
        raw = 1+epsilon*z
        delta = 6*kappa*epsilon/(1-2*epsilon)
        m = kappa/2
        require(raw > 0 and delta < m/8, 'actual free-SU2 probe envelope')
        character_gradient_squared = 4-z*z
        character_Hessian_squared = 6+F(3, 2)*z*z
        require(character_Hessian_squared-F(5, 2)*character_gradient_squared == 4*z*z-4, 'actual source Bochner identity')
        coefficient = epsilon/raw
        Hessian_squared = (coefficient**2*character_Hessian_squared
                           +2*coefficient**3*z*character_gradient_squared
                           +coefficient**4*character_gradient_squared**2)
        simple_bound = 4*epsilon/(1-2*epsilon)+4*epsilon**2/(1-2*epsilon)**2
        require(0 < Hessian_squared <= simple_bound**2, 'actual pointwise force-Hessian bound')
        M_bound = 12*kappa*epsilon/(1-2*epsilon)**2
        L = M_bound/m
        require(8*L < 1, 'rational upper envelope for exp(2pi L)')
        H_bound = 1/(1-8*L)  # exp(2pi L)<exp(8L)<=1/(1-8L).
        x = (kappa+2*delta)/kappa
        alpha = 64*kappa*(1+x)**2
        generic_bound = H_bound**2*(alpha*L+M_bound)/(2*kappa*(1+x))+L*L+L
        require(simple_bound <= generic_bound, 'volume-independent source force bound is conservative')
        # J(D raw_psi)=kappa*D raw_psi; omitting J loses this coefficient.
        defect = kappa*epsilon
        if n == 1 and kappa == 1 and z == 0:
            missing_J = defect
            require(defect == F(256, 65537), 'actual omitted frame-curl coefficient')
            force_example = {'point': 'plaquette character0', 'Hessian_norm_squared': str(Hessian_squared), 'simple_HS_upper_bound': str(simple_bound)}
        source_packets += 1
    range_packets = 0
    for kappa, R, delta_fraction, L in product([F(1, 2), F(1), F(2)], [F(0), F(1, 64), F(1, 16)], [F(0), F(1, 8)], [F(0), F(1, 8), F(1, 2), F(2)]):
        m = kappa*(F(1, 2)-3*R)
        delta = m*delta_fraction
        b = kappa*(1+4*R)+2*delta
        x = b/kappa
        alpha = 64*kappa*(1+x)**2
        q_bound = F(5, 16)/(1+x)+x/(64*(1+x)**2)
        require(q_bound <= F(81, 256) < F(1, 2), 'vector Banach Neumann margin')
        require(6*kappa/alpha <= (F(5, 16)/(1+x))**2, 'first-order J resolvent envelope')
        d_coarse = 1/(4*kappa*(1+x))
        inverse_derivative_bound = d_coarse/(1-q_bound)
        require(inverse_derivative_bound <= 1/(2*kappa*(1+x)), 'closed-gradient inverse bound')
        require(alpha > 0 and m-2*delta > 0 and (alpha*L+m*L)/(2*kappa*(1+x)) >= 0, 'coercivity and derivative-envelope endpoints')
        range_packets += 1
    frame_packets = 0
    symmetric = [
        [[F(0) for _ in range(3)] for _ in range(3)],
        [[F(a == b) for b in range(3)] for a in range(3)],
        list(map(lambda row: list(map(F, row)), [[1, 2, 0], [2, -1, 1], [0, 1, 2]]))]
    for values, Hessian in product(product(map(F, [-1, 0, 1]), repeat=3), symmetric):
        v = list(values)
        flat = [[Hessian[a][b]+sum((F(levi(a, b, d), 2)*v[d] for d in range(3)), F(0)) for b in range(3)] for a in range(3)]
        curl = [sum((F(levi(c, a, b))*flat[a][b] for a in range(3) for b in range(3)), F(0)) for c in range(3)]
        require(curl == v, 'first-order connection cancels the geometric zeroth-order term on exact gradients')
        require(sum(a*a for a in curl) <= 3*sum(a*a for row in flat for a in row), 'HS first-order envelope')
        connection_norm = sum(a*a for k in range(3) for a in connection(k, v))
        require(connection_norm == sum(a*a for a in v)/2, 'covariant-versus-flat derivative HS correction')
        twice = [connection(k, connection(k, v)) for k in range(3)]
        require([sum(row[j] for row in twice) for j in range(3)] == [-a/2 for a in v], 'connection-square is minus one-half identity')
        frame_packets += 1
    tail_packets = 0
    for kappa, R, T, L in product([F(1, 2), F(1), F(2)], [F(0), F(1, 64), F(1, 8)], [F(1, 4), F(1), F(4)], [F(0), F(1, 8)]):
        y = 3*kappa*R*T
        twice = 2*y
        n0 = max(1, (twice.numerator+twice.denominator-1)//twice.denominator)
        remainder = 8*y**n0/factorial(n0)  # diameter2pi<8.
        for n in range(n0, n0+8):
            following = remainder*y/(n+1)
            require(0 <= following <= remainder/2, 'factorial remainder has an explicit eventual geometric tail')
            remainder = following
        first_forcing = 4*kappa*L*T
        require((first_forcing == 0) == (L == 0), 'same-leaf forcing respects constant probes')
        tail_packets += 1
    noise_packets = 0
    for sigma in [F(1, 2), F(1), F(2)]:
        kappa = sigma*sigma/2
        require(sigma*sigma == 2*kappa, 'actual free-SU2 marked covariance')
        correct_cross, wrong_cross = sigma, -sigma  # X_1(2q_1)=1 at identity.
        require(correct_cross-wrong_cross == 2*sigma and correct_cross**2 == wrong_cross**2, 'marginal covariance does not determine marked cross bracket')
        if kappa == F(1, 2):
            require(correct_cross-wrong_cross == 2, 'actual marked-noise hostile defect')
        noise_packets += 1
    require((source_packets, range_packets, frame_packets, tail_packets, noise_packets) == (90, 72, 81, 54, 3), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, c['parent_net']['path']]
    for name in ['probe-pointwise-core', 'probe-long-window', 'propagator-comparison', 'probe-gradient-core']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md', BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-strong-noise.result.v1', 'passed': True,
            'strength': 'written vector Banach range, HS force regularity and strong marked-noise realization; independent analytic review open',
            'actual_free_SU2_Hessian_packets': source_packets, 'vector_Banach_packets': range_packets,
            'frame_jet_packets': frame_packets, 'factorial_tail_certificates': tail_packets, 'marked_noise_packets': noise_packets,
            'actual_free_SU2_missing_frame_curl_coefficient': str(missing_J), 'actual_free_SU2_opposite_noise_cross_reader_defect': '2',
            'actual_free_SU2_force_example': force_example, 'written_strong_marked_noise_realization': True,
            'written_HS_force_derivative_recovery': True, 'actual_finite_box_common_noise_map_transport_proved': False,
            'independent_analytic_review': False, 'infinite_horizon_density_extension_reopened': False,
            'physical_clock_or_continuum_Yang_Mills': False, 'ready_frontier': c['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'actual_free_SU2_Hessian_packets', 'vector_Banach_packets',
                     'frame_jet_packets', 'factorial_tail_certificates', 'marked_noise_packets',
                     'actual_free_SU2_missing_frame_curl_coefficient', 'actual_free_SU2_opposite_noise_cross_reader_defect']}, indent=2))
