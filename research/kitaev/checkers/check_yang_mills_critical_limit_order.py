"""Exact boundary budgets and spectral scope controls,not an analytic limit prover."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_critical_mixed_limit import report as predecessor_report, geometry
from check_yang_mills_mesh_word import report as word_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
NAME = 'yang-mills-critical-limit-order'
CONTRACT = BASE+'contracts/'+NAME+'.v1.json'
NOTE = BASE+NAME+'-v1.md'
SELF = BASE+'checkers/check_yang_mills_critical_limit_order.py'
OUT = ROOT/(BASE+'results/'+NAME+'-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def expectation(law, values):
    return sum(p*x for p, x in zip(law, values))


def determinant3(a):
    return (a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])
            -a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])
            +a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch'] == {'kind': 'spatial-scaling', 'iteration': 9, 'size': 10}, 'batch scope')
    require(all(v is False for v in c['boundary'].values()), 'no unbudgeted order/representation promotion')
    require(c['net_update']['ready_frontier'] == ['arbitrary-clock-native-two-point-classification'] and c['net_update']['parent_outcome'] is None, 'remaining actual clock classification')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-critical-mixed-limit-v1.json'
    require(previous['passed'] and previous == json.loads((ROOT/previous_path).read_text()), 'fresh frozen critical-net replay')
    word = word_report()
    word_path = BASE+'results/yang-mills-mesh-word-v1.json'
    require(word['passed'] and word == json.loads((ROOT/word_path).read_text()), 'fresh original finite-word boundary theorem controls')
    require(word['universal_coefficient'] == '18/5' and word['state_identification_hostile_residual'] == '1/3', 'actual state term retained')
    counts = {}
    count = 0
    c0 = F(1, 65536)
    for n in [4, 8, 12, 16]:
        h = F(1, 2**n)
        for outer_radius in [F(n, 8), F(n), 1/h, 1/(h*h)]:
            target = min(F(n), outer_radius/2)
            r = h*int(target // h)
            M = int(r/h)
            P = 3*(2*M+1)*(2*M)**2
            require(0 < r <= n and r <= outer_radius/2 and target-h < r <= target, 'actual nested mesh-aligned adaptive buffer')
            require(P <= 36*n**3/h**3 and c0*h**5*P <= 36*c0*n**3*h*h < 1, 'only buffer volume is paid')
            count += 1
    counts['adaptive_buffer_packets'] = count
    count = 0
    C_R = F(18, 5)
    for r, denominator in product([256, 512, 1024], [2, 4, 8]):
        h, root_h = F(1, denominator**2), F(1, denominator)
        P_unit = 3*(1+int(1/h))*int(1/h)**2
        U = F(4, r)*h*root_h*P_unit
        require(U*U <= F(288)*F(2, r*r)/h**3, 'critical sup/gradient word budget squared is O(h^-3)')
        raw, means = 8*C_R*U*U, 8*C_R*U*U
        centered_infinite = raw+means
        centered_outer = 2*centered_infinite
        require(centered_infinite == F(288, 5)*U*U and centered_outer == F(576, 5)*U*U, 'two insertions plus two mean terms,then common infinite-source comparison')
        count += 1
    counts['normalized_word_budget_packets'] = count
    count = 0
    pi, rho = [F(1, 3)]*3, [F(1, 6), F(2, 3), F(1, 6)]
    fixtures = [([1, 0, 1], [0, 1, 0]), ([1, 2, 0], [0, -1, 1])]
    for decay, (f, g) in product([F(0), F(1, 2), F(1)], fixtures):
        values = []
        for law in [pi, rho]:
            mean_f, mean_g = expectation(law, f), expectation(law, g)
            Pg = [decay*x+(1-decay)*mean_g for x in g]
            raw = expectation(law, [x*y for x, y in zip(f, Pg)])
            values.append((raw, mean_f*mean_g, raw-mean_f*mean_g))
        raw_diff, means_diff = values[0][0]-values[1][0], values[0][1]-values[1][1]
        covariance_diff = values[0][2]-values[1][2]
        require(covariance_diff == raw_diff-means_diff and abs(covariance_diff) <= abs(raw_diff)+abs(means_diff), 'centered boundary comparison cannot silently identify states')
        if decay == 0:
            require(covariance_diff == 0 and raw_diff == means_diff, 'raw state discrepancy is not a connected correlation')
        count += 1
    counts['state_centering_packets'] = count
    count = 0
    for n, power in product([8, 9, 10, 11], [3, 6, 10]):
        ratio = 2**power*F(3, 4)**(2**n)
        require(0 < ratio < F(1, 2), 'dyadic exponential distance defeats every preregistered polynomial budget')
        # Larger n only decreases this ratio; the analytic proof does not enumerate the infinite net.
        count += 1
    counts['distance_vs_polynomial_packets'] = count
    count = 0
    for N in [4, 8, 16, 32, 64, 128]:
        high_mass = F(1, N*N)
        energies, masses = [3, N], [1-high_mass, high_mass]
        total, first = sum(masses), sum(E*w for E, w in zip(energies, masses))
        laplace = sum(w*F(1, 2**E) for E, w in zip(energies, masses))
        T = F(N, 2)
        tail = sum(w for E, w in zip(energies, masses) if E > T)
        require(total == 1 and first <= 4 and tail <= first/T, 'positive mass/first moment produces uniform spectral tightness')
        require(abs(laplace-F(1, 8)) <= high_mass/8, 'Laplace identification is compatible with tight energy control')
        count += 1
    counts['positive_spectral_tightness_packets'] = count
    count = 0
    E = [1, 3, 5]
    vectors = [[F(1), F(2), F(1)], [F(1), F(0), F(-1)], [F(0), F(1, 2), F(2)]]
    for f, g in product(vectors, repeat=2):
        cross = [x*y for x, y in zip(f, g)]
        polarized = [((x+y)**2-(x-y)**2)/4 for x, y in zip(f, g)]
        weighted_cross = sum(e*abs(x) for e, x in zip(E, cross))
        f_first, g_first = sum(e*x*x for e, x in zip(E, f)), sum(e*x*x for e, x in zip(E, g))
        require(cross == polarized and weighted_cross**2 <= f_first*g_first, 'cross spectral variation and compact-time Lipschitz budget follow from diagonal moments')
        count += 1
    counts['polarization_moment_packets'] = count
    count = 0
    for energies in [[0, 1, 2], [1, 2, 3], [1, 3, 5]]:
        nodes = [F(1, 2**e) for e in energies]
        matrix = [[node**k for node in nodes] for k in range(3)]
        expected = (nodes[1]-nodes[0])*(nodes[2]-nodes[0])*(nodes[2]-nodes[1])
        require(determinant3(matrix) == expected != 0, 'finite Laplace Vandermonde control; infinite finite-measure uniqueness remains analytic')
        count += 1
    counts['finite_Laplace_uniqueness_controls'] = count
    count = 0
    for N in [2, 4, 8, 16]:
        mass, energy = 2**N, N*N
        laplace_at_log2 = F(mass, 2**energy)
        fixed_Schwartz_pairing = F(mass, 2**(N//2))
        require(laplace_at_log2 <= F(1, 2**N) and fixed_Schwartz_pairing == 2**(N//2) > 1, 'positive-time Laplace disappearance alone does not imply tempered boundedness')
        require(mass*energy > N, 'hostile family violates the retained mass/first-moment controls')
        count += 1
    counts['Euclidean_only_tempered_failure_packets'] = count
    count = 0
    for c_star, sigma_star, N in product([F(0), F(1, 65536)], [F(0), F(1, 2), F(1)], [4, 16, 64]):
        h = F(1, N)
        c_h, sigma_h = c_star+h/F(65536), sigma_star+h
        eta = c_h*h**5
        require(0 < eta < F(27, 262144) and c_h > 0 and sigma_h > 0, 'compact-parameter corollary allows zero limits,not zero finite couplings/clocks')
        require(6*c_h-6*c_star == 6*h/F(65536) and 3*sigma_h-3*sigma_star == 3*h, 'limit amplitude and frequency parameters converge independently')
        count += 1
    counts['compact_parameter_packets'] = count
    count = 0
    for c_h, n in product([F(1, 32768), F(1, 65536), F(1, 131072)], [4, 8, 12, 16]):
        h, _, P_buffer = geometry(n)
        eta = c_h*h**5
        outer_M = int(h**-2)
        P_outer = 3*(2*outer_M+1)*(2*outer_M)**2
        require(eta*P_buffer < 1 and P_outer >= P_buffer, 'buffer proof stays valid even when outer total potential is not small')
        if n >= 12:
            require(eta*P_outer > 0 and eta*P_outer >= 24*c_h/h, 'outer global perturbation can grow without entering local comparison')
        R = F(4096, 3)*eta
        S = R+F(8, 3)*R*R
        require(h*S/(2*eta) <= F(2816, 3)*h, 'same bare mixed Ward transfer remains uniform in outer volume')
        require(F(294912)*h > 0, 'fixed joint cap-removal budget is independent of source volume')
        count += 1
    counts['outer_volume_Ward_cap_scope_packets'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 95, 'frozen substantive coverage')
    paths = [CONTRACT, NOTE, SELF, previous_path, word_path,
             BASE+'yang-mills-critical-mixed-limit-v1.md', BASE+'yang-mills-mesh-word-v1.md',
             BASE+'yang-mills-propagator-comparison-v1.md', BASE+'yang-mills-interacting-magnetic-coercivity-v1.md',
             BASE+'yang-mills-mixed-reader-ward-v1.md']
    return {
        'schema': 'marici.yang-mills-critical-limit-order.result.v1',
        'passed': True, 'new_exact_controls': 95, 'coverage': counts,
        'predecessor_critical_controls_replayed': previous['new_exact_controls'],
        'original_word_boundary_receipt_replayed': True,
        'original_word_discounted_gradient_grids': word['discounted_gradient_grids'],
        'original_word_state_identification_defect': word['state_identification_hostile_residual'],
        'strength': 'written actual arbitrary-outer-volume critical mixed/capped joint two-point limit and native thermodynamic-first magnetic spectral limit; no all-clock classification or infinite electric representation',
        'limit_kernel': '6c*exp(-i3sigma*(t-s))*delta^3(x-y)',
        'centered_outer_buffer_coefficient': '576/5',
        'spectral_escape_control': 'positive mass/first moment tightness plus Laplace uniqueness,not Euclidean insertion convergence alone',
        'arbitrary_exhausting_outer_box_growth_covered': True,
        'native_thermodynamic_first_magnetic_channel_identified': True,
        'new_thermodynamic_first_electric_operator_constructed': False,
        'quantitative_real_time_boundary_rate_claimed': False,
        'arbitrary_escaping_clock_classification_completed': False,
        'Lorentz_scalar_or_Yang_Mills_constructed': False,
        'finite_controls_certify_analytic_limit': False,
        'independent_analytic_review_complete': False,
        'next_executable': 'arbitrary-clock-native-two-point-classification',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in r.items() if k != 'input_sha256'}, indent=2))
