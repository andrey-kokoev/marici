import json
import unittest
from check_programme_controls import HOME, validate


class ControlAttachmentTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v10.json').read_text())
        self.receipt = json.loads((HOME / 'results/pilot-control-screen.json').read_text())

    def test_live_conditional_screen(self):
        result = validate(self.hierarchy, self.receipt)
        self.assertTrue(result['conditional_u4_family_supplied'])
        self.assertFalse(result['physical_control_authorization'])
        self.assertFalse(result['source_bridge_constructed'])

    def test_symmetry_is_not_an_actuator(self):
        self.hierarchy['conditional_control_screens'][0]['physical_source_selection'] = 'supplied'
        with self.assertRaisesRegex(ValueError, 'promoted beyond scope'):
            validate(self.hierarchy, self.receipt)

    def test_source_enrichment_not_native_derivation(self):
        self.receipt['added_controls_derived_from_native_flips'] = True
        with self.assertRaisesRegex(ValueError, 'verification upgrade'):
            validate(self.hierarchy, self.receipt)


if __name__ == '__main__':
    unittest.main()
