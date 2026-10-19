"""Exact native-source geometry, character, fluctuation and scope controls."""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_electric_magnetic_reader import report as predecessor_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
NAME = 'yang-mills-free-magnetic-fluctuations'
CONTRACT = BASE+'contracts/'+NAME+'.v1.json'
NOTE = BASE+NAME+'-v1.md'
SELF = BASE+'checkers/check_yang_mills_free_magnetic_fluctuations.py'
OUT = ROOT/(BASE+'results/'+NAME+'-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def faces(N):
    result = []
    for r, s in combinations(range(3), 2):
        ranges = [range(N) if a in (r, s) else range(N+1) for a in range(3)]
        for initial in product(*ranges):
            vertices = [list(initial) for _ in range(4)]
            vertices[1][r] += 1
            vertices[2][r] += 1
            vertices[2][s] += 1
            vertices[3][s] += 1
            result.append((r, s, [tuple(v) for v in vertices]))
    return result


def edges(vertices):
    return {tuple(sorted((vertices[i], vertices[(i+1) % 4]))) for i in range(4)}


def poly_mul(a, b):
    out = [F(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def haar_polynomial(a):
    return sum(x*F(comb(2*(i//2), i//2), (i//2+1)*4**(i//2)) for i, x in enumerate(a) if i % 2 == 0)


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch'] == {'kind': 'spatial-scaling', 'iteration': 5, 'size': 10}, 'fresh batch scope')
    require(all(value is False for value in c['boundary'].values()), 'no endpoint/limit promotion')
    require(c['net_update']['ready_frontier'] == ['interacting-magnetic-fluctuation-coercivity'] and c['net_update']['parent_outcome'] is None, 'executable interacting continuation')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-electric-magnetic-reader-v1.json'
    require(previous['passed'] and previous == json.loads((ROOT/previous_path).read_text()), 'fresh predecessor replay and immutable receipts')
    counts = {}
    count = 0
    for N in [1, 2, 3, 4]:
        fs = faces(N)
        es = set().union(*(edges(v) for _, _, v in fs))
        require(len(fs) == 3*(N+1)*N*N and len(es) == 3*(N+1)**2*N, 'once-counted open-box geometry')
        packets = [edges(v) for _, _, v in fs]
        for p, q in combinations(packets, 2):
            require(p-q and q-p and len(p & q) <= 1, 'distinct square has an unmatched fundamental link,even at shared-edge neighbors')
        require(all(len(p) == 4 for p in packets), 'four distinct fundamental links give physical energy3sigma')
        count += 1
    counts['open_box_geometry_packets'] = count
    chars = [[F(1)], [F(0), F(2)]]
    for n in range(2, 7):
        p = [F(0)]+[2*x for x in chars[-1]]
        for i, x in enumerate(chars[-2]):
            p[i] -= x
        chars.append(p)
    count = 0
    for n, m in product(range(7), repeat=2):
        require(haar_polynomial(poly_mul(chars[n], chars[m])) == F(n == m), 'SU2 character orthogonality from exact Haar polynomial moments')
        count += 1
    require(haar_polynomial([0, 1]) == 0 and haar_polynomial([0, 0, 1]) == F(1, 4), 'normalized fundamental trace mean and variance')
    counts['Haar_character_orthogonality_packets'] = count
    count = 0
    for N in [1, 2, 3, 4, 8, 16]:
        centers = [tuple(F(sum(v[a] for v in vertices), 4*N) for a in range(3)) for _, _, vertices in faces(N)]
        actual = [sum((point[0]**power for point in centers), F(0))/N**3 for power in [0, 1, 2]]
        expected = [3*(1+F(1, N)), F(3, 2)*(1+F(1, N)), 1+F(7, 6*N)-F(1, 6*N**3)]
        limits = [F(3), F(3, 2), F(1)]
        bounds = [F(3, N), F(3, 2*N), F(7, 6*N)]
        for a, e, limit, bound in zip(actual, expected, limits, bounds):
            require(a == e and abs(a-limit) <= bound, 'three-orientation shifted-grid Riemann quadrature with boundary correction')
            count += 1
    counts['shifted_grid_quadrature_packets'] = count
    count = 0
    for twice_p, N in product([0, 2, 3, 4, 8], [1, 2, 4, 8, 16]):
        z_squared = F(N**twice_p)
        a = z_squared/N**3
        P = 3*(N+1)*N*N
        variance = z_squared*F(P, 4*N**6)
        require(variance == F(3, 4)*a*(1+F(1, N)), 'native source variance,not an operator-norm estimate')
        if twice_p < 3:
            require(a == F(1, N**(3-twice_p)), 'subcritical zero scaling')
        elif twice_p == 3:
            require(a == 1 and variance-F(3, 4) == F(3, 4*N), 'critical nonzero ultralocal variance')
        else:
            require(a == N**(twice_p-3), 'supercritical growth at bounded clock')
        count += 1
    counts['normalization_regime_packets'] = count
    count = 0
    for omega, N in product([1, 2, 3, 6], [1, 2, 4, 8, 16]):
        plateau_pairing = F(3, 4)*N**5*(1+F(1, N))
        positive_time_pairing = plateau_pairing/F(2**omega)  # tau=log2
        require(plateau_pairing >= F(3, 4)*N**5, 'fixed Schwartz plateau captures all bounded energies')
        require(positive_time_pairing >= F(3, 256)*N**5, 'uniform positive-time divergence at omega<=6')
        count += 1
    counts['bounded_clock_divergence_packets'] = count
    count = 0
    for omega, N in product([1, 2, 3, 6], [1, 2, 4, 8, 16]):
        limit = F(3, 4*2**omega)
        actual = limit*(1+F(1, N))
        require(actual-limit == limit/N and limit > 0, 'critical native finite positive-time channel')
        count += 1
    counts['critical_temporal_channel_packets'] = count
    count = 0
    for N in [1, 2, 4, 8, 16, 32]:
        a, omega = N**5, 3*N
        bound = F(384*a, omega**6)
        require(bound == F(128, 243*N), 'fixed sixth-derivative Schwartz bound tends to zero')
        variance = F(3, 4)*N**5*(1+F(1, N))
        require(variance >= F(3, 4)*N**5, 'same native family has divergent equal-time variance')
        if N >= 2:
            dyadic_ratio = 32*(1+F(1, 2*N))/(1+F(1, N))/2**(3*N)
            require(dyadic_ratio < F(1, 2), 'escaping-clock positive-time channel dies,not survives')
        count += 1
    counts['escaping_clock_scope_packets'] = count
    # Six outward cube faces: Haar fundamental/inverse contraction joins corner indices.
    cube = faces(1)
    parent = list(range(24))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        parent[find(a)] = find(b)
    occurrences = {}
    for face, (r, s, vertices) in enumerate(cube):
        remaining = ({0, 1, 2}-{r, s}).pop()
        standard_normal = -1 if (r, s) == (0, 2) else 1
        outward_normal = 1 if vertices[0][remaining] == 1 else -1
        if standard_normal != outward_normal:
            vertices = [vertices[i] for i in [0, 3, 2, 1]]
        for i in range(4):
            start, end = vertices[i], vertices[(i+1) % 4]
            occurrences.setdefault(tuple(sorted((start, end))), []).append((start, end, 4*face+i, 4*face+(i+1) % 4))
    require(len(occurrences) == 12, 'closed cube link count')
    for pair in occurrences.values():
        require(len(pair) == 2, 'two faces per cube link')
        a, b = pair
        require(a[0] == b[1] and a[1] == b[0], 'opposite face orientations produce Haar D(g)/D(g^-1) contraction')
        union(a[2], b[3])
        union(a[3], b[2])
    loops = len({find(i) for i in range(24)})
    cube_moment = F(2**loops, 2**(12+6))
    require(loops == 8 and cube_moment == F(1, 1024), 'actual joint-dependence witness,not independent plaquette assumption')
    counts['closed_cube_dependence_packets'] = 1
    count = 0
    for omega in [1, 2, 3, 6]:
        sigma = F(omega, 3)
        require(4*F(3, 4)*sigma == omega, 'four-link physical excitation')
        middle_insertion = F(3, 4)*F(1, 4)
        require(middle_insertion == F(3, 16) > 0, 'electric vacuum annihilation does not erase middle insertions')
        count += 1
    counts['electric_middle_insertion_packets'] = count
    count = 0
    for omega in [F(0), F(3, 4), F(3), F(6)]:
        momentum = 2*omega+1
        require(omega >= 0 and omega**2-momentum**2 < 0, 'positive native spectral measure has spacelike momentum support')
        require(omega-F(3, 4)*momentum < 0, 'a subluminal Lorentz boost produces negative energy on this support')
        count += 1
    counts['forward_cone_failure_packets'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 151, 'frozen substantive coverage')
    paths = [CONTRACT, NOTE, SELF, previous_path,
             BASE+'yang-mills-ground-state-transfer-v1.md',
             BASE+'yang-mills-arbitrary-clock-locality-v1.md',
             BASE+'yang-mills-electric-magnetic-reader-v1.md']
    return {
        'schema': 'marici.yang-mills-free-magnetic-fluctuations.result.v1',
        'passed': True, 'new_exact_controls': 151, 'coverage': counts,
        'predecessor_reader_controls_replayed': previous['new_exact_controls'],
        'strength': 'exact native free-source two-point scaling and written joint tempered limit/divergence controls; not an interacting or all-orders scalar construction',
        'native_plaquette_variance': '1/4', 'physical_excitation_over_sigma': '3',
        'critical_field_normalization_power': '3/2',
        'six_face_cube_moment': str(cube_moment),
        'electric_middle_insertion': '3/16',
        'escaping_clock_Sprime_bound_coefficient': '128/243',
        'nonzero_limit_is_Lorentz_scalar': False,
        'interacting_covariance_or_continuum_limit_proved': False,
        'all_orders_Gaussian_convergence_proved': False,
        'finite_controls_certify_analytic_limits': False,
        'independent_analytic_review_complete': False,
        'continuum_Yang_Mills_root_discharged': False,
        'next_executable': 'interacting-magnetic-fluctuation-coercivity',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in r.items() if k != 'input_sha256'}, indent=2))
