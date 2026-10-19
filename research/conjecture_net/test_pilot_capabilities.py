import json
import unittest
from fractions import Fraction
from check_pilot_capabilities import HOME, audit, rank, validate_contract


class CapabilityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = audit()

    def test_action_capability_not_inferred_from_label_orbit(self):
        action = self.result['action']
        self.assertEqual(action['native_label_orbit_size'], 4)
        self.assertEqual(action['linear_action_algebra_dimension'], 4)
        self.assertEqual(action['continuous_control_lie_dimension'], 2)
        self.assertFalse(action['full_unitary_control_supplied'])

    def test_seven_observer_directions_missing(self):
        observation = self.result['observation']
        self.assertEqual(observation['propagated_readout_rank'], 9)
        self.assertEqual(set(observation['invisible_pauli_directions']), {'IX', 'XI', 'XX', 'XY', 'XZ', 'YX', 'ZX'})
        self.assertTrue(observation['native_label_separation'])
        self.assertFalse(observation['full_hermitian_observation_supplied'])

    def test_positive_normalized_hostile(self):
        hostile = self.result['hostile']
        self.assertEqual(hostile['trace_each'], '1')
        self.assertEqual(hostile['positive_eigenvalues'], ['3/8', '1/8'])
        self.assertTrue(hostile['same_propagated_coordinate_records'])

    def test_finite_bound_does_not_extend_over_kernel(self):
        stability = self.result['finite_stability']
        self.assertEqual(stability['visible_lower_bound'], '1/4')
        self.assertEqual(stability['full_hermitian_domain_lower_bound'], '0')
        self.assertFalse(stability['infinite_completion_claimed'])

    def test_exact_rank_no_float_tolerance(self):
        self.assertEqual(rank([[1, 1], [1, 1 + Fraction(1, 10**100)]]), 2)
        self.assertEqual(rank([[1, 1], [2, 2]]), 1)

    def test_physical_promotion_rejected(self):
        contract = json.loads((HOME / 'contracts/pilot-capability-audit.v1.json').read_text())
        contract['boundary']['physical_observers_authorized'] = True
        with self.assertRaisesRegex(ValueError, 'boundary upgrade'):
            validate_contract(contract)


if __name__ == '__main__':
    unittest.main()
