"""Bind the written all-time spectral interpretation to fresh operational closure.

The result never asserts kernel semantic correspondence or operator acceptance.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from check_half_turn_coefficients import ROOT, REPO, AGDA, closure, digest
from check_completion_refinement_net import CONTRACT, validate
from outcome_reference import load


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timeout', type=int, default=3600)
    args = parser.parse_args()
    validate(REPO, load(REPO, CONTRACT))
    pointer_path = ROOT / 'contracts/imports/standard-local-lift.pointer.v1.json'
    pointer = json.loads(pointer_path.read_text(encoding='utf-8'))
    exported = REPO / pointer['export']['path']
    assert digest(exported) == pointer['export']['sha256']
    pi_path = ROOT / 'results/pi-mixed-level-accepted.json'
    pi = json.loads(pi_path.read_text(encoding='utf-8'))
    assert pi['status'] == 'pass' and pi['mixed_level_accepted'] is True
    assert pi['standard_pi_identification_kernel_proved'] is False
    kernel_checker = ROOT / 'checkers/check_operational_whole_return_kernel.py'
    sources = closure(ROOT / 'agda/TickOperationalWholeReturnKernel.agda') | {
        Path(__file__).resolve(), ROOT / 'checkers/check_half_turn_coefficients.py', kernel_checker,
        ROOT / 'standard-spectral-correspondence.md', ROOT / 'standard-pi-identification.md',
        ROOT / 'uniform-local-core-proof.md', ROOT / 'spectral-whole-return-proof.md',
        pointer_path, exported, REPO / pointer['head'], pi_path,
    }
    for name, expected in pi['source_sha256'].items():
        path = REPO / name
        assert digest(path) == expected, 'stale pi evidence: ' + name
        sources.add(path)
    for name, expected in pi['external_dependency_sha256'].items():
        path = Path(name)
        assert digest(path) == expected, 'stale pi external evidence: ' + name
        sources.add(path)
    before = {p.resolve(): digest(p) for p in sources}
    compiler = digest(AGDA)
    command = [sys.executable, str(kernel_checker), '--timeout', str(args.timeout)]
    run = subprocess.run(command, capture_output=True, timeout=args.timeout + 120)
    kernel_path = ROOT / 'results/operational-whole-return-kernel-fresh.json'
    kernel = json.loads(kernel_path.read_text(encoding='utf-8')) if run.returncode == 0 else {}
    stable = all(digest(p) == h for p, h in before.items()) and digest(AGDA) == compiler
    fresh = run.returncode == 0 and stable and kernel.get('operational_kernel_bundle_proved') is True and kernel.get('fresh_closure_completed') is True
    stem = 'standard-spectral-correspondence'
    (ROOT / 'results' / (stem + '.log')).write_bytes(run.stdout + run.stderr)
    if fresh:
        before[kernel_path.resolve()] = digest(kernel_path)
    result = {
        'schema': 'marici.nima.standard-spectral-correspondence-result.v1',
        'status': 'pass' if fresh else 'fail',
        'verification_level': 'fresh safe Agda operational bundle plus written classical all-time interpretation',
        'command': command, 'exit_code': run.returncode, 'sources_stable': stable,
        'fresh_closure_completed': fresh, 'compiler_sha256': compiler,
        'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
        'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
        'written_semantic_correspondence_supplied': True,
        'operational_kernel_bundle_proved': fresh,
        'semantic_correspondence_kernel_proved': False,
        'additional_mixed_level_accepted': False,
        'whole_return_proved_at_admitted_level': False,
        'target_outcome': None,
        'remaining_admission_gate': 'explicit acceptance of this additional mixed verification level, or kernel semantic interpretation formalization',
        'boundary': 'Source/hash binding and fresh operational closure do not mechanically verify the written completeness/calculus proof. No target promotion or broader operator acceptance inferred.',
    }
    (ROOT / 'results' / (stem + '.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'fresh_closure_completed', 'semantic_correspondence_kernel_proved', 'additional_mixed_level_accepted', 'remaining_admission_gate')}, indent=2))
    raise SystemExit(0 if fresh else 1)


if __name__ == '__main__':
    main()
