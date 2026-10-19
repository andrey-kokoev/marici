import json
import unittest
from check_programme_joint_defects import HOME, validate


class JointDefectAttachmentTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v14.json').read_text())
        self.receipt = json.loads((HOME / 'results/joint-defect-audit.json').read_text())

    def test_live_restricted_joint_interface(self):
        result = validate(self.hierarchy, self.receipt)
        self.assertEqual(result['joint_structural_rank'], 55)
        self.assertEqual(result['frozen_response_completion_rank'], 56)
        self.assertEqual(result['governing_sewing_conjecture'], 'falsified')

    def test_no_implicit_chain_map(self):
        self.hierarchy['joint_defect_interfaces'][0]['chain_map_constructed'] = True
        with self.assertRaisesRegex(ValueError, 'beyond their source stratum'):
            validate(self.hierarchy, self.receipt)

    def test_falsifier_cannot_become_sewing_proof(self):
        self.receipt['governing_conjecture_falsified'] = False
        with self.assertRaisesRegex(ValueError, 'relabelled as sewing proof'):
            validate(self.hierarchy, self.receipt)


if __name__ == '__main__':
    unittest.main()
