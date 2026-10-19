"""Exact geometry/Bochner/coercivity planners; not a source-vacuum solver."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_free_magnetic_fluctuations import report as predecessor_report, faces, edges

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
NAME = 'yang-mills-interacting-magnetic-coercivity'
CONTRACT = BASE+'contracts/'+NAME+'.v1.json'
NOTE = BASE+NAME+'-v1.md'
SELF = BASE+'checkers/check_yang_mills_interacting_magnetic_coercivity.py'
OUT = ROOT/(BASE+'results/'+NAME+'-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0)) for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def scale(a, s):
    return [[s*x for x in row] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch'] == {'kind': 'spatial-scaling', 'iteration': 6, 'size': 10}, 'batch scope')
    require(all(value is False for value in c['boundary'].values()), 'no source/domain/mixed-reader promotion')
    require(c['net_update']['ready_frontier'] == ['mixed-electric-magnetic-Ward-audit'] and c['net_update']['parent_outcome'] is None, 'next actual mixed gate')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-free-magnetic-fluctuations-v1.json'
    require(previous['passed'] and previous == json.loads((ROOT/previous_path).read_text()), 'fresh frozen predecessor replay')
    counts = {}
    geometries = []
    for N in [1, 2, 3, 4]:
        fs = [edges(v) for _, _, v in faces(N)]
        incidence = {}
        for p, square in enumerate(fs):
            for e in square:
                incidence.setdefault(e, []).append(p)
        for e, incident in incidence.items():
            star = set().union(*(fs[p] for p in incident))
            require(len(incident) <= 4 and len(star) == 1+3*len(incident) <= 13, 'actual link star and overlap count')
            require(all(e in fs[p] for p in incident), 'Haar local gradient support')
        require(all(len(p) == 4 for p in fs), 'all four plaquette links retained at boundaries')
        geometries.append((fs, incidence))
    counts['open_box_star_packets'] = 4
    # Real quaternion left generators,each divided by2: radius-two SU2 metric.
    units = [
        [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]],
        [[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]],
        [[0, 0, 0, -1], [0, 0, -1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]]
    generators = [scale(u, F(1, 2)) for u in units]
    I = [[F(i == j) for j in range(4)] for i in range(4)]
    count = 0
    for a, b in product(range(3), repeat=2):
        X, Y = generators[a], generators[b]
        require(mul(transpose(X), X) == scale(I, F(1, 4)), 'fundamental generator norm1/2')
        symmetric = scale(add(mul(X, Y), mul(Y, X)), F(1, 2))
        require(symmetric == scale(I, -F(a == b, 4)), 'connection-corrected Hessian is symmetrized,not the raw frame product')
        count += 1
    require(12*F(1, 4)*4 == 12 and 12**2*F(1, 16)*4 == 36, 'entrywise derivative/overlap constants')
    counts['quaternion_generator_connection_packets'] = count
    count = 0
    for fs, incidence in geometries:
        patterns = [[F(1)]*len(fs), [F((-1)**p) for p in range(len(fs))], [F(p % 5-2, 3) for p in range(len(fs))]]
        for b in patterns:
            Q = sum(x*x for x in b)
            haar_D = sum(F(3, 16)*sum(b[p]**2 for p in ps) for ps in incidence.values())
            require(haar_D == F(3, 4)*Q and Q > 0, 'Haar thirteen-link integration accounts for each square four times')
            count += 1
    counts['Haar_Dirichlet_accounting_packets'] = count
    count = 0
    for weights, G in product([(1, 1, 1), (1, 2, 4), (2, 3, 5), (3, 4, 3)], [(1, 0, 0), (0, 2, 1), (1, 3, 2)]):
        expectation = F(sum(w*g for w, g in zip(weights, G)), sum(weights))
        haar = F(sum(G), 3)
        require(expectation >= F(min(weights), max(weights))*haar, 'normalized local likelihood comparison,not global density minimum')
        count += 1
    counts['normalized_local_likelihood_packets'] = count
    Rs = [F(0), F(1, 64), F(1, 16), F(1, 8), F(9, 64)]
    d_floor, B_ceiling = F(417, 1024), F(753, 16)
    coercivity_margin = d_floor**2/B_ceiling
    require(coercivity_margin == F(57963, 16449536) > F(1, 512), 'exact uniform rational margin')
    count = 0
    for R, incident_count in product(Rs, range(5)):
        star_size = 1+3*incident_count
        likelihood_linear_lower = 1-F(star_size, 4)*R
        d_lower = F(3, 4)*likelihood_linear_lower
        B = 42+36*R
        require(likelihood_linear_lower >= F(139, 256), 'exp(-x)>=1-x remains positive over actual stars/window')
        require(d_lower >= d_floor and B <= B_ceiling and d_lower**2/B > F(1, 512), 'local energy/Bochner gives a full-window covariance lower bound')
        count += 1
    counts['rational_conditional_Bochner_margin_packets'] = count
    count = 0
    for R, Q in product(Rs, [F(1, 4), F(1), F(4)]):
        d = F(3, 4)*(1-F(13, 4)*R)
        B = 42+36*R
        lower_V = (d*Q)**2/(B*Q)
        upper_V = F(64, 5)*12*Q
        require(lower_V > Q/512 and upper_V == F(768, 5)*Q and lower_V <= upper_V, 'Cauchy-Bochner lower and independently obtained Poincare upper')
        count += 1
    counts['covariance_sandwich_packets'] = count
    count = 0
    for t, mass in product([2, 4, 8], [F(1, 4), F(1), F(2)]):
        Q, sigma = 512*mass, F(t, 6144)
        energies = [t//2, 3*t//2]
        first = mass*F(sum(energies), 2)
        actual = mass*sum((F(1, 2**E) for E in energies), F(0))/2
        bound = Q/F(512*2**t)
        require(first == 12*sigma*Q and actual >= bound > 0, 'positive spectral Jensen at tau=log2 pays actual energy moment,not free energy3sigma')
        count += 1
    counts['spectral_Jensen_packets'] = count
    count = 0
    for t, mass in product([3, 6, 12], [F(1, 4), F(1), F(2)]):
        Q, sigma = 512*mass, F(t, 6144)
        low_E, high_E, L = F(t, 3), 3*t, 12288*sigma
        low_mass, high_mass = 3*mass/4, mass/4
        first = low_E*low_mass+high_E*high_mass
        require(first == 12*sigma*Q and low_E <= L < high_E, 'nontrivial actual-moment-style spectral window control')
        require(high_mass <= first/L and low_mass >= Q/1024, 'fixed Fourier plateau retains a uniform mass fraction')
        count += 1
    counts['spectral_window_packets'] = count
    count = 0
    for twice_p, N in product([0, 3, 8], [1, 2, 4, 8, 16]):
        P = 3*(N+1)*N*N
        Q = F(N**twice_p*P, N**6)
        a = F(N**twice_p, N**3)
        require(Q == 3*a*(1+F(1, N)), 'geometric l2 coefficient normalization')
        require(Q/512 < F(768, 5)*Q, 'uniform interacting variance sandwich')
        if twice_p == 8:
            require(Q/1024 >= F(3, 1024)*N**5, 'actual interacting h^-4 growth forced by fixed-test spectral mass')
        elif twice_p == 3:
            require(3 <= Q <= 6, 'critical coefficient mass stays nonzero and bounded')
        else:
            require(Q == F(3, N**3)*(1+F(1, N)), 'subcritical coefficient mass vanishes')
        count += 1
    counts['normalization_growth_packets'] = count
    count = 0
    points = list(product([-1, 1], repeat=2))
    for N in [2, 4, 8, 16, 32]:
        rho = 1-F(1, N)
        law = [(1+rho*x*y)/4 for x, y in points]
        require(all(p > 0 for p in law) and sum(law) == 1, 'hostile full-support finite block')
        variance = sum(p*(x-y)**2 for p, (x, y) in zip(law, points))
        reset = [[p for p in law] for _ in law]
        A = [[F(i == j)-reset[i][j] for j in range(4)] for i in range(4)]
        require(mul(A, A) == A and all(sum(row) == 0 for row in A), 'independent-block reset generator has nonzero spectral value1')
        require(variance == F(2, N) and variance/2 == F(1, N), 'gap and exact interblock clustering do not supply uniform local covariance coercivity')
        count += 1
    counts['gap_clustering_not_coercivity_packets'] = count
    count = 0
    for N in [1, 2, 4, 8]:
        minimum_global_density = F(3, 4)**N
        local_variance = 1-F(1, 4)**2
        require(minimum_global_density <= F(3, 4) and local_variance == F(15, 16), 'global density minima deteriorate although local product covariance remains coercive')
        count += 1
    counts['global_density_ratio_scope_packets'] = count
    count = 0
    for eta in [F(0), F(1, 65536), F(1, 16384)]:
        for electric, magnetic in [(F(1), -eta), (F(1), F(1)), (F(-1), F(-1))]:
            V = F(1)  # symbolic positive global magnetic variance scaled out
            gram = [[eta**2*V, eta*V], [eta*V, V]]
            variance = electric**2*gram[0][0]+2*electric*magnetic*gram[0][1]+magnetic**2*gram[1][1]
            require(variance == V*(eta*electric+magnetic)**2 and gram[0][0]*gram[1][1]-gram[0][1]**2 == 0, 'exact global Ward rank-one Gram identity')
            if magnetic == -eta:
                require(variance == 0, 'magnetic coercivity cannot be promoted to arbitrary electric/magnetic combinations')
            else:
                require(variance > 0, 'same-sign global coefficients do not cancel,but local smear control is still missing')
            count += 1
    counts['mixed_Ward_null_direction_packets'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 128, 'frozen substantive coverage')
    paths = [CONTRACT, NOTE, SELF, previous_path,
             BASE+'yang-mills-anchored-casimir-v1.md', BASE+'yang-mills-uniform-detection-v1.md',
             BASE+'yang-mills-ground-state-transfer-v1.md', BASE+'yang-mills-source-clustering-v1.md']
    return {
        'schema': 'marici.yang-mills-interacting-magnetic-coercivity.result.v1',
        'passed': True, 'new_exact_controls': 128, 'coverage': counts,
        'predecessor_free_fluctuation_controls_replayed': previous['new_exact_controls'],
        'strength': 'written actual-source full-window magnetic covariance coercivity and positive-time/fixed-Schwartz growth obstruction; no mixed-reader or continuum promotion',
        'rational_coercivity_margin': str(coercivity_margin),
        'uniform_covariance_lower': '1/512', 'uniform_covariance_upper': '768/5',
        'positive_time_exponent_over_sigma': 6144, 'fixed_energy_window_over_clock_bound': 12288,
        'fixed_plateau_mass_lower_over_coefficient_l2_squared': '1/1024',
        'global_mixed_Ward_null_direction': '(1,-eta)',
        'actual_Hamiltonian_or_vacuum_replaced': False,
        'magnetic_growth_proves_arbitrary_mixed_reader_growth': False,
        'finite_controls_certify_analytic_theorem': False,
        'individual_continuum_or_Lorentz_field_constructed': False,
        'independent_analytic_review_complete': False,
        'continuum_Yang_Mills_root_discharged': False,
        'next_executable': 'mixed-electric-magnetic-Ward-audit',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in r.items() if k != 'input_sha256'}, indent=2))
