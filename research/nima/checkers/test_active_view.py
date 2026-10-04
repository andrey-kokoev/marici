"""Hostile and bounded exhaustive conformance checks for the Python engine."""
from copy import deepcopy
from itertools import product
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import active_view as av


class ActiveViewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = av.Engine()

    def full(self):
        return self.engine.build([{'history': [], 'input': True},
                                  {'history': ['turn', 'turn'], 'input': True}])

    def test_all_small_histories_and_modes(self):
        # All 126 requests through instruction length 5; four cache modes each.
        for n in range(6):
            for h in product(('stay', 'turn'), repeat=n):
                for b in (False, True):
                    full = self.engine.build([{'history': list(h), 'input': b}])
                    expected = [bool(b ^ (h[:i].count('turn') % 2)) for i in range(n + 1)]
                    self.assertEqual(full['views'][0]['cache']['trace']['value'], expected)
                    self.assertIs(full['views'][0]['cache']['output']['value'], expected[-1])
                    for fields in ((), ('output',), ('trace',), ('output', 'trace')):
                        partial = deepcopy(full)
                        partial['views'][0]['cache'] = {f: full['views'][0]['cache'][f] for f in fields}
                        restored, cost = self.engine.recover(partial)
                        self.assertEqual(av.wire(restored), av.wire(full))
                        self.assertEqual(cost['validation_steps'] + cost['recovery_steps'], n)
                        plan_partial = self.engine.plan(partial)
                        cleared_partial = self.engine.apply(partial, plan_partial)
                        self.assertEqual(self.engine.undo(cleared_partial, plan_partial)[0], partial)
                    plan = self.engine.plan(full)
                    cleared = self.engine.apply(full, plan)
                    self.assertEqual(cleared['views'][0]['cache'], {})
                    self.assertEqual(av.wire(self.engine.recover(cleared)[0]), av.wire(full))

    def test_dependency_retention_and_score_collision(self):
        full = self.full()
        a, b = full['views']
        self.assertEqual(a['cache']['output'], b['cache']['output'])
        self.assertNotEqual(a['request'], b['request'])
        old = av.wire(full)
        cleared = self.engine.apply(full, self.engine.plan(full))
        self.assertEqual(full['requests'], cleared['requests'])
        self.assertEqual(av.wire(full), old)
        self.assertNotEqual(cleared['views'][0], cleared['views'][1])

    def test_explicit_stays_are_not_erased(self):
        full = self.engine.build([{'history': [], 'input': True}, {'history': ['stay'], 'input': True}])
        self.assertNotEqual(full['views'][0]['request'], full['views'][1]['request'])

    def test_shared_requests_replayed_once(self):
        request = {'history': ['turn'] * 9, 'input': False}
        full = self.engine.build([request, request])
        plan = self.engine.plan(full, replay_budget=9)
        self.assertEqual(len(plan['actions']), 4)
        self.assertEqual(plan['full_recovery_steps_bound'], 9)
        restored, cost = self.engine.recover(self.engine.apply(full, plan))
        self.assertEqual(restored, full)
        self.assertEqual(cost['recovery_steps'], 9)
        self.assertEqual(len(full['requests']), 1)

    def test_budget_and_storage_accounting(self):
        full = self.full()
        plan = self.engine.plan(full, replay_budget=0)
        self.assertEqual({a['view'] for a in plan['actions']}, {0})
        cleared = self.engine.apply(full, plan)
        self.assertEqual(plan['before']['active_bytes'] - plan['after']['active_bytes'],
                         sum(a['bytes_saved'] for a in plan['actions']))
        self.assertEqual(plan['after'], self.engine.sizes(cleared))
        self.assertEqual(plan['before']['retained_dependency_bytes'], plan['after']['retained_dependency_bytes'])
        self.assertEqual(self.engine.plan(full, min_savings=av.MAX_BYTES)['actions'], [])
        all_clear = self.engine.apply(full, self.engine.plan(full))
        with self.assertRaises(av.Invalid):
            self.engine.plan(all_clear, replay_budget=0)

    def test_idempotence_and_partial_recovery(self):
        full = self.full()
        clear = self.engine.apply(full, self.engine.plan(full))
        self.assertEqual(self.engine.plan(clear)['actions'], [])
        partial, _ = self.engine.recover(clear, ['output'])
        self.assertEqual([set(v['cache']) for v in partial['views']], [{'output'}, {'output'}])
        self.assertEqual(self.engine.recover(partial)[0], full)
        self.assertEqual(self.engine.recover(full)[0], full)

    def test_stale_and_forged_plans(self):
        full = self.full()
        plan = self.engine.plan(full)
        changed = self.engine.build([{'history': ['stay'], 'input': True}])
        with self.assertRaisesRegex(av.Invalid, 'stale source'):
            self.engine.apply(changed, plan)
        for field, replacement in [('actions', []), ('binding', 'forged'), ('schema', 'unknown'),
                                   ('full_recovery_steps_bound', True), ('after', {})]:
            bad = deepcopy(plan)
            bad[field] = replacement
            with self.assertRaises(av.Invalid):
                self.engine.apply(full, bad)
        bad = deepcopy(plan)
        bad['actions'][0]['field'] = 'history'
        with self.assertRaises(av.Invalid):
            self.engine.apply(full, bad)
        bad = deepcopy(plan)
        bad['parameters']['replay_budget'] = True
        with self.assertRaises(av.Invalid):
            self.engine.apply(full, bad)

    def test_undo_rejects_stale_or_forged_receipt(self):
        full = self.full()
        plan = self.engine.plan(full)
        cleared = self.engine.apply(full, plan)
        with self.assertRaises(av.Invalid):
            self.engine.undo(full, plan)
        for field, value in [('source', 'forged'), ('target', 'forged'), ('actions', []), ('binding', 'forged')]:
            bad = deepcopy(plan)
            bad[field] = value
            with self.assertRaises(av.Invalid):
                self.engine.undo(cleared, bad)
        bad = deepcopy(plan)
        bad['actions'][0]['view'] = True
        with self.assertRaises(av.Invalid):
            self.engine.undo(cleared, bad)

    def test_replay_evidence_is_not_trusted(self):
        for field, value in [('output', False), ('output', 1), ('trace', [False]), ('trace', [1])]:
            bad = self.full()
            bad['views'][0]['cache'][field]['value'] = value
            with self.assertRaises(av.Invalid):
                self.engine.plan(bad)
        bad = self.full()
        bad['views'][0]['cache']['output']['rule'] = 'asserted-correct'
        with self.assertRaises(av.Invalid):
            self.engine.recover(bad)

    def test_missing_and_changed_dependencies(self):
        bad = self.full()
        del bad['requests'][bad['views'][0]['request']]
        with self.assertRaises(av.Invalid):
            self.engine.recover(bad)
        bad = self.full()
        next(iter(bad['requests'].values()))['input'] = False
        with self.assertRaises(av.Invalid):
            self.engine.plan(bad)

    def test_unknown_fields_and_policy(self):
        for location in ('root', 'view', 'request', 'cache'):
            bad = self.full()
            target = {'root': bad, 'view': bad['views'][0],
                      'request': next(iter(bad['requests'].values())), 'cache': bad['views'][0]['cache']}[location]
            target['untyped'] = 42
            with self.assertRaises(av.Invalid):
                self.engine.plan(bad)
        bad = self.full()
        bad['binding'] = 'stale'
        with self.assertRaises(av.Invalid):
            self.engine.plan(bad)

    def test_limits_and_invalid_instructions(self):
        for r in [{'history': ['eval'], 'input': True}, {'history': [], 'input': 1},
                  {'history': ['stay'] * (av.MAX_STEPS + 1), 'input': True}]:
            with self.assertRaises(av.Invalid):
                self.engine.build([r])
        with self.assertRaises(av.Invalid):
            self.engine.build([{'history': [], 'input': False}] * (av.MAX_REQUESTS + 1))
        with self.assertRaises(av.Invalid):
            self.engine.recover(self.full(), ['history'])

    def test_local_source_staleness(self):
        full = self.full()
        with patch('active_view.file_digest', return_value='0' * 64):
            with self.assertRaisesRegex(av.Invalid, 'sources changed'):
                self.engine.plan(full)

    def test_json_duplicate_keys_and_nonfinite_numbers(self):
        with tempfile.TemporaryDirectory(prefix='active-view-test-') as tmp:
            path = Path(tmp) / 'input.json'
            for text in ('{"input":true,"input":false}', '{"x":NaN}'):
                path.write_text(text, encoding='utf-8')
                with self.assertRaises(av.Invalid):
                    av.load(path)

    def test_small_view_can_cost_more_with_undo_receipt(self):
        full = self.engine.build([{'history': [], 'input': True}])
        plan = self.engine.plan(full)
        cleared = self.engine.apply(full, plan)
        self.assertLess(len(av.wire(cleared)), len(av.wire(full)))
        self.assertGreater(len(av.wire(cleared)) + len(av.wire(plan)), len(av.wire(full)))

    def test_empty_document(self):
        full = self.engine.build([])
        plan = self.engine.plan(full)
        self.assertEqual(plan['actions'], [])
        self.assertEqual(self.engine.recover(self.engine.apply(full, plan))[0], full)

    def test_cli_pipeline(self):
        class Capture:
            def __init__(self):
                self.buffer = io.BytesIO()
        def command(args):
            out = Capture()
            with patch('sys.argv', ['active_view.py'] + args), patch('sys.stdout', out), patch('sys.stderr', io.StringIO()):
                code = av.main()
            self.assertEqual(code, 0)
            return json.loads(out.buffer.getvalue())
        with tempfile.TemporaryDirectory(prefix='active-view-cli-') as tmp:
            tmp = Path(tmp)
            source, full_path, plan_path, clear_path = [tmp / name for name in ('requests.json', 'full.json', 'plan.json', 'clear.json')]
            source.write_bytes(av.wire([{'history': ['stay', 'turn', 'turn'], 'input': True}]))
            full = command(['build', str(source)])
            full_path.write_bytes(av.wire(full))
            plan = command(['plan', str(full_path), '--replay-budget', '3'])
            plan_path.write_bytes(av.wire(plan))
            cleared = command(['apply', str(full_path), str(plan_path)])
            clear_path.write_bytes(av.wire(cleared))
            self.assertEqual(command(['recover', str(clear_path)]), full)
            self.assertEqual(command(['undo', str(clear_path), str(plan_path)]), full)
            self.assertEqual(command(['inspect', str(clear_path)])['visible_fields'], [[]])


if __name__ == '__main__':
    unittest.main()
