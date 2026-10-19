import json
import unittest
from fractions import Fraction as Q

import check_photon_box_cut_sharpness_v1 as t


class BoxCutSharpnessTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_sharp_power(self):
        self.assertEqual(self.r['sharp_exponent'],'1/3')
        self.assertEqual(self.r['excluded_exponents'],'alpha>1/3')
        self.assertTrue(self.r['one_third_cut_exponent_sharp'])

    def test_exact_algebraic_source(self):
        self.assertEqual(self.r['algebraic_leading_ratio_square'],'175/72')
        self.assertEqual(self.r['source_coefficients_in_basis_1_k']['parity'],[1,0,1,0,0,1,1,0])

    def test_uniform_unit_box_not_only_samples(self):
        self.assertTrue(all(Q(v)<1 for row in self.r['uniform_source_coordinate_bounds'] for v in row))
        for side in ('X','Y'):
            self.assertTrue(all(Q(v['denominator'][0])!=0 for v in self.r['source_coefficients_in_basis_1_k'][side]))

    def test_positive_uniform_gap_constants(self):
        for key in ('data_gap_upper_coefficient','data_gap_positive_lower_coefficient','cut_gap_positive_lower_coefficient'):
            self.assertGreater(Q(self.r[key]),0)

    def test_gap_orders_and_limits(self):
        self.assertEqual(self.r['data_gap_over_r_cubed_limit'],'1000/113')
        self.assertEqual(self.r['cut_gap_over_r_limit'],'5/50624')
        self.assertEqual(len(self.r['exact_samples']),3)
        self.assertTrue(self.r['equal_degree5_data_and_transport_certified'])

    def test_rational_function_exact_cancellation(self):
        r=t.RF((0,1));self.assertEqual((r*r)/r,r)
        self.assertEqual(((1+r)*(1-r))/(1-r),1+r)

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('uniform_half_power_cut_modulus_derived','optimal_modulus_prefactor_derived','physical_source_box_licensed',
                    'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
