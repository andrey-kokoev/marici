import copy
import json
import unittest
from connect_ledger4320 import HOME, CONTRACT, validate_binding, replay_software, sha, ROOT


class Ledger4320Tests(unittest.TestCase):
    def setUp(self):
        self.binding = json.loads(CONTRACT.read_text())

    def test_live_evidence_and_software_binding(self):
        validate_binding(self.binding)
        result = replay_software()
        self.assertEqual(result['domain_pairs'], 977)
        self.assertEqual(result['final_families'], 32)
        self.assertTrue(result['both_squares'])
        self.assertTrue(result['J4_unchanged'])

    def test_physical_promotion_rejected(self):
        self.binding['boundary']['physical_T9_selected'] = True
        with self.assertRaisesRegex(ValueError, 'strength promotion'):
            validate_binding(self.binding)

    def test_unreviewed_proof_outcome_rejected(self):
        self.binding['conjectures'][0]['outcome'] = '++'
        with self.assertRaisesRegex(ValueError, 'proof-outcome'):
            validate_binding(self.binding)

    def test_evidence_drift_rejected(self):
        key = next(iter(self.binding['evidence_sha256']))
        self.binding['evidence_sha256'][key] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'stale ledger evidence'):
            validate_binding(self.binding)

    def test_software_selection_not_physical_selection(self):
        self.binding['software']['selection_scope'] = 'physical_and_software'
        with self.assertRaisesRegex(ValueError, 'software scope'):
            validate_binding(self.binding)

    def test_programme_keeps_previous_results_and_scattering(self):
        old = json.loads((HOME / 'contracts/programme-hierarchy.v15.json').read_text())
        new = json.loads((HOME / 'contracts/programme-hierarchy.v16.json').read_text())
        changes = {'schema', 'id', 'phase', 'predecessor', 'endpoint_role_binding_gate', 'ledger_evidence_links'}
        self.assertEqual({k: v for k, v in old.items() if k not in changes}, {k: v for k, v in new.items() if k not in changes})
        self.assertTrue(new['ledger_evidence_links'][0]['software_binding_complete'])
        self.assertFalse(new['ledger_evidence_links'][0]['proof_bearing'])
        self.assertFalse(new['endpoint_role_binding_gate']['physical_T9_selected'])
        self.assertEqual(new['scattering_conjecture_nets'], old['scattering_conjecture_nets'])
        registry = json.loads((HOME / 'registry.json').read_text())
        self.assertTrue(any(e['id'] == self.binding['id'] for e in registry['nets']))
        ledger = self.binding['ledger']
        collected = HOME / 'collection' / ledger['path']
        self.assertEqual(sha(collected), ledger['sha256'])


if __name__ == '__main__':
    unittest.main()
