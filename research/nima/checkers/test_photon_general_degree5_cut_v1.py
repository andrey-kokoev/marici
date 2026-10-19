from fractions import Fraction as Q
import json
import unittest

import check_photon_general_degree5_cut_v1 as t


class GeneralDegreeFiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_source_and_readout_dimensions_differ(self):
        self.assertEqual(self.r['source_coordinate_dimension'],6)
        self.assertEqual(self.r['cut_readout_rank'],4)
        self.assertEqual(self.r['readout_kernel'],[['0','-10','0','1','0','0'],['0','0','-1/6','0','0','1']])

    def test_induced_single_minus(self):
        self.assertEqual(self.r['single_minus_g2_h3_coefficient'],'1/80')
        self.assertEqual(self.r['single_minus_f2_h3_coefficient'],'1/480')
        self.assertIn('(6*g2+f2)*h3/480',self.r['single_minus_polynomial'])

    def test_coupled_wave_not_discarded(self):
        waves=self.r['pi_times_unit_Bose_waves']
        self.assertEqual(waves[4]['off'],'1/240')
        self.assertEqual(waves[0]['off'],'0')

    def test_exact_R_family_restriction(self):self.assertTrue(self.r['restricted_R_family_match'])

    def test_interference_not_positive_by_itself(self):
        self.assertLess(Q(self.r['indefinite_interference_J2_determinant']),0)
        self.assertEqual(self.r['complete_wave_square_PSD_controls'],243)

    def test_Wigner_norm(self):self.assertEqual(6*t.family.integral(t.family.mul(t.K,t.K)),Q(1,5))

    def test_unearned_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('general_log_window_tensor_constructed','signed_interference_assumed_positive',
                    'couplings_selected_from_cut_readout','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
