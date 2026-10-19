import json
import unittest
from fractions import Fraction as Q

import check_photon_branchwise_double_margin_v1 as t


class BranchwiseDoubleMarginTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_cross_ray_scope(self):
        self.assertTrue(self.r['no_common_ray_assumption'])
        self.assertGreater(self.r['cross_ray_comparisons'],0)
        self.assertTrue(self.r['explicit_fractional_h3_cross_ray_control'])
        self.assertTrue(self.r['pairwise_projection_and_auxiliary_ratio_controls'])

    def test_both_sign_sectors(self):
        self.assertEqual(set(self.r['control_counts_by_branch']),{'-1','1'})
        self.assertTrue(all(v['two_point_controls']>0 for v in self.r['control_counts_by_branch'].values()))

    def test_computable_constants(self):
        c=t.constants(Q(1,4),Q(1,10))
        self.assertTrue(all(v>0 for v in c.values()))
        self.assertEqual(t.bound(Q(),Q(1),Q(1,4),Q(1,10)),0)
        self.assertFalse(self.r['cubic_single_minus_margin_assumed'])
        self.assertTrue(self.r['explicit_cubic_trace_zero_control'])

    def test_sharp_half_power(self):
        self.assertEqual(self.r['uniform_cut_exponent'],'1/2')
        self.assertEqual(len(self.r['sharpness_controls']),6)
        self.assertTrue(self.r['half_power_sharp_on_stated_margin_range'])

    def test_opposite_labels_not_selected(self):
        x=(Q(1),Q(),Q(1),Q(1),Q(),Q(),Q(),Q());y=x[:3]+(-x[3],)+x[4:]
        with self.assertRaises(ValueError):t.check_pair(x,y,Q(1),Q(1,2),Q(1),1)
        self.assertFalse(self.r['opposite_branch_pairs_classified'])

    def test_margin_assumptions_required(self):
        with self.assertRaises(AssertionError):t.constants(Q(),Q(1))
        self.assertTrue(self.r['zero_strata_by_homogeneous_inequalities'])
        self.assertFalse(self.r['physical_branch_margin_box_or_noise_licensed'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('opposite_branch_pairs_classified','physical_branch_margin_box_or_noise_licensed',
                    'cubic_single_minus_margin_assumed','physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
