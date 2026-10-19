import json
import unittest
from check_programme_transport import HOME, validate


class AttachmentTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v4.json').read_text())
        self.audit = json.loads((HOME / 'results/structural-pilot-transport-audit.json').read_text())

    def test_live_attachment(self):
        self.assertEqual(validate(self.hierarchy, self.audit)['programme_proof_links_admitted'], 0)

    def test_admission_without_review_rejected(self):
        self.hierarchy['structural_pilot_transports'][0]['proof_bearing'] = True
        with self.assertRaisesRegex(ValueError, 'prematurely admitted'):
            validate(self.hierarchy, self.audit)

    def test_stale_contract_rejected(self):
        self.hierarchy['structural_pilot_transports'][0]['contract_sha256'] = '0' * 64
        with self.assertRaisesRegex(ValueError, 'contract drift'):
            validate(self.hierarchy, self.audit)

    def test_audit_cannot_supply_kernel_upgrade(self):
        self.audit['new_transport_kernel_proved'] = True
        with self.assertRaisesRegex(ValueError, 'overclaim'):
            validate(self.hierarchy, self.audit)


if __name__ == '__main__':
    unittest.main()
