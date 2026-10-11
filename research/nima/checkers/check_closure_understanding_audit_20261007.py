"""Bounded audit reproductions; does not execute or overwrite historical receipts.

Extracts the actual Fraction definitions from immutable PRE-REPAIR snapshots.
Runs the archived square checker in memory with its sole result write removed,
then injects one failed predicate. No native Agda or physical theorem is tested.
"""
from contextlib import redirect_stdout
from fractions import Fraction
from pathlib import Path
import ast
import hashlib
import io
import json

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / 'quarantine/20261007-tick-evidence'
SNAPSHOTS = json.loads((ARCHIVE / 'manifest.json').read_text(encoding='utf-8'))['files']
checks = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def parsed(name):
    archived = [r for r in SNAPSHOTS if r['original'] == 'checkers/' + name]
    path = ROOT / archived[0]['snapshot'] if archived else ROOT / 'checkers' / name
    if archived and hashlib.sha256(path.read_bytes()).hexdigest() != archived[0]['sha256']:
        raise AssertionError('historical snapshot changed: ' + name)
    return path, ast.parse(path.read_text(encoding='utf-8'))


selection_path, selection_tree = parsed('check_tick_selects_generator.py')
main = next(n for n in selection_tree.body
            if isinstance(n, ast.FunctionDef) and n.name == 'main')
constants = {'I', 'L', 'R', 'PL', 'PR'}
functions = {'scale', 'add', 'mm'}
nodes = [n for n in main.body
         if (isinstance(n, ast.FunctionDef) and n.name in functions)
         or (isinstance(n, ast.Assign) and len(n.targets) == 1
             and isinstance(n.targets[0], ast.Name)
             and n.targets[0].id in constants)]
check('exact-matrix-extraction-node-count', len(nodes) == 8)
ns = {'F': Fraction}
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(selection_path), 'exec'), ns)
PL, PR = ns['PL'], ns['PR']
H = ns['add'](PL, PR)
He00 = tuple(row[0] for row in H)
check('printed-stationary-source-claim-is-false',
      He00 == (Fraction(1), Fraction(-1, 2), Fraction(-1, 2), Fraction(0)))
check('source-velocity-norm-squared', sum(x*x for x in He00) == Fraction(3, 2))
check('printed-spectrum-is-only-matrix-diagonal', tuple(H[i][i] for i in range(4)) == (1, 1, 1, 1))
eigenvectors = ((1, 1, 1, 1), (1, 1, -1, -1),
                (1, -1, 1, -1), (1, -1, -1, 1))
for v, eigenvalue in zip(eigenvectors, (0, 1, 1, 2)):
    Hv = tuple(sum(H[i][j]*v[j] for j in range(4)) for i in range(4))
    check('actual-eigenpair-' + str(v), Hv == tuple(eigenvalue*x for x in v))
PLPR = ns['mm'](PL, PR)
check('projector-ranges-are-not-orthogonal', any(x != 0 for row in PLPR for x in row))
check('extra-commutant-direction-commutes',
      ns['mm'](PLPR, ns['L']) == ns['mm'](ns['L'], PLPR)
      and ns['mm'](PLPR, ns['R']) == ns['mm'](ns['R'], PLPR))
# Joint eigenvalues (0,0,0,1) cannot be a*(0,1,0,1)+b*(0,0,1,1).
for v, eigenvalue in zip(eigenvectors, (0, 0, 0, 1)):
    image = tuple(sum(PLPR[i][j]*v[j] for j in range(4)) for i in range(4))
    check('extra-direction-eigenpair-' + str(v), image == tuple(eigenvalue*x for x in v))
assertions = [n for n in ast.walk(main) if isinstance(n, ast.Assert)]
check('selection-script-has-only-prior-receipt-assertion',
      len(assertions) == 1 and ast.unparse(assertions[0].test) == "proof['passed']")

square_path, _ = parsed('check_tick_to_square_realization.py')
old_receipt = ROOT / 'results/tick-to-square-realization-faithfulness.json'
before = old_receipt.read_bytes() if old_receipt.exists() else None


def square_run(inject_failure):
    tree = ast.parse(square_path.read_text(encoding='utf-8'))
    writes = [n for n in tree.body if isinstance(n, ast.Expr)
              and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Attribute)
              and n.value.func.attr == 'write_text']
    check('one-result-write-' + str(inject_failure), len(writes) == 1)
    tree.body = [n for n in tree.body if n not in writes]
    if inject_failure:
        p1 = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'p1')
        p1.body = [ast.Return(value=ast.Constant(value=False))]
    env = {'__file__': str(square_path)}
    with redirect_stdout(io.StringIO()):
        exec(compile(ast.fix_missing_locations(tree), str(square_path), 'exec'), env)
    return {'passed': env['passed'], 'failed': env['failed'],
            'status': env['result']['status'], 'model_checks': env['result']['model_checks'],
            'returned_normally': True}


baseline = square_run(False)
mutant = square_run(True)
check('baseline-control-10-of-10', baseline['passed'] == 10 and baseline['failed'] == 0)
check('injected-failure-is-counted', mutant['failed'] == 1 and mutant['passed'] == 9)
check('json-still-claims-every-property-true', all(mutant['model_checks'].values()))
check('failed-model-returns-without-exception', mutant['returned_normally'] and mutant['status'] == 'partial')
check('historical-receipt-untouched',
      (old_receipt.read_bytes() if old_receipt.exists() else None) == before)

# Positive controls: later checkers really reject a failed property.
for name in ('check_tick_interpretation_nonuniqueness.py', 'check_shared_recoil_cotangent_binding.py'):
    path, tree = parsed(name)
    function = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'check')
    env = {'checks': []}
    exec(compile(ast.Module(body=[function], type_ignores=[]), str(path), 'exec'), env)
    raised = False
    try:
        env['check']('deliberate-failure', False)
    except AssertionError:
        raised = True
    check('positive-failure-gate/' + name, raised)

source_paths = [selection_path, square_path, ARCHIVE/'source-to-generator-audit.md.txt',
                ROOT/'checkers/check_tick_interpretation_nonuniqueness.py',
                ROOT/'checkers/check_shared_recoil_cotangent_binding.py', Path(__file__)]
result = {
    'schema': 'marici.nima.closure-understanding-audit.v2',
    'scope': 'historical pre-repair defects reproduced from hash-pinned snapshots; not claims about current checkers',
    'checks': checks, 'check_count': len(checks),
    'exact_source_counterexample': {'H_e00': list(map(str, He00)),
        'squared_norm': '3/2', 'printed_diagonal': [1, 1, 1, 1], 'actual_spectrum': [0, 1, 1, 2]},
    'square_baseline': baseline, 'square_failed_predicate_mutation': mutant,
    'historical_results_modified': False,
    'source_sha256': {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in source_paths},
}
out = ROOT/'results/closure-understanding-audit-20261007-controls.json'
out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(f'{len(checks)} audit controls passed against PRE-REPAIR snapshots; current quarantine receipts untouched.')
