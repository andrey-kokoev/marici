"""Regression boundaries for the local operational whole-return outcome export."""
import copy
import json
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch

import export_operational_whole_return as exporter
from outcome_reference import OutcomeReferenceError, load


class ExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temporary = tempfile.TemporaryDirectory()
        cls.root = Path(cls.temporary.name)
        cls.pointer = load(exporter.REPO, exporter.POINTER)
        export = load(exporter.REPO, cls.pointer['export']['path'])
        paths = set(export['artifact_sha256']) | {
            exporter.HEAD, exporter.POINTER, cls.pointer['export']['path']}
        for relative in paths:
            target = cls.root / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(exporter.REPO / relative, target)

    @classmethod
    def tearDownClass(cls):
        cls.temporary.cleanup()

    def setUp(self):
        self.root_patch = patch.object(exporter, 'REPO', self.root)
        self.root_patch.start()
        self.addCleanup(self.root_patch.stop)

    def change(self, relative, content):
        path = self.root / relative
        original = path.read_bytes()
        self.addCleanup(path.write_bytes, original)
        path.write_bytes(content)

    def test_live_mixed_level(self):
        result = exporter.check(self.pointer)
        self.assertEqual(result['outcome'], '++')
        self.assertTrue(result['verification']['operational_kernel_bundle_proved'])
        self.assertFalse(result['verification']['kernel_verified_analytic_theorem'])
        self.assertFalse(result['verification']['semantic_correspondence_kernel_proved'])

    def test_semantic_kernel_upgrade_rejected(self):
        pointer = copy.deepcopy(self.pointer)
        pointer['accepted_verification']['semantic_correspondence_kernel_proved'] = True
        with self.assertRaisesRegex(OutcomeReferenceError, 'verification-level mismatch'):
            exporter.check(pointer)

    def test_different_scope_rejected(self):
        pointer = copy.deepcopy(self.pointer)
        pointer['expected_claim']['scope_id'] = 'unique-physical-dynamics'
        with self.assertRaisesRegex(OutcomeReferenceError, 'scope mismatch'):
            exporter.check(pointer)

    def test_stale_acceptance_rejected(self):
        self.change(exporter.ACCEPTED, b'{}')
        with self.assertRaisesRegex(OutcomeReferenceError, 'stale source/evidence'):
            exporter.check(self.pointer)

    def test_revoked_head_rejected(self):
        head = load(self.root, exporter.HEAD)
        head['status'] = 'revoked'
        self.change(exporter.HEAD, exporter.encode(head))
        with self.assertRaisesRegex(OutcomeReferenceError, 'revoked or superseded'):
            exporter.check(self.pointer)

    def test_adapter_drift_rejected(self):
        adapter = load(self.root, exporter.ADAPTER)
        adapter['conjectures'][0]['outcome'] = '-+'
        self.change(exporter.ADAPTER, exporter.encode(adapter))
        with self.assertRaisesRegex(OutcomeReferenceError, 'stale source/evidence'):
            exporter.check(self.pointer)

    def test_external_compiler_drift_rejected(self):
        path = self.root / 'dummy-compiler'
        path.write_bytes(b'changed')
        with self.assertRaisesRegex(OutcomeReferenceError, 'stale external/compiler'):
            exporter.verify_external({'external_dependency_sha256': {str(path): '0' * 64}})

    def test_reexport_deterministic(self):
        payload, pointer, receipt, adapter = exporter.prepare()
        self.assertEqual(pointer, self.pointer)
        self.assertEqual(payload, (self.root / pointer['export']['path']).read_bytes())
        self.assertEqual(receipt, (self.root / exporter.RECEIPT).read_bytes())
        self.assertEqual(adapter, (self.root / exporter.ADAPTER).read_bytes())

    def test_implicit_head_reactivation_refused(self):
        head = load(self.root, exporter.HEAD)
        head['status'] = 'revoked'
        self.change(exporter.HEAD, exporter.encode(head))
        with patch.object(exporter.subprocess, 'run'), patch('sys.argv', ['export']):
            with self.assertRaisesRegex(OutcomeReferenceError, 'Refusing implicit correction'):
                exporter.main()
        self.assertEqual(load(self.root, exporter.HEAD)['status'], 'revoked')


if __name__ == '__main__':
    unittest.main()
