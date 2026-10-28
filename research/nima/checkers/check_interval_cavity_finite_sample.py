"""Fixed-design mathematical certificate. Exact arithmetic; no acquired trials."""
import itertools
import json
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
N = 40000
EPS = F(1, 100)
ALPHA = F(1, 100)
A_MIN = F(1, 5)
LOW = F(9, 25)
PAIRS = tuple((i, j) for j in range(1, 4) for i in range(1, j+1))
SOURCES = [
    'research/nima/interval-cavity-finite-sample-protocol.md',
    'research/nima/interval-cavity-probes.md',
    'research/nima/results/interval-cavity-probes.json',
    'research/nima/checkers/check_interval_cavity_finite_sample.py',
]


def require(ok, why):
    if not ok:
        raise ValueError(why)


def signature(pair):
    i, j = pair
    return tuple(LOW if i-1 <= k <= j-1 else F(1) for k in range(3))


def candidates(reference, validation, radius):
    """Region engine; broad radii are diagnostics, not the issued certificate."""
    require(len(reference) == len(validation) == 3, 'rate vector size')
    require(0 <= radius <= 1, 'radius domain')
    require(all(0 <= x <= 1 for x in reference+validation), 'rate domain')
    intervals = []
    for b, c in zip(reference, validation):
        blo, bhi = max(A_MIN, b-radius), min(F(1), b+radius)
        clo, chi = max(F(0), c-radius), min(F(1), c+radius)
        if blo > bhi:
            return []
        intervals.append((blo, bhi, clo, chi))
    out = []
    for pair in PAIRS:
        # Exact existential test: some a in B has a*t in C at every port.
        if all(max(blo, clo/t) <= min(bhi, chi/t)
               for t, (blo, bhi, clo, chi) in zip(signature(pair), intervals)):
            out.append(pair)
    return out


def decision(possible):
    return {'status': 'certified' if len(possible) == 1 else
                      'ambiguous' if possible else 'model_inconsistent',
            'interval': list(possible[0]) if len(possible) == 1 else None,
            'compatible_intervals': [list(p) for p in possible]}


def certify(rows):
    """Fixed n, epsilon and six arms: no adaptive continuation or tuned radius."""
    require(isinstance(rows, list) and len(rows) == 6, 'six complete arms required')
    rates = {}
    for r in rows:
        require(set(r) == {'kind', 'port', 'attempted', 'C', 'N'}, 'record fields')
        require(r['kind'] in ('reference', 'validation'), 'arm kind')
        require(type(r['port']) is int and 0 <= r['port'] < 3, 'port')
        require(all(type(r[k]) is int for k in ('attempted', 'C', 'N')), 'integer counts')
        require(r['attempted'] == N and 0 <= r['C'] <= N and 0 <= r['N'] <= N,
                'fixed sample/count bounds')
        require(r['C']+r['N'] == N, 'missing outcomes')
        key = (r['kind'], r['port'])
        require(key not in rates, 'duplicate arm')
        rates[key] = F(r['C'], N)
    require(set(rates) == set(itertools.product(('reference', 'validation'), range(3))), 'arm coverage')
    return decision(candidates([rates['reference', k] for k in range(3)],
                               [rates['validation', k] for k in range(3)], EPS))


def packet(b, c):
    rows = []
    for kind, rates in (('reference', b), ('validation', c)):
        for k, p in enumerate(rates):
            count = p*N
            require(count.denominator == 1, 'fixture must have integral counts')
            rows.append({'kind': kind, 'port': k, 'attempted': N, 'C': int(count), 'N': N-int(count)})
    return rows


def hashes():
    return {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCES}


def main():
    pins = hashes()
    prior = json.loads((ROOT/SOURCES[2]).read_text())
    require(prior['passed'] and not prior['physical_realization_admitted'], 'prior scope')
    for row in prior['response_table']:
        require(tuple(F(o['C'])/LOW for o in row['outcomes']) == signature(tuple(row['interval'])), 'prior signature')
    # Two-sided Hoeffding and union bound: P(any bad rate)<=12 exp(-2 N eps^2).
    exponent = 2*N*EPS*EPS
    require(exponent == 8, 'fixed exponent')
    exp_lower = sum(exponent**k/F(factorial(k)) for k in range(9))
    tail_upper = 12/exp_lower
    require(tail_upper < ALPHA, 'outward conservative exponential bound')
    # On the good event any confidence-compatible rates differ from truth by <=2 eps.
    good_event_ratio_bound = 4*EPS/(A_MIN-2*EPS)
    require(good_event_ratio_bound == F(2, 9) < 1-LOW, 'uniform unique identification')
    # In fact no production data can fit both t values at one coordinate.
    require((1-LOW)*A_MIN-2*LOW*EPS > 2*EPS, 'narrow-box per-port uniqueness')
    cases = 0
    factors = [(a,)*3 for a in (A_MIN, LOW, F(1))] + [(A_MIN, LOW, F(1))]
    for pair, b, signs in itertools.product(PAIRS, factors, itertools.product((-1, 1), repeat=6)):
        c = tuple(a*t for a, t in zip(b, signature(pair)))
        rates = tuple(min(F(1), max(F(0), p+s*EPS)) for p, s in zip(b+c, signs))
        result = certify(packet(rates[:3], rates[3:]))
        require(result['status'] == 'certified' and result['interval'] == list(pair), 'good-event corner classification')
        cases += 1

    hostiles = []
    baseline = packet((A_MIN,)*3, tuple(A_MIN*t for t in signature((1, 2))))

    def rejects(name, rows):
        try:
            certify(rows)
        except ValueError:
            hostiles.append(name)
        else:
            raise AssertionError('invalid data accepted: '+name)

    rejects('incomplete-arms', baseline[:-1])
    bad = deepcopy(baseline); bad[0]['C'] = -1
    rejects('negative-count', bad)
    bad = deepcopy(baseline); bad[0]['C'] = True
    rejects('boolean-count', bad)
    bad = deepcopy(baseline); bad[0]['attempted'] += 1
    rejects('adaptive-or-wrong-sample-count', bad)
    bad = deepcopy(baseline); bad[0]['N'] -= 1
    rejects('omitted-no-click', bad)
    bad = deepcopy(baseline); bad[-1] = deepcopy(bad[0])
    rejects('duplicate-arm', bad)
    zero = certify(packet((F(0),)*3, (F(0),)*3))
    require(zero['status'] == 'model_inconsistent' and zero['interval'] is None, 'zero-reference abstention')
    hostiles.append('zero-reference-no-division')
    noninterval = certify(packet((LOW,)*3, (LOW*LOW, LOW, LOW*LOW)))
    require(noninterval['status'] == 'model_inconsistent', 'noninterval counts')
    hostiles.append('noninterval-mask')
    # At this fixed tight radius ambiguity is impossible; exercise the region engine
    # with a wider diagnostic box instead of fabricating an ambiguous production input.
    ambiguous = decision(candidates([A_MIN]*3, [F(3, 25)]*3, F(1, 5)))
    require(ambiguous['status'] == 'ambiguous' and len(ambiguous['compatible_intervals']) == 6, 'wide-box ambiguity')
    hostiles.append('wide-diagnostic-region-abstains-not-issued-confidence')
    # Shared-factor violation: true [1,2] with drift exactly mimics stationary [2,3].
    b = (F(1, 4), F(1, 2), F(3, 4))
    target_c = tuple(a*t for a, t in zip(b, signature((2, 3))))
    drift = tuple(c/t for c, t in zip(target_c, signature((1, 2))))
    require(all(A_MIN <= a <= 1 for a in drift) and drift != b, 'admissible factors but not shared')
    drift_result = certify(packet(b, target_c))
    require(drift_result['interval'] == [2, 3], 'drift alias')
    hostiles.append('shared-factor-violation-can-falsely-identify-true-interval')
    require(hashes() == pins, 'source drift')
    result = {
        'schema': 'marici.nima.interval-cavity-finite-sample.v1', 'passed': True,
        'verdict': 'conditional_fixed_sample_interval_certification_constructed',
        'trials_per_arm': N, 'arms': 6, 'total_trials': 6*N,
        'epsilon': str(EPS), 'alpha': str(ALPHA),
        'failure_probability_upper_bound': str(tail_upper),
        'good_event_ratio_bound': str(good_event_ratio_bound),
        'good_event_corner_cases': cases,
        'production_ambiguity': 'Impossible at frozen bounds; no match yields model_inconsistent and no interval.',
        'wide_region_diagnostic': ambiguous,
        'drift_alias': {'true_interval': [1, 2], 'reported_interval': [2, 3],
                        'reference_factors': [str(x) for x in b], 'validation_factors': [str(x) for x in drift]},
        'hostiles': hostiles, 'hardware_scope': 'excluded', 'acquired_data': False,
        'coverage_scope': 'Unconditional error probability for the fixed design, not posterior error conditional on certification; independent Bernoulli trials within each arm and static shared factors assumed.',
        'source_sha256': pins,
    }
    (ROOT/'research/nima/results/interval-cavity-finite-sample.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, indent=2))


if __name__ == '__main__':
    main()
