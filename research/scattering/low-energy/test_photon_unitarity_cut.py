import copy
import json
import unittest
from fractions import Fraction as Q
import check_photon_unitarity_cut as cut


class PhotonUnitarityCutTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=cut.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(cut.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['full_helicity_matrix_checks'],9)
        self.assertEqual(self.result['general_J_moment_checks'],110)
        self.assertEqual(self.result['IR_integrand_division_checks'],27)

    def test_moments_and_Bose_carrier(self):
        self.assertEqual(cut.equal_cross_moment(2,2),Q(1,30))
        self.assertEqual(cut.mixed_cross_moment(2,2),Q(1,5))
        self.assertEqual(cut.mixed_cross_moment(3,3),Q(-1,42))
        self.assertEqual(cut.mixed_cross_moment(2,3),0)
        self.assertEqual(self.result['mixed_Bose_norm_squared_over_single_ordered_diagonal_squared'],'4')
        with self.assertRaises(AssertionError):cut.equal_cross_moment(2,1)

    def test_IR_regimes_and_scope(self):
        for case,q in (('c0_nonzero',4),('c0_zero_c1_nonzero',6),('both_zero',8)):
            self.assertEqual(self.result['IR_regimes'][case]['IR_power'],q)
            self.assertTrue(cut.zero_point_IR_subtractions_exist(q,q))
            self.assertFalse(cut.zero_point_IR_subtractions_exist(q,q+1))
        self.assertEqual(cut.ir_window_polynomial(4),{2:Q(1,2),3:Q(1)})
        self.assertFalse(self.result['right_cut_log_is_already_full_crossed_IR_germ'])
        self.assertFalse(self.result['all_orders_scattering_constructed'])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)
        for waves in self.result['zero_subtraction_cut_boxes'].values():
            self.assertEqual(len(waves),5)
            for box in waves.values():self.assertGreater(Q(box['ImB_lower']),0)

    def test_contract_guards(self):
        c=json.loads(cut.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):cut.validate_contract(bad)
        bad=copy.deepcopy(c);bad['normalization']='ImB=A_dagger*A/2'
        with self.assertRaises(AssertionError):cut.validate_contract(bad)


if __name__=='__main__':unittest.main()
