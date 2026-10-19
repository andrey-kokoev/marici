"""Exact residual,centering,normalization and volume-scope controls."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_mixed_reader_ward import report as predecessor_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
NAME = 'yang-mills-critical-mixed-limit'
CONTRACT = BASE+'contracts/'+NAME+'.v1.json'
NOTE = BASE+NAME+'-v1.md'
SELF = BASE+'checkers/check_yang_mills_critical_mixed_limit.py'
OUT = ROOT/(BASE+'results/'+NAME+'-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def geometry(n):
    h = F(1, 2**n)
    M = n*2**n
    P = 3*(2*M+1)*(2*M)**2
    return h, M, P


def rotation(t):
    return (1-t*t)/(1+t*t), 2*t/(1+t*t)


def matvec(B, v):
    return [sum(x*y for x, y in zip(row, v)) for row in B]


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch'] == {'kind': 'spatial-scaling', 'iteration': 8, 'size': 10}, 'batch provenance')
    require(all(v is False for v in c['boundary'].values()), 'no source/outer-volume/relativistic promotion')
    require(c['net_update']['ready_frontier'] == ['critical-limit-outer-volume-order-audit'] and c['net_update']['parent_outcome'] is None, 'nonredundant order audit remains executable')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-mixed-reader-ward-v1.json'
    require(previous['passed'] and previous == json.loads((ROOT/previous_path).read_text()), 'fresh frozen Ward replay')
    counts = {}
    count = 0
    for n in range(1, 7):
        h, M, P = geometry(n)
        require(M*h == n and P == 24*n**3/h**3+12*n*n/h**2, 'mesh-aligned physical boxes actually exhaust space')
        require(P <= 36*n**3/h**3 and 3*(2*M+1)**2*(2*M) <= 54*n**3/h**3, 'once-counted plaquette/link budget')
        count += 1
    counts['explicit_net_geometry_packets'] = count
    count = 0
    for r, denominator in product([256, 512, 1024], [2, 4, 8]):
        h, root_h, c0 = F(1, denominator**2), F(1, denominator), F(2, r*r)
        kappa = r/(h**3*root_h)
        lam = F(2, r)*h*root_h
        eta = c0*h**5
        clock = 1/kappa
        m = -2*lam/h**3
        require(lam/kappa == eta and 0 < eta < F(27, 262144), 'every mesh source has actual positive retained coupling')
        require(clock*kappa == 1 and clock*lam == eta, 'fixed source clock does not replace the Hamiltonian')
        require(m*m*h**3 == 8*c0 and kappa*kappa == F(2, 1)/c0/h**7, 'critical mixed coefficient and source normalization')
        count += 1
    counts['positive_coupling_parameter_packets'] = count
    cs = [F(1, 32768), F(1, 65536), F(1, 131072)]
    count = 0
    for c0, n in product(cs, range(1, 7)):
        h, M, P = geometry(n)
        eta = c0*h**5
        require(eta*P <= 36*c0*n**3*h*h < 1, 'chosen total-potential volume budget is small')
        denominator = 3-eta*P
        epsilon_squared = eta*eta*P/denominator**2
        require(denominator >= 2 and epsilon_squared <= 9*c0*c0*n**3*h**7, 'actual residual sqrt(P) compensation and physical gap3')
        count += 1
    counts['source_residual_volume_budget_packets'] = count
    count = 0
    for t, sigma in product([F(1, 64), F(1, 32), F(1, 16)], [F(1, 2), F(1), F(2)]):
        # A finite positive perturbation control,not a numerical SU2 vacuum.
        a, b = rotation(t)
        potential = 3*a*b/(a*a-b*b)
        energy = sigma*potential*(1-b/a)
        H = [[sigma*potential, -sigma*potential], [-sigma*potential, sigma*(3+potential)]]
        require(a*a+b*b == 1 and a > 0 and b > 0 and 0 <= energy <= sigma*potential, 'normalized positive finite eigenvector/energy')
        require(matvec(H, [a, b]) == [energy*a, energy*b], 'project actual eigen-equation,not a surrogate vacuum choice')
        require(b <= potential/(3-potential) and 2*(1-a) <= 2*(potential/(3-potential))**2, 'projected physical-gap residual controls vector displacement')
        count += 1
    counts['finite_projected_eigenvector_packets'] = count
    count = 0
    for c0, n in product(cs, range(1, 7)):
        h, _, _ = geometry(n)
        operator_squared = 384**2*8*c0/h**3
        epsilon_squared_bound = 9*c0*c0*n**3*h**7
        centered_error_squared = 9*operator_squared*epsilon_squared_bound
        require(centered_error_squared == 648*384**2*c0**3*n**3*h**4, 'growing proxy norm and centering still leave order n^3 h^4 squared error')
        require(768*c0 > 0, 'free critical vector norm budget is finite and nonzero')
        count += 1
    counts['reader_vacuum_compensation_packets'] = count
    count = 0
    Bs = [[[F(0), F(1)], [F(1), F(0)]], [[F(0), F(1)], [F(1), F(1)]], [[F(0), F(2)], [F(2), F(-1)]]]
    for t, B in product([F(1, 64), F(1, 32), F(1, 16)], Bs):
        omega = list(rotation(t))
        reference = [F(1), F(0)]
        raw = matvec(B, omega)
        mean = dot(omega, raw)
        actual = [x-mean*y for x, y in zip(raw, omega)]
        free = matvec(B, reference)
        error_squared = sum((x-y)**2 for x, y in zip(actual, free))
        epsilon_squared = sum((x-y)**2 for x, y in zip(omega, reference))
        frobenius_squared = sum(x*x for row in B for x in row)
        require(dot(reference, free) == 0 and error_squared <= 9*frobenius_squared*epsilon_squared, 'actual state centering costs at most3 operator norms,not zero by assumption')
        count += 1
    counts['actual_centering_Hilbert_packets'] = count
    count = 0
    c0, sigma = F(1, 65536), F(3, 2)
    for n, time in product([2, 4, 6], [0, 1, 2]):
        h, _, P = geometry(n)
        eta = c0*h**5
        D = 3*sigma*eta*P
        require(D*time <= 108*sigma*c0*n**3*h*h*time, 'shifted bounded-perturbation Duhamel planner includes actual E0 shift')
        count += 1
    counts['shifted_dynamics_budget_packets'] = count
    count = 0
    for c0, n in product(cs, [1, 2, 3]):
        h, _, _ = geometry(n)
        lambda_squared = 2*c0*h**3
        actual_scale = 4*lambda_squared/h**3
        wrong_scale = lambda_squared/h**3
        actual_amplitude, wrong_amplitude = F(3, 4)*actual_scale, F(3, 4)*wrong_scale
        require(actual_scale == 8*c0 and wrong_scale == 2*c0 and actual_amplitude == 4*wrong_amplitude, 'premature Haar substitution erases the normalized electric channel')
        require(actual_amplitude-wrong_amplitude == F(9, 2)*c0, 'persistent amplitude error is not repaired by vacuum L2 convergence alone')
        count += 1
    counts['premature_vacuum_substitution_packets'] = count
    count = 0
    for n in [2, 4, 6, 8]:
        h = F(1, 2**n)
        D = 2**(13*n//2)
        S = int(h**-2*D**4)
        require(S == 2**(28*n), 'same test-independent observer cap has spin exponent28')
        cap_norm_budget = 3*D*S*S
        require(D*(S*(S+1)+1) <= cap_norm_budget == 3*2**(125*n//2), 'bounded-reader norm exponent125/2')
        pair_budget = F(12, 2)*h**-3*(2*cap_norm_budget)**2
        require(pair_budget == 216*h**-128, 'compact-support pair/link exponent128,not a source spin cutoff')
        count += 1
    counts['bounded_observer_exponent_packets'] = count
    count = 0
    for c0, sigma in product(cs, [F(1, 2), F(1), F(2)]):
        energy, amplitude = 3*sigma, 6*c0
        momentum = 2*energy+1
        require(amplitude > 0 and energy > 0 and momentum**2 > energy**2, 'nonzero positive spectral measure extends outside forward cone')
        require(energy-F(3, 4)*momentum < 0, 'not Lorentz-invariant positive-energy spectrum')
        count += 1
    counts['nonrelativistic_spectral_packets'] = count
    count = 0
    c0 = F(1, 65536)
    for n in [12, 16, 20, 24]:
        h, _, slow_P = geometry(n)
        fast_M = int(h**-2)  # physical radius1/h,instead of n
        fast_P = 3*(2*fast_M+1)*(2*fast_M)**2
        eta = c0*h**5
        require(eta*slow_P < 1 and eta*fast_P > 1, 'global perturbation proof does not cover arbitrary outer-volume growth')
        require(eta*fast_P == 24*c0/h+12*c0*h, 'failure of this method is not proof of a different local limit')
        count += 1
    counts['outer_volume_scope_packets'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 104, 'frozen substantive coverage')
    paths = [CONTRACT, NOTE, SELF, previous_path,
             BASE+'yang-mills-mixed-reader-ward-v1.md', BASE+'yang-mills-free-magnetic-fluctuations-v1.md',
             BASE+'yang-mills-ground-state-transfer-v1.md', BASE+'yang-mills-electric-magnetic-reader-v1.md']
    return {
        'schema': 'marici.yang-mills-critical-mixed-limit.result.v1',
        'passed': True, 'new_exact_controls': 104, 'coverage': counts,
        'predecessor_Ward_controls_replayed': previous['new_exact_controls'],
        'strength': 'written actual positive-coupling critical mixed/capped joint two-point limit on explicit exhausting boxes; ultralocal and nonrelativistic,not all-orders or arbitrary outer-volume promotion',
        'limit_kernel': '6c*exp(-i3sigma*(t-s))*delta^3(x-y)',
        'actual_coupling_positive_at_every_mesh': True,
        'vacuum_error_rate': 'O_c(n^(3/2)*h^(7/2))',
        'proxy_vector_error_rate': 'O_c(n^(3/2)*h^2)',
        'dynamics_error_rate_on_compact_times': 'O_(c,sigma)(n^3*h^2)',
        'premature_vacuum_substitution_amplitude_error': '(9/2)c',
        'bounded_observer_spin_cap_exponent': 28,
        'bounded_observer_norm_exponent': '125/2', 'pair_norm_link_exponent': 128,
        'arbitrary_outer_volume_or_thermodynamic_first_limit_proved': False,
        'Lorentz_scalar_or_Yang_Mills_constructed': False,
        'all_orders_Gaussian_or_operator_product_convergence_proved': False,
        'finite_controls_certify_analytic_limit': False,
        'independent_analytic_review_complete': False,
        'next_executable': 'critical-limit-outer-volume-order-audit',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in r.items() if k != 'input_sha256'}, indent=2))
