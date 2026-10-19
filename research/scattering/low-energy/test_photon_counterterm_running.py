import copy
import json
import unittest
from fractions import Fraction as Q
import check_photon_counterterm_running as ct


class PhotonCountertermRunningTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=ct.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(ct.RESULT.read_text(encoding='utf-8')))
        for key,value in (('finite_scale_tensor_cancellation_checks',432),('basis_permutation_checks',1152),
                          ('Ward_counterterm_checks',24),('Lorentz_counterterm_checks',6),
                          ('scalar_running_projection_checks',6),('physical_basis_normalization_checks',18),('independent_finite_matching_tensor_witnesses',6)):
            self.assertEqual(self.result[key],value)

    def test_basis_and_running(self):
        for q,n in ((4,3),(6,5),(8,6)):
            w,s,m=ct.basis_polynomials(q)
            self.assertEqual(len(s)+len(m),n)
            hs,hm=ct.running_vectors(q//2)
            self.assertEqual(len(hs),len(w));self.assertEqual(len(hm),len(m))
            self.assertTrue(all(2*a+3*b==q for a,b in w))
        self.assertEqual(ct.running_vectors(2),([Q(-5,24)],[Q(21,160),Q(-7,240)]))
        self.assertEqual(self.result['counterterm_data_by_degree']['6']['normalized_beta_all_same'],['-1/16','3/32'])
        with self.assertRaises(AssertionError):ct.basis_polynomials(5)
        with self.assertRaises(AssertionError):ct.decompose([Q(),Q(1)],ct.basis_polynomials(4)[2])

    def test_scope(self):
        for key in ('finite_matching_selected_by_running','running_of_g2_or_g3_derived',
                    'complete_off_shell_EFT_operator_basis_constructed','all_order_g2_power4_mixed_coefficients_constructed'):
            self.assertFalse(self.result[key])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)
        self.assertEqual([self.result['counterterm_data_by_degree'][str(q)]['operator_dimension'] for q in (4,6,8)],[12,16,20])

    def test_contract_guards(self):
        c=json.loads(ct.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):ct.validate_contract(bad)
        bad=copy.deepcopy(c);bad['running']='d a_i/d log(nu)=+h_i'
        with self.assertRaises(AssertionError):ct.validate_contract(bad)


if __name__=='__main__':unittest.main()
