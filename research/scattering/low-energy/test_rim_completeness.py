"""Controls for the continuum rank-two resolvent support, not a theorem prover."""
import unittest
from fractions import Fraction as Q
import check_rim_completeness as rim


class RimCompletenessTests(unittest.TestCase):
    def test_contact_mismatch_sign(self):
        A=rim.eye(2);Cinv=rim.scale(Q(1,3),rim.eye(2))
        rim.verify_mismatch(A,Cinv)
        with self.assertRaisesRegex(AssertionError,'wrong contact mismatch'):
            rim.verify_mismatch(A,Cinv,sign=1)

    def test_free_green_trace_cannot_be_omitted(self):
        A=rim.scale(Q(1,2),rim.eye(2))
        rim.verify_mismatch(A,rim.scale(Q(1,2),rim.eye(2)))
        with self.assertRaisesRegex(AssertionError,'wrong contact mismatch'):
            rim.verify_mismatch(A,rim.eye(2))

    def test_full_fixture_and_scope(self):
        r=rim.build()
        self.assertEqual(r['resolvent_difference_rank'],2)
        self.assertEqual(r['free_energy_fiber_multiplicity'],4)
        self.assertEqual(r['full_point_dimension'],21)
        self.assertEqual(r['secular_polynomial_determinant_degree'],72)
        self.assertTrue(r['no_singular_continuous_spectrum'])
        self.assertTrue(r['wave_operators_exist_and_complete_on_ac'])
        for key in ('bounded_operator_difference_claimed','all_central_preparations_escape',
                    'analytic_argument_machine_formalized','new_live_proposition_admitted',
                    'C12_protocol_renewed','physical_outcomes_admitted'):
            self.assertFalse(r[key],key)


if __name__=='__main__':unittest.main()
