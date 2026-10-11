"""Fresh Cubical check, matched negative controls and descriptive source counts.

Dependency-free Python. Override AGDA and CUBICAL_DIR for another installation.
No theorem is inferred from source counts or SCC classification.
"""
from pathlib import Path
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
OWNER = ROOT / 'research/voevodsky'
SOURCES = OWNER / 'agda'
RESULTS = OWNER / 'results'
TOOLS = Path.home() / 'tools/cubical-agda'
AGDA = Path(os.environ.get('AGDA', str(TOOLS / 'agda-2.8.0/agda.exe')))
LIB = Path(os.environ.get('CUBICAL_DIR', str(TOOLS / 'cubical-0.9')))
INCLUDES = [SOURCES, SOURCES / 'negative', ROOT / 'research/nima/agda',
            ROOT / 'research/nima/adapters/native-application',
            ROOT / 'research/nima/adapters/application-extension', LIB]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory():
    files = {p for directory in INCLUDES for p in directory.rglob('*.agda')}
    files.update([AGDA, Path(__file__).resolve()])
    return {str(p): digest(p) for p in sorted(files)}


def code_lines(path):
    # Counts physical nonblank, non-comment lines; not proof complexity or effort.
    return sum(bool(s.strip()) and not s.lstrip().startswith('--')
               for s in path.read_text(encoding='utf-8').splitlines())


def main():
    RESULTS.mkdir(exist_ok=True)
    before = inventory()
    version = subprocess.check_output([str(AGDA), '--version'], text=True).strip()
    flags = ['--safe', '--cubical', '--guardedness', '--transliterate', '--ignore-interfaces']
    for directory in INCLUDES:
        flags.extend(['-i', str(directory)])
    runs = []
    for name, relative, negative in [
        ('comparison', 'WGRefinementComparison.agda', False),
        ('library-comparison', 'WGRefinementLibraryComparison.agda', False),
        ('baseline-erasure', 'negative/WGRefinementBaselineBad.agda', True),
        ('library-erasure', 'negative/WGRefinementLibraryBad.agda', True),
        ('wg-erasure', 'negative/WGRefinementClientBad.agda', True),
    ]:
        command = [str(AGDA), *flags, str(SOURCES / relative)]
        run = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT, timeout=240)
        text = run.stdout.decode('utf-8', errors='replace')
        log = RESULTS / f'wg-refinement-{name}.log'
        log.write_text(text, encoding='utf-8')
        # Exit failure alone is insufficient: the intended type mismatch must appear.
        expected_mismatch = bool(re.search(r'false\s*!=\s*true|true\s*!=\s*false', text))
        passed = (run.returncode == 42 and expected_mismatch) if negative else run.returncode == 0
        runs.append({'name': name, 'command': command, 'exit_code': run.returncode,
                     'expected_rejection': negative, 'intended_mismatch': expected_mismatch,
                     'passed': passed, 'log': log.relative_to(ROOT).as_posix()})
    after = inventory()
    baseline = (SOURCES / 'WGRefinementBaseline.agda').read_text(encoding='utf-8')
    imports = re.findall(r'^\s*(?:open\s+)?import\s+(\S+)', baseline, flags=re.M)
    independent = bool(imports) and all(name.startswith('Cubical.') for name in imports)
    library_baseline = (SOURCES / 'WGRefinementLibraryBaseline.agda').read_text(encoding='utf-8')
    library_imports = re.findall(r'^\s*(?:open\s+)?import\s+(\S+)', library_baseline, flags=re.M)
    helper = (SOURCES / 'SigmaReassociation.agda').read_text(encoding='utf-8')
    helper_imports = re.findall(r'^\s*(?:open\s+)?import\s+(\S+)', helper, flags=re.M)
    library_independent = (bool(library_imports) and bool(helper_imports)
        and all(n.startswith('Cubical.') or n == 'SigmaReassociation' for n in library_imports)
        and all(n.startswith('Cubical.') for n in helper_imports))
    original_tests = (SOURCES / 'WGRefinementComparison.agda').read_text(encoding='utf-8')
    library_tests = (SOURCES / 'WGRefinementLibraryComparison.agda').read_text(encoding='utf-8')
    same_tests = library_tests == original_tests.replace('module WGRefinementComparison where',
        'module WGRefinementLibraryComparison where').replace('import WGRefinementBaseline as B',
        'import WGRefinementLibraryBaseline as B')
    passed = (before == after and independent and library_independent and same_tests
              and all(r['passed'] for r in runs))
    report = {
        'schema': 'marici.voevodsky.wg-refinement-comparison.v2',
        'checked_at': datetime.now(timezone.utc).isoformat(),
        'obligation': 'forward_realization_of_full_steps_and_source_reassociation',
        'stratum': 'fixed Boolean proof-dependent fixture; arbitrary inhabitants of its edge types',
        'passed': passed, 'compiler_version': version,
        'fresh': True, 'inputs_stable': before == after,
        'baseline_imports_only_cubical': independent,
        'library_baseline_independent_of_wg': library_independent,
        'comparison_tests_unchanged_except_module_names': same_tests, 'runs': runs,
        'physical_nonblank_noncomment_lines': {
            name: code_lines(SOURCES / f'{name}.agda') for name in
            ['WGRefinementBaseline', 'WGRefinementLibraryBaseline', 'SigmaReassociation',
             'WGRefinementClient', 'WGRefinementComparison', 'WGRefinementLibraryComparison']}, 
        'direct_generic_api_lines': code_lines(ROOT / 'research/nima/agda/ComposableWitnessSpecialization.agda'),
        'count_boundary': 'Includes imports/signatures. Library baseline reuses Cubical plus the separately counted SigmaReassociation helper; WG reuses its domain-specific API. Not a total-cost, effort or optimal-baseline metric.',
        'source_inventory_sha256': after,
        'nonverification': ['no performance benchmark', 'no claim of globally minimal glue',
                            'no four-layer pentagon or unit comparison', 'no general novelty theorem'],
    }
    output = RESULTS / 'wg-refinement-comparison.json'
    output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in report.items() if k not in ['source_inventory_sha256', 'runs']}, indent=2))
    for r in runs:
        print(f"{r['name']}: {'PASS' if r['passed'] else 'FAIL'} (compiler exit {r['exit_code']})")
    return 0 if passed else 1


if __name__ == '__main__':
    sys.exit(main())
