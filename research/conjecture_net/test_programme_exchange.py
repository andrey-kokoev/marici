import json
import unittest
from check_programme_exchange import HOME, validate


class ExchangeAttachmentTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v11.json').read_text())
        self.receipt = json.loads((HOME / 'results/exchange-source-bridge-audit.json').read_text())

    def test_live_second_structural_instance(self):
        result = validate(self.hierarchy, self.receipt)
        self.assertEqual(result['scoped_structural_instances'], 2)
        self.assertEqual(result['retained_exchange_source_dimension'], 22)
        self.assertFalse(result['physical_source_bridge'])

    def test_common_recipe_not_common_physical_witness(self):
        self.hierarchy['shared_finite_structural_recipe']['one_common_physical_witness'] = True
        with self.assertRaisesRegex(ValueError, 'common physical witness'):
            validate(self.hierarchy, self.receipt)

    def test_typed_ports_not_arbitrary_control_switching(self):
        self.receipt['freely_switchable_six_port_controls_authorized'] = True
        with self.assertRaisesRegex(ValueError, 'verification upgrade'):
            validate(self.hierarchy, self.receipt)


if __name__ == '__main__':
    unittest.main()
