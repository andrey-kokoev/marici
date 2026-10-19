from fractions import Fraction as Q
import json
import unittest

import check_photon_general_degree6_cut_v1 as t


class GeneralDegreeSixCutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.r=t.build()

    def test_fresh_receipt(self):self.assertEqual(json.loads(t.RESULT.read_text(encoding='utf-8')),self.r)

    def test_both_sectors_and_all_sources(self):
        self.assertEqual(self.r['source_monomial_dimension'],12)
        self.assertEqual(self.r['independent_complete_square_coefficient_checks'],264)
        self.assertEqual(self.r['R_family_sector_matches'],['c1_squared','c0_r4'])

    def test_higher_Born_waves_retained(self):
        self.assertEqual(self.r['unit_Born_Bose_waves'][7]['plus'][4],'1/2520')
        self.assertEqual(self.r['unit_Born_Bose_waves'][5]['mixed'][2],'1/2016')

    def test_h3_square_and_single_minus(self):
        self.assertEqual(self.r['h3_square_forward_D_O_M'],['1/480']*3)
        self.assertEqual(self.r['Phi5_cut'],'-h3*(10*g3+f3)*s^4*t*u/960')

    def test_nuisance_not_silently_dropped(self):
        self.assertEqual(self.r['quartic_nuisance_vs_h3_square_ranks'],[3,4])

    def test_sign_ambiguity_survives(self):
        self.assertEqual(self.r['remaining_sign_witness']['Born_Phi5_difference'],'288/625')
        self.assertFalse(self.r['all_h3_fibres_resolved_by_degree6'])

    def test_complete_square_controls(self):self.assertEqual(self.r['complete_Born_block_PSD_controls'],256)

    def test_scope_promotions_refused(self):
        c=json.loads(t.CONTRACT.read_text(encoding='utf-8'))
        for key in ('all_h3_fibres_resolved_by_degree6','degree6_log_window_tensor_constructed',
                    'finite_physical_matching_selected','native_or_UV_dynamics_derived','C12_budget_renewed'):
            with self.assertRaises(AssertionError,msg=key):t.validate({**c,key:True})


if __name__=='__main__':unittest.main()
