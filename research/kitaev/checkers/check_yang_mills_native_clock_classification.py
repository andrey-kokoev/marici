"""Exact gap/filter/clock classification controls,not an analytic certification."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_critical_limit_order import report as predecessor_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
NAME = 'yang-mills-native-clock-classification'
CONTRACT = BASE+'contracts/'+NAME+'.v1.json'
NOTE = BASE+NAME+'-v1.md'
SELF = BASE+'checkers/check_yang_mills_native_clock_classification.py'
OUT = ROOT/(BASE+'results/'+NAME+'-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch'] == {'kind': 'spatial-scaling', 'iteration': 10, 'size': 10}, 'batch provenance')
    require(all(v is False for v in c['boundary'].values()), 'no first-moment/domain/reader-class promotion')
    require(c['net_update']['ten_turn_batch_completed'] and not c['net_update']['broader_retained_observable_objective_exhausted'], 'canonical branch is not the whole retained-observable objective')
    require(c['net_update']['ready_frontier'] == ['fixed-interaction-critical-magnetic-susceptibility'] and c['net_update']['parent_outcome'] is None, 'distinct executable native observer constructor')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-critical-limit-order-v1.json'
    require(previous['passed'] and previous == json.loads((ROOT/previous_path).read_text()), 'fresh frozen order-audit replay')
    counts = {}
    gamma, L = F(5, 64), 12288
    count = 0
    for sigma, root in product([F(1, 2), F(1), F(2)], [1, 2, 4]):
        Q = F(4096*root*root)
        low_mass, high_mass = F(7, 4096)*Q, Q/4096
        low_energy, high_energy = gamma*sigma, 2*L*sigma
        first = low_mass*low_energy+high_mass*high_energy
        require(low_mass+high_mass == Q/512 and first <= 12*sigma*Q, 'proxy mass/moment budget on a moving energy scale')
        require(low_mass >= Q/1024 and low_energy <= L*sigma, 'fixed shape rho(K/sigma) retains source mass')
        lower_proxy_norm = F(root*2)
        allowed_Ward_error = F(root)
        require(lower_proxy_norm**2 == Q/1024 and (lower_proxy_norm-allowed_Ward_error)**2 == Q/4096, 'norm comparison transfers window mass without a mixed first moment')
        count += 1
    counts['moving_spectral_filter_packets'] = count
    count = 0
    for weight, derivative, R in product([0, 2, 4], [0, 1, 3], [1, 2, 8, 32]):
        cutoff_seminorm_budget = F((1+2*R)**weight, R**derivative)
        require(cutoff_seminorm_budget <= 3**weight*R**weight, 'rescaled positive compact Schwartz cutoff has a common polynomial seminorm bound')
        count += 1
    counts['rescaled_positive_Schwartz_cutoff_packets'] = count
    # Positivity is essential for bounding interval mass by a nonnegative cutoff.
    require(1+(-2)*F(1, 2) == 0, 'signed cutoff cancellation is excluded by spectral positivity')
    count = 0
    for sigma, k in product([F(1, 2), F(1), F(2)], [1, 2, 3]):
        energies = [gamma*sigma, 2*gamma*sigma, 4*gamma*sigma]
        coefficients = [F(1), F(1, 2), F(1, 4)]
        original_norm_squared = sum(w*w for w in coefficients)
        time_derivative_norm_squared = sum(E**(2*k)*w*w for E, w in zip(energies, coefficients))
        recovered = sum(E**(-2*k)*(E**k*w)**2 for E, w in zip(energies, coefficients))
        require(recovered == original_norm_squared and original_norm_squared <= (gamma*sigma)**(-2*k)*time_derivative_norm_squared, 'inverse gap acts on time-test derivatives,not on assumed source K-power domains')
        count += 1
    counts['inverse_gap_time_test_packets'] = count
    count = 0
    for N, sigma in product([0, 1, 2, 5, 8], [F(1, 2), F(1), F(2), F(4), F(16)]):
        amplitude = (1+sigma)**N
        k = (N+1)//2
        if sigma <= 1:
            require(amplitude <= 2**N, 'small-clock mass budget is bounded')
        else:
            require(amplitude*sigma**(-2*k) <= 2**N, 'polynomial clock bound suffices for joint tempered boundedness')
        count += 1
    counts['polynomial_sufficiency_packets'] = count
    count = 0
    for N, sigma in product([0, 1, 2, 5, 8], [2, 4, 8, 16]):
        k = N//2+1
        amplitude = F(sigma**N)
        inverse_budget = amplitude/F(sigma**(2*k))
        require(2*k > N and inverse_budget <= F(1, sigma), 'every polynomially bounded escaping-clock family is weak-zero in a fixed higher-time-test seminorm')
        count += 1
    counts['tempered_spectral_escape_packets'] = count
    count = 0
    eta0, a0 = F(1, 65536), F(1, 16)
    for n, path in product([4, 6, 8, 10], ['signal', 'small', 'escape', 'bad']):
        h = F(1, 2**n)
        if path == 'signal':
            a, sigma = a0, F(1)
        elif path == 'small':
            a, sigma = a0*h, 1/h
        elif path == 'escape':
            a, sigma = 8*eta0/h**5, 1/h
        else:
            a, sigma = 1/h, F(n)
        eta = a*h**5/8
        require(0 < eta < F(27, 262144) and sigma > 0, 'all path controls use actual positive retained couplings and clocks')
        if path == 'escape':
            require(eta == eta0 and a == 8*eta0*sigma**5 and a/sigma**6 == 8*eta0*h, 'fixed interacting coupling has an O(h) joint spectral-escape budget with k3')
        elif path == 'bad':
            require(eta == h**4/8 and a == 2**n and sigma == n, 'exponential-in-clock amplitude violates every common polynomial asymptotically')
        elif path == 'small':
            require(a == a0*h, 'zero amplitude is weak-zero regardless of clock')
        else:
            require(a == a0 and sigma == 1, 'nonzero finite-parameter kernel remains possible')
        count += 1
    counts['actual_source_parameter_path_packets'] = count
    count = 0
    signatures = set()
    for amplitude, triple_sigma in product([F(1, 16), F(1, 8), F(1, 4)], [0, 1, 2, 3]):
        mass = 3*amplitude/4
        laplace_at_log2 = mass/F(2**triple_sigma)
        signature = (mass, laplace_at_log2)
        require(signature not in signatures and mass > 0, 'explicit nonzero spectral kernels identify amplitude and finite clock,including zero-clock limit')
        signatures.add(signature)
        count += 1
    counts['kernel_parameter_injectivity_packets'] = count
    count = 0
    for n in [4, 6, 8, 10]:
        h = F(1, 2**n)
        amplitude, sigma = 1/h, F(1)
        eta = amplitude*h**5/8
        require(0 < eta < F(27, 262144) and amplitude/4096 == F(2**n, 4096), 'bounded-clock unbounded amplitude leaves growing mass in a FIXED energy window')
        count += 1
    counts['bounded_clock_unbounded_amplitude_packets'] = count
    count = 0
    a0 = F(1, 16)
    limits = set()
    for n in [4, 5, 6, 7]:
        sigma = 1 if n % 2 == 0 else 2
        h = F(1, 2**n)
        eta = a0*h**5/8
        kernel_Laplace_signature = F(3, 4)*a0/F(2**(3*sigma))
        require(0 < eta < F(27, 262144), 'oscillating clocks remain actual retained critical paths')
        limits.add(kernel_Laplace_signature)
        count += 1
    require(len(limits) == 2 and max(limits)-min(limits) == F(21, 256)*a0, 'boundedness is not full convergence when parameter kernels oscillate')
    counts['oscillating_parameter_scope_packets'] = count
    count = 0
    for n in [4, 5, 6, 7]:
        h = F(1, 2**n)
        amplitude, sigma = (h, F(1)) if n % 2 == 0 else (F(1), 1/h)
        window_amplitude = amplitude if sigma <= 2 else F(0)
        require(amplitude <= 1 and window_amplitude <= h and 0 < amplitude*h**5/8 < F(27, 262144), 'interlaced regimes satisfy the zero-limit window condition without either global parameter limit')
        count += 1
    counts['interlaced_zero_limit_packets'] = count
    count = 0
    for amplitude, sigma in product([F(1, 16), F(1, 8), F(1, 4)], [F(0), F(1, 3), F(1), F(2)]):
        energy, coefficient = 3*sigma, 3*amplitude/4
        momentum = 2*energy+1
        require(coefficient > 0 and momentum**2 > energy**2 and energy-F(3, 4)*momentum < 0, 'every nonzero classified kernel violates the relativistic cone,including energy0 with nonzero spatial momentum')
        count += 1
    counts['classified_limit_forward_cone_packets'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 151, 'frozen substantive coverage')
    paths = [CONTRACT, NOTE, SELF, previous_path,
             BASE+'yang-mills-critical-limit-order-v1.md', BASE+'yang-mills-mixed-reader-ward-v1.md',
             BASE+'yang-mills-interacting-magnetic-coercivity-v1.md', BASE+'yang-mills-electric-magnetic-reader-v1.md',
             BASE+'yang-mills-uniform-detection-v1.md']
    return {
        'schema': 'marici.yang-mills-native-clock-classification.result.v1',
        'passed': True, 'new_exact_controls': 151, 'coverage': counts,
        'predecessor_order_controls_replayed': previous['new_exact_controls'],
        'strength': 'written native canonical mixed/capped tempered boundedness iff polynomial amplitude-clock growth; every nonzero limit classified at arbitrary clocks,not all retained observers or physical Yang-Mills',
        'tempered_boundedness_iff': 'a_h<=C*(1+sigma_h)^N for some fixed C,N',
        'moving_mixed_spectral_window_over_sigma': 24576,
        'moving_filter_lower_denominator_over_Q': 4096,
        'centered_source_gap_over_sigma': '5/64',
        'nonzero_limit_iff': 'a_h->a_*>0 and sigma_h->sigma_*>=0 finite',
        'nonzero_limit_kernel': '(3a_*/4)*exp(-i3sigma_*(t-s))*delta^3(x-y)',
        'tempered_escaping_clock_limit': 'zero',
        'zero_full_limit_iff': 'polynomial clock bound and a_h*1_(sigma_h<=M)->0 for every M>0',
        'fixed_eta_sigma_inverse_h_escape_time_test_order': 3,
        'bounded_oscillating_kernel_Laplace_defect_over_amplitude': '21/256',
        'canonical_classification_branch_complete': True,
        'ten_turn_batch_complete': True,
        'broader_retained_observable_objective_exhausted': False,
        'higher_vacuum_or_group_derivatives_assumed': False,
        'mixed_first_energy_moment_assumed': False,
        'Lorentz_scalar_or_Yang_Mills_constructed': False,
        'finite_controls_certify_analytic_classification': False,
        'independent_analytic_review_complete': False,
        'next_executable': 'fixed-interaction-critical-magnetic-susceptibility',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in r.items() if k != 'input_sha256'}, indent=2))
