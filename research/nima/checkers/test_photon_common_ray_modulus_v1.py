import json
import unittest
from fractions import Fraction as Q

import check_photon_common_ray_modulus_v1 as t


class CommonRayModulusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_positive_radius_certificate(self):
        c=self.r['certificate']
        self.assertEqual((c['quartic_polynomial_cancellation_constraints'],c['cubic_coefficient_constraints']),(12,18))
        self.assertEqual(c['metric_eigenvalue_lower'],'49/7680')
        self.assertEqual(c['radius_data_gain'],'3821/36')

    def test_single_source_coercivity_not_pairwise(self):
        self.assertEqual(self.r['single_source_cut_coercivity_gain'],'80879/1029')
        self.assertTrue(self.r['universal_single_source_zero_transport_coercivity'])

    def test_general_ray_controls(self):
        self.assertEqual((self.r['radius_identity_controls'],self.r['two_data_common_ray_controls']),(3240,64))
        self.assertTrue(self.r['cubic_trace_zero_control'])
        self.assertTrue(self.r['nonzero_h3_and_all_quartics_retained'])

    def test_half_power_sharpness(self):
        self.assertEqual(self.r['sharp_common_ray_exponent'],'1/2')
        self.assertEqual(len(self.r['sharpness_controls']),4)

    def test_zero_gap_and_valid_margin(self):
        self.assertEqual(t.bound(Q(),Q(1),Q(1,10)),0)
        with self.assertRaises(AssertionError):t.constants(Q(1),Q())

    def test_no_cross_ray_conclusion(self):
        self.assertFalse(self.r['general_cross_ray_double_margin_sector_classified'])
        self.assertFalse(self.r['near_ray_projection_licensed'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('general_cross_ray_double_margin_sector_classified','common_ray_or_margin_physically_licensed',
                    'near_ray_projection_licensed','physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
