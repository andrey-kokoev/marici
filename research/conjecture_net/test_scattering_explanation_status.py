import json
import unittest
from capture_scattering_explanation import ASSESSMENT, HOME, validate


class ScatteringExplanationStatusTests(unittest.TestCase):
    def setUp(self):
        self.status = json.loads(ASSESSMENT.read_text())

    def test_existing_net_and_gaps_are_bound(self):
        self.assertTrue(validate(self.status))
        self.assertEqual(self.status['assessment'], 'physical_scattering_not_yet_explained')
        self.assertEqual(len(self.status['remaining_gaps']), 3)

    def test_wiring_does_not_become_physical_explanation(self):
        self.status['boundary']['wiring_is_proof'] = True
        with self.assertRaisesRegex(ValueError, 'strength promotion'):
            validate(self.status)

    def test_software_closure_does_not_close_physics(self):
        self.status['ledger4320']['physical_reference_boundary_closed'] = True
        with self.assertRaisesRegex(ValueError, 'boundary conflated'):
            validate(self.status)

    def test_gap_cannot_silently_close(self):
        self.status['remaining_gaps'][0]['status'] = 'proved'
        with self.assertRaisesRegex(ValueError, 'silently closed'):
            validate(self.status)

    def test_unestablished_does_not_mean_refuted(self):
        self.status['boundary']['physical_scattering_refuted'] = True
        with self.assertRaisesRegex(ValueError, 'strength promotion'):
            validate(self.status)

    def test_source_justification_gap_cannot_be_replaced(self):
        self.status['remaining_gaps'][1]['id'] = 'mere_implementation_cleanup'
        with self.assertRaisesRegex(ValueError, 'gap set changed'):
            validate(self.status)

    def test_evidence_pins_cannot_be_dropped(self):
        self.status['source_sha256'] = {}
        with self.assertRaisesRegex(ValueError, 'pins incomplete'):
            validate(self.status)

    def test_programme_preserves_previous_bindings(self):
        old = json.loads((HOME / 'contracts/programme-hierarchy.v16.json').read_text())
        new = json.loads((HOME / 'contracts/programme-hierarchy.v17.json').read_text())
        changed = {'schema', 'id', 'phase', 'predecessor', 'scattering_explanation_assessments'}
        self.assertEqual({k: v for k, v in old.items() if k not in changed}, {k: v for k, v in new.items() if k not in changed})
        self.assertFalse(new['scattering_explanation_assessments'][0]['proof_bearing'])
        self.assertIsNone(new['root']['outcome'])


if __name__ == '__main__':
    unittest.main()
