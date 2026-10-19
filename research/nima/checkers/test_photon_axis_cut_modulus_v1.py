import json
import unittest
from fractions import Fraction as Q

import check_photon_axis_cut_modulus_v1 as t


class AxisCutModulusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_radius_invariant_retains_h3_and_quartics(self):
        self.assertEqual(self.r['certificate']['axis_radius'],'g3^2/224+f3^2/960')
        self.assertTrue(self.r['nonzero_h3_and_all_quartics_retained'])
        self.assertEqual(self.r['axis_radius_controls'],2187)

    def test_sharp_half_power(self):
        self.assertEqual(self.r['sharp_axis_exponent'],'1/2')
        self.assertTrue(self.r['axis_half_power_exponent_sharp'])
        self.assertTrue(all(Q(row['margin_squared_X'])>=Q(1,4) and Q(row['margin_squared_Y'])>=Q(1,4)
                            for row in self.r['separated_sharpness_controls']))

    def test_pair_controls(self):
        self.assertEqual((self.r['two_point_axis_controls'],self.r['scaled_h3_controls']),(71,3))
        self.assertTrue(self.r['zero_leading_and_zero_cubic_strata_retained'])

    def test_square_root_enclosure_and_zero_gap(self):
        for q in (Q(),Q(1,1000),Q(1,10**90),Q(1000)):
            hi=t.sqrt_upper(q);self.assertGreaterEqual(hi*hi,q)
            if q:self.assertLessEqual(hi*hi,4*q)
        self.assertEqual(t.bound(Q(),Q(1)),0)

    def test_near_axis_is_not_axis(self):
        x=(Q(1),Q(1,10**12),Q(),Q(),Q(),Q(),Q(),Q())
        with self.assertRaises(ValueError):t.check_pair(x,(Q(),)*8,Q(1))

    def test_general_margin_question_still_open(self):
        self.assertFalse(self.r['general_separation_only_sector_classified'])
        self.assertFalse(self.r['physical_axis_or_box_prior_licensed'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('general_separation_only_sector_classified','near_axis_projection_licensed','physical_axis_or_box_prior_licensed',
                    'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
