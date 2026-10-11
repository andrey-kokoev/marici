"""Fresh operational half-turn closure plus the explicitly accepted pi identification."""
import argparse
import json
from pathlib import Path
import subprocess
import time
from check_half_turn_coefficients import ROOT, REPO, AGDA, SEARCH, closure, digest

MODULE = 'TickConstructedUnitaryHalfTurn'
PI_RECEIPT = 'research/nima/results/pi-mixed-level-accepted.json'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--timeout', type=int, default=3000)
    args = parser.parse_args()
    pi = json.loads((REPO / PI_RECEIPT).read_text(encoding='utf-8'))
    assert pi['status'] == 'pass' and pi['claim'] == 'completion-pi-half-turn' and pi['outcome'] == '++'
    assert pi['mixed_level_accepted'] is True and pi['standard_pi_identification_kernel_proved'] is False
    acceptance = json.loads((REPO / pi['acceptance']).read_text(encoding='utf-8'))
    assert acceptance['accepted'] and acceptance['operator_instruction'] == 'accept mixed-level certificate'
    source = ROOT / 'agda' / (MODULE + '.agda')
    before = {p: digest(p) for p in closure(source) | {Path(__file__).resolve(), ROOT / 'checkers/check_half_turn_coefficients.py'}}
    for p, h in pi['source_sha256'].items():
        assert digest(REPO / p) == h, 'stale pi evidence: ' + p
        before[REPO / p] = h
    for p, h in pi['external_dependency_sha256'].items():
        assert digest(Path(p)) == h, 'stale pi external evidence: ' + p
        before[Path(p)] = h
    before[REPO / PI_RECEIPT] = digest(REPO / PI_RECEIPT)
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
    stem = 'constructed-unitary-half-turn-' + ('cached' if args.cached else 'fresh')
    (ROOT / 'results' / (stem + '.log')).write_bytes(output)
    result = {
        'schema': 'marici.nima.constructed-unitary-half-turn-result.v1',
        'status': status, 'claim': 'operational-unitary-half-turn',
        'scope_id': 'operational-TickCompletionPhase-standard-pi-unitary-half-turn',
        'intent': 'prove', 'outcome': '++' if fresh else None,
        'module': MODULE, 'exit_code': code, 'command': command,
        'elapsed_seconds': round(time.monotonic()-started, 3),
        'fresh_dependency_check': not args.cached, 'fresh_closure_completed': fresh,
        'sources_stable': stable, 'compiler_sha256': compiler,
        'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
        'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
        'theorems': ['machin-start-law-definition', 'machin-finish-law-definition',
                     'OperationalMachinHalfTurn', 'operational-machin-half-turn'],
        'same_operational_phase_and_machin_candidate': True,
        'operational_half_turn_kernel_proved': fresh, 'unitary_half_turn_proved_at_accepted_level': fresh,
        'standard_pi_identification_kernel_proved': False, 'mixed_level_accepted': True,
        'pi_identification_receipt': PI_RECEIPT,
        'verification_level': 'fresh safe Agda operational norm/continuity/derivative/endpoints; operator-accepted written standard-pi identification',
        'whole_return_proved': False,
        'boundary': 'Closes the identified half-turn at the accepted mixed level, not a kernel standard-real interpretation or whole-return certificate.',
    }
    (ROOT / 'results' / (stem + '.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'elapsed_seconds', 'operational_half_turn_kernel_proved', 'outcome')}, indent=2))
    raise SystemExit(0 if status == 'pass' else 1)


if __name__ == '__main__':
    main()
