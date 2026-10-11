"""Check the unconditional operational norm theorem; fresh closure gates ++ admission."""
import argparse
import json
from pathlib import Path
import subprocess
import time
from check_half_turn_coefficients import ROOT, REPO, AGDA, SEARCH, closure, digest

MODULE = 'TickConstructedScheduledNorm'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--timeout', type=int, default=1800)
    args = parser.parse_args()
    source = ROOT / 'agda' / (MODULE + '.agda')
    files = closure(source) | {Path(__file__).resolve(), ROOT / 'checkers/check_half_turn_coefficients.py'}
    before = {p: digest(p) for p in files}
    command = [str(AGDA), '--safe', '--cubical', '--guardedness', '--transliterate']
    if not args.cached:
        command.append('--ignore-interfaces')
    for path in SEARCH:
        command.extend(['-i', str(path)])
    command.append(str(source))
    started = time.monotonic()
    try:
        run = subprocess.run(command, capture_output=True, timeout=args.timeout)
        output, code = run.stdout + run.stderr, run.returncode
    except subprocess.TimeoutExpired as error:
        output, code = (error.stdout or b'') + (error.stderr or b''), None
    elapsed = time.monotonic() - started
    stable = all(digest(p) == h for p, h in before.items())
    status = 'pass' if code == 0 and stable else ('timeout' if code is None else 'fail')
    fresh_pass = status == 'pass' and not args.cached
    stem = 'constructed-scheduled-norm-' + ('cached' if args.cached else 'fresh')
    (ROOT / 'results' / (stem + '.log')).write_bytes(output)
    result = {
        'schema': 'marici.nima.constructed-scheduled-norm-result.v1',
        'status': status, 'claim': 'completion-phase-unit-norm',
        'scope_id': 'operational-TickCompletionPhase-all-scale-all-time',
        'outcome': '++' if fresh_pass else None,
        'module': MODULE, 'exit_code': code, 'command': command,
        'timeout_seconds': args.timeout, 'elapsed_seconds': round(elapsed, 3),
        'fresh_dependency_check': not args.cached, 'fresh_closure_completed': fresh_pass,
        'sources_stable': stable, 'compiler_sha256': digest(AGDA),
        'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
        'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
        'theorems': ['constructed-eventual-controls', 'constructed-scheduled-norm-bound', 'operational-trig-unit-norm', 'operational-phase-unit-norm'],
        'norm_bound_is_assumed_input': False, 'uniform_on_bounded_moving_inputs': True,
        'kernel_checked_with_cached_dependencies': status == 'pass' and args.cached,
        'completion_unit_norm_freshly_proved': fresh_pass,
        'unitary_half_turn_proved': False,
        'remaining_half_turn_obligations': ['identified completion pi and its half-turn endpoints', 'metric continuity and derivative'],
    }
    (ROOT / 'results' / (stem + '.json')).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'outcome', 'fresh_closure_completed', 'elapsed_seconds', 'unitary_half_turn_proved')}, indent=2), flush=True)
    raise SystemExit(0 if status == 'pass' else 1)

if __name__ == '__main__':
    main()
