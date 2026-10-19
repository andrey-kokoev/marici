import json
import unittest

import check_photon_joint_transport_v1 as t


class JointTransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_augmented_inverse(self):self.assertEqual(self.r['certificate']['augmented_linear_inverse_basis_checks'],7)

    def test_all_source_charts(self):
        self.assertEqual(self.r['source_checks'],414)
        self.assertEqual(self.r['chart_counts'],{'g2-nonzero':352,'f2-only':2,'zero-leading':60})

    def test_actual_fibres_preserved(self):
        self.assertTrue(self.r['source_fibres_equal_full_joint_cut_fibres'])
        self.assertEqual(self.r['zero_leading_quartic_free_dimension'],3)

    def test_irrational_branches(self):self.assertEqual(self.r['algebraic_controls'],3)

    def test_full_real_image_checks(self):self.assertEqual(self.r['invalid_joint_data_refused'],6)

    def test_no_transport_only_or_stability_promotion(self):
        self.assertFalse(self.r['transport_alone_recovers_full_cut'])
        self.assertFalse(self.r['uniformly_stable_cut_reconstruction_derived'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('transport_alone_recovers_full_cut','uniformly_stable_cut_reconstruction_derived',
                    'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
