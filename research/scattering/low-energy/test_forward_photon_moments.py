import copy
import json
import unittest
from fractions import Fraction as Q
import check_forward_photon_moments as mom


class ForwardPhotonMomentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.result=mom.build()

    def test_receipt(self):
        self.assertEqual(self.result,json.loads(mom.RESULT.read_text(encoding='utf-8')))
        self.assertEqual(self.result['closed_forward_pair_checks'],49)
        self.assertEqual(self.result['independent_angular_Gram_and_twirl_checks'],12)
        self.assertEqual(self.result['complex_coherent_polarization_checks'],48)

    def test_coherence_and_IR_limits(self):
        eig=mom.pair_eigenvalues(2,2)
        self.assertEqual(eig,(Q(107,480),Q(7,480),Q(1,80)))
        self.assertEqual(mom.coherent(eig,((1,0),(1,0),(0,0),(0,0))),Q(7,480))
        self.assertEqual(mom.coherent(eig,((1,0),(-1,0),(0,0),(0,0))),Q(107,480))
        self.assertEqual(mom.moment({4:Q(1)},3,Q(1,2)),Q(1,2))
        with self.assertRaises(AssertionError):mom.moment({4:Q(1)},4,Q(1,2))
        self.assertEqual([self.result['IR_threshold_controls'][str(k)]['largest_finite_integer_n'] for k in (2,3,4)],[3,5,7])

    def test_density_subtraction_and_operator_error(self):
        self.assertEqual(self.result['two_monomial_IR_subtracted_eigenvalues'][1:],['-79/7680','-25/2688'])
        boxes=self.result['spectral_comparison']['eigenvalue_boxes']
        self.assertTrue(all(Q(b[0])>0 for n in ('2','3') for b in boxes[n].values()))
        self.assertLess(Q(boxes['8']['plus'][1]),0)
        self.assertLess(Q(boxes['8']['mixed'][1]),0)
        for n in (2,3):self.assertLess(mom.spectral_moment_error(16,n,Q(1,2)),Q(3,10**18))
        with self.assertRaises(AssertionError):mom.spectral_moment_error(4,9,Q(1,2))
        self.assertFalse(self.result['finite_matching_fixed_or_bounded'])
        self.assertEqual(len(self.result['hostile_controls_refused']),8)

    def test_contract_guards(self):
        c=json.loads(mom.CONTRACT.read_text(encoding='utf-8'))
        for key,value in c.items():
            if isinstance(value,bool):
                bad=copy.deepcopy(c);bad[key]=not value
                with self.subTest(key=key),self.assertRaises(AssertionError):mom.validate_contract(bad)
        bad=copy.deepcopy(c);bad['IR_condition']='all_n_without_subtraction'
        with self.assertRaises(AssertionError):mom.validate_contract(bad)


if __name__=='__main__':unittest.main()
