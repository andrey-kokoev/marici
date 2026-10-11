"""Check closed-order density and the bounded all-completion-input residual estimate."""
import argparse
import json
from pathlib import Path
import subprocess
import time
from check_half_turn_coefficients import ROOT, REPO, AGDA, SEARCH, closure, digest

MODULE = 'TickCompletionRelativeBound'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--timeout', type=int, default=2400)
    args = parser.parse_args()
    files = closure(ROOT / 'agda' / (MODULE + '.agda')) | {Path(__file__).resolve(), ROOT / 'checkers/check_half_turn_coefficients.py'}
    before = {p: digest(p) for p in files}
    compiler_before = digest(AGDA)
    command = [str(AGDA), '--safe', '--cubical', '--guardedness', '--transliterate']
    if not args.cached:
        command.append('--ignore-interfaces')
    for path in SEARCH:
        command.extend(['-i', str(path)])
    command.append(str(ROOT / 'agda' / (MODULE + '.agda')))
    started = time.monotonic()
    try:
        run = subprocess.run(command, capture_output=True, timeout=args.timeout)
        output, code = run.stdout + run.stderr, run.returncode
    except subprocess.TimeoutExpired as error:
        output, code = (error.stdout or b'') + (error.stderr or b''), None
    stable = all(digest(p) == h for p, h in before.items()) and digest(AGDA) == compiler_before
    status = 'pass' if code == 0 and stable else ('timeout' if code is None else 'fail')
    fresh = status == 'pass' and not args.cached
    stem = 'completion-relative-bound-' + ('cached' if args.cached else 'fresh')
    (ROOT / 'results' / (stem + '.log')).write_bytes(output)
    result = {
        'schema': 'marici.nima.completion-relative-bound-result.v1',
        'status': status, 'claim': 'completion-phase-metric-regularity',
        'scope_id': 'operational-completion-phase-metric-calculus',
        'component': 'bounded-completion-relative-bound', 'outcome': None, 'attempt_state': 'in_progress',
        'module': MODULE, 'exit_code': code, 'command': command,
        'elapsed_seconds': round(time.monotonic()-started, 3), 'timeout_seconds': args.timeout,
        'fresh_dependency_check': not args.cached, 'fresh_closure_completed': fresh,
        'sources_stable': stable, 'compiler_sha256': compiler_before,
        'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
        'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
        'theorems': ['completion-limit-nonnegative', 'completion-limit-order', 'joint-continuous-order-limit',
                     'bounded-rational-order-density', 'square-limit', 'norm-limit', 'bounded-completion-relative-bound'],
        'bounded_completion_relative_bound_freshly_proved': fresh,
        'completion_valued_scales_and_increments': True,
        'explicit_radius_budget_and_eventual_bounds_required': True,
        'dyadic_modulus_constructed': False, 'local_derivative_bound_proved': False,
        'derivative_proved': False, 'full_metric_regularity_proved': False, 'unitary_half_turn_proved': False,
        'remaining_obligation': 'Choose the dyadic modulus, recover eventual representative bounds from the completion ball, and identify localResidualNorm with the origin-reduction residual.',
        'boundary': 'Operational all-completion-input bound under explicit radius budgets and eventual representative bounds; not yet the quantified derivative modulus.',
    }
    (ROOT / 'results' / (stem + '.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'elapsed_seconds', 'bounded_completion_relative_bound_freshly_proved',
                                            'derivative_proved', 'outcome')}, indent=2), flush=True)
    raise SystemExit(0 if status == 'pass' else 1)


if __name__ == '__main__':
    main()
