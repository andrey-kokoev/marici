"""Fresh constructive global spectral path on the external completion interval."""
import argparse
import json
import subprocess
import time
from pathlib import Path
from check_half_turn_coefficients import ROOT, REPO, AGDA, SEARCH, closure, digest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--timeout', type=int, default=3600)
    args = parser.parse_args()
    source = ROOT / 'agda/TickSpectralGlobalPath.agda'
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
        code, output = run.returncode, run.stdout + run.stderr
    except subprocess.TimeoutExpired as error:
        code, output = None, (error.stdout or b'') + (error.stderr or b'')
    stable = all(digest(p) == h for p, h in before.items()) and digest(AGDA) == compiler
    status = 'pass' if code == 0 and stable else ('timeout' if code is None else 'fail')
    fresh = status == 'pass' and not args.cached
    stem = 'spectral-global-path-' + ('cached' if args.cached else 'fresh')
    (ROOT / 'results' / (stem + '.log')).write_bytes(output)
    result = {
        'schema': 'marici.nima.spectral-global-path-result.v1',
        'status': status, 'module': 'TickSpectralGlobalPath',
        'command': command, 'exit_code': code, 'elapsed_seconds': round(time.monotonic()-started, 3),
        'fresh_dependency_check': not args.cached, 'fresh_closure_completed': fresh,
        'sources_stable': stable, 'compiler_sha256': compiler,
        'source_sha256': dict(sorted((p.relative_to(REPO).as_posix(), h) for p, h in before.items() if p.is_relative_to(REPO))),
        'external_dependency_sha256': dict(sorted((str(p), h) for p, h in before.items() if not p.is_relative_to(REPO))),
        'global_spectral_gluing_proved': fresh,
        'theorems': ['first-on-left', 'second-on-left', 'first-on-right', 'second-on-right',
                     'glued-metric-continuous', 'interval-path-continuous', 'glued-on-left', 'glued-on-right',
                     'interval-start', 'interval-finish', 'left-then-right-norm', 'right-then-left-norm'],
        'whole_return_proved': False, 'target_outcome': None,
        'boundary': 'Global positive-phase two-leg path on actual [0,2], metric continuity, exact closed-piece restrictions, operator endpoints and native-order norm preservation. Native source/retained-record binding, piecewise derivative transport and full exported-witness correspondence remain separate.',
    }
    (ROOT / 'results' / (stem + '.json')).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: result[k] for k in ('status', 'elapsed_seconds', 'fresh_closure_completed', 'whole_return_proved')}, indent=2))
    raise SystemExit(0 if status == 'pass' else 1)


if __name__ == '__main__':
    main()
