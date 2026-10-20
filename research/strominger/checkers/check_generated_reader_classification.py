"""Fresh generated-fragment classification and exact old-witness regression."""
from pathlib import Path
import hashlib
import itertools
import json
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
OUT = BASE / 'results/generated-reader-classification'
OUT.mkdir(parents=True, exist_ok=True)
EXE = shutil.which('agda')
LIB = Path.home() / 'tools/cubical-agda/cubical-0.9'
assert EXE and LIB.is_dir()
PRIM = Path(subprocess.check_output([EXE, '--print-agda-dir'], text=True).strip()) / 'lib/prim'
assert PRIM.is_dir()
roots = {'repo-strominger': BASE / 'agda', 'repo-nima': ROOT / 'research/nima/agda',
         'cubical': LIB, 'agda-primitive': PRIM}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inventory():
    entries = {}
    for label, folder in roots.items():
        for pattern in ('*.agda', '*.lagda.md', '*.lagda.rst', '*.agda-lib'):
            for p in folder.rglob(pattern):
                entries[label + '/' + p.relative_to(folder).as_posix()] = sha(p)
    return entries


before = inventory()
modules = [BASE / ('agda/' + m + '.agda') for m in
           ('GeneratedReaderClassification', 'GeneratedReaderClassificationRegression')]
negatives = [BASE / ('agda/negative/' + m + '.agda') for m in
             ('ReaderClassificationBadPrepared', 'ReaderClassificationBadExistence', 'ReaderClassificationBadRawCollapse')]
sources = modules + negatives + [Path(__file__).resolve()] + [BASE / ('agda/' + m + '.agda') for m in
          ('InternalSourceComparisons', 'InternalComparisonInterchange', 'NativeExtensionFamilyAudit',
           'SourceIndexedExtensionFamilies', 'RepeatedInterchangeCoherence', 'InterchangeHiddenFiberObstruction')]
hashes = {p.relative_to(ROOT).as_posix(): sha(p) for p in sources}
common = [EXE, '--transliterate', '--no-libraries', '--safe', '--cubical', '--guardedness',
          '--no-import-sorts', '-i', str(BASE / 'agda'), '-i', str(ROOT / 'research/nima/agda'), '-i', str(LIB)]
command = common + ['--ignore-interfaces', str(modules[1])]
start = time.monotonic()
positive = subprocess.run(command, capture_output=True, text=True, timeout=300)
log = positive.stdout + positive.stderr
(OUT / 'positive.log').write_text(log, encoding='utf-8')
assert positive.returncode == 0 and not any(s in log for s in ('Unsolved', 'error:')), log[-6000:]
warnings = sorted(set(line for line in log.splitlines() if 'warning:' in line))
assert all(line.lower().startswith(str(LIB).lower()) and 'UnsupportedIndexedMatch' in line
           for line in warnings), warnings
controls = []
for p in negatives:
    cmd = common + ['-i', str(BASE / 'agda/negative'), str(p)]
    run = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    diagnostic = run.stdout + run.stderr
    (OUT / (p.stem + '.log')).write_text(diagnostic, encoding='utf-8')
    assert run.returncode != 0 and 'UnequalTerms' in diagnostic, diagnostic[-5000:]
    controls.append({'module': p.stem, 'command': cmd, 'exit': run.returncode,
                     'diagnostic': diagnostic.strip()})
# Finite shadow of the inductive theorem, not its proof. Images retain vertex
# labels and are not identified merely because they have equal cardinality.
vertices = set('ABCD')
edges = ['AB', 'BC', 'CA', 'BA', 'AD', 'DB']
images = {'whole': vertices, **{'out-' + v: {e[1] for e in edges if e[0] == v} for v in 'ABCD'}}
assert len({frozenset(s) for s in images.values()}) == 5
sigma = dict(zip('ABCD', 'BADC'))
rows = []
for mode, (a, x), (b, y) in itertools.product(('stay', 'exchange'), images.items(), images.items()):
    moved = x if mode == 'stay' else {sigma[v] for v in x}
    candidates = []
    for values in itertools.permutations(sorted(y), len(x)):
        f = dict(zip(sorted(x), values))
        if set(values) == y and all(f[v] == (v if mode == 'stay' else sigma[v]) for v in x):
            candidates.append(f)
    assert len(candidates) == int(moved == y)
    rows.append({'mode': mode, 'source': a, 'target': b, 'compatible_maps': len(candidates)})
assert len(images['out-A']) == len(images['out-B']) and images['out-A'] != images['out-B']
assert 'A' in images['whole'] & images['out-C'] and images['whole'] != images['out-C']
assert inventory() == before, 'Source inputs changed during closure'
assert all(sha(ROOT / p) == h for p, h in hashes.items())
lock = {'scope': 'Complete declared include-root and primitive-source inventory; conservative superset, not an exact import graph',
        'implicit_libraries_disabled': True, 'roots': {k: str(v) for k, v in roots.items()},
        'agda_version': subprocess.check_output([EXE, '--version'], text=True).strip(),
        'agda_executable': EXE, 'agda_executable_sha256': sha(Path(EXE)), 'sources': before}
manifest = OUT / 'dependency-manifest.json'
manifest.write_text(json.dumps(lock, indent=2) + '\n', encoding='utf-8')
report = {'status': 'pass', 'fresh_agda_exit': positive.returncode, 'command': command,
          'elapsed_seconds': round(time.monotonic() - start, 3), 'source_hashes': hashes,
          'dependency_manifest': manifest.relative_to(ROOT).as_posix(),
          'dependency_manifest_sha256': sha(manifest), 'locked_source_files': len(before),
          'dependency_warnings': warnings, 'repository_source_warnings': [], 'negative_controls': controls,
          'reader_images': {k: sorted(v) for k, v in images.items()}, 'finite_classification': rows,
          'formal_results': ['Inductive Fragment erases to unchanged Body with actual native input histories',
                             'Every generated carrier normalizes reader-preservingly to Vertex or Out(v)',
                             'Readers are embeddings and their exact images are proposition-valued',
                             'Complete compatible filler type is equivalent to mode-transported image agreement',
                             'Compatible fillers are propositions and contractible when inhabited',
                             'Native comparisons and their dependent coherence use actual operand derivations',
                             'One-comparison/two-attachment previous Bodies and higher witness recovered exactly',
                             'Same selected point can have no compatible filler',
                             'An unrestricted prepared constant reader is not injective despite unchanged native seeds'],
          'scope': ['Only the explicitly generated source-pointed/attachment/comparison fragment',
                    'No claim that arbitrary Body, Resolve or raw history types are sets or contractible',
                    'No unconditional filler existence or source-mode higher-action theorem',
                    'ImageAgreement and comparison parameters are not yet supplied by a certified decision compiler',
                    'No new native seed/rule or complete parameter-origin certification',
                    'No physical state count, global topology ceiling, or native admission of bare atomic fillers']}
(OUT / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'pass', 'fresh_agda_exit': positive.returncode,
                  'negative_exits': [c['exit'] for c in controls], 'locked_source_files': len(before),
                  'finite_image_cases': len(rows)}))
