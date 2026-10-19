import copy
from fractions import Fraction as Q
import json
import unittest
import check_photon_normalization_v1 as c


class PhotonNormalization(unittest.TestCase):
    def test_bose_phase_volume_not_double_counted(self):
        self.assertEqual(c.phase_dictionary(),Q(1,16))
        for factor in (Q(1),Q(1,4)):
            with self.assertRaises(AssertionError):c.assert_standard_bridge(c.phase_dictionary(factor))

    def test_standard_Gram_for_independent_contact_coefficients(self):
        for g,f in ((Q(1),Q()),(Q(),Q(1)),(Q(1),Q(-1)),(Q(2,3),Q(-4,5))):
            self.assertEqual(c.invariant_pi_cut(g,f),c.direct_invariant_pi_cut(g,f))
        self.assertEqual(Q(14,5)-Q(25,9),Q(1,45))

    def test_exact_review_target_with_no_source_promotion(self):
        r=c.build()
        self.assertEqual(r['pi_times_invariant_B_std_D_O_M'],['19/2560','-5/768','1/1280'])
        self.assertFalse(r['primary_source_regression_independently_verified'])
        self.assertTrue(r['reported_source_target_is_review_derived_not_primary_transcription'])
        self.assertEqual(r['status'],'pass_with_primary_source_residual')

    def test_mixed_physical_eigenvalue_not_one_ordered_entry(self):
        H=Q(1,5);A=[[H/2,H/2],[H/2,H/2]]
        self.assertEqual(c.mm(A,A)[0][0]/8,H*H/16)
        self.assertNotEqual((H/2)**2/8,H*H/8)

    def test_source_calibration_and_parameter_promotions_refused(self):
        contract=json.loads(c.CONTRACT.read_text(encoding='utf-8'))
        for key in ('primary_source_regression_independently_verified','physical_g2_or_g3_calibration_derived',
                    'project_Dirac_coupling_equals_photon_EFT_Wilson_coefficient','existing_reduced_coefficients_rescaled',
                    'cross_sector_single_16pi_factor_derived','native_preparation_selected'):
            with self.subTest(key=key):
                bad=copy.deepcopy(contract);bad[key]=True
                with self.assertRaises(AssertionError):c.validate_contract(bad)

    def test_earlier_Dirac_g2_phase_factors_retained(self):
        r=c.build()
        self.assertTrue(r['earlier_amplitude_normalized_g2_dictionary_derived'])
        self.assertTrue(r['g3_remains_independent'])
        self.assertEqual(r['b_pi_squared_per_abs_kappa_g2_m3_squared'],'1/128')
        self.assertEqual(r['common_Born_lambda_pi_per_abs_kappa_g2_m3_squared'],'1/8')
        self.assertEqual(r['invariant_Born_M_prefactor_pi_per_abs_kappa_g2_m3_squared'],'1/16')
        bad=json.loads(c.CONTRACT.read_text(encoding='utf-8'))
        bad['earlier_g2_dictionary']='b=|kappa*g2|^2*m^6/(64*pi^2)'
        with self.assertRaises(AssertionError):c.validate_contract(bad)

    def test_fixed_b_conversion_not_common_A_conversion(self):
        # Formal monomials represented as (rational coefficient, pi exponent).
        fixed_b=(Q(16),1);common_A=(Q(1,16),-1)
        self.assertNotEqual(fixed_b,common_A)
        # 16*pi*b^2 == (16*pi*b)^2/(16*pi).
        self.assertEqual((16**2*common_A[0],2+common_A[1]),fixed_b)

    def test_weighted_channel_dictionary_not_common_constant(self):
        M=[[Q(1),Q(2)],[Q(3),Q(5)]]
        lhs,rhs=c.weighted_channel_pullback(M,(Q(1),Q(1,2)))
        self.assertEqual(lhs,rhs)
        self.assertNotEqual(lhs,c.mm(c.adj(M),M))

    def test_receipt_is_current(self):
        self.assertEqual(json.loads(c.RESULT.read_text(encoding='utf-8')),c.build())


if __name__=='__main__':unittest.main()
