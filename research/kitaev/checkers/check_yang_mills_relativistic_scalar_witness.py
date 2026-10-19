"""Exact scalar-bridge scope guards; not a distribution/reconstruction prover."""
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_arbitrary_clock_locality import report as predecessor_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-relativistic-scalar-witness.v1.json'
NOTE = BASE+'yang-mills-relativistic-scalar-witness-v1.md'
SELF = BASE+'checkers/check_yang_mills_relativistic_scalar_witness.py'
OUT = ROOT/(BASE+'results/yang-mills-relativistic-scalar-witness-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0)) for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def mv(a, v):
    return [sum((x*y for x, y in zip(row, v)), F(0)) for row in a]


def det(a):
    a = [list(map(F, row)) for row in a]
    result = F(1)
    for i in range(len(a)):
        pivot = next((j for j in range(i, len(a)) if a[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            a[i], a[pivot] = a[pivot], a[i]
            result = -result
        p = a[i][i]
        result *= p
        for j in range(i+1, len(a)):
            ratio = a[j][i]/p
            for k in range(i+1, len(a)):
                a[j][k] -= ratio*a[i][k]
    return result


def boost(beta, gamma, axis=1):
    result = [[F(i == j) for j in range(4)] for i in range(4)]
    result[0][0] = result[axis][axis] = gamma
    result[0][axis] = result[axis][0] = -gamma*beta
    return result


def norm2(v):
    return v[0]**2-sum(x*x for x in v[1:])


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def report():
    c = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    require(c['batch'] == {'kind': 'spatial-scaling', 'iteration': 3, 'size': 10}, 'batch provenance')
    require(all(v is False for v in c['boundary'].values()), 'scope guards')
    require(c['net_update']['ready_frontier'] == ['bounded-electric-magnetic-reader-audit'] and c['net_update']['parent_outcome'] is None, 'actual source comparison remains executable')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-arbitrary-clock-locality-v1.json'
    require(previous['passed'] and previous == json.loads((ROOT/previous_path).read_text()), 'fresh locality controls and unchanged frozen evidence')
    counts = {}
    velocities = [(F(3, 5), F(5, 4)), (F(5, 13), F(13, 12)), (F(8, 17), F(17, 15))]
    metric = [[F(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        metric[i][i] = F(1 if i == 0 else -1)
    count = 0
    for (beta, gamma), axis, t in product(velocities, [1, 2, 3], map(F, [-4, -2, -1, 1, 2, 4])):
        L = boost(beta, gamma, axis)
        require(mul(mul(transpose(L), metric), L) == metric and det(L) == 1 and gamma > 0, 'proper orthochronous rational boost')
        transformed = mv(L, [t, F(0), F(0), F(0)])
        require(transformed[axis] != 0 and norm2(transformed) == t*t, 'nonzero time-axis support is not boost invariant')
        require(mv(L, [F(0)]*4) == [F(0)]*4, 'only the origin remains on every boosted axis')
        count += 1
    counts['rational_boost_support_packets'] = count
    count = 0
    for degree in range(5):
        coordinates = [[F(i, degree+1) for i in range(degree+1)] for _ in range(4)]
        coordinates[1] = [2+x for x in coordinates[1]]
        require(all(norm2(p) < 0 for p in product(*coordinates)), 'entire polynomial-testing grid is spacelike')
        for nodes in coordinates:
            vandermonde = [[x**k for k in range(degree+1)] for x in nodes]
            expected = F(1)
            for i in range(len(nodes)):
                for j in range(i+1, len(nodes)):
                    expected *= nodes[j]-nodes[i]
            require(det(vandermonde) == expected != 0, 'finite-degree tensor evaluation has no hidden polynomial null direction')
            count += 1
    counts['finite_degree_spacelike_polynomial_packets'] = count
    zero = (0, 0, 0, 0)
    spectral_points = [(1, 0, 0, 0), (2, 1, 0, 0), (2, -1, 0, 0), (1, 1, 0, 0), (1, -1, 0, 0)]
    count = 0
    for p, mass, vacuum in product(spectral_points, [F(1, 4), F(1), F(3)], [F(0), F(1)]):
        require(p[0] > 0 and norm2(p) >= 0, 'positive forward-cone spectral point')
        measure = {p: mass, zero: vacuum}
        reflected = {tuple(-x for x in q): weight for q, weight in measure.items()}
        require(measure.get(p, F(0))-reflected.get(p, F(0)) == mass, 'nonzero energy measure cannot equal its reflection in one cone')
        negative = tuple(-x for x in p)
        require(measure.get(negative, F(0))-reflected.get(negative, F(0)) == -mass, 'reflection counterpart')
        require(mass*F(1, 2**p[0]) > 0, 'nonzero positive spectral weight has a positive finite Laplace reader')
        count += 1
    density = [[F(1, 2)]*2 for _ in range(2)]
    for variance in [0, 1, 4, 9]:
        amplitude = isqrt(variance)
        Z = [[F(amplitude), F(0)], [F(0), F(-amplitude)]]
        require(tr(density) == 1 and det(density) == 0, 'constant-field pure vacuum preparation')
        require(tr(mul(density, Z)) == 0 and tr(mul(density, mul(Z, Z))) == variance, 'centering leaves zero-energy variance without a vacuum/clustering condition')
        count += 1
    counts['spectral_reflection_zero_mode_packets'] = count
    count = 0
    for omega, spatial_multiple, (beta, gamma) in product([1, 2, 4], [2, 3, 4], velocities):
        p = [F(omega), F(spatial_multiple*omega), F(0), F(0)]
        require(p[0] > 0 and norm2(p) < 0, 'positive Hamiltonian energy alone does not impose the relativistic spectrum')
        boosted_rest = mv(boost(beta, gamma), [F(omega), F(0), F(0), F(0)])
        require(boosted_rest[0] != omega, 'ultralocal oscillator energy hyperplane is not boost invariant')
        require(F(1, 2**omega) > 0, 'ultralocal positive-time channel survives despite missing relativistic hypotheses')
        count += 1
    counts['ultralocal_oscillator_scope_packets'] = count
    count = 0
    r = F(1, 2)
    geometric_moments = {0: r/(1-r), 2: r*(1+r)/(1-r)**3,
                         4: r*(1+11*r+11*r*r+r**3)/(1-r)**5}
    require(geometric_moments == {0: 1, 2: 6, 4: 150}, 'exact positive-time geometric moment values')
    for power, N in product([0, 2, 4], [1, 2, 4, 8, 16, 32]):
        equal_time = sum(n**power for n in range(1, N+1))
        positive_time = sum(F(n**power, 2**n) for n in range(1, N+1))
        require(equal_time >= N and 0 < positive_time <= geometric_moments[power], 'positive-time finiteness does not require a sharp-time norm bound')
        count += 1
    counts['positive_time_not_sharp_time_packets'] = count
    count = 0
    for N in [2, 3, 4, 5, 6, 8]:
        amplitude, gaussian_value = F(2**(2*N*N)), F(1, 2**(N*N))
        require(N > 1 and amplitude*gaussian_value == 2**(N*N), 'escaping delta support is locally null but unbounded on one Schwartz test')
        count += 1
    counts['distribution_topology_scope_packets'] = count
    count = 0
    for E, sign, (beta, gamma) in product([1, 2, 4], [-1, 1], velocities[:2]):
        p = [F(E), F(sign*E), F(0), F(0)]
        transformed = mv(boost(beta, gamma), p)
        require(norm2(p) == norm2(transformed) == 0 and transformed[0] > 0 and transformed[1] != 0, 'causal light-cone support is not strictly timelike support')
        count += 1
    counts['massless_lightcone_scope_packets'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 171, 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, previous_path]
    paths += [BASE+name for name in [
        'yang-mills-arbitrary-clock-locality-v1.md', 'contracts/yang-mills-arbitrary-clock-locality.v1.json',
        'yang-mills-spatial-scaling-budget-v1.md', 'yang-mills-spatial-scaling-next-step-v1.md']]
    return {
        'schema': 'marici.yang-mills-relativistic-scalar-witness.result.v1', 'passed': True,
        'strength': 'written conditional scalar support/spectrum bridge and explicit joint-tempered observer comparison; no actual continuum field constructed',
        'coverage': counts, 'new_exact_controls': 171,
        'predecessor_locality_controls_replayed': previous['new_exact_controls'],
        'centered_constant_field_zero_mode_variance': '1',
        'ultralocal_oscillator_has_positive_time_channel_but_fails_relativistic_hypotheses': True,
        'strictly_timelike_inference_rejected': True,
        'actual_continuum_reader_limit_constructed': False,
        'finite_controls_certify_distribution_theorem': False,
        'independent_analytic_review_complete': False,
        'physical_continuum_or_Yang_Mills_root_discharged': False,
        'next_executable': 'bounded-electric-magnetic-reader-audit',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2))
