"""Regression tests for shared proof-attempt semantics in the local tower net."""
import copy
import unittest
from unittest.mock import patch
import check_marici_tower_cut_domain_net as net


class AttemptOutcomes(unittest.TestCase):
    def setUp(self):
        self.hash_patch = patch.object(net, 'file_hash', return_value='synthetic-receipt-hash')
        self.hash_patch.start()
        self.addCleanup(self.hash_patch.stop)

    def node(self, outcome):
        node = {
            'id': 'synthetic-proposition', 'statement': 'Synthetic test proposition only',
            'scope_id': 'one-frozen-proposition',
            'status': 'resolved' if outcome in ('++', '-+') else 'open',
            'outcome': outcome,
            'attempts': [{'intent': net.PORTS[outcome]['attempt'], 'outcome': outcome,
                          'scope_id': 'one-frozen-proposition', 'receipt': 'synthetic-receipt.json',
                          'verification_level': 'test fixture only', 'evidence_group': 'fixture',
                          'receipt_sha256': 'synthetic-receipt-hash'}],
        }
        node['attempts'][0]['claim_sha256'] = net.claim_hash(node)
        return node

    def test_all_four_ports(self):
        # Test fixtures only: no scientific attempts are generated or recorded.
        with patch.object(net, 'load', return_value={'status': 'pass'}):
            for outcome in net.PORTS:
                with self.subTest(outcome=outcome):
                    node = self.node(outcome)
                    net.validate_attempts(node)
                    self.assertEqual(net.attempt_outcome(node['attempts']), outcome)

    def test_unattempted_is_not_failed(self):
        node = {'scope_id': 'unattempted', 'outcome': None, 'attempts': [], 'status': 'open'}
        net.validate_attempts(node)
        self.assertIsNone(net.attempt_outcome([]))

    def test_failed_attempts_remain_history_not_truth(self):
        failed = self.node('+-')['attempts'] + self.node('--')['attempts']
        self.assertEqual(net.attempt_outcome(failed), '--')
        history = copy.deepcopy(failed) + self.node('++')['attempts']
        self.assertEqual(net.attempt_outcome(history), '++')
        self.assertEqual([a['outcome'] for a in history], ['+-', '--', '++'])
        self.assertEqual([a['outcome'] for a in failed], ['+-', '--'])

    def test_failed_refutation_does_not_erase_a_proof(self):
        history = self.node('++')['attempts'] + self.node('--')['attempts']
        self.assertEqual(net.attempt_outcome(history), '++')

    def test_conflicting_claim_outcomes_require_correction(self):
        with self.assertRaisesRegex(ValueError, 'Conflicting outcomes'):
            net.attempt_outcome(self.node('++')['attempts'] + self.node('-+')['attempts'])

    def test_failed_attempts_cannot_resolve(self):
        with patch.object(net, 'load', return_value={'status': 'pass'}):
            for outcome in ('+-', '--'):
                node = self.node(outcome)
                node['status'] = 'resolved'
                with self.assertRaisesRegex(ValueError, 'Failed attempt'):
                    net.validate_attempts(node)

    def test_checker_pass_does_not_turn_refutation_into_proof(self):
        with patch.object(net, 'load', return_value={'status': 'pass'}):
            node = self.node('-+')
            net.validate_attempts(node)
            self.assertEqual(node['outcome'], '-+')

    def test_scope_and_intent_are_checked(self):
        with patch.object(net, 'load', return_value={'status': 'pass'}):
            for field, bad in (('scope_id', 'larger-domain'), ('intent', 'reject')):
                node = self.node('++')
                node['attempts'][0][field] = bad
                with self.assertRaises(ValueError):
                    net.validate_attempts(node)

    def test_inspection_is_not_an_import(self):
        with patch.object(net, 'load', return_value={'status': 'pass'}):
            node = self.node('++')
            node['status'] = 'recorded'
            with self.assertRaisesRegex(ValueError, 'silently imported'):
                net.validate_attempts(node)


if __name__ == '__main__':
    unittest.main()
