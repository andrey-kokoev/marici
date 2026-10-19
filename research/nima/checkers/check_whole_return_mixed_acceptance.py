"""Validate live pinned evidence and record the explicitly accepted mixed target."""
import json
from pathlib import Path
from check_half_turn_coefficients import REPO, ROOT, AGDA, digest, closure

ACCEPTANCE = 'research/nima/contracts/whole-return-mixed-level-acceptance.v1.json'
EVIDENCE = 'research/nima/results/standard-spectral-correspondence.json'
KERNEL = 'research/nima/results/operational-whole-return-kernel-fresh.json'


def main():
    acceptance = json.loads((REPO / ACCEPTANCE).read_text(encoding='utf-8'))
    assert acceptance['accepted'] is True and acceptance['operator_instruction'] == 'yes'
    assert acceptance['evidence'] == EVIDENCE
    assert acceptance['accepted_verification'] == {
        'operational_kernel_bundle_proved': True, 'standard_real_correspondence_written_proved': True,
        'semantic_correspondence_kernel_proved': False, 'C1_at_seam_claimed': False}
    pins, external = {}, {}
    evidence = json.loads((REPO / EVIDENCE).read_text(encoding='utf-8'))
    kernel = json.loads((REPO / KERNEL).read_text(encoding='utf-8'))
    assert evidence['status'] == 'pass' and evidence['fresh_closure_completed'] and evidence['sources_stable']
    assert evidence['written_semantic_correspondence_supplied'] and evidence['operational_kernel_bundle_proved']
    assert evidence['semantic_correspondence_kernel_proved'] is False
    assert evidence['additional_mixed_level_accepted'] is False and evidence['target_outcome'] is None
    assert kernel['status'] == 'pass' and kernel['fresh_closure_completed'] and kernel['sources_stable']
    assert kernel['operational_kernel_bundle_proved'] and kernel['whole_return_proved'] is False
    assert kernel['module'] == 'TickOperationalWholeReturnKernel'
    assert {'--safe', '--ignore-interfaces'} <= set(kernel['command'])
    for receipt in (evidence, kernel):
        assert receipt['compiler_sha256'] == digest(AGDA)
        for name, h in receipt['source_sha256'].items():
            assert digest(REPO / name) == h, 'stale evidence: ' + name
            pins[name] = h
        for name, h in receipt['external_dependency_sha256'].items():
            assert digest(Path(name)) == h, 'stale external evidence: ' + name
            external[name] = h
    for path in closure(ROOT / 'agda/TickOperationalWholeReturnKernel.agda'):
        if path.is_relative_to(REPO):
            assert pins[path.relative_to(REPO).as_posix()] == digest(path)
        else:
            assert external[str(path)] == digest(path)
    for path in (ACCEPTANCE, EVIDENCE, KERNEL, 'research/nima/checkers/check_whole_return_mixed_acceptance.py'):
        pins[path] = digest(REPO / path)
    external[str(AGDA)] = digest(AGDA)
    result = {
        'schema': 'marici.nima.whole-return-mixed-level-accepted-result.v1',
        'status': 'pass', 'claim': acceptance['claim'], 'scope_id': acceptance['scope_id'],
        'intent': 'prove', 'outcome': '++', 'acceptance': ACCEPTANCE, 'evidence': EVIDENCE,
        'kernel_receipt': KERNEL,
        'verification_level': 'operator-accepted mixed: fresh safe Agda whole operational record plus written all-time standard-real spectral interpretation',
        'operational_kernel_bundle_proved': True, 'standard_real_correspondence_written_proved': True,
        'semantic_correspondence_kernel_proved': False, 'mixed_level_accepted': True,
        'full_claim_proved_at_accepted_level': True, 'C1_at_seam_claimed': False,
        'remaining_obligations_at_accepted_level': [],
        'source_sha256': dict(sorted(pins.items())), 'external_dependency_sha256': dict(sorted(external.items())),
    }
    (ROOT / 'results/whole-return-mixed-level-accepted.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'claim', 'outcome', 'verification_level')}, indent=2))


if __name__ == '__main__':
    main()
