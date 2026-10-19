import json
import unittest
from fractions import Fraction as Q

import check_photon_double_margin_cut_modulus_v1 as t


class DoubleMarginCutModulusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_both_signs_without_prior(self):
        self.assertGreater(self.r['opposite_sign_comparisons'],0)
        self.assertGreater(self.r['same_or_zero_sign_comparisons'],0)
        self.assertTrue(self.r['previously_refused_cross_label_pair_now_admitted'])
        self.assertFalse(self.r['factorization_label_prior_assumed'])

    def test_far_root_controls_not_just_diameter(self):
        controls=self.r['far_opposite_nonzero_h3_all_quartics_controls']
        self.assertEqual(len(controls),3)
        self.assertTrue(all(c['regime']=='far' for c in controls))
        self.assertEqual(self.r['certificate']['far_pair_square_bound'],'s_i^2<=100*delta')

    def test_zero_strata_and_sharpness(self):
        self.assertGreater(self.r['zero_stratum_comparisons'],0)
        self.assertEqual(self.r['full_double_margin_exponent'],'1/2')
        self.assertEqual(len(self.r['sharpness_controls_inherited']),6)

    def test_constants_and_zero_gap(self):
        c=t.constants(Q(1,4),Q(1,10))
        self.assertGreaterEqual(c['A'],Q(439,84))
        self.assertGreaterEqual(c['B'],Q(229,70)/Q(1,4))
        self.assertEqual(t.bound(Q(),Q(1),Q(1,4),Q(1,10)),0)
        self.assertEqual(t.opposite_bound(Q(),Q(1),Q(1,4)),0)

    def test_leading_trace_scope_preserved(self):
        self.assertTrue(self.r['cancelled_leading_trace_opposite_lemma_control'])
        self.assertFalse(self.r['opposite_root_lemma_requires_leading_trace_margin'])
        self.assertFalse(self.r['discriminant_margin_alone_full_sector_half_power'])

    def test_mathematical_not_native_completion(self):
        self.assertTrue(self.r['bounded_double_margin_frontier_resolved'])
        self.assertFalse(self.r['full_physical_programme_complete'])
        self.assertFalse(self.r['native_source_box_margin_or_noise_licensed'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('factorization_label_prior_assumed','common_ray_assumed','cubic_single_minus_margin_assumed',
                    'discriminant_margin_alone_full_sector_half_power','native_source_box_margin_or_noise_licensed',
                    'physical_matching_selected','native_or_UV_dynamics_derived','full_physical_programme_complete','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
