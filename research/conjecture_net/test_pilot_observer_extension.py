import json
import unittest
from fractions import Fraction
from pilot_observers import factor_generators, product_probes, spectral_effect
from check_pilot_observer_extension import HOME, audit, validate_contract


class ObserverExtensionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = audit()

    def test_uniform_complete_family(self):
        self.assertEqual(self.result['settings'], 9)
        self.assertEqual(self.result['complete_effects'], 36)
        self.assertEqual(self.result['hermitian_observation_rank'], 16)
        self.assertEqual(self.result['basis_reconstruction_cases'], 16)

    def test_old_observer_gap_stays_scoped(self):
        self.assertEqual(self.result['old_restricted_observer_rank'], 9)

    def test_old_hostile_separated(self):
        records = self.result['old_hostile_separation']
        self.assertEqual(records['rho_plus_record'], '3/8')
        self.assertEqual(records['rho_minus_record'], '1/8')

    def test_positive_finite_bound_not_control_claim(self):
        self.assertEqual(self.result['full_finite_lower_bound'], '1/4')
        self.assertEqual(self.result['continuous_control_dimension_unchanged'], 2)

    def test_marking_covariance(self):
        self.assertEqual(self.result['covariance_cells'], 108)

    def test_invalid_outcome_rejected(self):
        with self.assertRaisesRegex(ValueError, 'outcome sign'):
            spectral_effect(factor_generators()['X'], 0)

    def test_physical_instrument_upgrade_rejected(self):
        contract = json.loads((HOME / 'contracts/pilot-observer-extension.v1.json').read_text())
        contract['boundary']['physical_observers_authorized'] = True
        with self.assertRaisesRegex(ValueError, 'boundary promotion'):
            validate_contract(contract)

    def test_observer_not_actuator(self):
        contract = json.loads((HOME / 'contracts/pilot-observer-extension.v1.json').read_text())
        contract['boundary']['new_controls_supplied'] = True
        with self.assertRaisesRegex(ValueError, 'boundary promotion'):
            validate_contract(contract)


if __name__ == '__main__':
    unittest.main()
