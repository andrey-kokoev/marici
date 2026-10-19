import json
import unittest
from check_programme_carrier import HOME, validate


class FragmentAttachmentTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v7.json').read_text())
        self.audit = json.loads((HOME / 'results/pilot-carrier-interface-audit.json').read_text())

    def test_live_finite_fragment(self):
        result = validate(self.hierarchy, self.audit)
        self.assertEqual(result['implemented_finite_fragments'], 1)
        self.assertFalse(result['new_adapter_admitted'])
        self.assertIsNone(result['root_outcome'])

    def test_premature_admission_rejected(self):
        self.hierarchy['implemented_source_fragments'][0]['proof_bearing'] = True
        with self.assertRaisesRegex(ValueError, 'promoted beyond scope'):
            validate(self.hierarchy, self.audit)

    def test_native_agda_execution_overclaim_rejected(self):
        self.audit['full_native_agda_tick_executed_in_python'] = True
        with self.assertRaisesRegex(ValueError, 'verification upgrade'):
            validate(self.hierarchy, self.audit)

    def test_parent_closure_rejected(self):
        self.hierarchy['obligations'][0]['outcome'] = '++'
        with self.assertRaisesRegex(ValueError, 'programme scope/outcomes changed'):
            validate(self.hierarchy, self.audit)


if __name__ == '__main__':
    unittest.main()
