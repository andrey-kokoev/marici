"""Record the next incomplete half-turn attempt, preserving the earlier receipt."""
from pathlib import Path
import json
from check_half_turn_coefficients import REPO, ROOT, digest


def main():
    names = ['TickDenseTrigCutoffs-fresh', 'TickOperationalTrigResidual-cached', 'TickOperationalTrigResidual-fresh']
    receipts = {name: json.loads((ROOT / 'results' / (name + '.json')).read_text(encoding='utf-8')) for name in names}
    assert [receipts[name]['status'] for name in names] == ['pass', 'pass', 'timeout']
    pins = {}
    for name, receipt in receipts.items():
        assert receipt['completion_unit_norm_proved'] is False
        for path, expected in {**receipt['source_sha256'], **receipt['external_dependency_sha256']}.items():
            assert digest(REPO / path) == expected, 'stale proof evidence: ' + path
        pins.update(receipt['source_sha256'])
        path = 'research/nima/results/' + name + '.json'
        pins[path] = digest(REPO / path)
    path = Path(__file__).resolve().relative_to(REPO).as_posix()
    pins[path] = digest(REPO / path)
    note = 'research/nima/operational-trig-residual-progress.md'
    pins[note] = digest(REPO / note)
    result = {
        'schema': 'marici.nima.operational-unitary-half-turn-attempt.v1',
        'status': 'incomplete_proof_attempt', 'claim': 'operational-unitary-half-turn',
        'scope_id': 'operational-TickCompletionPhase-standard-pi-unitary-half-turn',
        'intent': 'prove', 'outcome': '+-', 'full_claim_proved': False, 'full_claim_refuted': False,
        'previous_attempt': 'research/nima/results/operational-unitary-half-turn-attempt.json',
        'freshly_proved': 'Dense cosine/sine sums at degree 2N+1 equal the actual operational partial sums at index N.',
        'cached_dependency_check_only': 'For every fixed rational q, the actual partial-sum norm defect is the sum of two generic triangular residuals and is bounded by K(q)*precision(N). A constructed offset gives precision(n) at offset+n.',
        'fresh_residual_check': 'Timeout after 600 seconds rebuilding dependencies; last logged module CompletionUnaryDescent.',
        'remaining_mathematics': ['uniform norm-defect modulus on bounded moving rational inputs, or fixed-rational-to-completion approximation transport', 'instantiate ScheduledNormBound and its quotient transfer', 'identified completion pi and half-turn endpoints', 'metric continuity and derivative of the implemented phase'],
        'remaining_verification': ['fresh closure of the residual and subsequent completion theorems'],
        'coefficient_and_residual_receipts': ['research/nima/results/' + name + '.json' for name in names],
        'source_sha256': dict(sorted(pins.items())),
    }
    (ROOT / 'results/operational-unitary-half-turn-residual-attempt.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'source_sha256'}, indent=2))

if __name__ == '__main__':
    main()
