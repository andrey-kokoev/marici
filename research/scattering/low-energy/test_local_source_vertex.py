"""Local current candidates are not a native or nonperturbative QFT completion."""
import copy
from fractions import Fraction as Q
import json
import unittest
import check_local_source_vertex as local


class LocalSourceVertexTests(unittest.TestCase):
    def test_pseudoscalar_Ward_and_nonzero_vertex(self):
        F=local.F
        ks=[[F(1),F(),F(),F(1)],[F(1),F(),F(),F(-1)]]
        es=[[F(),F(1),F(),F()],[F(),F(),F(1),F()]]
        self.assertNotEqual(local.two_amplitude(ks,es),F())
        self.assertEqual(local.two_amplitude(ks,[ks[0],es[1]]),F())
        self.assertEqual(local.two_amplitude(ks[::-1],es[::-1]),local.two_amplitude(ks,es))

    def test_contact_divisor_obstruction(self):
        factor=[Q(1),Q(3),Q(3),Q(1)]
        p=[Q(3),Q(2),Q(-1),Q(5),Q(9)]
        self.assertEqual(local.polynomial_at(local.multiply_polynomials(factor,p),Q(-1)),0)
        self.assertNotEqual(local.polynomial_at([Q(),Q(1)],Q(-1)),0)
        self.assertNotEqual(local.polynomial_at([Q(1)],Q(-1)),0)

    def test_fresh_local_candidate_receipt(self):
        r=local.build()
        self.assertEqual(r,json.loads(local.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(r['Dirac_bilinear_C_signs'],{'pseudoscalar':1,'vector':-1})
        self.assertEqual(r['Ward_identity_cases'],50)
        self.assertEqual(r['single_Maxwell_factor_divergence_checks'],48)
        self.assertEqual(r['three_photon_Bose_permutation_cases'],96)
        self.assertEqual(r['Lorentz_tensor_covariance_cases'],17)
        self.assertEqual(r['homogeneous_scaling_cases'],34)
        self.assertGreater(r['nonzero_three_photon_helicity_configurations'],0)
        self.assertTrue(r['this_cubic_candidate_leaks_outside_prior_equal_helicity_code'])
        self.assertTrue(r['exact_rational_envelope_from_finite_derivative_point_current_excluded'])
        self.assertFalse(r['native_Dirac_source_licensed'])
        self.assertFalse(r['self_adjoint_interacting_QFT_Hamiltonian_constructed'])
        self.assertFalse(r['branching_ratio_derived'])

    def test_no_field_or_source_promotion(self):
        c=json.loads(local.CONTRACT.read_text(encoding='utf-8'));local.validate_contract(c)
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.assertRaises(AssertionError):local.validate_contract(bad)


if __name__=='__main__':unittest.main()
