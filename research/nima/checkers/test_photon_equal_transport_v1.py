import json
import unittest
from fractions import Fraction as Q

import check_photon_equal_transport_v1 as t


class EqualTransportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_actual_polynomial_curve(self):
        c=self.r['certificate']
        self.assertEqual((c['factorization_polynomial_identities'],c['constant_transport_polynomial_identities'],c['cut_response_polynomial_identities']),(12,6,7))
        self.assertEqual(c['denominator'],['7','0','30'])

    def test_nonzero_common_transport(self):
        self.assertEqual(self.r['constant_transport'],['-1/960','1/960','0','0','0','0'])
        self.assertEqual(self.r['rational_parameter_controls'],36)

    def test_distinct_full_cut(self):
        self.assertEqual(self.r['forward_D_cut_difference'],'24857/176644808')
        self.assertNotEqual(self.r['cut_coordinates_at_1'],self.r['cut_coordinates_at_2'])

    def test_not_common_sign_partners(self):
        x=tuple(map(Q,self.r['source_at_parameter_1']));y=tuple(map(Q,self.r['source_at_parameter_2']))
        self.assertNotEqual(x,y);self.assertNotEqual(x,tuple(-v for v in y))

    def test_unknown_quartics_retained_nonzero(self):self.assertTrue(self.r['all_three_quartic_contacts_nonzero_in_pair'])

    def test_lower_data_limitation(self):
        self.assertTrue(self.r['degree4_data_equal']);self.assertFalse(self.r['degree5_data_equal'])
        self.assertFalse(self.r['joint_degree45_and_transport_fibres_classified'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('joint_degree45_and_transport_fibres_classified','physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
