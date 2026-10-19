import copy
from fractions import Fraction as Q
import json
import unittest

import check_photon_window_lift_v1 as t


class WindowLiftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_exact_forward_not_only_cuts(self):
        self.assertEqual(self.r['forward_polynomial_checks'],27)
        self.assertEqual(self.r['forward_jet_checks'],36)
        self.assertTrue(self.r['normalized_legacy_cut_matches'])

    def test_lower_subtractions_are_not_optional(self):
        self.assertEqual(self.r['lower_jet_at_tau_half_common_Born_pi_squared'],
                         {'g2':'21/20480','f2':'-5/6144','g3':'17/5120'})

    def test_all_higher_forward_coefficients(self):self.assertEqual(self.r['higher_forward_analytic_coefficients'],72)

    def test_window_rims_and_exterior_cut(self):
        self.assertEqual(self.r['rim_checks'],12)
        self.assertEqual(t.channel_rim(Q(1,4),Q(1,2)),1)
        self.assertEqual(t.channel_rim(Q(3,4),Q(1,2)),0)

    def test_two_variable_tail_domain(self):
        self.assertLess(t.scalar_tail_bound(12,Q(1,16),Q(1,2)),Q(1,10**9))
        with self.assertRaises(AssertionError):t.scalar_tail_bound(12,Q(1,4),Q(1,2))

    def test_local_forward_invisible_directions_retained(self):
        self.assertEqual(self.r['forward_invisible_local_ambiguity'],['f3','h3','g4prime'])
        self.assertEqual(t.w.nullspace(t.w.forward_map()),tuple(tuple(Q(int(j==i)) for j in range(8)) for i in (3,4,6)))

    def test_no_uniqueness_or_physical_promotion(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('off_forward_lift_unique_from_forward_data','finite_matching_coefficients_selected',
                    'full_unsubtracted_amplitude_analytic_at_origin','all_orders_or_full_IR_inventory_covered',
                    'global_UV_positivity_or_native_dynamics_derived','C12_budget_renewed'):
            bad=copy.deepcopy(c);bad[key]=True
            with self.assertRaises(AssertionError,msg=key):t.validate(bad)


if __name__=='__main__':unittest.main()
