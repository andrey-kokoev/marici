"""Fresh-check the exact origin reduction, not the remaining derivative estimate."""
import argparse
import json
from pathlib import Path
import subprocess
import time
from check_half_turn_coefficients import ROOT, REPO, AGDA, SEARCH, closure, digest

MODULE = 'TickPhaseDerivativeReduction'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--timeout', type=int, default=2400)
    args = parser.parse_args()
    source = ROOT / 'agda' / (MODULE + '.agda')
    files = closure(source) | {Path(__file__).resolve(), ROOT / 'checkers/check_half_turn_coefficients.py'}
    before = {p: digest(p) for p in files}
    compiler_before = digest(AGDA)
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
    stable = all(digest(p) == h for p, h in before.items()) and digest(AGDA) == compiler_before
    status = 'pass' if code == 0 and stable else ('timeout' if code is None else 'fail')
    fresh = status == 'pass' and not args.cached
    stem = 'phase-derivative-reduction-' + ('cached' if args.cached else 'fresh')
    (ROOT / 'results' / (stem + '.log')).write_bytes(output)
    result = {
        'schema': 'marici.nima.phase-derivative-reduction-result.v1',
        'status': status, 'claim': 'completion-phase-metric-regularity',
        'scope_id': 'operational-completion-phase-metric-calculus',
        'component': 'phase-derivative-origin-reduction',
        'outcome': None, 'attempt_state': 'in_progress',
        'module': MODULE, 'exit_code': code, 'command': command,
        'elapsed_seconds': round(time.monotonic()-started, 3), 'timeout_seconds': args.timeout,
        'fresh_dependency_check': not args.cached, 'fresh_closure_completed': fresh,
        'sources_stable': stable, 'compiler_sha256': compiler_before,
        'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
        'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
        'theorems': ['phase-remainder-factor', 'complex-norm-product', 'phase-remainder-norm-local',
                     'local-bound-to-phase-derivative', 'phase-derivative-to-local-bound',
                     'origin-derivative-to-all-times'],
        'all_completion_scales_times_and_increments': True,
        'origin_reduction_freshly_proved': fresh,
        'local_derivative_bound_proved': False,
        'derivative_proved': False, 'full_metric_regularity_proved': False,
        'unitary_half_turn_proved': False,
        'remaining_obligation': '(p : MetricCompletionCandidate) -> LocalPhaseDerivativeBound p',
        'boundary': 'Exact unit-norm rotation removes centre dependence. The completion-order estimate proportional to h squared remains open. This component is not a full derivative proof or an exhausted attempt.',
    }
    (ROOT / 'results' / (stem + '.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'elapsed_seconds', 'origin_reduction_freshly_proved',
                                            'derivative_proved', 'outcome')}, indent=2), flush=True)
    raise SystemExit(0 if status == 'pass' else 1)


if __name__ == '__main__':
    main()
