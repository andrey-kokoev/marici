"""Check exact Machin candidate endpoints, not identification with standard pi."""
import argparse
import json
import subprocess
from pathlib import Path
from check_half_turn_coefficients import AGDA, SEARCH, ROOT, REPO, closure, digest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timeout', type=int, default=1200)
    args = parser.parse_args()
    source = ROOT / 'agda/TickMachinEndpoints.agda'
    sources = closure(source) | {Path(__file__).resolve(), Path(__file__).with_name('check_half_turn_coefficients.py')}
    before = {p: digest(p) for p in sources}
    command = [str(AGDA), '--safe', '--cubical', '--guardedness', '--ignore-interfaces', '--transliterate']
    for path in SEARCH:
        command += ['-i', str(path)]
    command.append(str(source))
    try:
        run = subprocess.run(command, capture_output=True, timeout=args.timeout)
        output, code = run.stdout + run.stderr, run.returncode
    except subprocess.TimeoutExpired as error:
        output, code = (error.stdout or b'') + (error.stderr or b''), None
    stable = all(digest(p) == h for p, h in before.items())
    passed = code == 0 and stable
    result = {
        'schema': 'marici.nima.machin-endpoints-result.v1',
        'claim': 'completion-pi-half-turn', 'scope_id': 'operational-completion-standard-pi-half-turn',
        'component': 'machin-endpoints', 'module': source.stem,
        'status': 'pass' if passed else ('timeout' if code is None else 'fail'),
        'exit_code': code, 'command': command,
        'fresh_dependency_check': True, 'fresh_closure_completed': passed, 'sources_stable': stable,
        'outcome': None, 'attempt_state': 'in_progress',
        'rational_machin_gate_proved': passed, 'machin_endpoints_proved': passed,
        'machin_phase_half_turn_proved': passed,
        'standard_pi_identification_kernel_proved': False,
        'unitary_half_turn_proved': False, 'full_claim_proved': False,
        'theorems': ['rational-machin-gate', 'machin-endpoints', 'machin-phase-half-turn'],
        'remaining_obligations': ['standard-pi identification at the accepted formal level'],
        'compiler_sha256': digest(AGDA),
        'source_sha256': {p.relative_to(REPO).as_posix(): h for p, h in before.items() if p.is_relative_to(REPO)},
        'external_dependency_sha256': {str(p): h for p, h in before.items() if not p.is_relative_to(REPO)},
    }
    (ROOT / 'results/machin-endpoints-fresh.log').write_bytes(output)
    (ROOT / 'results/machin-endpoints-fresh.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ['status', 'fresh_closure_completed', 'machin_endpoints_proved',
                                         'machin_phase_half_turn_proved', 'standard_pi_identification_kernel_proved']}))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
