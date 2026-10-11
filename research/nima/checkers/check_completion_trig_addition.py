"""Check operational completion sine/cosine and phase addition, not pi endpoints."""
import argparse
import json
from pathlib import Path
import subprocess
import time
from check_half_turn_coefficients import ROOT, REPO, AGDA, SEARCH, closure, digest

MODULE = 'TickPhaseComposition'
THEOREMS = [
    'multiplication-joint-continuous', 'close-limits-equal',
    'continuous-agree-on-rationals', 'rational-cosine-addition', 'rational-sine-addition',
    'completion-cosine-addition', 'completion-sine-addition',
    'operational-rotation-addition', 'operational-phase-addition',
]
REMAINING = [
    'operational arctangent/Cayley bridge',
    'standard-pi identification at the accepted formal level',
    'MachinEndpoints',
]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--timeout', type=int, default=1800)
    args = parser.parse_args()
    source = ROOT / 'agda' / (MODULE+'.agda')
    files = closure(source) | {Path(__file__).resolve(), ROOT/'checkers/check_half_turn_coefficients.py'}
    before = {p: digest(p) for p in files}
    compiler_before = digest(AGDA)
    command = [str(AGDA), '--safe', '--cubical', '--guardedness', '--transliterate']
    if not args.cached:
        command.append('--ignore-interfaces')
    for p in SEARCH:
        command.extend(['-i', str(p)])
    command.append(str(source))
    started = time.monotonic()
    try:
        run = subprocess.run(command, capture_output=True, timeout=args.timeout)
        output, code = run.stdout+run.stderr, run.returncode
    except subprocess.TimeoutExpired as error:
        output, code = (error.stdout or b'')+(error.stderr or b''), None
    stable = all(digest(p) == h for p, h in before.items()) and digest(AGDA) == compiler_before
    status = 'pass' if code == 0 and stable else ('timeout' if code is None else 'fail')
    fresh = status == 'pass' and not args.cached
    stem = 'completion-trig-addition-' + ('cached' if args.cached else 'fresh')
    (ROOT/'results'/(stem+'.log')).write_bytes(output)
    result = {
        'schema': 'marici.nima.completion-trig-addition-result.v1', 'status': status,
        'claim': 'completion-pi-half-turn', 'scope_id': 'operational-completion-standard-pi-half-turn',
        'component': 'completion-trig-addition',
        'component_scope_id': 'operational-completion-trig-addition-all-inputs',
        'outcome': None, 'attempt_state': 'in_progress',
        'module': MODULE, 'exit_code': code, 'command': command, 'timeout_seconds': args.timeout,
        'elapsed_seconds': round(time.monotonic()-started, 3),
        'fresh_dependency_check': not args.cached, 'fresh_closure_completed': fresh,
        'sources_stable': stable, 'compiler_sha256': compiler_before,
        'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
        'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
        'theorems': THEOREMS,
        'completion_addition_laws_proved': fresh,
        'phase_addition_law_proved': fresh,
        'all_completion_inputs': True, 'all_completion_scales_and_times': True,
        'uses_operational_sine_cosine_and_phase': True, 'assumed_addition_law': False,
        'arctangent_cayley_bridge_proved': False,
        'pi_endpoints_proved': False, 'standard_pi_identification_kernel_proved': False,
        'derivative_proved': False, 'unitary_half_turn_proved': False, 'full_claim_proved': False,
        'remaining_obligations': REMAINING,
        'boundary': 'Unconditional operational completion addition laws, not an arctangent/Cayley, derivative, standard-pi identification or endpoint certificate.',
    }
    (ROOT/'results'/(stem+'.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'elapsed_seconds', 'fresh_closure_completed',
                    'completion_addition_laws_proved', 'phase_addition_law_proved', 'pi_endpoints_proved', 'outcome')}, indent=2), flush=True)
    raise SystemExit(0 if status == 'pass' else 1)


if __name__ == '__main__':
    main()
