"""Bounded first-circle provenance audit; does not compile the join tower."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import time

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/strominger'
OUT = BASE / 'results/source-circle-provenance-audit'
OUT.mkdir(parents=True, exist_ok=True)
EXE = shutil.which('agda')
LIB = Path.home() / 'tools/cubical-agda/cubical-0.9'
assert EXE and LIB.is_dir()
PRIM = Path(subprocess.check_output([EXE, '--print-agda-dir'], text=True).strip()) / 'lib/prim'
assert PRIM.is_dir()
roots = {**{'repo-' + owner: ROOT / ('research/' + owner + '/agda')
            for owner in ('strominger', 'nima', 'voevodsky', 'grothendieck')},
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


contract_path = BASE / 'contracts/source-circle-provenance-audit.v1.json'
contract = json.loads(contract_path.read_text(encoding='utf-8'))
assert all(v is False for v in contract['scope_guards'].values())
module = BASE / 'agda/SourceCircleProvenanceAudit.agda'
negatives = [BASE / ('agda/negative/' + m + '.agda') for m in
             ('CircleAuditBadFaithfulBridge', 'CircleAuditBadUniformCircle', 'CircleAuditBadSeedPolicy')]
sources = [module, contract_path, Path(__file__).resolve(), *negatives]
sources += [ROOT / p for p in contract['predecessors']]
sources += [ROOT / p for p in ('research/nima/agda/WholePackageResolution.agda',
           'research/nima/agda/WholePackageSigmaPi.agda',
           'research/strominger/agda/CoherentDependentExtensions.agda',
           'research/strominger/agda/NativeExtensionFamilyAudit.agda',
           'research/strominger/agda/SourceIndexedExtensionFamilies.agda',
           'research/strominger/agda/RetainedPackageFeedback.agda',
           'research/voevodsky/agda/ClosureDependentRefinementRegression.agda')]
hashes = {p.relative_to(ROOT).as_posix(): sha(p) for p in sources}
before = inventory()
common = [EXE, '--transliterate', '--no-libraries', '--safe', '--cubical', '--guardedness', '--no-import-sorts']
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
assert all(line.lower().startswith(str(LIB).lower()) and 'UnsupportedIndexedMatch' in line
           for line in warnings), warnings
controls = []
for p in negatives:
    cmd = common + ['-i', str(BASE / 'agda/negative'), str(p)]
    run = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
    diagnostic = run.stdout + run.stderr
    (OUT / (p.stem + '.log')).write_text(diagnostic, encoding='utf-8')
    assert run.returncode != 0 and 'UnequalTerms' in diagnostic, diagnostic[-5000:]
    controls.append({'module': p.stem, 'command': cmd, 'exit': run.returncode,
                     'diagnostic': diagnostic.strip()})
# Finite cellular shadow only; formal S1/Unit equivalences above do the
# homotopy-type work. The graph edge table stays fixed; pointed input varies.
edges = ['AB', 'BC', 'CA', 'BA', 'AD', 'DB']
sigma = dict(zip('ABCD', 'BADC'))
rows = []
for v in 'ABCD':
    boundary = [e for e in edges if e[0] == v]
    moved = [''.join(sigma[x] for x in e) for e in boundary]
    assert sorted(moved) == sorted(e for e in edges if e[0] == sigma[v])
    rows.append({'pointed_source': v, 'boundary_edges': boundary,
                 'constant_circle_boundary_count': 2, 'outgoing_span_boundary_count': len(boundary),
                 'outgoing_span_cellular_H1_rank': len(boundary) - 1})
assert [r['outgoing_span_boundary_count'] for r in rows] == [2, 2, 1, 1]
candidates = sorted(p.relative_to(ROOT).as_posix() for p in (ROOT / 'research').rglob('WGCircleJoinIntegration.agda'))
assert inventory() == before, 'Declared source inventory changed during verification'
assert all(sha(ROOT / p) == h for p, h in hashes.items())
lock = {'scope': 'Complete declared include-root and primitive-source inventory; conservative superset, not exact import graph',
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
          'negative_controls': controls, 'pointed_source_controls': rows,
          'join_candidate_search': {'root': 'research', 'matches': candidates, 'compiled_this_audit': False},
          'formal_results': ['Existing retained circle and nontrivial loop reused in fresh closure',
                             'Actual pushout tree assembled with identity local realization, without a supplied sphere target',
                             'No classified Fragment carrier is equivalent to the actual retained/raw circle',
                             'Unchanged native E/reflexivity rules faithfully encode any already supplied type from an admitted set carrier',
                             'Native graph-source circle retains its original native parent',
                             'Replacing graph seeds by a declared Unit seed leaves the fixed circle carrier equivalent',
                             'Uniform Out(v)-pushout policy yields S1 at A/B and Unit at C/D',
                             'A/C contrast is provably inequivalent and source sigma covariance is constructed',
                             'Constant-circle and Out(v)-pushout policies pass one-step covariance but differ at C',
                             'The old discrete reader cannot distinguish A/B endpoints connected by the new pushout path'],
          'scope': ['Ablation changes seed policy explicitly; it does not add Unit to original Seeds',
                    'Out(v)-pushout changes the adapter/parameter policy, not the native twelve-rule signature',
                    'Pointed-source variation is not graph-edge ablation',
                    'Carrier-equivalence obstruction does not prohibit topology-changing operations or other realizations',
                    'No source selection of the span, complete parameter-program certificate, all-dimensional action or physical claim',
                    'Join/action/orbit/colimit candidate is not compiled by this audit']}
(OUT / 'verification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'status': 'pass', 'fresh_agda_exit': positive.returncode,
                  'negative_exits': [c['exit'] for c in controls], 'locked_source_files': len(before),
                  'join_candidate_matches': candidates}))
