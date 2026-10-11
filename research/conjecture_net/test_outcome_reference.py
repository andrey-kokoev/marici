import copy
import json
from pathlib import Path
import tempfile
import unittest
from outcome_reference import PORTS, SEMANTICS, OutcomeReferenceError, file_hash, resolve

class OutcomeReferenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.make()

    def put(self, path, value):
        (self.root / path).write_text(json.dumps(value, sort_keys=True), encoding='utf-8')

    def make(self, outcome='++'):
        self.claim = {'id': 'p', 'statement': 'Scoped proposition P', 'scope_id': 'scope-v1'}
        self.contract = {'outcome_ports': PORTS, 'nodes': [dict(self.claim, outcome=outcome)]}
        self.put('contract.json', self.contract)
        self.put('result.json', {'status': 'pass', 'claim': 'p', 'outcome': outcome})
        self.verification = {'proof_kind': 'written-proof', 'kernel_verified_analytic_theorem': False}
        self.put('receipt.json', dict(self.verification, status='pass'))
        self.export = {
            'schema': 'marici.conjecture-net.outcome-export.v1', 'export_id': 'p-v1',
            'outcome_semantics': SEMANTICS, 'head_path': 'head.json',
            'artifact_sha256': {p: file_hash(self.root, p) for p in ('contract.json', 'result.json', 'receipt.json')},
            'source': {'contract': 'contract.json', 'result': 'result.json', 'node_pointer': '/nodes/0',
                       'result_claim_pointer': '/claim', 'result_outcome_pointer': '/outcome'},
            'claim_bindings': {k: '/nodes/0/' + k for k in self.claim}, 'claim': self.claim,
            'outcome': outcome, 'verification_receipt': 'receipt.json', 'verification': self.verification,
        }
        self.pointer = {'schema': 'marici.conjecture-net.outcome-pointer.v1', 'head': 'head.json',
                        'expected_claim': copy.deepcopy(self.claim), 'expected_outcome': outcome,
                        'accepted_verification': copy.deepcopy(self.verification)}
        self.publish()

    def publish(self):
        self.put('export.json', self.export)
        ref = {'path': 'export.json', 'sha256': file_hash(self.root, 'export.json')}
        self.pointer['export'] = ref
        self.put('head.json', {'schema': 'marici.conjecture-net.outcome-head.v1', 'status': 'active',
                              'export_id': 'p-v1', 'export': ref})

    def test_import(self):
        self.assertIs(resolve(self.root, self.pointer)['proposition_truth'], True)

    def test_all_attempt_outcomes_without_polarity_conflation(self):
        for outcome, truth in [('++', True), ('-+', False), ('+-', None), ('--', None)]:
            self.make(outcome)
            r = resolve(self.root, self.pointer)
            self.assertIs(r['proposition_truth'], truth)
            self.assertEqual(r['resolved_proposition'], truth is not None)

    def test_scope_mismatch(self):
        self.pointer['expected_claim']['scope_id'] = 'stronger-scope'
        with self.assertRaisesRegex(OutcomeReferenceError, 'scope mismatch'):
            resolve(self.root, self.pointer)

    def test_correction_invalidates_live_import(self):
        self.contract['nodes'][0]['outcome'] = '-+'
        self.put('contract.json', self.contract)
        with self.assertRaisesRegex(OutcomeReferenceError, 'stale source'):
            resolve(self.root, self.pointer)

    def test_changed_evidence(self):
        self.put('receipt.json', {'status': 'fail'})
        with self.assertRaisesRegex(OutcomeReferenceError, 'stale source'):
            resolve(self.root, self.pointer)

    def test_revocation_and_supersession(self):
        for status in ('revoked', 'superseded'):
            self.put('head.json', {'schema': 'marici.conjecture-net.outcome-head.v1', 'status': status,
                                  'export_id': 'p-v1', 'export': self.pointer['export']})
            with self.assertRaisesRegex(OutcomeReferenceError, 'revoked or superseded'):
                resolve(self.root, self.pointer)

    def test_changed_active_head_requires_repinning(self):
        self.put('head.json', {'schema': 'marici.conjecture-net.outcome-head.v1', 'status': 'active',
                              'export_id': 'p-v1', 'export': {'path': 'new-export.json', 'sha256': 'new'}})
        with self.assertRaisesRegex(OutcomeReferenceError, 'revoked or superseded'):
            resolve(self.root, self.pointer)

    def test_incomplete_scope_export(self):
        del self.export['claim_bindings']['scope_id']
        del self.export['claim']['scope_id']
        del self.pointer['expected_claim']['scope_id']
        self.publish()
        with self.assertRaisesRegex(OutcomeReferenceError, 'bindings incomplete'):
            resolve(self.root, self.pointer)

    def test_no_verification_upgrade(self):
        self.pointer['accepted_verification']['kernel_verified_analytic_theorem'] = True
        with self.assertRaisesRegex(OutcomeReferenceError, 'verification-level mismatch'):
            resolve(self.root, self.pointer)

    def test_export_tampering(self):
        self.put('export.json', {})
        with self.assertRaisesRegex(OutcomeReferenceError, 'digest mismatch'):
            resolve(self.root, self.pointer)

    def test_no_false_outcome_even_if_export_rehashed(self):
        self.export['outcome'] = '-+'
        self.pointer['expected_outcome'] = '-+'
        self.publish()
        with self.assertRaisesRegex(OutcomeReferenceError, 'outcome mismatch'):
            resolve(self.root, self.pointer)

    def test_no_polarity_export(self):
        self.export['outcome_semantics'] = 'signed-port-arrows'
        self.publish()
        with self.assertRaisesRegex(OutcomeReferenceError, 'polarity'):
            resolve(self.root, self.pointer)

    def test_no_unpinned_source(self):
        del self.export['artifact_sha256']['receipt.json']
        self.publish()
        with self.assertRaisesRegex(OutcomeReferenceError, 'unpinned source'):
            resolve(self.root, self.pointer)

    def test_no_path_escape(self):
        self.pointer['export']['path'] = '../outside.json'
        with self.assertRaisesRegex(OutcomeReferenceError, 'escapes repository'):
            resolve(self.root, self.pointer)

if __name__ == '__main__':
    unittest.main()
