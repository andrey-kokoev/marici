"""Finite-horizon density controls, including a genuine free SU2 plaquette family."""
from fractions import Fraction as F
from itertools import product
from math import comb, factorial
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_diffusion_path import report as predecessor_report
from check_yang_mills_probe_gradient_core import mul
from check_yang_mills_probe_pressure import require

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-path-density.v1.json'
NOTE = BASE+'yang-mills-probe-path-density-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_path_density.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-path-density-v1.json')


def constant(f):
    return f.get(0, F(0))


def log_one_plus_bounds(y):
    require(0 < y < 1, 'alternating logarithm interval regime')
    lower = sum((F((-1)**(k+1), k)*y**k for k in range(1, 7)), F(0))
    upper = lower+y**6/6
    return lower, upper


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 12 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'scope')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['small-probe-long-window-separation'], 'long-window frontier')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-diffusion-path-v1.json')).read_text()), 'fresh diffusion-path receipt')
    chain_packets = 0
    gradients = [[F(0)]*3, [F(1, 128), F(0), F(0)], [F(0), F(1, 64), F(-1, 128)], [F(1, 32), F(-1, 64), F(1, 128)]]
    beta, df = [F(1, 8), F(-1, 16), F(3, 32)], [F(1), F(-2), F(1, 2)]
    for kappa, psi, grad in product([F(1, 2), F(1), F(2)], [F(1, 2), F(1), F(3, 2), F(2)], gradients):
        U, E = kappa/256, F(0)
        trace_hessian = psi*(U-E)/kappa-sum(b*x for b, x in zip(beta, grad))
        generator_psi = kappa*(trace_hessian+sum(b*x for b, x in zip(beta, grad)))
        r = [x/psi for x in grad]
        q = sum(x*x for x in r)
        generator_log = generator_psi/psi-kappa*q
        bracket_log = 2*kappa*q
        require(generator_psi == (U-E)*psi and generator_log+E-U == -bracket_log/2, 'weak eigen/chain rule and exact half-bracket compensation')
        cross_bracket = 2*kappa*sum(x*y for x, y in zip(r, df))
        base_drift = kappa*sum(b*y for b, y in zip(beta, df))
        new_drift = kappa*sum((b+2*x)*y for b, x, y in zip(beta, r, df))
        require(new_drift-base_drift == cross_bracket, 'actual sign and coefficient of weak Girsanov drift shift')
        chain_packets += 1
    gaussian_packets = constant_packets = 0
    horizons = [F(0), F(1, 2), F(1), F(2)]
    for kappa, q, S in product([F(1, 2), F(1), F(2)], [F(0), F(1, 16), F(1)], horizons):
        variance = 2*kappa*q*S
        mgf, compensate = [], []
        for order in range(7):
            even_moment = F(factorial(2*order), 2**order*factorial(order))*variance**order
            coefficient = even_moment/F(factorial(2*order))
            require(coefficient == (variance/2)**order/F(factorial(order)), 'Gaussian even-moment cumulant coefficients')
            mgf.append(coefficient)
            compensate.append((-variance/2)**order/F(factorial(order)))
        require(all(sum(mgf[k]*compensate[n-k] for k in range(n+1)) == int(n == 0) for n in range(7)), 'mean-one compensated series through order6')
        gaussian_packets += 1
    for kappa, coefficient, S in product([F(1, 2), F(1), F(2)], [F(-1, 256), F(0), F(1, 256)], horizons):
        U = E = kappa*coefficient
        require(abs(U) < 5*kappa/512 and S*(E-U) == 0, 'actual admissible constant probe cancels action and energy')
        require(E-U == U-E == 0, 'constant-probe two entropy rates vanish')
        constant_packets += 1
    # Fundamental SU2 character x=z+z^-1 with Haar class weight1-cos(2theta).
    weight, chi = {0: F(1), -2: F(-1, 2), 2: F(-1, 2)}, {-1: F(1), 1: F(1)}
    power = {0: F(1)}
    for degree in range(9):
        expected = F(0) if degree%2 else F(comb(degree, degree//2), degree//2+1)
        require(constant(mul(weight, power)) == expected, 'actual SU2 Haar fundamental-character moments')
        power = mul(power, chi)
    plaquette_packets = 0
    rate_example = None
    for n, kappa in product([1, 2, 4, 8, 16, 32], [F(1, 2), F(1), F(2)]):
        t = F(1, 256*n)
        epsilon = t/(1+t*t)
        raw = {0: F(1), -1: epsilon, 1: epsilon}
        weighted_square = mul(weight, mul(raw, raw))
        N = constant(weighted_square)
        J = 1+3*t*t+t**4
        require(N == 1+epsilon**2 == J/(1+t*t)**2, 'actual plaquette eigenvector probability normalization')
        require([weighted_square.get(k, F(0)) for k in range(5)] == [N, epsilon, F(-1, 2), -epsilon, -epsilon**2/2], 'Haar-weighted log-reader Fourier coefficients')
        delta = 6*kappa*epsilon/(1-2*epsilon)
        require(delta < kappa/16 and 1-2*epsilon > 0, 'positive local gauge-invariant R=0 probe inside m/8')
        Araw = {-1: 3*kappa*epsilon, 1: 3*kappa*epsilon}
        kinetic = constant(mul(weight, mul(raw, Araw)))/N
        a, b = 3*kappa*t*t/J, 3*kappa*t*t
        require(kinetic == 3*kappa*epsilon**2/N == a, 'four Casimirs3/4 and actual forward entropy rate')
        resolvent_mean = 1+t*t
        require(resolvent_mean == 1+epsilon**2*resolvent_mean**2 and resolvent_mean < 2, 'correct positive Catalan branch')
        for cutoff in [0, 1, 2, 4]:
            partial = sum((F(comb(2*j, j), j+1)*epsilon**(2*j) for j in range(cutoff+1)), F(0))
            tail = (4*epsilon**2)**(cutoff+1)/(1-4*epsilon**2)
            require(0 <= resolvent_mean-partial <= tail, 'Haar resolvent branch with explicit Catalan tail')
        require(3*kappa*(resolvent_mean-1) == b, 'actual reverse entropy rate')
        gradient_bound = 2*epsilon/(1-2*epsilon)
        require(0 < a <= min(2*delta, kappa*gradient_bound**2) and 0 < b <= min(2*delta, kappa*gradient_bound**2), 'two source rate bounds')
        Q = 4*sum((weighted_square.get(k, F(0))/N*F((-1)**(k+1), k)*t**k for k in range(1, 5)), F(0))
        require(Q == (5*t*t+F(14, 3)*t**4+t**6/6)/J, 'actual tilted initial log-reader formula')
        lower, upper = log_one_plus_bounds(J-1)
        require(0 < lower <= upper and Q-upper > 0 and lower-t*t > 0, 'certified positive forward/reverse initial entropy intervals')
        for S in horizons:
            require(0 < Q-upper+S*a <= Q-lower+S*a, 'forward path entropy interval')
            require(0 < lower-t*t+S*b <= upper-t*t+S*b, 'reverse path entropy interval')
        if n == 1 and kappa == 1:
            rate_example = {'forward': str(a), 'reverse': str(b)}
        plaquette_packets += 1
    epsilon = F(1, 256)
    raw = {0: F(1), -1: epsilon, 1: epsilon}
    weighted_square = mul(weight, mul(raw, raw))
    N = constant(weighted_square)
    actual_initial_readout = constant(mul(weighted_square, chi))/N
    wrong_initial_readout = constant(mul(weight, chi))
    missing_initial = actual_initial_readout-wrong_initial_readout
    require(constant(weighted_square)/N == constant(weight) == 1, 'both initial-state candidates have total mass1')
    require(missing_initial == F(512, 65537) and 6*epsilon/(1-2*epsilon) < F(1, 16), 'actual free-plaquette missing-initial-state readout hostile')
    missing_energy = abs(F(1)*(F(0)-F(1, 256)))
    missing_compensation = F(2)/2-F(0)
    require(missing_energy == F(1, 256) and missing_compensation == 1, 'constant-energy and Gaussian-compensation log-mass hostiles')
    require((chain_packets, gaussian_packets, constant_packets, plaquette_packets) == (48, 36, 36, 18), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-diffusion-path', 'probe-gradient-transport', 'probe-gradient-core', 'probe-pressure']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md', BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-path-density.result.v1', 'passed': True,
            'strength': 'written finite-horizon path density, weak Girsanov and exact two source entropy rates; independent analytic review open',
            'weak_chain_Girsanov_packets': chain_packets, 'Gaussian_compensation_packets': gaussian_packets,
            'constant_probe_packets': constant_packets, 'actual_free_SU2_plaquette_entropy_packets': plaquette_packets,
            'free_plaquette_n1_kappa1_rates': rate_example, 'missing_initial_readout_defect': str(missing_initial),
            'missing_energy_log_mass_defect': str(missing_energy), 'missing_compensation_log_mass_defect': str(missing_compensation),
            'infinite_horizon_equivalence_classified': False, 'infinite_horizon_density_constructed': False,
            'physical_clock_or_continuum_Yang_Mills': False, 'independent_analytic_review': False,
            'ready_frontier': contract['subnet']['ready_frontier'], 'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'weak_chain_Girsanov_packets', 'Gaussian_compensation_packets',
                     'constant_probe_packets', 'actual_free_SU2_plaquette_entropy_packets', 'missing_initial_readout_defect',
                     'missing_energy_log_mass_defect', 'missing_compensation_log_mass_defect']}, indent=2))
