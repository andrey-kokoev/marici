"""Verify operational parity alignment and the fixed-rational norm-defect modulus."""
import argparse
import json
from pathlib import Path
import subprocess
from check_half_turn_coefficients import ROOT, REPO, AGDA, SEARCH, closure, digest

MODULES = {
    'TickDenseTrigCutoffs': 'Dense cosine/sine sums through degree 2N+1 equal the actual operational partial sums through index N.',
    'TickOperationalTrigResidual': 'For every rational q, an explicit cutoff offset makes the actual partial-sum norm defect at offset+n bounded by precision(n).',
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--module', choices=list(MODULES))
    parser.add_argument('--timeout', type=int, default=600)
    args = parser.parse_args()
    passed = True
    for module in ([args.module] if args.module else list(MODULES)):
        source = ROOT / 'agda' / (module + '.agda')
        files = closure(source) | {Path(__file__).resolve(), ROOT / 'checkers/check_half_turn_coefficients.py'}
        before = {p: digest(p) for p in files}
        command = [str(AGDA), '--safe', '--cubical', '--guardedness', '--transliterate']
        if not args.cached:
            command.append('--ignore-interfaces')
        for path in SEARCH:
            command.extend(['-i', str(path)])
        command.append(str(source))
        try:
            run = subprocess.run(command, capture_output=True, timeout=args.timeout)
            output, code = run.stdout + run.stderr, run.returncode
        except subprocess.TimeoutExpired as error:
            output, code = (error.stdout or b'') + (error.stderr or b''), None
        stable = all(digest(p) == h for p, h in before.items())
        status = 'pass' if code == 0 and stable else ('timeout' if code is None else 'fail')
        stem = module + ('-cached' if args.cached else '-fresh')
        (ROOT / 'results' / (stem + '.log')).write_bytes(output)
        result = {
            'status': status, 'module': module, 'exit_code': code, 'command': command,
            'timeout_seconds': args.timeout, 'fresh_dependency_check': not args.cached,
            'sources_stable': stable, 'compiler_sha256': digest(AGDA),
            'theorem_scope': MODULES[module],
            'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
            'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
            'fixed_rational_input': True, 'uniform_on_completion_input_schedule_proved': False,
            'completion_unit_norm_proved': False, 'unitary_half_turn_proved': False,
        }
        (ROOT / 'results' / (stem + '.json')).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        print(json.dumps({k: result[k] for k in ('module', 'status', 'fresh_dependency_check', 'theorem_scope')}), flush=True)
        passed &= status == 'pass'
    raise SystemExit(0 if passed else 1)

if __name__ == '__main__':
    main()
