"""Check the convergent Machin candidate and audit rotation arithmetic; no endpoint promotion."""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import subprocess
import time
from check_half_turn_coefficients import ROOT, REPO, AGDA, SEARCH, closure, digest

MODULE = 'TickMachinPiEndpointContract'


def mul(z, w):
    a, b = z
    c, d = w
    return a*c-b*d, a*d+b*c


def power(z, n):
    result = (F(1), F(0))
    for _ in range(n):
        result = mul(result, z)
    return result


def cayley(q):
    return (1-q*q)/(1+q*q), 2*q/(1+q*q)


def partial(q, cutoff):
    term = total = q
    for n in range(cutoff):
        term *= -q*q*F(2*n+1, 2*n+3)
        total += term
    return total


def exact_audit(cutoff=40):
    a, b = F(1, 5), F(1, 239)
    r5, r239 = cayley(a), cayley(b)
    quarter = mul(power(r5, 4), (r239[0], -r239[1]))
    half = power(quarter, 2)
    if quarter != (0, 1) or half != (-1, 0):
        raise ValueError('Machin rotation arithmetic failed')
    for q in (a, b):
        expected = sum(((-1)**n * q**(2*n+1)/F(2*n+1) for n in range(cutoff+1)), F(0))
        if partial(q, cutoff) != expected:
            raise ValueError('series recurrence/odd-power sum mismatch')
    center = 16*partial(a, cutoff)-4*partial(b, cutoff)
    radius = F(20, 2**cutoff)
    if not 3 < center-radius < center+radius < 4:
        raise ValueError('Machin candidate enclosure failed')
    return {
        'status': 'pass', 'arithmetic': 'exact rational, no floating-point acceptance',
        'quarter_rotation': [str(x) for x in quarter], 'half_rotation': [str(x) for x in half],
        'cutoff': cutoff, 'candidate_center_rational': str(center), 'tail_radius_rational': str(radius),
        'candidate_inside_3_4_from_tail_estimate': True,
        'concrete_rotation_check_kind': 'Python Fraction audit; generic sibling-rotation identity is separately kernel-checked',
        'boundary': 'These are not evaluations or endpoint theorems for operational completion sine/cosine.',
    }


def main():
    parser = argparse.ArgumentParser()
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
    stem = 'machin-pi-candidate-' + ('cached' if args.cached else 'fresh')
    (ROOT/'results'/ (stem+'.log')).write_bytes(output)
    result = {
        'schema': 'marici.nima.machin-pi-candidate-result.v1', 'status': status,
        'claim': 'completion-pi-half-turn', 'scope_id': 'operational-completion-standard-pi-half-turn',
        'outcome': None, 'attempt_state': 'in_progress', 'module': MODULE,
        'exit_code': code, 'command': command, 'timeout_seconds': args.timeout,
        'elapsed_seconds': round(time.monotonic()-started, 3),
        'fresh_dependency_check': not args.cached, 'fresh_closure_completed': fresh,
        'sources_stable': stable, 'compiler_sha256': compiler_before,
        'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
        'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
        'theorems': ['atan-term-geometric', 'atan-segment-bound', 'atan-later-error', 'machin-pi-formula',
                     'Certificate.sibling-rotation', 'machin-endpoints-to-phase'],
        'convergent_machin_candidate_freshly_constructed': fresh,
        'assumed_arctangent_or_pi_constant': False,
        'pi_endpoints_proved': False, 'standard_pi_identification_kernel_proved': False,
        'unitary_half_turn_proved': False, 'full_claim_proved': False,
        'exact_arithmetic_audit': audit,
        'remaining_obligations': ['operational arctangent/Cayley bridge and angle composition',
                                  'standard-pi identification at the accepted formal level', 'MachinEndpoints'],
        'boundary': 'A construction checkpoint. Convergence and finite rotation arithmetic do not prove the operational endpoints.',
    }
    (ROOT/'results'/(stem+'.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'elapsed_seconds', 'fresh_closure_completed',
                    'convergent_machin_candidate_freshly_constructed', 'pi_endpoints_proved', 'outcome')}, indent=2), flush=True)
    raise SystemExit(0 if status == 'pass' else 1)

if __name__ == '__main__':
    main()
