import copy
import json
import unittest
from fractions import Fraction as Q
import check_scalar_dispersive_response as response


class ScalarDispersiveResponseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=response.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(response.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['rational_change_of_variable_checks'],20)
        self.assertEqual(self.result['exact_tail_moment_checks'],36)
        self.assertEqual(self.result['free_local_subtraction_degrees'],[2,3])

    def test_subtractions_and_coefficients(self):
        self.assertFalse(response.convergent_subtractions(3,3))
        self.assertTrue(response.convergent_subtractions(3,4))
        self.assertFalse(response.convergent_subtractions(1,1))
        self.assertTrue(response.convergent_subtractions(1,2))
        self.assertEqual([response.coefficient(k) for k in range(3)],[Q(1,6),Q(1,60),Q(1,420)])
        self.assertEqual(response.series_box(0),(Q(1,6),Q(1,6)))
        with self.assertRaises(AssertionError):response.series_box(4)
        with self.assertRaises(AssertionError):response.coefficient(-1)

    def test_scope_and_phase_freedom(self):
        self.assertTrue(self.result['charged_pair_absorptive_cut_matched'])
        self.assertEqual(self.result['same_cut_s2_subtraction_sign_controls'],['-1','1'])
        self.assertFalse(self.result['exact_unitary_scattering_constructed'])
        self.assertFalse(self.result['eta1_higher_order_contractivity_failure_repaired'])
        self.assertFalse(self.result['crossing_complete_four_photon_amplitude_constructed'])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(response.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):response.validate_contract(bad)
        bad=copy.deepcopy(c);bad['minimum_subtractions']['full_response']=2
        with self.assertRaises(AssertionError):response.validate_contract(bad)


if __name__=='__main__':unittest.main()
