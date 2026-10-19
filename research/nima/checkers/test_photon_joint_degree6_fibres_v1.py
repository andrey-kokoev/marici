from fractions import Fraction as Q
import json
import unittest

import check_photon_joint_degree6_fibres_v1 as t


class JointDegreeSixFibreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_all_source_strata(self):
        self.assertEqual(self.r['source_checks'],354)
        self.assertEqual(self.r['stratum_counts'],{'ordinary':258,'leading-cancellation-resolved':24,'double-cancellation':72})

    def test_quartic_inputs_reconstructed_not_fixed(self):
        self.assertTrue(self.r['quartic_Born_nuisance_contacts_reconstructed'])
        self.assertEqual(set(self.r['quartic_nuisance_ranks'].values()),{3})

    def test_actual_sign_fibres(self):
        self.assertEqual(self.r['ordinary_actual_fibre_size'],2)
        self.assertEqual(self.r['resolved_cancellation_actual_fibre_size'],2)
        self.assertEqual(self.r['double_cancellation_nonzero_h_actual_fibre_size'],4)
        self.assertEqual(self.r['double_cancellation_zero_h_actual_fibre_size'],2)

    def test_irrational_h3_allowed(self):self.assertEqual(self.r['nonsquare_h3_square_control'],'2')

    def test_sign_inverse_not_uniform(self):
        self.assertEqual(self.r['relative_h_sign_inverse_lower_bounds'],{'10':'9600','100':'96000','1000':'960000'})

    def test_zero_leading_scope_is_explicit(self):
        _,_,cases=t.six.inventory()
        with self.assertRaises(NotImplementedError):t.classify((Q(),)*7,((Q(),),)*4,cases)
        self.assertFalse(self.r['zero_leading_fibres_classified'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('zero_leading_fibres_classified','global_unique_physical_source_selected','uniformly_stable_inverse_derived',
                    'native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
