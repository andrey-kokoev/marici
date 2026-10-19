#!/usr/bin/env python3
"""Fresh shared-assembly elaboration, with expected rejection controls."""
import argparse
import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LOCAL = [ROOT / 'research/strominger/agda', ROOT / 'research/nima/agda']
CASES = {
    'RootedSpokeSharedAssembly': None,
    'RootedSpokeAssemblyBadErasure': 'false',
    'SpokeBadDirectedCompletion': 'A != B',
}


def closure(roots, includes):
    found = set()
    pending = list(roots)
    while pending:
        path = pending.pop().resolve()
        if path in found:
            continue
        found.add(path)
        for name in re.findall(r'\bimport\s+([\w.]+)', path.read_text(encoding='utf-8')):
            relative = Path(*name.split('.')).with_suffix('.agda')
            candidate = next((d / relative for d in includes if (d / relative).is_file()), None)
            if candidate:
                pending.append(candidate)
    return found


def name(path):
    return path.relative_to(ROOT).as_posix() if path.is_relative_to(ROOT) else path.as_posix()


def hashes(paths):
    return {name(p): hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agda', default=os.environ.get('AGDA', 'C:/Users/andrey/tools/cubical-agda/agda-2.8.0/agda.exe'))
    parser.add_argument('--cubical', default=os.environ.get('CUBICAL', 'C:/Users/andrey/tools/cubical-agda/cubical-0.9'))
    args = parser.parse_args()
    agda, cubical = Path(args.agda).resolve(), Path(args.cubical).resolve()
    paths = closure([LOCAL[0] / f'{m}.agda' for m in CASES], LOCAL + [cubical])
    paths.update([Path(__file__).resolve(), agda, cubical / 'cubical.agda-lib'])
    before = hashes(paths)
    flags = ['--transliterate', '--cubical', '--safe', '--guardedness', '--no-import-sorts',
             '--no-libraries', '--ignore-interfaces', '-WnoUnsupportedIndexedMatch']
    for include in LOCAL + [cubical]:
        flags += ['-i', str(include)]
    result_dir = ROOT / 'research/strominger/results'
    result_dir.mkdir(parents=True, exist_ok=True)
    executions, checks = {}, {}
    started = datetime.now(timezone.utc).isoformat()
    for module, diagnostic in CASES.items():
        command = [str(agda)] + flags + [str(LOCAL[0] / f'{module}.agda')]
        proc = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=300)
        log = proc.stdout.decode('utf-8', errors='replace')
        log_path = result_dir / f'{module}.log'
        log_path.write_text(log, encoding='utf-8')
        checks[module] = proc.returncode == 0 if diagnostic is None else (
            proc.returncode != 0 and diagnostic in log and f'{module}.agda:' in log
            and 'when checking' in log)
        executions[module] = {'command': command, 'returncode': proc.returncode,
                              'expected_success': diagnostic is None, 'diagnostic_required': diagnostic,
                              'log': name(log_path), 'log_sha256': hashlib.sha256(log_path.read_bytes()).hexdigest(),
                              'module_export_warning': 'ModuleDoesntExport' in log}
    checks['source_closure_unchanged'] = before == hashes(paths)
    out = {
        'schema': 'marici.strominger.rooted-spoke-shared-assembly.v1',
        'status': 'passed' if all(checks.values()) else 'failed',
        'started_utc': started, 'finished_utc': datetime.now(timezone.utc).isoformat(),
        'fresh_execution': True, 'ignore_interfaces': True,
        'checks': checks, 'executions': executions, 'source_hashes': before,
        'input': {'vertices': ['A', 'B', 'C', 'D'], 'primitive_occurrences': ['AB', 'AC', 'AD'],
                  'interpretation': 'free path realization: node constructors and three edge constructors; no face constructors'},
        'shared_calls': ['TableFibrationCycle.group-from/unpack', 'TableFibrationCycle.four',
                         'MarkedTetrahedronCoherence.unique123', 'RetainedTetrahedralPackage.Cells.build',
                         'RetainedTetrahedralPackage.Cells.WG.generate'],
        'output': {'structural_slots': {'vertices': 4, 'edges': 6, 'faces': 4, 'filler': 1},
                   'primitive_spokes_preserved': True, 'six_shared_edge_checks': True,
                   'request_recovered': True, 'ACD_face_and_filler_paired_agreement': True,
                   'primitive_occurrence_table_retained': True},
        'scope': 'Shared retained path/coherence assembly, not the metric facet assembler. No coordinates, metric, leaf symmetry, phase or proton coefficient protocol supplied.',
        'proton_comparison': 'Tetrahedral package shape agrees; full proton arrow/coefficient record equality is not established.',
    }
    (result_dir / 'rooted_spoke_shared_assembly.json').write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': out['status'], 'checks': checks, 'output': out['output']}, indent=2))
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
