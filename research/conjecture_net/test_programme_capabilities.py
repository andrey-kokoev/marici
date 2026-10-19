import json
import unittest
from check_programme_capabilities import HOME, validate


class CapabilityAttachmentTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v8.json').read_text())
        self.receipt = json.loads((HOME / 'results/pilot-capability-audit.json').read_text())

    def test_live_capability_attachment(self):
        result = validate(self.hierarchy, self.receipt)
        self.assertEqual(result['invisible_directions'], 7)
        self.assertEqual(result['candidate_forks'], 4)
        self.assertIsNone(result['root_outcome'])

    def test_observer_kernel_cannot_be_hidden(self):
        self.receipt['gates']['observation']['propagated_readout_rank'] = 16
        with self.assertRaisesRegex(ValueError, 'capability controls changed'):
            validate(self.hierarchy, self.receipt)

    def test_candidate_enrichment_is_not_a_proof(self):
        self.hierarchy['candidate_synthesis_forks'][1]['outcome'] = '++'
        with self.assertRaisesRegex(ValueError, 'prematurely solved'):
            validate(self.hierarchy, self.receipt)

    def test_audit_does_not_discharge_parent(self):
        self.hierarchy['capability_audits'][0]['discharges_parent_obligation'] = True
        with self.assertRaisesRegex(ValueError, 'programme closure'):
            validate(self.hierarchy, self.receipt)


if __name__ == '__main__':
    unittest.main()
