import json
import unittest
from check_programme_endpoint_roles import HOME, validate


class EndpointRoleAttachmentTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v13.json').read_text())
        self.receipt = json.loads((HOME / 'results/marked137-endpoint-audit.json').read_text())

    def test_live_endpoint_branch(self):
        result = validate(self.hierarchy, self.receipt)
        self.assertEqual(result['endpoint_role_grouping_counts'], [32, 1])
        self.assertEqual(result['partial_endpoint_readouts'], 145)
        self.assertFalse(result['intended_T9_selected'])

    def test_endpoint_observer_not_inverse_connector(self):
        self.hierarchy['source_endpoint_audits'][0]['readout_is_invertible_connector'] = True
        with self.assertRaisesRegex(ValueError, 'promoted to a constructor'):
            validate(self.hierarchy, self.receipt)

    def test_role_view_not_intended_constructor_selection(self):
        self.hierarchy['source_endpoint_audits'][0]['intended_T9_selected'] = True
        with self.assertRaisesRegex(ValueError, 'promoted to a constructor'):
            validate(self.hierarchy, self.receipt)


if __name__ == '__main__':
    unittest.main()
