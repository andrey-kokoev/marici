import json
import unittest
from check_programme_observers import HOME, validate


class ObserverAttachmentTests(unittest.TestCase):
    def setUp(self):
        self.hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v9.json').read_text())
        self.receipt = json.loads((HOME / 'results/pilot-observer-extension-audit.json').read_text())

    def test_live_observer_construction(self):
        result = validate(self.hierarchy, self.receipt)
        self.assertEqual(result['mathematical_observation_rank'], 16)
        self.assertFalse(result['physical_observers_authorized'])
        self.assertEqual(result['continuous_control_dimension'], 2)

    def test_mathematical_effects_not_physical_instruments(self):
        self.hierarchy['mathematical_observer_extensions'][0]['physical_observer_authorization'] = 'supplied'
        with self.assertRaisesRegex(ValueError, 'promoted beyond scope'):
            validate(self.hierarchy, self.receipt)

    def test_tomography_does_not_supply_control(self):
        self.receipt['new_controls_supplied'] = True
        with self.assertRaisesRegex(ValueError, 'verification upgrade'):
            validate(self.hierarchy, self.receipt)


if __name__ == '__main__':
    unittest.main()
