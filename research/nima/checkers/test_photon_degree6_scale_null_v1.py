import json
import unittest
from fractions import Fraction as Q

import check_photon_degree6_scale_null_v1 as t


class ScaleNullSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_response_null_line(self):self.assertEqual(self.r['certificate']['response_null_line'],['-3','-3','0','0','5','1','0'])

    def test_h_zero_positive_squares(self):
        self.assertTrue(all(Q(v)>0 for v in self.r['certificate']['h_zero_positive_square_coefficients']))

    def test_h_nonzero_universal_sign_certificate(self):
        coeffs=tuple(map(Q,self.r['certificate']['h_nonzero_strictly_negative_polynomial']))
        self.assertEqual(len(coeffs),4)
        self.assertTrue(all(v<0 for v in coeffs))
        self.assertTrue(all(Q(v)>0 for v in self.r['certificate']['h_nonzero_a_affine']))

    def test_complete_grid_and_locus(self):
        self.assertEqual((self.r['grid_source_checks'],self.r['grid_null_sources']),(6561,35))
        self.assertTrue(self.r['real_source_zero_transport_iff_zero_cut'])

    def test_nonzero_interactions_not_deleted(self):
        self.assertEqual(self.r['nonzero_Born_witness_forward_values'],['1','1'])
        self.assertFalse(self.r['zero_transport_implies_zero_entire_interaction'])

    def test_not_a_global_inverse(self):self.assertFalse(self.r['global_transport_fibres_classified'])

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('global_transport_fibres_classified','zero_transport_implies_zero_entire_interaction',
                    'physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
