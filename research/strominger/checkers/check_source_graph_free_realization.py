"""Fresh closure for the reused six-edge realization and its bouquet comparison."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import re
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
OUT = BASE / 'results/source-graph-free-realization'
OUT.mkdir(parents=True, exist_ok=True)
EXE = shutil.which('agda')
LIB = Path.home() / 'tools/cubical-agda/cubical-0.9'
assert EXE and LIB.is_dir()
PRIM = Path(subprocess.check_output([EXE, '--print-agda-dir'], text=True).strip()) / 'lib/prim'
roots = {**{'repo-' + owner: ROOT / ('research/' + owner + '/agda')
            for owner in ('strominger', 'nima', 'voevodsky', 'grothendieck')},
         'cubical': LIB, 'agda-primitive': PRIM}

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def inventory():
    return {label + '/' + p.relative_to(folder).as_posix(): sha(p)
            for label, folder in roots.items()
            for pattern in ('*.agda', '*.lagda.md', '*.lagda.rst', '*.agda-lib')
            for p in folder.rglob(pattern)}

contract_path = BASE / 'contracts/source-graph-free-realization.v1.json'
contract = json.loads(contract_path.read_text(encoding='utf-8'))
assert all(v is False for v in contract['scope_guards'].values())
module = BASE / 'agda/SourceGraphFreeRealization.agda'
negatives = [BASE / ('agda/negative/' + name + '.agda') for name in
             ('GraphBadEraseChord', 'GraphBadFillABC', 'GraphBadEndpointRetraction')]
sources = [module, contract_path, Path(__file__).resolve(), *negatives,
           *[ROOT / p for p in contract['predecessors']]]
hashes = {p.relative_to(ROOT).as_posix(): sha(p) for p in sources}
before = inventory()
common = [EXE, '--transliterate', '--no-libraries', '--safe', '--cubical',
          '--guardedness', '--no-import-sorts']
for label, folder in roots.items():
    if label != 'agda-primitive':
        common += ['-i', str(folder)]
command = common + ['--ignore-interfaces', str(module)]
start = time.monotonic()
positive = subprocess.run(command, capture_output=True, text=True, timeout=600)
log = positive.stdout + positive.stderr
(OUT / 'positive.log').write_text(log, encoding='utf-8')
assert positive.returncode == 0 and not any(s in log for s in ('Unsolved', 'error:')), log[-7000:]
warnings = sorted(set(line for line in log.splitlines() if 'warning:' in line))
known_repository_warning = str(ROOT / 'research/nima/agda/TypedGeneratorLayers.agda') + ':7.41-62: warning: -W[no]ModuleDoesntExport'
assert all((line.lower().startswith(str(LIB).lower()) and 'UnsupportedIndexedMatch' in line)
           or line == known_repository_warning for line in warnings), warnings
repository_warnings = [line for line in warnings if line == known_repository_warning]
controls = []
for p in negatives:
    cmd = common + ['-i', str(BASE / 'agda/negative'), str(p)]
    run = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    diagnostic = run.stdout + run.stderr
    (OUT / (p.stem + '.log')).write_text(diagnostic, encoding='utf-8')
    assert run.returncode != 0 and 'UnequalTerms' in diagnostic, diagnostic[-5000:]
    controls.append({'module': p.stem, 'exit': run.returncode, 'command': cmd,
                     'diagnostic': diagnostic.strip()})

# Independent finite cellular shadow, parsed from the predecessor endpoint table.
text = (ROOT / contract['predecessors'][0]).read_text(encoding='utf-8')
source = dict(re.findall(r'^source (\w+) = (\w+)$', text, re.M))
target = dict(re.findall(r'^target (\w+) = (\w+)$', text, re.M))
edges = contract['relation_inventory']['occurrences']
vertices = contract['relation_inventory']['vertices']
assert set(source) == set(target) == set(edges)
assert all(source[e] + target[e] == e for e in edges)
boundary = [[int(target[e] == v) - int(source[e] == v) for e in edges] for v in vertices]

def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    pivot = 0
    for col in range(len(a[0])):
        found = next((i for i in range(pivot, len(a)) if a[i][col]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        scale = a[pivot][col]
        a[pivot] = [x / scale for x in a[pivot]]
        for i in range(len(a)):
            if i != pivot:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[pivot])]
        pivot += 1
    return pivot

cycles = [[1, 1, 1, 0, 0, 0], [-1, 0, 0, 1, 1, 0], [1, 0, 0, 0, 0, 1]]
assert rank(boundary) == 3 and rank(cycles) == 3
assert all(sum(x * y for x, y in zip(row, cycle)) == 0 for row in boundary for cycle in cycles)
# Chord coordinates form an integral identity matrix: primitive cycle basis.
assert [[cycle[edges.index(e)] for e in ('BC', 'DB', 'BA')] for cycle in cycles] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
assert len(edges) - rank(boundary) == 3
without_ba = [[x for e, x in zip(edges, row) if e != 'BA'] for row in boundary]
assert 5 - rank(without_ba) == 2
# Adjoining the two prohibited faces is a CHANGED presentation. These are
# rational H1 rank controls, not compiled HIT equivalences for the quotients.
assert 3 - rank(cycles[:2]) == 1
assert 3 - rank(cycles) == 0
assert inventory() == before, 'Declared source inventory changed during verification'
assert all(sha(ROOT / p) == h for p, h in hashes.items())
manifest = OUT / 'dependency-manifest.json'
manifest.write_text(json.dumps({'scope': 'Conservative complete include-root and primitive inventory, not exact imports',
    'implicit_libraries_disabled': True, 'roots': {k: str(v) for k, v in roots.items()},
    'agda_version': subprocess.check_output([EXE, '--version'], text=True).strip(),
    'agda_executable_sha256': sha(Path(EXE)), 'sources': before}, indent=2) + '\n', encoding='utf-8')
report = {'status': 'pass', 'fresh_agda_exit': positive.returncode, 'command': command,
          'elapsed_seconds': round(time.monotonic() - start, 3), 'source_hashes': hashes,
          'dependency_manifest': manifest.relative_to(ROOT).as_posix(),
          'dependency_manifest_sha256': sha(manifest), 'locked_source_files': len(before),
          'dependency_warnings': [w for w in warnings if w not in repository_warnings],
          'repository_source_warnings': repository_warnings,
          'repository_warning_explanation': 'Retained predecessor TypedGeneratorLayers imports unused isPropIsContr from HLevels, which does not export it; no owner source changed.',
          'negative_controls': controls, 'formal_results': contract['new_formal_results'],
          'finite_cellular_shadow': {'edge_order': edges, 'boundary_matrix': boundary,
              'cycle_basis': cycles, 'H1_rank': 3, 'delete_BA_rank': 2,
              'adjoin_forward_and_ABC_faces_rank': 1, 'also_adjoin_reverse_AB_rank': 0,
              'quotient_HIT_equivalences_compiled': False},
          'scope_guards': contract['scope_guards']}
(OUT / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'pass', 'fresh_agda_exit': positive.returncode,
                  'negative_exits': [c['exit'] for c in controls], 'locked_source_files': len(before),
                  'cellular_H1_rank': 3}))
