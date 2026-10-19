from fractions import Fraction as Q
import json
import unittest

import check_photon_degree5_cut_v1 as t


class DegreeFiveCutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_independent_reconstruction_matches(self):
        self.assertEqual(t.reconstruct(t.project(t.born_polynomials())),t.archived_target())

    def test_exact_angular_coefficients(self):
        self.assertEqual(self.r['pi_times_invariant_degree5_cut_D_O_M'],
                         [['9/1280','1/1280','-1/1280'],['-13/1536'],['-1/768','1/384','-1/768']])

    def test_unretained_Born_waves_not_silently_dropped(self):
        self.assertEqual(self.r['r0_r1_J3_interference'],'0')
        self.assertEqual(self.r['r1_J3_Born_wave'],'-1/1344')

    def test_forward_Born_does_not_determine_forward_cut(self):
        self.assertTrue(self.r['drop_f3_forward_Born_unchanged'])
        self.assertEqual(self.r['drop_f3_forward_loop_D_defect'],'-1/320')
        self.assertEqual(self.r['drop_f3_forward_loop_O_defect'],'1/512')

    def test_interference_ordering_factor_is_not_fitted(self):
        waves=t.project(t.born_polynomials())
        self.assertNotEqual(t.reconstruct(waves,Q(1,2)),t.archived_target())

    def test_signed_interference_and_complete_square(self):
        waves=t.project(t.born_polynomials());a,b=(v['plus'][0] for v in waves)
        self.assertLess(a*b,0);self.assertEqual(3*a+4*b,0)

    def test_scope_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('general_degree5_photon_EFT_cut_classified','physical_matching_selected','native_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
