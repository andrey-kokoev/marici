import unittest
import check_hodge_fourth_prime_type_audit as s


class FourthPrimeTypeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=s.report()

    def test_failed_prediction_is_preserved(self):
        self.assertTrue(self.r['preregistered_both_CM_absent_prediction_falsified'])
        self.assertTrue(self.r['other_tested_literal_3087_excluded'])

    def test_positive_factor_is_opposite_not_same(self):
        self.assertEqual(self.r['same_type_certificate']['degree'],0)
        self.assertEqual(self.r['opposite_type_certificate']['degree'],1)
        self.assertEqual(self.r['inert3_projector']['opposite_eigenvalue'],[5,-4])

    def test_nonunit_polynomial_is_not_unit_veto_or_exact_lattice_denominator(self):
        self.assertFalse(self.r['inert3_projector']['integral_at3'])
        self.assertFalse(self.r['nonunit_polynomial_proves_actual_lattice_denominator'])
        self.assertEqual(self.r['primitive_axis_v3_upper_bound_conditional_on_axis_existence'],1)

    def test_target_valuation_is_conditional_not_axis_or_full_degree(self):
        self.assertEqual(self.r['primitive_axis_v3_values_conditional_on_target_isogeny'],[1])
        self.assertFalse(self.r['actual_opposite_complex_axis_constructed'])
        self.assertFalse(self.r['theta_degree6_constructed'])

    def test_fixed_End_and_norm_hypotheses_cannot_be_dropped(self):
        pol=s.source.previous.pol
        with self.assertRaisesRegex(ValueError,'fixed End field'):pol.norm_parity_certificate(end0='unknown')
        with self.assertRaisesRegex(ValueError,'norm class'):pol.norm_parity_certificate(det=-1)

    def test_partial_CRT_retains_uncounted_and_old_uncertified(self):
        c=self.r['partial_fourth_prime_CRT_partition']
        self.assertEqual(c['excluded_count'],331257)
        self.assertEqual(c['jointly_certified_necessary_classes'],[297459,333703])
        self.assertEqual(c['uncertified_or_uncounted_count'],3998)
        self.assertEqual((-37798)%8177,3087);self.assertEqual((-37798)%41,4)

    def test_four_primes_are_necessary_only(self):
        self.assertEqual(self.r['necessary_screened_primes'],[13,17,37,41])
        self.assertFalse(self.r['all_lifts_of_either_old_CRT_class_excluded'])
        self.assertFalse(self.r['fixed_X6_identified'])
        self.assertFalse(self.r['Hodge_proved']);self.assertFalse(self.r['Hodge_refuted'])


if __name__=='__main__':unittest.main()
