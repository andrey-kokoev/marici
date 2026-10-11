"""Regression and mutation checks for the narrowly scoped Tick evidence repair.

Exercises existing entrypoints in process; does not spawn subprocesses or
rerun Agda. Every temporary receipt is isolated from authoritative results.
"""
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
import ast
import hashlib
import io
import json
import runpy
import sys
import tempfile
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'results/tick-evidence-repair.json'
OUT.unlink(missing_ok=True)
SCRIPT = ROOT / 'checkers/check_tick_to_square_realization.py'
ARCHIVE = ROOT / 'quarantine/20261007-tick-evidence'
checks = []
mutations = []


def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)


def quiet_main(ns, output):
    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
        return ns['main'](['--output', str(output)])


for row in json.loads((ARCHIVE/'manifest.json').read_text(encoding='utf-8'))['files']:
    check('snapshot/' + row['original'],
          hashlib.sha256((ROOT/row['snapshot']).read_bytes()).hexdigest() == row['sha256'])

quarantined = runpy.run_path(str(ROOT/'checkers/check_tick_selects_generator.py'))
with redirect_stderr(io.StringIO()):
    check('selection-entrypoint-refuses', quarantined['main']() == 2)
for name in ('tick-selects-generator.json', 'tick-to-square-realization-faithfulness.json'):
    receipt = json.loads((ROOT/'results'/name).read_text(encoding='utf-8'))
    check('quarantined-receipt/' + name,
          receipt['status'] == 'quarantined' and receipt['passed'] is False)

with tempfile.TemporaryDirectory(prefix='tick-evidence-repair-', dir=ROOT/'results') as temp:
    output = Path(temp)/'receipt.json'
    ns = runpy.run_path(str(SCRIPT))
    check('matrix-baseline-exit', quiet_main(ns, output) == 0)
    baseline = json.loads(output.read_text(encoding='utf-8'))
    check('matrix-baseline-properties', baseline['passed_count'] == baseline['check_count'] == 10)
    check('matrix-baseline-status', baseline['status'] == 'pass' and baseline['passed'])
    for i, key in enumerate(baseline['model_checks'], 1):
        ns = runpy.run_path(str(SCRIPT))
        ns['run_checks'].__globals__['p' + str(i)] = lambda: False
        check('false-predicate-exit/' + key, quiet_main(ns, output) == 1)
        result = json.loads(output.read_text(encoding='utf-8'))
        check('false-predicate-receipt/' + key,
              result['status'] == 'fail' and result['passed'] is False
              and result['failed_count'] == 1 and result['passed_count'] == 9
              and result['model_checks'][key] is False)
        check('property-table-agrees/' + key,
              result['model_checks'] == {r['property']: r['passed'] for r in result['checks']})
        mutations.append({'injected_false': key, 'exit_code': 1, 'failed_count': 1})

    def boom():
        raise RuntimeError('deliberate audit exception')

    ns = runpy.run_path(str(SCRIPT))
    ns['run_checks'].__globals__['p4'] = boom
    check('predicate-exception-fails', quiet_main(ns, output) == 1)
    result = json.loads(output.read_text(encoding='utf-8'))
    check('predicate-exception-recorded', 'RuntimeError' in result['checks'][3]['error'])

    for label, factor in (('zero', 0), ('wrong-sign', -1), ('double', 2),
                          ('nan', float('nan')), ('infinite', float('inf'))):
        ns = runpy.run_path(str(SCRIPT))
        original = ns['generator']
        ns['p10'].__globals__['generator'] = lambda a, b, f=factor, g=original: ns['scale'](f, g(a, b))
        check('wrong-generator/' + label, quiet_main(ns, output) == 1)
        result = json.loads(output.read_text(encoding='utf-8'))
        check('wrong-generator-identified/' + label, result['model_checks']['P10_generator_form'] is False)

    ns = runpy.run_path(str(SCRIPT))
    original_u = ns['U']
    z = tuple(tuple((1 if i < 2 else -1) if i == j else 0 for j in range(4)) for i in range(4))
    ns['p7'].__globals__['U'] = lambda a, b: z if a == 0 and b == ns['math'].pi else original_u(a, b)
    check('different-routes-detected', quiet_main(ns, output) == 1)
    check('comparison-is-not-tautology',
          json.loads(output.read_text(encoding='utf-8'))['model_checks']['P7_comparison'] is False)

    ns = runpy.run_path(str(SCRIPT))
    ns['main'].__globals__['run_checks'] = boom
    output.write_text('{"status":"pass"}', encoding='utf-8')
    raised = False
    try:
        quiet_main(ns, output)
    except RuntimeError:
        raised = True
    check('unexpected-error-removes-stale-success', raised and not output.exists())

    # Exercise the real __main__ branch, not only the return value of main().
    for inject, expected in ((False, 0), (True, 1)):
        tree = ast.parse(SCRIPT.read_text(encoding='utf-8'))
        if inject:
            fn = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'p1')
            fn.body = [ast.Return(value=ast.Constant(value=False))]
        code = compile(ast.fix_missing_locations(tree), str(SCRIPT), 'exec')
        exit_code = None
        with patch.object(sys, 'argv', [str(SCRIPT), '--output', str(output)]), redirect_stdout(io.StringIO()):
            try:
                exec(code, {'__name__': '__main__', '__file__': str(SCRIPT)})
            except SystemExit as error:
                exit_code = error.code
        check('script-entrypoint-exit/' + str(inject), exit_code == expected)

result = {
    'schema': 'marici.nima.tick-evidence-repair.v1', 'status': 'pass',
    'scope': 'quarantine, result integrity and failure gates; no native analytic or physical selection theorem',
    'checks': checks, 'check_count': len(checks), 'required_predicate_mutations': mutations,
    'source_sha256': {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                      for p in (SCRIPT, ROOT/'checkers/check_tick_selects_generator.py', Path(__file__))},
}
OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(f'{len(checks)} repair controls passed; all 10 false predicates fail both receipt and execution.')
