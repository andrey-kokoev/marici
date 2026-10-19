from fractions import Fraction as Q
import json
import unittest

import check_photon_zero_leading_fibres_v1 as t


class ZeroLeadingFibreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_all_strata(self):
        self.assertEqual(self.r['source_checks'],1048)
        self.assertEqual(self.r['stratum_counts'],{'pair-ordinary':960,'pure-h':32,'zero-cubic':8,'pair-cancellation':48})

    def test_cubic_components(self):
        self.assertEqual(self.r['cubic_component_counts'],{'pair-ordinary':2,'pair-cancellation-nonzero-h':4,
                         'pair-cancellation-zero-h':2,'pure-h':2,'zero-cubic':1})

    def test_quartic_freedom_not_removed(self):
        self.assertEqual(self.r['quartic_free_dimension'],3)
        self.assertFalse(self.r['quartic_contacts_identified_at_these_cut_orders'])
        self.assertEqual(self.r['pure_quartic_same_cut_Born_difference'],'3')

    def test_zero_sign_action_not_free(self):self.assertEqual(self.r['zero_cubic_sign_quotient'],'R3_antipodal_fixed_origin')

    def test_irrational_sources_retained(self):self.assertEqual(self.r['nonsquare_h3_coefficient_square'],'2/7')

    def test_nonrealizable_and_wrong_shape_refused(self):
        self.assertEqual(self.r['invalid_data_refused'],6)
        _,_,cases=t.six.inventory()
        for wrong45 in ((Q(),)*6,(Q(1),)+(Q(),)*6):
            with self.assertRaises(ValueError):t.classify(wrong45,((Q(),),)*4,cases)

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('quartic_contacts_identified_at_these_cut_orders','actual_physical_source_selected',
                    'regular_degree6_tensor_completion_constructed','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
