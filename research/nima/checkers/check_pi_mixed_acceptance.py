"""Record operator-accepted mixed-level pi closure after live evidence validation."""
import json
from pathlib import Path
from check_completion_refinement_net import REPO, admit_written_pi_identification, admit_machin_endpoints, admit_machin_reference_series
from outcome_reference import load, file_hash, require

ACCEPTANCE = 'research/nima/contracts/pi-mixed-level-acceptance.v1.json'
OUT = REPO / 'research/nima/results/pi-mixed-level-accepted.json'


def main():
    acceptance = load(REPO, ACCEPTANCE)
    require(acceptance['accepted'] is True and acceptance['operator_instruction'] == 'accept mixed-level certificate',
            'explicit operator acceptance missing')
    require(acceptance['accepted_verification']['standard_pi_identification_kernel_proved'] is False,
            'mixed acceptance cannot promote kernel identification')
    node = {'id': acceptance['claim'], 'scope_id': acceptance['scope_id']}
    pins, external = {}, {}
    admit_written_pi_identification(REPO, node,
        {'id': 'standard-real-identification-written', 'receipt': acceptance['evidence']}, pins, external)
    admit_machin_endpoints(REPO, node,
        {'id': 'machin-endpoints', 'receipt': 'research/nima/results/machin-endpoints-fresh.json'}, pins, external)
    admit_machin_reference_series(REPO, node,
        {'id': 'machin-reference-series', 'receipt': 'research/nima/results/machin-reference-series-fresh.json'}, pins, external)
    pins[ACCEPTANCE] = file_hash(REPO, ACCEPTANCE)
    checker = 'research/nima/checkers/check_pi_mixed_acceptance.py'
    pins[checker] = file_hash(REPO, checker)
    result = {
        'schema': 'marici.nima.pi-mixed-level-accepted-result.v1',
        'claim': node['id'], 'scope_id': node['scope_id'], 'intent': 'prove', 'outcome': '++',
        'status': 'pass', 'acceptance': ACCEPTANCE, 'evidence': acceptance['evidence'],
        'verification_level': 'operator-accepted mixed: safe Agda construction/endpoints and written standard-real identification',
        'operational_endpoints_kernel_proved': True, 'standard_pi_identification_written_proved': True,
        'standard_pi_identification_kernel_proved': False, 'mixed_level_accepted': True,
        'full_claim_proved_at_accepted_level': True, 'unitary_half_turn_proved': False,
        'remaining_pi_obligations_at_accepted_level': [],
        'source_sha256': pins, 'external_dependency_sha256': external,
    }
    OUT.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'claim', 'outcome', 'verification_level')}))


if __name__ == '__main__':
    main()
