"""Freshly check the Machin input bridges and conditional endpoint reduction."""
import argparse
import json
import subprocess
from pathlib import Path
from check_half_turn_coefficients import AGDA, SEARCH, ROOT, REPO, closure, digest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timeout', type=int, default=1200)
    args = parser.parse_args()
    source = ROOT / 'agda/TickMachinEndpointReduction.agda'
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
        'schema': 'marici.nima.machin-endpoint-reduction-result.v1',
        'claim': 'completion-pi-half-turn',
        'scope_id': 'operational-completion-standard-pi-half-turn',
        'component': 'machin-endpoint-reduction',
        'module': source.stem,
        'status': 'pass' if passed else ('timeout' if code is None else 'fail'),
        'exit_code': code, 'command': command,
        'fresh_dependency_check': True, 'fresh_closure_completed': passed, 'sources_stable': stable,
        'outcome': None, 'attempt_state': 'in_progress',
        'machin_input_cayley_identities_proved': passed,
        'endpoint_reduction_proved': passed,
        'rational_machin_gate_proved': False,
        'pi_endpoints_proved': False,
        'standard_pi_identification_kernel_proved': False,
        'unitary_half_turn_proved': False, 'full_claim_proved': False,
        'theorems': ['fifth-completion-agreement', 'completion239-agreement',
                     'machin-fifth-cayley', 'machin239-cayley', 'machin-endpoints-from-rational'],
        'remaining_obligations': ['standard-pi identification at the accepted formal level', 'MachinEndpoints'],
        'next_gate': 'RationalMachinGate: square(square(Cayley(1/5))) = i*Cayley(1/239)',
        'compiler_sha256': digest(AGDA),
        'source_sha256': {p.relative_to(REPO).as_posix(): h for p, h in before.items() if p.is_relative_to(REPO)},
        'external_dependency_sha256': {str(p): h for p, h in before.items() if not p.is_relative_to(REPO)},
    }
    (ROOT / 'results/machin-endpoint-reduction-fresh.log').write_bytes(output)
    (ROOT / 'results/machin-endpoint-reduction-fresh.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ['status', 'fresh_closure_completed', 'machin_input_cayley_identities_proved',
                                         'endpoint_reduction_proved', 'pi_endpoints_proved']}))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
