from fractions import Fraction as Q
import json
import unittest

import check_photon_general_degree5_window_v1 as t


class GeneralDegreeFiveWindowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_new_h5_scale_term(self):
        self.assertEqual(t.FLOW[3],(Q(),Q(),-Q(1,80),Q(),Q(),-Q(1,480)))
        self.assertEqual(self.r['h5_scale_coefficient'],'-h3*(6*g2+f2)/480')

    def test_both_kernels_remain_distinct(self):
        self.assertEqual(self.r['cut_source_dimension'],6)
        self.assertEqual(self.r['cut_readout_rank'],4)
        self.assertEqual(len(self.r['source_kernel']),2)
        self.assertEqual(self.r['local_matching_dimension'],12)
        self.assertEqual(self.r['local_forward_kernel_dimension'],6)

    def test_component_and_helicity_controls(self):
        self.assertEqual(self.r['counts']['helicity'],64)
        self.assertEqual(self.r['counts']['Bose'],72)
        self.assertEqual(self.r['counts']['Ward'],4608)
        self.assertEqual(self.r['counts']['flow'],256)

    def test_exact_R_family_restriction(self):
        self.assertEqual(self.r['counts']['R_restriction'],256)
        self.assertEqual(tuple(t.dot(v,t.R) for v in t.FLOW),t.restricted.FLOW)

    def test_all_coordinate_Cauchy_checks(self):
        self.assertEqual(self.r['counts']['forward_polynomial'],54)
        self.assertEqual(self.r['counts']['forward_series'],90)
        self.assertEqual(self.r['counts']['rim'],72)

    def test_analytic_tail_domain(self):
        self.assertLess(t.tail_bound(12,Q(1,16),Q(1,2)),Q(1,10**9))
        with self.assertRaises(AssertionError):t.tail_bound(12,Q(1,4),Q(1,2))

    def test_scope_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('physical_couplings_selected','cut_readout_identifies_Born_source',
                    'all_orders_or_full_IR_inventory_derived','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
