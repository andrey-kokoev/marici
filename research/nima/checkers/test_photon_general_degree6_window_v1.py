import json
import unittest
from fractions import Fraction as Q

import check_photon_general_degree6_window_v1 as t


class GeneralDegreeSixWindowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_cut_and_scale_kernels_differ(self):
        self.assertEqual((self.r['cut_rank'],self.r['transport_rank']),(7,6))
        self.assertEqual((len(self.r['cut_kernel']),len(self.r['transport_kernel'])),(5,6))
        extra=tuple(map(Q,self.r['transport_null_but_cut_nonzero']))
        self.assertTrue(all(t.dot(row,extra)==0 for row in t.FLOW))

    def test_independent_h6_transport(self):
        self.assertEqual(self.r['common_log_H6'],'h3*(10*g3+f3)/320')
        self.assertEqual(self.r['mu_log_derivative_H6'],'-h3*(10*g3+f3)/160')

    def test_matching_not_selected(self):
        self.assertEqual((self.r['local_matching_dimension'],self.r['local_forward_kernel_dimension']),(18,10))
        self.assertFalse(self.r['physical_matching_selected'])

    def test_helicity_Ward_and_component_transport(self):
        self.assertEqual(self.r['counts']['helicity'],64)
        self.assertEqual(self.r['counts']['Bose'],72)
        self.assertEqual(self.r['counts']['flow'],256)
        self.assertEqual(self.r['counts']['Ward'],9216)

    def test_forward_window_and_archived_restrictions(self):
        self.assertEqual(self.r['counts']['R_restriction'],40)
        self.assertEqual(self.r['counts']['forward_polynomial'],108)
        self.assertEqual(self.r['counts']['forward_series'],180)
        self.assertEqual(self.r['counts']['rim'],144)

    def test_generated_difference_tail(self):
        self.assertEqual(self.r['tail_coefficient_bound_K'],'107/80')
        self.assertLess(Q(self.r['tail_bound_N12_a1_16_tau_half']),Q(1,10**8))
        with self.assertRaises(AssertionError):t.tail_bound(12,Q(1,4),Q(1,2))

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('physical_matching_selected','source_identified_by_scale_transport','full_massless_amplitude_jointly_analytic',
                    'all_orders_or_full_IR_inventory_derived','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
