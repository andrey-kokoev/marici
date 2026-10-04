"""Run actual runtime tests and produce a bounded, reproducible demonstration."""
import io
import json
import unittest
from agda_receipt_audit import OWNER, verify_receipt
from active_view import Engine, demo, wire, file_digest
from test_active_view import ActiveViewTests

checked = verify_receipt('ActiveViewMachine', 'active-view-machine',
                         ['ActiveViewBadTrace', 'ActiveViewBadHistory'])
stream = io.StringIO()
suite = unittest.defaultTestLoader.loadTestsFromTestCase(ActiveViewTests)
run = unittest.TextTestRunner(stream=stream, verbosity=2).run(suite)
(OWNER / 'results/active-view-tests.log').write_text(stream.getvalue(), encoding='utf-8')
if not run.wasSuccessful():
    print(stream.getvalue())
    raise SystemExit(1)
engine = Engine()
example = demo(engine)
for name, obj in [('active-view-full.json', example['full']), ('active-view-plan.json', example['plan']),
                  ('active-view-compact.json', example['compact'])]:
    (OWNER / 'results' / name).write_bytes(wire(obj) + b'\n')
result = {
    'schema': 'marici.nima.active-view-audit.v1', 'passed': run.wasSuccessful(), **checked,
    'runtime_tests_run': run.testsRun,
    'small_request_cases': sum(2 ** (n + 1) for n in range(6)),
    'cache_modes_per_request': 4,
    'runtime_sha256': file_digest(OWNER / 'checkers/active_view.py'),
    'tests_sha256': file_digest(OWNER / 'checkers/test_active_view.py'),
    'before': example['plan']['before'], 'after': example['plan']['after'],
    'plan_validation_steps': example['plan']['validation_steps'],
    'apply_validation_steps': example['plan']['apply_validation_steps'],
    'recovery': example['recovery'], 'undo': example['undo'],
    'undo_plan_bytes': example['undo_plan_bytes'],
    'total_compact_with_plan_bytes': example['total_compact_with_plan_bytes'],
    'exact_canonical_json_round_trip': example['exact_json_round_trip'],
    'formal_scope': 'All four cache visibility modes preserve the source request by certified reductions; output agrees with existing Layer3 execution; trace length is proved.',
    'runtime_scope': 'Closed Boolean history codec, allowlisted output/trace replay policies, conservative deterministic budgeting, dependency retention and hostile JSON/plan checks.',
    'trust_boundary': 'Python and its JSON codec are not extracted from Agda or proved to refine it. Finite tests compare replay with an independent parity oracle and exercise the CLI. Hashes are integrity/version guards, not authentication or proof terms.',
    'cost_scope': 'Canonical UTF-8 JSON bytes and instruction-replay counts, not peak RAM, latency, or total CPU work.'
}
(OWNER / 'results/active-view-audit.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'passed': True, 'runtime_tests': run.testsRun, 'requests_tested': result['small_request_cases'],
                  'active_bytes_before': result['before']['active_bytes'], 'active_bytes_after': result['after']['active_bytes'],
                  'total_bytes_before': result['before']['total_bytes'], 'total_bytes_after': result['after']['total_bytes'],
                  'total_compact_with_plan_bytes': result['total_compact_with_plan_bytes'],
                  'recovery_steps': result['recovery']['recovery_steps']}))
