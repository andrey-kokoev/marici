"""Fresh verification of the implemented forward lift's binary composition laws."""
from pathlib import Path
import hashlib
import itertools
import json
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
OUT = BASE / 'results/forward-source-lift-composition'
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
    files = {}
    for label, folder in roots.items():
        for pattern in ('*.agda', '*.lagda.md', '*.lagda.rst', '*.agda-lib'):
            for p in folder.rglob(pattern):
                files[label + '/' + p.relative_to(folder).as_posix()] = sha(p)
    return files


before = inventory()
module = BASE / 'agda/ForwardSourceLiftComposition.agda'
negatives = [BASE / ('agda/negative/' + name + '.agda') for name in
             ('ForwardLiftBadDefinitionalSquare', 'ForwardLiftBadReset', 'ForwardLiftBadReadyIdentity')]
sources = [module, Path(__file__).resolve(), BASE / 'agda/RetainedFeedbackCovariance.agda',
           BASE / 'agda/RetainedPackageFeedback.agda', BASE / 'agda/NativeExtensionFamilyAudit.agda',
           BASE / 'agda/SourceIndexedExtensionFamilies.agda',
           BASE / 'agda/InternalSourceComparisons.agda',
           ROOT / 'research/nima/agda/WholePackageResolution.agda',
           ROOT / 'research/nima/agda/WholePackageSigmaPi.agda'] + negatives
hashes = {p.relative_to(ROOT).as_posix(): sha(p) for p in sources}
common = [EXE, '--transliterate', '--no-libraries', '--safe', '--cubical', '--guardedness',
          '--no-import-sorts', '-i', str(BASE / 'agda'), '-i', str(ROOT / 'research/nima/agda'), '-i', str(LIB)]
command = common + ['--ignore-interfaces', str(module)]
start = time.monotonic()
positive = subprocess.run(command, capture_output=True, text=True, timeout=300)
log = positive.stdout + positive.stderr
(OUT / 'positive.log').write_text(log, encoding='utf-8')
assert positive.returncode == 0 and not any(s in log for s in ('Unsolved', 'error:')), log[-6000:]
# Cubical's library configuration normally suppresses these dependency
# warnings. The explicit closure run records them and rejects repository ones.
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
# Only a finite endpoint/edge regression: it is not the proof about Resolve.
sigma = dict(zip('ABCD', 'BADC'))
edges = ['AB', 'BC', 'CA', 'BA', 'AD', 'DB']
move_edge = lambda e: ''.join(sigma[x] for x in e)
assert all(move_edge(move_edge(e)) == e for e in edges)
act = lambda bit, v: sigma[v] if bit else v
for m, n, v in itertools.product((0, 1), (0, 1), 'ABCD'):
    assert act(m, act(n, v)) == act(m ^ n, v)
assert act(1, 'A') != 'A'
assert inventory() == before, 'Declared source inputs changed during verification'
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
          'dependency_warnings': warnings, 'repository_source_warnings': [],
          'negative_controls': controls,
          'formal_results': ['Chosen univalent pointed package path equals the inverse-facing path',
                             'Forward/backward initial transports agree for every actual Resolve input',
                             'Forward lift squared cancels on arbitrary indexed initial proofs',
                             'Forward/backward whole-chain maps agree; forward squared cancels on every finite retained chain',
                             'All four binary mode composition laws and their native closure images',
                             'Two actual dependent attachments and native histories respect forward cancellation',
                             'Ready cancellation reaches encode(decode r), not arbitrary admission-path equality',
                             'Single exchange remains provably nonidentity'],
          'scope': ['No source seeds, native schemas or existing path choices changed',
                    'Vertex sethood is used for dependent selected-point paths, not proof irrelevance of Resolve',
                    'Cancellation is propositional, not definitional, and does not reset initial proofs',
                    'TripleExchangeOverlap is a typed remaining boundary, not an inhabited theorem',
                    'Forward/forward Body interchange binding and general coherent action remain open',
                    'No topology-changing, parameter-generation or physical interpretation claim']}
(OUT / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'pass', 'fresh_agda_exit': positive.returncode,
                  'negative_exits': [c['exit'] for c in controls], 'locked_source_files': len(before)}))
