import json
import unittest
from fractions import Fraction
from pilot_controls import candidate_families, lie_closure, RealSpan, fixes_uniform
from check_pilot_control_screen import HOME, audit, validate_contract
from check_structural_pilot_transport import zeros


class ControlScreenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = audit()

    def test_exact_conditional_dimensions(self):
        dimensions = {name: family['real_lie_dimension'] for name, family in self.result['families'].items()}
        self.assertEqual(dimensions, {'native-local': 2, 'native-plus-exchange': 5, 'all-label-transpositions': 9,
                                     'native-plus-local-phase': 7, 'local-phase-plus-exchange': 16})

    def test_permutation_enrichment_keeps_uniform_obstruction(self):
        for name in ('native-local', 'native-plus-exchange', 'all-label-transpositions'):
            self.assertTrue(self.result['families'][name]['fixes_uniform_vector'])
            self.assertFalse(self.result['families'][name]['full_u4_algebra'])

    def test_local_phase_control_does_not_entangle_arbitrarily(self):
        self.assertFalse(self.result['families']['native-plus-local-phase']['full_u4_algebra'])
        self.assertEqual(self.result['families']['native-plus-local-phase']['real_lie_dimension'], 7)

    def test_full_conditional_family_not_physical_authorization(self):
        family = self.result['families']['local-phase-plus-exchange']
        self.assertTrue(family['full_u4_algebra'])
        self.assertFalse(family['physical_actuator_authorization'])

    def test_global_phase_is_explicit(self):
        self.assertFalse(self.result['families']['all-label-transpositions']['contains_global_phase_generator'])
        self.assertTrue(self.result['families']['local-phase-plus-exchange']['contains_global_phase_generator'])

    def test_exact_independence_no_tolerance(self):
        span = RealSpan()
        self.assertTrue(span.add([1, 1]))
        self.assertTrue(span.add([1, 1 + Fraction(1, 10**100)]))

    def test_nonhermitian_control_rejected(self):
        bad = zeros(4)
        bad[0][1] = 1
        with self.assertRaisesRegex(ValueError, 'real symmetric'):
            lie_closure([bad])

    def test_missing_added_control_premise_rejected(self):
        contract = json.loads((HOME / 'contracts/pilot-control-screen.v1.json').read_text())
        contract['families'][-1]['extra_premises'] = []
        with self.assertRaisesRegex(ValueError, 'lack explicit premises'):
            validate_contract(contract)


if __name__ == '__main__':
    unittest.main()
