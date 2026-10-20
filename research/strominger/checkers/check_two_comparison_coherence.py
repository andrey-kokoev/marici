"""Fresh 2-comparison/2-attachment closure, controls and conservative source lock."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
OUT = BASE / 'results/two-comparison-coherence'
OUT.mkdir(parents=True, exist_ok=True)
EXE = shutil.which('agda')
LIB = Path.home() / 'tools/cubical-agda/cubical-0.9'
assert EXE and LIB.is_dir()
DATA = Path(subprocess.check_output([EXE, '--print-agda-dir'], text=True).strip())
PRIM = DATA / 'lib/prim'
assert PRIM.is_dir(), PRIM
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
source_paths = [BASE / 'agda/TwoComparisonTwoAttachmentCoherence.agda',
                BASE / 'agda/TwoComparisonHigherAdmission.agda', Path(__file__).resolve()]
negatives = [BASE / ('agda/negative/' + name + '.agda') for name in
             ('TwoComparisonBadAtomicAdmission', 'TwoComparisonBadRawEquality', 'TwoComparisonBadFinalPort')]
source_paths += negatives
hashes = {p.relative_to(ROOT).as_posix(): sha(p) for p in source_paths}
common = [EXE, '--transliterate', '--no-libraries', '--safe', '--cubical',
          '--guardedness', '--no-import-sorts', '-i', str(BASE / 'agda'),
          '-i', str(ROOT / 'research/nima/agda'), '-i', str(LIB)]
command = common + ['--ignore-interfaces', str(source_paths[1])]
start = time.monotonic()
positive = subprocess.run(command, capture_output=True, text=True, timeout=300)
text = positive.stdout + positive.stderr
(OUT / 'positive.log').write_text(text, encoding='utf-8')
assert positive.returncode == 0, text[-6000:]
assert not any(s in text for s in ('Unsolved', 'error:')), text[-6000:]
# Disabling implicit libraries also exposes Cubical's normally suppressed
# indexed-match warnings. Record them; allow NONE in repository sources.
warnings = sorted(set(line for line in text.splitlines() if 'warning:' in line))
assert all(line.lower().startswith(str(LIB).lower()) and 'UnsupportedIndexedMatch' in line
           for line in warnings), warnings
controls = []
for p in negatives:
    cmd = common + ['-i', str(BASE / 'agda/negative'), str(p)]
    run = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
    diagnostic = run.stdout + run.stderr
    (OUT / (p.stem + '.log')).write_text(diagnostic, encoding='utf-8')
    assert run.returncode != 0 and 'UnequalTerms' in diagnostic, diagnostic
    controls.append({'module': p.stem, 'command': cmd, 'exit': run.returncode,
                     'diagnostic': diagnostic.strip()})
# Finite edge transport is a control, not an involution proof on native history.
sigma = dict(zip('ABCD', 'BADC'))
edges = ['AB', 'BC', 'CA', 'BA', 'AD', 'DB']
move = lambda e: ''.join(sigma[v] for v in e)
assert sorted(map(move, edges)) == sorted(edges)
assert all(move(move(e)) == e for e in edges)
assert [move(e) for e in ['AB', 'BC']] == ['BA', 'AD']
assert [move(e) for e in ['BA', 'AD']] == ['AB', 'BC']
assert inventory() == before, 'Source inventory changed during verification'
assert all(sha(ROOT / p) == h for p, h in hashes.items())
lock = {'scope': 'Complete declared include-root and primitive-source inventory; conservative superset, not an exact import graph',
        'implicit_libraries_disabled': True, 'roots': {k: str(v) for k, v in roots.items()},
        'agda_version': subprocess.check_output([EXE, '--version'], text=True).strip(),
        'agda_executable': EXE, 'agda_executable_sha256': sha(Path(EXE)),
        'sources': before}
lock_path = OUT / 'dependency-manifest.json'
lock_path.write_text(json.dumps(lock, indent=2) + '\n', encoding='utf-8')
result = {'status': 'pass', 'fresh_agda_exit': positive.returncode, 'command': command,
          'elapsed_seconds': round(time.monotonic() - start, 3),
          'dependency_manifest': lock_path.relative_to(ROOT).as_posix(),
          'dependency_manifest_sha256': sha(lock_path), 'locked_source_files': len(before),
          'dependency_warnings': warnings, 'repository_source_warnings': [],
          'source_hashes': hashes, 'negative_controls': controls,
          'diagram': {'source_comparisons': 2, 'source_attachments': 2,
                      'four_interchange_cells': ['R.First', 'R.Second', 'K', 'K2'],
                      'edges_before': ['AB', 'BC'], 'edges_between': ['BA', 'AD'],
                      'edges_after': ['AB', 'BC'], 'active_final_port': 'C',
                      'second_comparison': 'explicit inverse-facing graph comparison, not a second moveInitial'},
          'formal_results': ['Sequential and fused full equivalences with whole-carrier port laws',
                             'Complete-filler equality including selected-value and port witnesses',
                             'Dependent compatibility of native comparison histories',
                             'Native higher-path admission in a faithful E envelope and exact path recovery',
                             'Literal atomic higher-path package remains inadmissible',
                             'Raw Bodies and native derivations retained with exact payload recovery'],
          'scope': ['Fixed inverse-facing two-exchange control under the declared target-side policy',
                    'Local sethood and reader injectivity proved, not assumed universally',
                    'No arbitrary forward-history-lift composition law or general coherence induction',
                    'No source-free generation of supplied parameters or topology/physical claim']}
(OUT / 'verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'pass', 'fresh_agda_exit': positive.returncode,
                  'negative_exits': [c['exit'] for c in controls], 'locked_source_files': len(before)}))
