"""Exact controls for the written actual-ground-weighted readout comparison."""
from fractions import Fraction as F
from itertools import product
from math import prod
from hashlib import sha256
from pathlib import Path
import json
from check_yang_mills_mixed_correlator import report as predecessor_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-weighted-orientation.v1.json'
NOTE = BASE+'yang-mills-weighted-orientation-v1.md'
SELF = BASE+'checkers/check_yang_mills_weighted_orientation.py'
OUT = ROOT/(BASE+'results/yang-mills-weighted-orientation-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def haar_monomial(exponents):
    if any(e % 2 for e in exponents):
        return F(0)
    numerator = prod(prod(range(1, e, 2)) for e in exponents)
    denominator = prod(4+2*k for k in range(sum(exponents)//2))
    return F(numerator, denominator)


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 6 and all(v is False for v in c['boundary'].values()), 'scope')
    require(not c['parent_net']['discharges_parent'] and c['subnet']['parent_outcome'] is None, 'parent promotion')
    require(c['subnet']['ready_frontier'] == ['actual-trace-reader-dynamical-closure'], 'frontier')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'parent remains open')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-mixed-correlator-v1.json')).read_text()), 'predecessor stale')
    S = set(range(7))
    labels = [frozenset([0, 1, 2, 3]), frozenset([0, 4, 5, 6]), frozenset(range(7)),
              frozenset([3, 7, 8, 9]), frozenset([10, 11, 12, 13])]
    require(c['source']['support_links'] == 7 and c['source']['minimum_retained_label_size'] == 4, 'source label stratum')
    activity_cases = 0
    for pattern in product(range(3), repeat=len(labels)):
        activities = [F(n, 4096) for n in pattern]
        R = max(sum(2**len(A)*w for A, w in zip(labels, activities) if e in A) for e in range(14))
        meeting = sum(w for A, w in zip(labels, activities) if A & S)
        require(meeting <= 7*R/16 and 4*meeting <= 7*R/4, 'seven-link conditional norm/oscillation')
        require(all(len(A) >= 4 for A in labels), 'minimum label')
        activity_cases += 1
    cutoff_R = F(9, 64)
    D_max = 7*cutoff_R/4
    residual_floor = F(3, 4)*(1-D_max)
    require(D_max == F(63, 256) and residual_floor == F(579, 1024) > F(9, 16), 'full-window rational floor')
    for R in [F(0), F(1, 128), F(9, 128), cutoff_R]:
        require(0 <= 7*R/4 <= D_max < 1, 'likelihood comparison range')
        require(F(3, 4)*(1-7*R/4) >= residual_floor, 'monotone residual bound')
    singleton_w = F(1, 100)
    require(singleton_w > 7*(2*singleton_w)/16, 'minimum-size hypothesis hostile')

    axes = [tuple(F(sign*(i == axis)) for i in range(4)) for axis in range(4) for sign in [-1, 1]]
    cube = [tuple(F(sign, 2) for sign in signs) for signs in product([-1, 1], repeat=4)]
    qs = axes+cube
    require(len(qs) == 24 and all(sum(x*x for x in q) == 1 for q in qs), 'rational unit quaternion design')
    monomial_cases = 0
    for exponents in product(range(6), repeat=4):
        if sum(exponents) > 5:
            continue
        actual = sum(prod(q[i]**exponents[i] for i in range(4)) for q in qs)/24
        require(actual == haar_monomial(exponents), 'degree<=5 Haar moment')
        monomial_cases += 1
    pair_data = []
    for x, y in product(qs, repeat=2):
        a, cc = x[0], y[0]
        h = -2*sum(v*w for v, w in zip(x[1:], y[1:]))
        v0 = F(4, 3)*(1-a*a)*(1-cc*cc)
        pair_data.append((a, cc, h, v0))
    require(sum(h*h for a, cc, h, v0 in pair_data)/576 == F(3, 4), 'Haar residual input')
    require(sum(v0*v0 for a, cc, h, v0 in pair_data)/576 == F(25, 36), 'true fourth-moment conditional variance square')
    tilts = []
    for epsilon in [F(-1, 4), F(-1, 8), F(0), F(1, 8), F(1, 4)]:
        total = F(0)
        raw_mean = F(0)
        residual = F(0)
        reader_pairings = [F(0) for _ in range(6)]
        bins = {}
        for a, cc, h, v0 in pair_data:
            weight = (1+epsilon*h)/576
            require(1+epsilon*h >= F(1, 2), 'positive tilted diagnostic density')
            centered = h-epsilon*v0
            total += weight
            raw_mean += weight*h
            residual += weight*centered*centered
            for i, value in enumerate([F(1), 2*a, 2*cc, 4*a*cc, 4*a*a, 4*cc*cc]):
                reader_pairings[i] += weight*centered*value
            mass, numerator = bins.get((a, cc), (F(0), F(0)))
            bins[(a, cc)] = (mass+weight, numerator+weight*h)
        require(total == 1 and raw_mean == epsilon*F(3, 4), 'raw Haar centering is not actual centering')
        require(all(value == 0 for value in reader_pairings), 'weighted trace polynomial orthogonality')
        for (a, cc), (mass, numerator) in bins.items():
            require(numerator/mass == epsilon*F(4, 3)*(1-a*a)*(1-cc*cc), 'actual diagnostic conditional mean')
        expected = F(3, 4)-F(25, 36)*epsilon*epsilon
        require(residual == expected >= (1-2*abs(epsilon))*F(3, 4), 'positive-law variational comparison')
        if epsilon:
            require(raw_mean != 0, 'uncentered h fails even the vacuum test')
        if epsilon == F(1, 4):
            require(residual == F(407, 576), 'declared tilt fixture')
        tilts.append({'epsilon': str(epsilon), 'raw_mean': str(raw_mean), 'centered_norm_squared': str(residual), 'conditional_bins': len(bins)})
    singular_residual = F(0)
    for x in qs:
        h = -2*sum(v*v for v in x[1:])
        trace_only_h = -2*(1-x[0]*x[0])
        singular_residual += (h-trace_only_h)**2/24
    require(singular_residual == 0, 'singular orientation law removes blind sector')
    near_endpoint = F(4, 3)*(1-F(1023, 1024)**2)
    require(0 < near_endpoint < residual_floor, 'averaged floor is not a uniform trace-fiber floor')
    paths = [CONTRACT, NOTE, SELF, c['parent_net']['path'], BASE+'yang-mills-quotient-descent-v1.md']
    for name in ['mixed-correlator', 'thermodynamic-vacuum', 'anchored-casimir']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py',
                  BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-weighted-orientation.result.v1', 'passed': True,
            'strength': 'written actual-measure conditional comparison, with exact finite controls; independently unreviewed',
            'activity_cases': activity_cases, 'S3_degree5_monomials': monomial_cases,
            'loop_pair_cases_per_tilt': 576, 'tilt_results': tilts,
            'actual_norm_squared_lower': '3*exp(-7*R/4)/4', 'strict_uniform_rational_floor': str(residual_floor),
            'exterior_augmented_reader_bound': True, 'singular_law_residual': str(singular_residual),
            'near_endpoint_Haar_fiber_variance': str(near_endpoint),
            'projected_probe_energy_or_form_domain': False, 'independent_analytic_review': False,
            'continuum_Yang_Mills': False, 'ready_frontier': c['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'activity_cases', 'S3_degree5_monomials',
                     'loop_pair_cases_per_tilt', 'strict_uniform_rational_floor',
                     'exterior_augmented_reader_bound', 'projected_probe_energy_or_form_domain']}, indent=2))
