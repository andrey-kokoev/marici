"""Exact conditional-scaling/spectral scope controls; not a continuum prover."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-physical-scaling-obstruction.v1.json'
NOTE = BASE+'yang-mills-physical-scaling-obstruction-v1.md'
PACKET = BASE+'yang-mills-shoshin-second-pass-review-v1.md'
SELF = BASE+'checkers/check_yang_mills_physical_scaling_obstruction.py'
OUT = ROOT/(BASE+'results/yang-mills-physical-scaling-obstruction-v1.json')


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def decay(rate, steps=1):
    """exp(-steps*log(2)*rate), for integer rate, as an exact fraction."""
    return F(1, 2**(rate*steps))


def report():
    contract = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    require(all(v is False for v in contract['boundary'].values()), 'conditional claim boundaries')
    require(contract['review_status'] == 'prepared_for_external_handoff_not_dispatched', 'no implied external delivery')
    eta_limit = F(27, 262144)
    g4_floor = F(1048576, 27)
    require(4/eta_limit == g4_floor and F(1024)**2/27 == g4_floor, 'exact coupling floor')
    gap_coefficient_squared = F(1600, 27)
    require(F(5, 128)**2*g4_floor == gap_coefficient_squared, '40/sqrt(27) coefficient')
    counts = {}
    count = 0
    for multiplier in [F(1, 2), F(1), F(2), F(4), F(16)]:
        g4 = multiplier*g4_floor
        eta = 4/g4
        R = F(4096, 3)*eta
        curvature = F(1, 2)-3*R
        require((eta < eta_limit) == (multiplier > 1), 'open source endpoint')
        require((curvature > F(5, 64)) == (multiplier > 1), 'strict curvature threshold')
        if multiplier == 1:
            require(R == F(9, 64) and curvature == F(5, 64), 'excluded equality endpoint')
        count += 1
    counts['source_endpoint_packets'] = count
    count = 0
    for g2, spacing in product(map(F, [200, 256, 512, 1024]), [F(1), F(1, 2), F(1, 16), F(1, 256)]):
        kappa, lam = g2/(2*spacing), 2/(spacing*g2)
        eta = lam/kappa
        R = F(4096, 3)*eta
        m = kappa*(F(1, 2)-3*R)
        floor = F(5, 64)*kappa
        require(eta == 4/g2**2 and eta < eta_limit, 'actual declared matching in retained regime')
        require(m > floor > 0 and (spacing*floor)**2 > gap_coefficient_squared, 'divergent physical floor')
        require(spacing*m == g2/4-8192/g2, 'parameter-sensitive bound')
        count += 1
    counts['physical_matching_packets'] = count
    count = 0
    for n, weights in product(range(1, 9), [(F(1), F(0), F(0)), (F(1), F(2), F(3)), (F(1, 3), F(7, 4), F(5, 2))]):
        rates = [n, n+2, 2*n+1]
        earlier = sum(w*decay(rate) for w, rate in zip(weights, rates))
        later = sum(w*decay(rate, 2) for w, rate in zip(weights, rates))
        require(0 <= later <= decay(n)*earlier, 'two-time scalar spectral envelope')
        count += 1
    counts['spectral_envelope_packets'] = count
    count = 0
    for n in range(1, 13):
        # H_n has a centered eigenvector of energy n. Its squared amplitude is4^n.
        norm_squared = F(4**n)
        earlier = norm_squared*decay(n)
        later = norm_squared*decay(n, 2)
        require(later == 1 and earlier == 2**n, 'late-time renormalization forces earlier positive-time blowup')
        # Multiplying H_n by spacing=1/n changes the clock and gives energy1.
        spacing = F(1, n)
        require(spacing*n == 1 and decay(1) == F(1, 2), 'changed-clock escape is outside theorem premises')
        count += 1
    counts['renormalization_clock_packets'] = count
    count = 0
    for n in range(2, 13):
        # H=diag(0,1,n), vacuum e0. A fast reader e2 does not detect e1.
        require(decay(1, 2) > decay(n)*decay(1), 'hidden finite-energy reader violates falsely claimed whole-space threshold n')
        require(1-n < 0, 'form H-n*(I-Pvac) fails on the hidden mode')
        require(decay(n, 2) == decay(n)*decay(n), 'fast observed mode alone would pass')
        count += 1
    counts['hidden_mode_packets'] = count
    count = 0
    for N, amplitude in product([1, 2, 4, 8], [F(1, 4), F(1), F(3)]):
        distances = list(range(N))
        blocks = [amplitude*F(3, 4)**d/(i+1)**2 for i, d in enumerate(distances)]
        weighted_blocks = [F(4, 3)**d*b for d, b in zip(distances, blocks)]
        weighted_ell1 = sum(weighted_blocks)
        weighted_ell2_squared = sum(b*b for b in weighted_blocks)
        require(weighted_ell2_squared <= weighted_ell1**2, 'weighted block-ell1 implies the requested weighted ell2 bound')
        count += 1
    counts['weighted_localization_packets'] = count
    require(counts == contract['frozen_coverage'], 'preregistered finite coverage')
    previous_path = BASE+'results/yang-mills-probe-coupled-transport-v1.json'
    previous = json.loads((ROOT/previous_path).read_text(encoding='utf-8'))
    require(previous['passed'] and previous['written_native_common_noise_map_transport'], 'retain candidate predecessor disposition')
    require(all(sha256((ROOT/p).read_bytes()).hexdigest() == h for p, h in previous['input_sha256'].items()), 'frozen predecessor evidence unchanged')
    paths = [CONTRACT, NOTE, PACKET, SELF, previous_path]
    paths += [BASE+name for name in [
        'yang-mills-uniform-detection-v1.md', 'yang-mills-ground-state-transfer-v1.md',
        'yang-mills-propagator-comparison-v1.md', 'yang-mills-probe-quasilocal-v1.md',
        'yang-mills-probe-pointwise-core-v1.md', 'yang-mills-probe-strong-noise-v1.md',
        'yang-mills-probe-coupled-transport-v1.md']]
    return {
        'schema': 'marici.yang-mills-physical-scaling-obstruction.result.v1',
        'passed': True,
        'strength': 'written conditional divergent-gap/two-time obstruction with exact finite controls; source gap,matching and continuum hypotheses remain inputs',
        'coverage': counts,
        'g_fourth_strict_floor': str(g4_floor),
        'physical_gap_coefficient': '40/sqrt(27)',
        'physical_gap_coefficient_squared': str(gap_coefficient_squared),
        'late_normalization_earlier_correlation_n12': str(2**12),
        'late_normalization_later_correlation': '1',
        'changed_clock_fixed_positive_correlation': '1/2',
        'hidden_mode_form_defect_n2': '-1',
        'finite_controls_certify_source_or_continuum_theorem': False,
        'external_bibliography_independently_verified': False,
        'review_packet_dispatched': False,
        'frozen_predecessor_input_digests_unchanged': True,
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    result = report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2))
