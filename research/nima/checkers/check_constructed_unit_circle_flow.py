"""Fresh kernel closure of the same-phase operational unit-circle-flow record."""
import argparse
import json
from pathlib import Path
import subprocess
import time
from check_half_turn_coefficients import ROOT, REPO, AGDA, SEARCH, closure, digest

MODULE = 'TickConstructedUnitCircleFlow'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--timeout', type=int, default=2400)
    args = parser.parse_args()
    source = ROOT / 'agda' / (MODULE + '.agda')
    before = {p: digest(p) for p in closure(source) | {Path(__file__).resolve(), ROOT / 'checkers/check_half_turn_coefficients.py'}}
    compiler = digest(AGDA)
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
    stable = all(digest(p) == h for p, h in before.items()) and digest(AGDA) == compiler
    status = 'pass' if code == 0 and stable else ('timeout' if code is None else 'fail')
    fresh = status == 'pass' and not args.cached
    stem = 'constructed-unit-circle-flow-' + ('cached' if args.cached else 'fresh')
    (ROOT / 'results' / (stem + '.log')).write_bytes(output)
    result = {
        'schema': 'marici.nima.constructed-unit-circle-flow-result.v1',
        'status': status, 'claim': 'completion-unit-circle-flow',
        'scope_id': 'operational-TickCompletionPhase-all-scale-all-time',
        'intent': 'prove', 'outcome': '++' if fresh else None,
        'module': MODULE, 'exit_code': code, 'command': command,
        'elapsed_seconds': round(time.monotonic()-started, 3),
        'fresh_dependency_check': not args.cached, 'fresh_closure_completed': fresh,
        'sources_stable': stable, 'compiler_sha256': compiler,
        'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
        'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
        'theorems': ['unit-norm-law-definition', 'regularity-law-definition',
                     'OperationalUnitCircleFlow', 'operational-unit-circle-flow'],
        'unit_circle_flow_proved': fresh, 'same_operational_phase': True,
        'all_completion_scales_times_and_increments': True,
        'norm_continuity_and_derivative_proved': fresh,
        'unitary_half_turn_proved': False,
        'boundary': 'The fixed operational phase has all three flow laws. Pi identification, half-turn endpoints and whole-return assembly are not supplied by this record.',
    }
    (ROOT / 'results' / (stem + '.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'elapsed_seconds', 'unit_circle_flow_proved', 'outcome')}, indent=2))
    raise SystemExit(0 if status == 'pass' else 1)


if __name__ == '__main__':
    main()
