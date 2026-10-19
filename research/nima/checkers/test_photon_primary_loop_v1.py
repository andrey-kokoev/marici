import copy
from fractions import Fraction as Q
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import check_photon_primary_loop_v1 as c


class PrimaryPhotonLoopTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.provenance,cls.files,cls.text=c.load_primary()
        cls.parsed=c.parse_primary_betas(cls.text)

    def test_primary_source_binding_and_conventions(self):
        self.assertEqual(self.provenance['input_sha256']['pdf'],c.PDF_SHA)
        self.assertEqual(c.check_conventions(self.text),10)
        self.assertIn(4,self.provenance['pdf_page_numbers'])
        self.assertIn(67,self.provenance['pdf_page_numbers'])

    def test_four_exact_quadratic_polynomials(self):
        derived,moments=c.derive_betas()
        self.assertEqual(self.parsed,derived)
        self.assertEqual(moments,{'E0':'5/3','E2':'1/15','I22':'1/5'})
        self.assertEqual(self.parsed['beta12'],(Q(),Q(),Q(1,240)))

    def test_primary_forward_target_and_log_pi_grades(self):
        r=c.build()
        self.assertEqual(r['pi_times_invariant_B_std_D_O_M'],['19/2560','-5/768','1/1280'])
        self.assertEqual(r['pi_squared_beta_at_common_Born_R_s_squared'],
            {'beta11':'-19/2560','beta12':'1/3840','beta13':'-1/1280','beta2':'5/768'})
        self.assertTrue(r['primary_source_regression_independently_verified'])
        self.assertFalse(r['existing_reduced_coefficients_rescaled'])

    def test_forward_agreement_does_not_hide_wrong_beta12(self):
        text=self.text.replace(r'\frac{f_2^2}{240\pi^2}',r'\frac{f_2^2}{120\pi^2}')
        self.assertNotEqual(text,self.text)
        bad=c.parse_primary_betas(text)
        self.assertEqual(c.forward_abs(bad,Q(1,4),Q(-1,4)),c.forward_abs(self.parsed,Q(1,4),Q(-1,4)))
        with self.assertRaises(AssertionError):c.assert_primary_matches(bad)

    def test_wrong_printed_coefficient_is_not_fitted_away(self):
        text=self.text.replace(r'160\pi^2',r'80\pi^2')
        self.assertNotEqual(text,self.text)
        with self.assertRaises(AssertionError):c.assert_primary_matches(c.parse_primary_betas(text))

    def test_wrong_pi_power_is_not_parsed_as_same_coefficient(self):
        text=self.text.replace(r'160\pi^2',r'160\pi')
        with self.assertRaises(AssertionError):c.parse_primary_betas(text)

    def test_mixed_Bose_factor_and_log_rim_are_required(self):
        for before,after in ((r'1+2i\Phi_3^\ell(s)',r'1+i\Phi_3^\ell(s)'),
                             (r'- i\pi \theta(s)',r'+ i\pi \theta(s)')):
            text=self.text.replace(before,after)
            self.assertNotEqual(text,self.text)
            with self.assertRaises(AssertionError):c.check_conventions(text)

    def test_changed_source_snapshot_rejected(self):
        original=Path.read_bytes;target=self.files['tex_excerpt']
        def changed(path):return original(path)+(b'\n% changed' if path==target else b'')
        with patch.object(Path,'read_bytes',changed):
            with self.assertRaisesRegex(AssertionError,'changed primary excerpt'):c.load_primary()

    def test_physical_and_tensor_promotions_refused(self):
        contract=json.loads(c.CONTRACT.read_text(encoding='utf-8'))
        for key in ('off_forward_covariant_tensor_constructed','finite_matching_coefficients_fixed',
                    'native_preparation_or_physical_rates_derived','all_paper_claims_verified'):
            bad=copy.deepcopy(contract);bad[key]=True
            with self.subTest(key=key),self.assertRaises(AssertionError):c.validate_contract(bad)

    def test_earlier_nonverification_snapshot_not_rewritten(self):
        self.assertFalse(c.norm.build()['primary_source_regression_independently_verified'])
        self.assertTrue(c.build()['primary_source_regression_independently_verified'])

    def test_current_receipt(self):
        self.assertEqual(json.loads(c.RESULT.read_text(encoding='utf-8')),c.build())


if __name__=='__main__':unittest.main()
