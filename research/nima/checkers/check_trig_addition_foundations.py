"""Fresh safe closure of addition coefficients, uniform defects and scalar transfer.

This checkpoint does NOT prove the completion-valued addition laws or pi endpoints.
"""
import argparse
from fractions import Fraction as F
import json
from math import factorial
from pathlib import Path
import subprocess
import time
from check_half_turn_coefficients import ROOT, REPO, AGDA, SEARCH, closure, digest

MODULE = 'TickTrigPartialSumTransfer'
THEOREMS = [
    'Rotation.cosine-add-index', 'Rotation.sine-add-index',
    'cosine-addition-coefficient', 'sine-addition-coefficient',
    'cosine-defect-is-residuals', 'sine-defect-is-residuals',
    'AtRadius.cosine-addition-all-later', 'AtRadius.sine-addition-all-later',
    'cosine-partial-sum-to-operational', 'sine-partial-sum-to-operational',
]
REMAINING = [
    'combine scalar partial-sum transfer with completion products and sums',
    'extend rational-input addition laws to all completion inputs',
    'operational arctangent/Cayley bridge',
    'standard-pi identification at the accepted formal level',
    'MachinEndpoints',
]


def cosine_term(q, n):
    return (1, 0, -1, 0)[n % 4] * q**n / factorial(n)


def sine_term(q, n):
    return (0, 1, 0, -1)[n % 4] * q**n / factorial(n)


def convolution(a, b, n):
    return sum((a(k)*b(n-k) for k in range(n+1)), F(0))


def exact_audit():
    """Finite regression audit only; all-degree and tail claims come from Agda."""
    inputs = [F(0), F(1, 5), F(1, 239), F(-1, 2), F(3, 2)]
    coefficient_cases = residual_cases = 0
    for x in inputs:
        for y in inputs:
            cx, sx = lambda n: cosine_term(x, n), lambda n: sine_term(x, n)
            cy, sy = lambda n: cosine_term(y, n), lambda n: sine_term(y, n)
            for k in range(13):
                if convolution(cx, cy, k)-convolution(sx, sy, k) != cosine_term(x+y, k):
                    raise ValueError('cosine addition coefficient mismatch')
                if convolution(sx, cy, k)+convolution(cx, sy, k) != sine_term(x+y, k):
                    raise ValueError('sine addition coefficient mismatch')
                coefficient_cases += 1
            for n in range(5):
                cutoff = 2*n+1
                def total(a):
                    return sum((a(k) for k in range(cutoff+1)), F(0))
                def residual(a, b):
                    return total(a)*total(b)-sum((convolution(a, b, k) for k in range(cutoff+1)), F(0))
                cosine_defect = total(cx)*total(cy)-total(sx)*total(sy)-total(lambda k: cosine_term(x+y, k))
                sine_defect = total(sx)*total(cy)+total(cx)*total(sy)-total(lambda k: sine_term(x+y, k))
                if cosine_defect != residual(cx, cy)-residual(sx, sy):
                    raise ValueError('cosine residual mismatch')
                if sine_defect != residual(sx, cy)+residual(cx, sy):
                    raise ValueError('sine residual mismatch')
                residual_cases += 1
    return {
        'status': 'pass', 'arithmetic': 'exact rational finite regression only',
        'input_pairs': len(inputs)**2, 'coefficient_cases': coefficient_cases,
        'residual_cases': residual_cases,
        'boundary': 'Not a sampled substitute for the kernel-checked all-degree or all-later-cutoff theorems.',
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--timeout', type=int, default=1800)
    args = parser.parse_args()
    audit = exact_audit()
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
    stem = 'trig-addition-foundations-' + ('cached' if args.cached else 'fresh')
    (ROOT/'results'/(stem+'.log')).write_bytes(output)
    result = {
        'schema': 'marici.nima.trig-addition-foundations-result.v1', 'status': status,
        'claim': 'completion-pi-half-turn', 'scope_id': 'operational-completion-standard-pi-half-turn',
        'component': 'trig-addition-foundations', 'outcome': None, 'attempt_state': 'in_progress',
        'module': MODULE, 'exit_code': code, 'command': command, 'timeout_seconds': args.timeout,
        'elapsed_seconds': round(time.monotonic()-started, 3),
        'fresh_dependency_check': not args.cached, 'fresh_closure_completed': fresh,
        'sources_stable': stable, 'compiler_sha256': compiler_before,
        'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
        'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
        'theorems': THEOREMS,
        'distinct_input_coefficients_freshly_proved': fresh,
        'uniform_addition_defect_decay_freshly_proved': fresh,
        'rational_partial_sum_transfer_freshly_proved': fresh,
        'all_later_cutoffs': True, 'uniform_on_bounded_input_pairs': True,
        'completion_addition_laws_proved': False, 'arctangent_cayley_bridge_proved': False,
        'pi_endpoints_proved': False, 'standard_pi_identification_kernel_proved': False,
        'unitary_half_turn_proved': False, 'full_claim_proved': False,
        'exact_arithmetic_audit': audit, 'remaining_obligations': REMAINING,
        'boundary': 'Distinct-input coefficient identities, uniform finite defects and scalar native-schedule transfer only. Composite completion addition and endpoints remain open.',
    }
    (ROOT/'results'/(stem+'.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'elapsed_seconds', 'fresh_closure_completed',
                    'completion_addition_laws_proved', 'pi_endpoints_proved', 'outcome')}, indent=2), flush=True)
    raise SystemExit(0 if status == 'pass' else 1)


if __name__ == '__main__':
    main()
