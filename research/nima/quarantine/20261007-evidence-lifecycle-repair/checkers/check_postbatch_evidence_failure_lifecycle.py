"""Review-only fault injection into the completed batch's receipt lifecycle.

Run under SymPy. No scientific checker or live receipt is modified. Copy each
real pass receipt to an owner-local temporary directory, redirect only that
checker's output path there, and fail its first gate (or verification function).
This tests invalidation of previous success, not the mathematical propositions.
"""
import ast
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CASES = [
    (5,'check_continuum_embedding_evidence_boundary.py','continuum-embedding-evidence-boundary.json','require'),
    (6,'check_s4_gram_action_comparison.py','s4-gram-action-comparison.json','require'),
    (7,'check_twelve_arrow_generation_boundary.py','twelve-arrow-generation-boundary.json','require'),
    (8,'check_twelve_point_phase_readout.py','twelve-point-phase-readout.json','require'),
    (9,'check_gram_bell_readout_comparison.py','gram-bell-readout-comparison.json','require'),
    (10,'check_finite_canonical_constraint_comparison.py','finite-canonical-constraint-comparison.json','require'),
    (9,'check_gram_selection_principle.py','gram-selection-principle-repaired.json','verify'),
    (9,'check_entanglement.py','entanglement-repaired.json','verify'),
    (10,'check_discrete_constraint_algebra.py','discrete-stabilizer-covariance-repaired.json','verify'),
]


def load(path,receipt,output):
    tree = ast.parse(path.read_text(encoding='utf-8'))
    redirected = []
    class OutputOnly(ast.NodeTransformer):
        def visit_BinOp(self,node):
            if (isinstance(node.op,ast.Div) and isinstance(node.left,ast.Name)
                    and node.left.id in ('ROOT','OWNER') and isinstance(node.right,ast.Constant)
                    and node.right.value == 'results/'+receipt):
                redirected.append(receipt)
                return ast.copy_location(ast.Call(func=ast.Name(id='Path',ctx=ast.Load()),
                    args=[ast.Constant(str(output))],keywords=[]),node)
            return self.generic_visit(node)
    tree = OutputOnly().visit(tree)
    assert redirected == [receipt],(path,redirected)
    env = {'__file__':str(path),'__name__':'_review_isolated_'}
    exec(compile(ast.fix_missing_locations(tree),str(path),'exec'),env)
    return env


def failure(*args,**kwargs):
    raise AssertionError('review-injected first gate/verification failure')


def provenance_inventory():
    """Read declared hashes only; this is not a transitive proof-closure check."""
    names = ['tick-evidence-repair','old-spatial-recoil-poisson-obstruction',
             'tick-unitary-image-nonuniqueness','rotor-period-action-boundary',
             'continuum-embedding-evidence-boundary','s4-gram-action-comparison',
             'twelve-arrow-generation-boundary','twelve-point-phase-readout',
             'gram-bell-readout-comparison','finite-canonical-constraint-comparison']
    bindings = []
    for name in names:
        data = json.loads((ROOT/'results'/(name+'.json')).read_text(encoding='utf-8'))
        for relative,expected in data['source_sha256'].items():
            path = (ROOT.parents[1] if relative.startswith('research/') else ROOT)/relative
            bindings.append({'receipt':name,'source':relative,
                             'matches':hashlib.sha256(path.read_bytes()).hexdigest() == expected})
    archives = []
    for manifest in sorted(ROOT.glob('quarantine/20261007-*/manifest.json')):
        for row in json.loads(manifest.read_text(encoding='utf-8'))['files']:
            path = ROOT/row['snapshot'] if 'snapshot' in row else manifest.parent/row['path']
            archives.append({'archive':str(path.relative_to(ROOT)),
                             'matches':hashlib.sha256(path.read_bytes()).hexdigest() == row['sha256']})
    for manifest in sorted(ROOT.glob('quarantine/20261007-*/SHA256SUMS')):
        for line in manifest.read_text(encoding='utf-8').splitlines():
            expected,relative = line.split(maxsplit=1)
            path = manifest.parent/relative.lstrip('*')
            archives.append({'archive':str(path.relative_to(ROOT)),
                             'matches':hashlib.sha256(path.read_bytes()).hexdigest() == expected})
    return {'receipts_inspected':len(names),'declared_bindings_checked':len(bindings),
            'receipt_source_mismatches':[x for x in bindings if not x['matches']],
            'archive_entries_checked':len(archives),
            'archive_mismatches':[x for x in archives if not x['matches']],
            'scope':'Declared file hashes only, not transitive dependency freshness or mathematical verification.'}


def main():
    output = ROOT/'results/postbatch-evidence-failure-lifecycle.json'
    output.unlink(missing_ok=True)
    inventory = provenance_inventory()
    paths = {ROOT/'checkers'/script for _,script,_,_ in CASES}
    paths |= {ROOT/'results'/receipt for _,_,receipt,_ in CASES}
    control = ROOT/'checkers/check_tick_to_square_realization.py'
    paths |= {control,ROOT/'results/tick-to-square-realization-consistency.json'}
    before = {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    observations = []
    with tempfile.TemporaryDirectory(prefix='postbatch-review-',dir=ROOT/'results') as directory:
        directory = Path(directory)
        for step,script,receipt,gate in CASES:
            prior = (ROOT/'results'/receipt).read_bytes()
            assert json.loads(prior)['status'] == 'pass'
            isolated = directory/receipt
            isolated.write_bytes(prior)
            env = load(ROOT/'checkers'/script,receipt,isolated)
            env[gate] = failure
            propagated = False
            with redirect_stdout(io.StringIO()):
                try:
                    env['main']()
                except AssertionError as error:
                    assert 'review-injected' in str(error)
                    propagated = True
            assert propagated
            survived = isolated.exists() and isolated.read_bytes() == prior
            observations.append({'step':step,'script':script,'injected_failure_propagated':propagated,
                'previous_pass_receipt_survives_byte_identically':survived,
                'receipt_status_after_failure':json.loads(isolated.read_text())['status'] if isolated.exists() else None})
        # Positive control: the repair that explicitly introduced invalidation.
        receipt = 'tick-to-square-realization-consistency.json'
        isolated = directory/receipt
        prior = (ROOT/'results'/receipt).read_bytes()
        env = load(control,receipt,isolated)
        isolated.write_bytes(prior)
        env['p1'] = lambda:False
        with redirect_stdout(io.StringIO()):
            exit_code = env['main']([])
        assert exit_code == 1 and json.loads(isolated.read_text())['status'] == 'fail'
        failed_predicate_replaced_pass = True
        isolated.write_bytes(prior)
        env['run_checks'] = failure
        try:
            env['main']([])
        except AssertionError:
            pass
        assert not isolated.exists()
    assert before == {str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    result = {'schema':'marici.nima.postbatch-failure-lifecycle-review.v1',
              'role':'review regression, not mathematical refutation',
              'cases':observations,
              'step1_control':{'false_predicate_returns_1_and_replaces_pass':failed_predicate_replaced_pass,
                               'unexpected_verification_failure_removes_previous_pass':True},
              'live_sources_and_receipts_unchanged':True,
              'provenance_inventory':inventory,
              'interpretation':'All failures propagate; the defect is surviving stale pass JSON, not a false zero exit code.',
              'source_sha256':{str(p.relative_to(ROOT)).replace('\\','/'):h for p,h in
                              ((Path(name),h) for name,h in before.items())}}
    result['source_sha256']['checkers/'+Path(__file__).name] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'stale_pass_survivors':sum(x['previous_pass_receipt_survives_byte_identically'] for x in observations),
                      'tested_entrypoints':len(observations),'step1_control':'invalidates prior pass correctly',
                      'live_inputs_unchanged':True,'provenance_inventory':inventory},indent=2))


if __name__ == '__main__':
    main()
