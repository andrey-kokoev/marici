"""Record this incomplete proof attempt without promoting finite algebra to completion."""
from pathlib import Path
import hashlib
import json

REPO = Path(__file__).resolve().parents[3]
ROOT = REPO / 'research/nima'

def main():
    names = ['half-turn-TickBinomialLeibniz-fresh',
             'half-turn-TickNormalizedTrigConvolution-cached',
             'half-turn-TickNormalizedTrigConvolution-fresh']
    receipts = {name: json.loads((ROOT / 'results' / (name + '.json')).read_text(encoding='utf-8')) for name in names}
    assert receipts[names[0]]['status'] == 'pass'
    assert receipts[names[1]]['status'] == 'pass'
    assert receipts[names[2]]['status'] == 'timeout'
    pins = {}
    for name, receipt in receipts.items():
        for path, expected in {**receipt['source_sha256'], **receipt['external_dependency_sha256']}.items():
            actual = hashlib.sha256((REPO / path).read_bytes()).hexdigest()
            assert actual == expected, 'stale coefficient evidence: ' + path
        pins.update(receipt['source_sha256'])
        path = 'research/nima/results/' + name + '.json'
        pins[path] = hashlib.sha256((REPO / path).read_bytes()).hexdigest()
    path = Path(__file__).resolve().relative_to(REPO).as_posix()
    pins[path] = hashlib.sha256((REPO / path).read_bytes()).hexdigest()
    result = {
        'schema': 'marici.nima.operational-unitary-half-turn-attempt.v1',
        'status': 'incomplete_proof_attempt', 'claim': 'operational-unitary-half-turn',
        'scope_id': 'operational-TickCompletionPhase-standard-pi-unitary-half-turn',
        'intent': 'prove', 'outcome': '+-', 'full_claim_proved': False, 'full_claim_refuted': False,
        'freshly_proved': 'Finite binomial convolution equals the recursive Leibniz product derivative; the cosine/sine norm coefficients cancel in every positive degree.',
        'cached_dependency_check_only': 'For every rational q, the dense factorial-normalized cosine/sine Cauchy-product norm coefficient is 1 at degree zero and 0 at every positive degree.',
        'fresh_normalized_check': 'Timeout at 300 seconds while rebuilding dependencies; last logged module ExponentialTailSchedule.',
        'remaining_mathematics': ['dense-to-operational parity/cutoff alignment', 'majorants, triangular residual estimates and completion transport', 'identified completion pi with half-turn endpoint laws', 'metric continuity and derivative of the implemented phase'],
        'remaining_verification': ['fresh closure of the normalized coefficient theorem and subsequent completion theorems'],
        'source_sha256': dict(sorted(pins.items())),
        'coefficient_receipts': ['research/nima/results/' + name + '.json' for name in names],
    }
    (ROOT / 'results/operational-unitary-half-turn-attempt.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, indent=2))

if __name__ == '__main__':
    main()
