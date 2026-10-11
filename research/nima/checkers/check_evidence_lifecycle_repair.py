"""R1/R2 maintenance regression, not a new mathematical selection claim.

--snapshot preserves pre-repair sources/receipts once; --freeze refreshes only
content-addressed freezes for affected owner models; --refresh reruns their
canonical SCC checks and the repaired standalone entrypoints. Default checks
compare old/new failure handling in isolated outputs, unchanged computation
ASTs and mathematical receipt contents, source hashes, and continuation text.
"""
import argparse
import ast
from contextlib import redirect_stdout, redirect_stderr
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import runpy
import sys
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent.parent
ARCHIVE = ROOT/'quarantine/20261007-evidence-lifecycle-repair'
REVIEW = ROOT/'checkers/check_postbatch_evidence_failure_lifecycle.py'
CASES = [
    ('check_continuum_embedding_evidence_boundary.py','continuum-embedding-evidence-boundary.json','require'),
    ('check_s4_gram_action_comparison.py','s4-gram-action-comparison.json','require'),
    ('check_twelve_arrow_generation_boundary.py','twelve-arrow-generation-boundary.json','require'),
    ('check_twelve_point_phase_readout.py','twelve-point-phase-readout.json','require'),
    ('check_gram_bell_readout_comparison.py','gram-bell-readout-comparison.json','require'),
    ('check_finite_canonical_constraint_comparison.py','finite-canonical-constraint-comparison.json','require'),
    ('check_gram_selection_principle.py','gram-selection-principle-repaired.json','verify'),
    ('check_entanglement.py','entanglement-repaired.json','verify'),
    ('check_discrete_constraint_algebra.py','discrete-stabilizer-covariance-repaired.json','verify'),
    ('check_tick_evidence_repair.py','tick-evidence-repair.json','check'),
]
EXTRA_RECEIPTS = ['retained-rotor-phase-transport.json','retained-rotor-history-clock.json',
                  'rotor-period-action-boundary.json','tetrahedral-native-rotation-loop.json']


def must(condition, message):
    if not condition:
        raise AssertionError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot():
    must(not ARCHIVE.exists(), 'Refuse to overwrite pre-repair evidence')
    paths = {ROOT/'checkers'/script for script,_,_ in CASES}
    paths |= {ROOT/'results'/name for _,name,_ in CASES}
    paths |= {ROOT/'results'/name for name in EXTRA_RECEIPTS}
    paths |= {REVIEW, ROOT/'results/postbatch-evidence-failure-lifecycle.json',
              ROOT/'corrective-batch-critical-review-20261007.md',
              ROOT/'retained-rotor-phase-transport.md', ROOT/'conceptual-steps-table.md'}
    changed = {str(p.relative_to(REPO)).replace('\\','/') for p in paths
               if p.suffix == '.py' and p != REVIEW}
    changed.add('research/nima/retained-rotor-phase-transport.md')
    models = []
    for path in sorted((ROOT/'scc-models').glob('*.json')):
        data = json.loads(path.read_text(encoding='utf-8'))['model']
        inputs = set(data['inputs']) | {c['path'] for c in data['checks']}
        if inputs & changed:
            must(data['owner'] == 'marici.Nima','Cross-owner model')
            models.append({'id':data['id'],'depends_on':data.get('depends_on',[]),
                           'manifest':str(path.relative_to(ROOT)).replace('\\','/')})
            paths.add(path)
    # Read everything before making the immutable snapshot directory.
    contents = {p:p.read_bytes() for p in paths}
    freezes = {str(p.relative_to(ROOT)).replace('\\','/'):sha(p)
               for model in models for p in (ROOT/'scc-freezes').glob(model['id']+'.*.json')}
    entries = []
    for path,data in sorted(contents.items()):
        relative = path.relative_to(ROOT)
        target = ARCHIVE/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        target.write_bytes(data)
        entries.append({'path':relative.as_posix(),'sha256':sha(target),
                        'source_mtime_ns':path.stat().st_mtime_ns})
    manifest = {'schema':'marici.nima.evidence-lifecycle-before.v1',
                'status':'historical pre-repair evidence; not current certificates',
                'recorded_at':datetime.now(timezone.utc).isoformat(),
                'files':entries,'affected_models':models,'original_freezes':freezes}
    (ARCHIVE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'snapshot_files':len(entries),'affected_models':[m['id'] for m in models]},indent=2))


def manifest():
    data = json.loads((ARCHIVE/'manifest.json').read_text(encoding='utf-8'))
    for row in data['files']:
        must(sha(ARCHIVE/row['path']) == row['sha256'],'Changed archive: '+row['path'])
    for path,digest in data['original_freezes'].items():
        must(sha(ROOT/path) == digest,'Historical freeze changed: '+path)
    return data


def scc():
    directory = REPO/'research/aspect/scc'
    sys.path.insert(0,str(directory))
    return runpy.run_path(str(directory/'scc.py'))


def maintain(action):
    out = ROOT/('results/evidence-lifecycle-'+action+'.json')
    out.unlink(missing_ok=True)
    data = manifest()
    compiler = scc()
    pending = {m['id']:m for m in data['affected_models']}
    rows = []
    while pending:
        ready = [m for m in pending.values() if not set(m['depends_on']) & pending.keys()]
        must(bool(ready),'Dependency cycle')
        for model in ready:
            capture = io.StringIO()
            with redirect_stdout(capture):
                code = compiler['main']([action,model['id']])
            row = {'model':model['id'],'exit_code':code,'report':json.loads(capture.getvalue())}
            rows.append(row)
            if code:
                out.write_text(json.dumps({'status':'fail','rows':rows},indent=2)+'\n',encoding='utf-8')
                raise AssertionError(row)
            del pending[model['id']]
            print(action+': '+model['id'],flush=True)
    if action == 'check':
        # These repaired entrypoints are not themselves registered SCC models.
        for script,_,_ in CASES[6:]:
            with redirect_stdout(io.StringIO()):
                runpy.run_path(str(ROOT/'checkers'/script),run_name='__main__')
            rows.append({'standalone':script,'passed':True})
    out.write_text(json.dumps({'status':'pass','rows':rows},indent=2)+'\n',encoding='utf-8')


def scoped_models(compiler):
    models,errors = compiler['discover']()
    selected = {m['id'] for m in manifest()['affected_models']}
    queue = list(selected)
    while queue:
        name = queue.pop()
        must(name in models,'Affected model/dependency unavailable: '+name)
        for dep in models[name].get('depends_on',[]):
            if dep not in selected:
                selected.add(dep)
                queue.append(dep)
    paths = {Path(models[name]['_manifest']).resolve() for name in selected}
    relevant = [e for e in errors if Path(e['manifest']).resolve() in paths
                or any('duplicate model id: '+name in e['errors'] for name in selected)]
    must(not relevant,'Affected SCC discovery errors: '+repr(relevant))
    return models,errors


def refresh_with_manifest():
    """Own-process bookkeeping in the established ignored results directory."""
    compiler = scc()
    models,errors = scoped_models(compiler)
    selected = [models[m['id']] for m in manifest()['affected_models']]
    inputs = {REPO/p for m in selected for p in m['inputs']}
    inputs |= {REPO/c['path'] for m in selected for c in compiler['checks_for'](m)}
    inputs |= {Path(__file__).resolve(),REPO/'research/aspect/scc/scc.py'}
    record = {'command':[sys.executable,*sys.argv],
              'build':'Interpreted Python in the preflighted uv SymPy environment; no native build',
              'input_sha256':{str(p.relative_to(REPO)).replace('\\','/'):sha(p) for p in inputs},
              'python':sys.executable,'executable_sha256':sha(Path(sys.executable)),
              'pid':os.getpid(),'parent_pid':os.getppid(),
              'child_process_authority':'Canonical SCC run_checks; outer execution owned by structured-command',
              'started_at':datetime.now(timezone.utc).isoformat(),
              'output':'research/nima/results/evidence-lifecycle-check.json',
              'expected_status':'pass','expected_exit_code':0,'state':'running',
              'scope':'Only directly affected owner models and four standalone entrypoints; no transitive formal closure claim',
              'unrelated_SCC_discovery_errors':errors}
    path = ROOT/'results/evidence-lifecycle-refresh-run.json'
    path.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
    try:
        maintain('check')
        record.update(state='finished',exit_code=0)
    except BaseException as error:
        record.update(state='failed',exit_code=1,error=repr(error))
        raise
    finally:
        record['ended_at'] = datetime.now(timezone.utc).isoformat()
        path.write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')


def is_destination(node, receipt):
    return (isinstance(node,ast.BinOp) and isinstance(node.op,ast.Div)
            and isinstance(node.left,ast.Name) and node.left.id in ('ROOT','OWNER')
            and isinstance(node.right,ast.Constant) and node.right.value == 'results/'+receipt)


def computation_tree(text,receipt):
    """Erase only the checker-owned output protocol, not any required gate."""
    class Strip(ast.NodeTransformer):
        def visit_Assign(self,node):
            if is_destination(node.value,receipt):
                must(len(node.targets) == 1 and isinstance(node.targets[0],ast.Name)
                     and node.targets[0].id in ('out','OUT'),'Unexpected receipt binding')
                return None
            return self.generic_visit(node)
        def visit_Expr(self,node):
            f = node.value.func if isinstance(node.value,ast.Call) else None
            if isinstance(f,ast.Attribute) and f.attr in ('unlink','write_text'):
                own = is_destination(f.value,receipt) or (isinstance(f.value,ast.Name) and f.value.id in ('out','OUT'))
                if own:
                    return None
            return self.generic_visit(node)
    return ast.dump(Strip().visit(ast.parse(text)),include_attributes=False)


def failed_run(text,path,receipt,gate,destination,exception):
    redirected, injected = [],[]
    class Inject(ast.NodeTransformer):
        def visit_BinOp(self,node):
            if is_destination(node,receipt):
                redirected.append(receipt)
                return ast.copy_location(ast.Call(func=ast.Name(id='Path',ctx=ast.Load()),
                    args=[ast.Constant(str(destination))],keywords=[]),node)
            return self.generic_visit(node)
        def visit_FunctionDef(self,node):
            if node.name == gate:
                injected.append(gate)
                node.body = ast.parse("raise "+exception.__name__+"('repair-injected verification failure')").body
                return node
            return self.generic_visit(node)
    tree = Inject().visit(ast.parse(text))
    must(redirected == [receipt] and injected == [gate],'Unexpected injection sites: '+path.name)
    try:
        with patch.object(sys,'argv',[str(path)]), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            exec(compile(ast.fix_missing_locations(tree),str(path),'exec'),
                 {'__file__':str(path),'__name__':'__main__'})
    except exception as error:
        must(str(error) == 'repair-injected verification failure','Unrelated exception')
        return
    raise AssertionError('Verification failure swallowed: '+path.name)


def without_hashes(value):
    if isinstance(value,dict):
        return {k:without_hashes(v) for k,v in value.items() if k not in ('source_sha256','input_sha256')}
    if isinstance(value,list):
        return [without_hashes(v) for v in value]
    return value


def verify():
    out = ROOT/'results/evidence-lifecycle-repair.json'
    out.unlink(missing_ok=True)
    saved = manifest()
    protected = {ROOT/'checkers'/script for script,_,_ in CASES}
    protected |= {ROOT/'results'/name for _,name,_ in CASES}
    protected |= {REVIEW,ROOT/'results/postbatch-evidence-failure-lifecycle.json'}
    before = {p:sha(p) for p in protected}
    observations = []
    with tempfile.TemporaryDirectory(prefix='lifecycle-repair-',dir=ROOT/'results') as directory:
        for script,receipt,gate in CASES:
            path = ROOT/'checkers'/script
            old = (ARCHIVE/'checkers'/script).read_text(encoding='utf-8')
            current = path.read_text(encoding='utf-8')
            must(computation_tree(old,receipt) == computation_tree(current,receipt),
                 'Non-lifecycle computation changed: '+script)
            prior = (ARCHIVE/'results'/receipt).read_bytes()
            must(json.loads(prior)['status'] == 'pass','Not a real previous pass')
            destination = Path(directory)/receipt
            for exception in (AssertionError,RuntimeError):
                for version,text,expected_exists in [('historical',old,True),('repaired',current,False)]:
                    destination.write_bytes(prior)
                    failed_run(text,path,receipt,gate,destination,exception)
                    must(destination.exists() == expected_exists,'Receipt lifecycle: '+script)
                    if expected_exists:
                        must(destination.read_bytes() == prior,'Historical control was not unchanged')
                    observations.append({'script':script,'version':version,'exception':exception.__name__,
                                         'failure_propagated':True,'stale_pass_survives':destination.exists()})
    retired_code = None
    with redirect_stdout(io.StringIO()):
        try:
            runpy.run_path(str(REVIEW),run_name='__main__')
        except SystemExit as error:
            retired_code = error.code
    must(retired_code == 2,'Historical review must refuse rewriting its old receipt')
    must(before == {p:sha(p) for p in protected},'Live inputs modified by isolated fault injection')
    # Baselines were executed separately through the canonical commands, not faked here.
    normal = json.loads((ROOT/'results/evidence-lifecycle-check.json').read_text())
    must(normal['status'] == 'pass','Normal refresh did not finish')
    receipts = [name for _,name,_ in CASES]+EXTRA_RECEIPTS
    for name in receipts:
        old = json.loads((ARCHIVE/'results'/name).read_text(encoding='utf-8'))
        current = json.loads((ROOT/'results'/name).read_text(encoding='utf-8'))
        must(without_hashes(old) == without_hashes(current),'Scientific receipt changed: '+name)
        for field in ('source_sha256','input_sha256'):
            for relative,digest in current.get(field,{}).items():
                relative = relative.replace('\\','/')
                if name == 'tetrahedral-native-rotation-loop.json':
                    bound = ROOT/('checkers' if relative.endswith('.py') else 'contracts')/relative
                else:
                    bound = (REPO if relative.startswith('research/') else ROOT)/relative
                must(sha(bound) == digest,'Current source binding: '+name+' / '+relative)
    phase = (ROOT/'retained-rotor-phase-transport.md').read_text(encoding='utf-8')
    must('## Current continuation' in phase[:1000]
         and 'retained-rotor-history-clock.md' in phase[:1000]
         and 'retained-clock-calibration-identifiability.md' in phase[:1000]
         and 'The next local question is a clock' not in phase,'Stale clock frontier')
    inventory = runpy.run_path(str(REVIEW))['provenance_inventory']()
    must(not inventory['receipt_source_mismatches'] and not inventory['archive_mismatches'],
         'Declared source/archive hash mismatch')
    compiler = scc()
    models,errors = scoped_models(compiler)
    states = {m['id']:{'status':compiler['model_status'](models[m['id']])['status'],
                       'freeze':compiler['freeze_status'](models[m['id']])}
              for m in saved['affected_models']}
    must(all(x == {'status':'current_checks_passed','freeze':'current'} for x in states.values()),
         'Affected SCC status/freeze not current')
    result = {'schema':'marici.nima.evidence-lifecycle-repair.v1','status':'pass',
              'recorded_at':datetime.now(timezone.utc).isoformat(),
              'scope':'Verification-body failures after checker startup; not launch/import failure, concurrent writers, or physical selection.',
              'cases':observations,'repaired_entrypoints':len(CASES),
              'repaired_stale_pass_survivors':sum(x['stale_pass_survives'] for x in observations if x['version']=='repaired'),
              'mathematical_computation_ASTs_unchanged':True,'scientific_receipts_unchanged_except_hashes':receipts,
              'isolated_tests_preserved_live_inputs':True,'clock_frontier_corrected':True,
              'historical_review_entrypoint_exit_code':retired_code,
              'provenance_inventory':inventory,'SCC':states,'unrelated_SCC_discovery_errors':errors,
              'source_sha256':{p.relative_to(ROOT).as_posix():sha(p) for p in protected | {Path(__file__).resolve(),ROOT/'retained-rotor-phase-transport.md'}}}
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','repaired_entrypoints','repaired_stale_pass_survivors',
                       'mathematical_computation_ASTs_unchanged','clock_frontier_corrected','provenance_inventory','SCC')},indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--snapshot',action='store_true')
    mode.add_argument('--freeze',action='store_true')
    mode.add_argument('--refresh',action='store_true')
    args = parser.parse_args()
    if args.snapshot:
        snapshot()
    elif args.freeze:
        maintain('freeze')
    elif args.refresh:
        refresh_with_manifest()
    else:
        verify()
