import json
import unittest
from fractions import Fraction as Q

import check_photon_margin_only_obstruction_v1 as t


class MarginOnlyObstructionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_positive_margin_same_branch(self):
        self.assertEqual(self.r['normalized_discriminant_margin_lower'],'2')
        self.assertTrue(self.r['same_factorization_branch_sign_retained'])

    def test_h3_mode_not_erased(self):
        self.assertTrue(self.r['independent_nonzero_h3_retained'])
        self.assertEqual(self.r['radical_source_index'],4)
        self.assertEqual(self.r['normalized_leading_single_minus_trace'],'0')
        self.assertTrue(self.r['cubic_single_minus_trace_nonzero'])

    def test_uniform_unit_box(self):
        self.assertTrue(all(Q(v)<1 for row in self.r['uniform_source_coordinate_bounds'].values() for v in row))
        self.assertTrue(self.r['all_twelve_product_difference_identities'])

    def test_gap_order(self):
        self.assertEqual(self.r['data_gap_over_r_cubed_limit'],'72')
        self.assertEqual(self.r['cut_gap_over_r_limit'],'1/11200')
        self.assertEqual(self.r['excluded_exponents'],'alpha>1/3')

    def test_algebraic_root_isolation(self):
        f=lambda x:588553*x*x-475440*x-9509250
        self.assertLess(f(Q(4)),0);self.assertGreater(f(Q(9,2)),0)
        self.assertEqual(len(self.r['exact_samples']),3)

    def test_double_margin_not_claimed(self):self.assertFalse(self.r['double_margin_sector_classified'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('double_margin_sector_classified','physical_margin_or_source_box_licensed','physical_matching_selected',
                    'native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
