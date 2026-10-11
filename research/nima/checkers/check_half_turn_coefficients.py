"""Headless checks for finite algebra used in the half-turn proof attempt."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
LIB = Path(os.environ.get('NIMA_CUBICAL', str(Path.home() / 'tools/cubical-agda/cubical-0.9')))
AGDA = Path(os.environ.get('NIMA_AGDA', str(Path.home() / 'tools/cubical-agda/agda-2.8.0/agda.exe')))
SEARCH = [ROOT / 'agda', REPO / 'research/voevodsky/agda', LIB]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def closure(source):
    seen = set()
    todo = [source]
    while todo:
        path = todo.pop().resolve()
        if path in seen:
            continue
        seen.add(path)
        text = path.read_text(encoding='utf-8-sig')
        for name in re.findall(r'\bimport\s+([\w.]+)', text):
            relative = Path(*name.split('.')).with_suffix('.agda')
            matches = [p / relative for p in SEARCH if (p / relative).is_file()]
            if matches:
                todo.append(matches[0])
    return seen

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cached', action='store_true')
    parser.add_argument('--module', choices=['TickBinomialLeibniz', 'TickNormalizedTrigConvolution'])
    parser.add_argument('--timeout', type=int, default=300)
    args = parser.parse_args()
    modules = [args.module] if args.module else ['TickBinomialLeibniz', 'TickNormalizedTrigConvolution']
    passed = True
    for module in modules:
        source = ROOT / 'agda' / (module + '.agda')
        sources = closure(source) | {Path(__file__).resolve()}
        before = {p: digest(p) for p in sources}
        command = [str(AGDA), '--safe', '--cubical', '--guardedness', '--transliterate']
        if not args.cached:
            command.append('--ignore-interfaces')
        for path in SEARCH:
            command.extend(['-i', str(path)])
        command.append(str(source))
        try:
            run = subprocess.run(command, capture_output=True, timeout=args.timeout)
            output = run.stdout + run.stderr
            code = run.returncode
        except subprocess.TimeoutExpired as error:
            output = (error.stdout or b'') + (error.stderr or b'')
            code = None
        stable = all(digest(p) == h for p, h in before.items())
        status = 'pass' if code == 0 and stable else ('timeout' if code is None else 'fail')
        suffix = '-cached' if args.cached else '-fresh'
        stem = 'half-turn-' + module + suffix
        (ROOT / 'results' / (stem + '.log')).write_bytes(output)
        result = {
            'status': status, 'module': module, 'exit_code': code, 'command': command,
            'fresh_dependency_check': not args.cached, 'sources_stable': stable,
            'compiler_sha256': digest(AGDA),
            'source_sha256': {p.relative_to(REPO).as_posix(): h for p, h in before.items() if p.is_relative_to(REPO)},
            'external_dependency_sha256': {str(p): h for p, h in before.items() if not p.is_relative_to(REPO)},
            'theorem_scope': 'finite binomial/Leibniz identity' if module == 'TickBinomialLeibniz' else 'all-rational, all-degree normalized trigonometric Cauchy coefficient identity',
            'operational_unit_norm_proved': False, 'unitary_half_turn_proved': False,
        }
        (ROOT / 'results' / (stem + '.json')).write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        print(json.dumps({k: result[k] for k in ('module', 'status', 'fresh_dependency_check', 'unitary_half_turn_proved')}), flush=True)
        passed &= status == 'pass'
    raise SystemExit(0 if passed else 1)

if __name__ == '__main__':
    main()
