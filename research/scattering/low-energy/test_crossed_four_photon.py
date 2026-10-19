import copy
import json
import unittest
from fractions import Fraction as Q
import check_crossed_four_photon as crossed


class CrossedFourPhotonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=crossed.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(crossed.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['physical_helicity_configurations'],64)
        self.assertEqual(self.result['all_outgoing_Bose_crossing_permutation_checks'],1536)
        self.assertEqual(self.result['pair_vertex_Ward_checks'],48)
        self.assertEqual(self.result['equal_helicity_matrix_checks'],16)

    def test_partial_wave_moments(self):
        self.assertEqual(crossed.crossed_monomial_moment(2),Q(1,3))
        self.assertEqual(crossed.crossed_monomial_moment(3),Q(-1,4))
        self.assertEqual(crossed.crossed_monomial_moment(2,2),Q(1,30))
        self.assertEqual(crossed.crossed_monomial_moment(4,2),Q(2,35))
        with self.assertRaises(AssertionError):crossed.crossed_monomial_moment(2,1)
        with self.assertRaises(AssertionError):crossed.left_spectral_integral_box(Q(3,4))

    def test_scope_and_complement(self):
        self.assertTrue(self.result['selected_J0_parity_preserved_in_photon_elastic_block'])
        self.assertFalse(self.result['orthogonal_photon_complement_remains_identity'])
        self.assertFalse(self.result['angular_dependence_proves_J0_to_J2_leakage'])
        self.assertFalse(self.result['scalar_parity_channels_mixed'])
        self.assertFalse(self.result['physical_rates_or_branching_derived'])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)
        for box in self.result['left_cut_positive_spectral_boxes'].values():
            self.assertGreater(Q(box['Im_Aplus_lower']),0)

    def test_contract_guards(self):
        c=json.loads(crossed.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):crossed.validate_contract(bad)
        bad=copy.deepcopy(c);bad['cut_thresholds']['left']=0
        with self.assertRaises(AssertionError):crossed.validate_contract(bad)


if __name__=='__main__':unittest.main()
