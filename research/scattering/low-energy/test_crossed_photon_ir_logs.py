import copy
import json
import unittest
from fractions import Fraction as Q
import check_crossed_photon_ir_logs as logs


class CrossedPhotonIRLogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=logs.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(logs.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['physical_right_cut_coefficient_checks'],144)
        self.assertEqual(self.result['all_outgoing_permutation_checks'],1152)
        self.assertEqual(self.result['Ward_log_tensor_checks'],24)
        self.assertEqual(self.result['Lorentz_log_tensor_checks'],6)
        self.assertEqual(self.result['mixed_helicity_projection_checks'],6)
        self.assertEqual(self.result['independent_scalar_log_projections'],6)

    def test_scalar_logs(self):
        self.assertEqual(logs.scalar_logs(2)['plus']['real_log'],Q(-7,360))
        self.assertEqual(logs.scalar_logs(3)['plus']['real_log'],Q(1,384))
        self.assertEqual(logs.scalar_logs(4)['minus']['real_log'],Q(5927,29400))
        for k in (2,3,4):
            for row in logs.scalar_logs(k).values():
                self.assertGreater(row['right_cut'],0)
                self.assertNotEqual(row['real_log'],0)
        with self.assertRaises(AssertionError):logs.cut_polynomials(1)

    def test_scope_and_polynomial_sections(self):
        for k in (2,3,4):
            D,_,M,_=logs.cut_polynomials(k)
            self.assertEqual(M[:2],[0,0])
            self.assertTrue(all(a==0 for j,a in enumerate(D) if j%2))
        self.assertFalse(self.result['real_scalar_logs_cancel_completely'])
        self.assertFalse(self.result['full_order_g2_power4_cut_spectrum_constructed'])
        self.assertFalse(self.result['finite_counterterms_source_selected'])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(logs.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):logs.validate_contract(bad)
        bad=copy.deepcopy(c);bad['scope']='full_quartic_scattering'
        with self.assertRaises(AssertionError):logs.validate_contract(bad)


if __name__=='__main__':unittest.main()
